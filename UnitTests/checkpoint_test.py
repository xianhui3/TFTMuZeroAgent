import pytest
import ray
from Concurrency.storage import Storage

def setup_function(episode):
    global storage
    storage = Storage.remote(0)
    # yield storage

def test_store_checkpoint():
    storage.store_checkpoint.remote(1000000)
    checkpoint_list = ray.get(storage.get_checkpoint_list.remote())
    assert checkpoint_list[-1].epoch == 1000000

def test_update_checkpoint_score():
    # First test is for a random checkpoint,
    storage.store_checkpoint.remote(123456)
    storage.update_checkpoint_score.remote(123456, 1)
    checkpoint_list = ray.get(storage.get_checkpoint_list.remote())
    assert checkpoint_list[-1].q_score < 1

def test_sample_past_model():
    model, choice, probability = ray.get(storage.sample_past_model.remote())
    assert model
    assert choice % 100 == 0
    assert probability < 1

def get_model_test(storage):
    pass

def update_q_score_test(storage):
    pass
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

# So let me make a list of the methods that I need to test
# Storage - store_checkpoint, update_checkpoint, update_checkpoint_score, sample_past_model, get_model
# Checkpoint - get_model, update_q_score
# def test_list():
#     store_checkpoint_test(storage)
#     update_checkpoint_score_test(storage)
#     sample_past_model_test(storage)
#     get_model_test(storage)
#     update_q_score_test(storage)

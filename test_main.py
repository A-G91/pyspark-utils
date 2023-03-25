import main
import random


def test_get_weights_no_remainder():
    assert main.get_weights(1000000, 100000) == [.1] * 10

def test_get_weights_with_remainder():
    assert main.get_weights(1000000, 70000) == [0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.02]

def test_weights_sum_to_one():

    num_tests = 1000

    for _ in range(num_tests):
        dataframe_size = random.randint(1000, 1000000) 
        partition_size = random.randint(1000, dataframe_size - 1)

        weights = main.get_weights(dataframe_size, partition_size)
        assert round(sum(weights), 2) == 1
    


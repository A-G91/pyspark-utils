import math


def get_weights(dataframe_size: int, partition_size: int) -> list:
    '''
    Find the best weights to partition the dataframe based on the desired partition size. Weights are rounded to 2 decimal places.
    '''
    if partition_size >= dataframe_size:
        return [1]

    weight = round(partition_size / dataframe_size, 2)
    if weight == 0:
        # This happens when partition size requested is too small.
        # Setting weight to 1% for now
        weight = 0.01

    num_partitions = 1 / weight
    print(weight, num_partitions)
    if num_partitions.is_integer():
        return [weight] * int(num_partitions)

    # Number of partitions has a decimal portion. Try to distribute weight evenly across partitions.
    num_partitions = math.ceil(num_partitions)
    weight = round(1 / num_partitions, 2)
    weights = [weight] * num_partitions

    # If sum of weights is not equal to 1, adjust the last weight in weights with the difference.
    diff = 1 - sum(weights)
    weights.append(round(weights.pop() + diff, 2))

    return weights

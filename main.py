
def get_weights(dataframe_size: int, partition_size: int) -> list:
    '''Find the best weights to partition the dataframe based on the desired partition size. Weights are accurate to 2 decimal places.'''
    if partition_size >= dataframe_size:
        return [1]

    weight = round(partition_size / dataframe_size, 2)
    if weight == 0:
        # This happens when partition size requested is too small.
        # Setting weight to 1% for now
        weight = 0.01
    num_partitions = int(1 / weight)

    weights = [weight] * num_partitions
    remainder = round(1 - sum(weights), 2)
    if remainder > 0:
        weights.append(remainder)

    return weights


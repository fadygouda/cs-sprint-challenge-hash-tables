def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    index = {}

    for i in range(len(weights)):
        if limit - weights[i] in index:
            return [i, index[limit-weights[i]]]
        else:
            index[weights[i]] = i

    return None

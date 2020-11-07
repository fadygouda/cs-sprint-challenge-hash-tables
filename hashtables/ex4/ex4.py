def has_negatives(a):
    """
    YOUR CODE HERE
    """
    neg = {}
    for i in a:
        if i < 0:
            neg[abs(i)] = i

    result = []

    for i in a:
        if i in neg:
            result.append(i)
    # Your code here

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

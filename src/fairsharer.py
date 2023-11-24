def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.

    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
        
    Args
    values:
        1D array of values (list or numpy array)
    num_iteration:
        Integer to set the number of iterations
    """

    values_new = values.copy()
    for _ in range(num_iterations):
        # find the maximum value and its index
        max_value = max(values_new)
        max_index = values_new.index(max(values_new))

        # calculate the left and right neighbour so it also works for the first and last index
        left_neighbor = (max_index - 1) % len(values_new)
        right_neighbor = (max_index + 1) % len(values_new)

        # calculate the new values and update the new list
        values_new[max_index] -= 2 * (max_value * share)
        values_new[left_neighbor] += max_value * share
        values_new[right_neighbor] += max_value * share

    return values_new
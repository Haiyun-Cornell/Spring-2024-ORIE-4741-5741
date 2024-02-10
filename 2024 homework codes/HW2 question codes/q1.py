import numpy as np

def perceptron_algo(features, labels, N_iters, geom_margins=[],
        initial_weights=None, margin=None, 
        variable_increment=False, batch=False):
    """ run the perceptron algorithm
    :param features: the input features vector
    :param labels: the ground-truth labels
    :param N_iters: number of iterations to run
    :param geom_margins: buffer to record the geometric margin
    :param initial_weights: the initial theta
    :param margin: the margin that the data can be separated by 
    :param variable_increment: if to run with variable increment
    :param batch: if to run with batch variable increment
    :return theta: the result w for y = sign(wx)
    """
    theta = np.zeros(2)
    if initial_weights is not None:
        theta = initial_weights

    for _ in range(N_iters):
        agreements = []
        count = 1
        for x, y in zip(features, labels):
            prediction = np.dot(theta, x)
            agreement = prediction * y
            mistake = agreement <= 0

            if margin is not None:
                # TODO Q1(b): implement margin perceptron
                # now we need to consider margin mistakes
                # change 'mistake' accordingly
                pass

            if mistake:
                # update when there is a disagreement
                update = y * x
                # TODO Q1(c): apply variable increment
                
                # TODO Q1(d): apply batch update
                theta += update
            agreements.append(agreement)
            count += 1

        # TODO Q1(d): update if batch increment

        # TODO Q1(a): compute the geometric margin
        geom_margin = 0.0
        geom_margins.append(geom_margin)

    return theta

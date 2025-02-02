
def mean(samples):
    return sum(samples)/len(samples)
def evaluate(true_values, samples):
    time_periods = len(true_values)
    prediction = [mean(s) for s in samples] # mean of samples
    error = 0

    for i in range(time_periods):
        predicted_value = prediction[i]
        true_value = true_values[i]
        error += abs(true_value - predicted_value)

    mean_absolute_error = error/time_periods

    return mean_absolute_error
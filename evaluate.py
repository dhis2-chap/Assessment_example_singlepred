

def evaluate(true_values, samples):
    time_periods = len(true_values)
    prediction = samples[0]
    error = 0

    for i in range(time_periods):
        predicted_value = prediction[i]
        true_value = true_values[i]
        error += abs(true_value - predicted_value)

    mean_absolute_error = error/time_periods

    return mean_absolute_error
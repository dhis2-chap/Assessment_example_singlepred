# Minimalist Example of Model Assessment

This document provides a minimalist example of how to write Python code for basic model assessment. The data and model are taken from the `minimalist_example` repository. The model is evaluated using Mean Absolute Error (MAE), assuming a single predicted value per month. This example is neither CHAP-compatible nor a robust evaluation pipeline. Its sole purpose is to serve as a simple introduction to writing model assessment code.


## Running assessment in isolation

Before evaluating on more complex data, it might be useful to test the evaluation directly on a small example of prediction samples and true values. 

The example can be run in isolation (e.g. from the command line) using the file isolated_asses.py:
```bash
python isolated_asses.py
```

This isolated assessment evaluates on these arbitrarily chosen true values and prediction samples
```bash
true_values = [0, 10, 35]
samples = [[0,2], [9,13], [31,41]]
```

It then runs and prints the returned error value of the evaluate function from evaluate.py:
```bash
MAE = evaluate(true_values, samples)
print(f"MAE: {MAE}")
```


### The evaluation function 
In this minimalist example of model assessment, we use an evaluation function that takes the true values and prediction samples as input and returns an error value. More specifically, the evaluator computes the Mean Absolute Error (MAE) between the true values and the mean of the prediction samples.
```bash
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
```


## Running assessment with Minimalist Example
The `asses_minimalist.py` script demonstrates how to evaluate a model’s performance using actual data and corresponding predictions. The process involves training the model, generating predictions, and evaluating the results.

For simplicity, only the first prediction sample is used for each time step. The evaluation is performed using the `evaluate` function, which returns the Mean Absolute Error (MAE).


```bash
def get_arbitrary_sample(predictions_fn):
    df = pd.read_csv(predictions_fn)
    samples = [[x] for x in df["sample_0"].tolist()]
    return samples


train("Minimalist_example/input/trainData.csv", "Minimalist_example/output/model.bin")
predict("Minimalist_example/output/model.bin", "Minimalist_example/input/trainData.csv", "Minimalist_example/input/futureClimateData.csv", "Minimalist_example/output/predictions.csv")

samples = get_arbitrary_sample("Minimalist_example/output/predictions.csv")
assert len(samples)==3
true_values = [250, 400, 450]

MAE = evaluate(true_values, samples)
print(f"MAE: {MAE}")
```

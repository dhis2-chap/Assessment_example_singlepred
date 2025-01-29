from evaluate import evaluate

true_values = [0, 10, 35]
samples = [[10, 5, 20]]

MAE = evaluate(true_values, samples)
print(f"MAE: {MAE}")

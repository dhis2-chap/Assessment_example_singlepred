from evaluate import evaluate

true_values = [0, 10, 35]
samples = [[0,2], [9,13], [31,41]]

MAE = evaluate(true_values, samples)
print(f"MAE: {MAE}")

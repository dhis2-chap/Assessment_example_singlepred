from evaluate import evaluate
import sys
sys.path.append("Minimalist_example")

from train import train
from predict import predict


train("input/trainData.csv", "output/model.bin")
samples = predict("output/model.bin", "input/trainData.csv", "input/futureClimateData.csv", "output/predictions.csv")
true_values = [250, 400, 450]

MAE = evaluate(true_values, samples)
print(f"MAE: {MAE}")


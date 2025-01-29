from evaluate import evaluate
from Minimalist_example.train import train
from Minimalist_example.predict import predict
import pandas as pd

def get_samples():
    df = pd.read_csv("your_file.csv")
    samples = list(df["sample_0"].tolist())
    return samples


train("input/trainData.csv", "output/model.bin")
predict("output/model.bin", "input/trainData.csv", "input/futureClimateData.csv", "output/predictions.csv")


samples = get_samples()
true_values = [250, 400, 450]

MAE = evaluate(true_values, samples)
print(f"MAE: {MAE}")


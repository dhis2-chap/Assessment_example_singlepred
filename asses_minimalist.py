from evaluate import evaluate
from Minimalist_example.train import train
from Minimalist_example.predict import predict
import pandas as pd

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


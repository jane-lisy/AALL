import pandas as pd

exp_id = "5"

dat = pd.read_csv(f"exp{exp_id}/eval/results.csv")

# accuracy by condition
print(dat.groupby("condition")["correct"].mean())

print(dat.groupby(["condition", "run"])["correct"].mean())
# output as csv
dat.groupby(["condition", "run"])["correct"].mean().reset_index().to_csv(
    f"exp{exp_id}.csv", index=False
)

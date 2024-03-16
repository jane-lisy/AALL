import pandas as pd

exp_id = "5"
conditions = ["baseline", "front-round", "front-unround", "back-round", "back-unround"]

dat = pd.DataFrame()
dat_merged = pd.DataFrame()


def read_list(path: str) -> list:
    with open(path, "r") as f:
        return f.read().splitlines()


for condition in conditions:
    # get gold src and tgt
    gold_src_path = f"exp{exp_id}/{condition}/data/src-test.txt"
    gold_tgt_path = f"exp{exp_id}/{condition}/data/tgt-test.txt"
    gold_src = read_list(gold_src_path)
    gold_tgt = read_list(gold_tgt_path)
    # load test.csv
    test_df = pd.read_csv(f"exp{exp_id}/{condition}/data/test.csv")
    for i in range(1, 6):
        pred_path = f"exp{exp_id}/{condition}/predict/{i}.txt"
        pred = read_list(pred_path)
        df = pd.DataFrame(
            {
                "gold_src": gold_src,
                "gold_tgt": gold_tgt,
                "pred": pred,
                "condition": condition,
                "run": i,
            }
        )
        df["correct"] = (df["gold_tgt"] == df["pred"]).astype(int)
        dat = pd.concat([dat, df])
        # merge with test.csv
        dat_ = pd.concat([df, test_df], axis=1)
        dat_merged = pd.concat([dat_merged, dat_])

dat.to_csv(f"exp{exp_id}/eval/results.csv", index=False)
dat_merged.to_csv(f"exp{exp_id}/eval/results_merged.csv", index=False)

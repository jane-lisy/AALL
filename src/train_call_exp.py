import os

exp_id = "5"
conditions = ["baseline", "front-round", "front-unround", "back-round", "back-unround"]

calls = []

for condition in conditions:
    # cd command into condition directory
    calls.append(f"cd exp{exp_id}/{condition}")

    for i in range(1, 6):
        folder = f"models/{i}"
        # create the folder if it doesn't exist
        os.makedirs(f"exp{exp_id}/{condition}/{folder}", exist_ok=True)
        call = f"onmt_train -config rnn.yaml -save_model {folder}/rnn -seed {i}"
        calls.append(call)

    # cd command out of condition directory
    calls.append("cd ../..")

print(" && ".join(calls))

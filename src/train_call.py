import os

exp_id = "1"
condition = "front-round"

calls = []

# cd command into condition directory
calls.append(f"cd exp{exp_id}/{condition}")

for i in range(1, 6):
    folder = f"models/{i}"
    # create the folder if it doesn't exist
    os.makedirs(f"exp{exp_id}/{condition}/{folder}", exist_ok=True)
    call = f"onmt_train -config rnn.yaml -save_model {folder}/rnn -seed {i}"
    calls.append(call)

print(" && ".join(calls))

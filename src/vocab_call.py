exp_id = "5"
conditions = ["baseline", "front-round", "front-unround", "back-round", "back-unround"]

calls = []

for condition in conditions:
    calls.append(f"cd exp{exp_id}/{condition}")
    calls.append("onmt_build_vocab -config rnn.yaml")
    calls.append("cd ../..")

print(" && ".join(calls))

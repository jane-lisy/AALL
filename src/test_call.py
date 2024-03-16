# copy and paste the output of this code to command line
# (after activating the virtual environment nnorphology)

exp_id = "5"
conditions = ["baseline", "front-round", "front-unround", "back-round", "back-unround"]
model_name = "rnn_step_2900.pt"  # "rnn_step_3775.pt"

calls = []

for condition in conditions:
    for i in range(1, 6):
        model = f"exp{exp_id}/{condition}/models/{i}/{model_name}"
        src = f"exp{exp_id}/{condition}/data/src-test.txt"
        output = f"exp{exp_id}/{condition}/predict/{i}.txt"
        calls.append(f"onmt_translate -model {model} -src {src} -output {output}")

print(" && ".join(calls))

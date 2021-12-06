import json
import sys
import numpy as np

with open(sys.argv[1], 'r') as json_file:
    dataset = json.load(json_file)
    # dataset = [json.loads(jline) for jline in json_file.readlines()]
    # json_list = list(json_file)

lens = []
cnt = 0

with open(sys.argv[2], 'w') as wf:
    for result in dataset:
        # print(type(result['intent']))
        result['intent'] = result['intent'][:min(len(result['intent']), 120)]
        wf.write(json.dumps(result) + "\n")



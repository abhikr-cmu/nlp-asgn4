import json
import sys
import numpy as np

dataset = []

with open(sys.argv[1], 'r') as json_file:
    for jline in json_file.readlines():
        dataset.append(json.loads(jline))



with open(sys.argv[2], 'w') as wf:
    for result in dataset:
        result['intent'] = result['intent'] + " " + sys.argv[3]
        wf.write(json.dumps(result) + "\n")

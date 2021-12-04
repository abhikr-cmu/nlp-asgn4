import json
import sys

with open(sys.argv[2], 'w') as wf:
    with open(sys.argv[1]) as rf:
        for line in rf:
            print(line)
            cur =  json.loads(line);
            cur['question_id'] += int(sys.argv[3])
            wf.write(json.dumps(cur)+"\n")

import csv
import numpy as np
import sys
from elasticsearch import Elasticsearch
import json

tsv_file = open(sys.argv[1])
read_tsv = csv.reader(tsv_file, delimiter="\t")

qids = []
prob = []

for row in read_tsv:
    qids.append(row[0])
    prob.append(row[1])

sampled_qids = np.random.choice(qids, size=10000,  p=prob, replace=True)

es = Elasticsearch()

with open(sys.argv[2], 'w') as wf:
    for sq in sampled_qids:
        si = es.search(index="python-code", q="question_id:{}".format(sq))['hits']['hits'][0]['_source']
        wf.write(json.dumps(si) + "\n")

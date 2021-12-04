import json

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import sys

es = Elasticsearch()

es.indices.delete(index='python-code', ignore=[400, 404])

print(es.indices.create(index='python-code', ignore=400))

jsonl_file = "python_docs.jsonl"

def gendata(filename):
    with open(filename, encoding='utf-8') as jsonl:
        results = []
        for line in jsonl:
            doc = json.loads(line)
            result = {

                    "_index": "python-code",
                    "_type": "document"
            }
            for k, v in doc.items():
                result[k] = v
            results.append(result)
        return results

print(bulk(es, gendata(jsonl_file), index='python-code', doc_type='_doc'))

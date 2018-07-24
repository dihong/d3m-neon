import simplejson
import sys
sys.path.insert(0, "..")
from convert_single_csv import encode_json

fname = 'GroundData/hyper_bands_test.csv'
taskid = 3
with open(fname) as fp:
    fields = fp.read().strip().split('\n')[0].strip().split(',')
columns = [{"colIndex":0, "colName":"crown_id",
            "colType":"integer", "role": ["attribute"]}]
for k, f in enumerate(fields[1:]):
    columns.append({"colIndex": k, "colName": f,
                    "colType":"real", "role": ["attribute"]})
data = encode_json(fname, columns, taskid)
with open('hyper_bands_test.json', 'w+') as fp:
    fp.write(simplejson.dumps(data, indent=4, sort_keys=True))

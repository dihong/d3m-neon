import simplejson
import sys
sys.path.insert(0, "..")
from convert_single_csv import encode_json

fname = 'hyper_bands.csv'
taskid = 3
columns = [{"colIndex":0, "colName":"Band_Number",
            "colType":"string", "role": ["attribute"]},
           {"colIndex":1, "colName":"Band_nanometers",
            "colType":"real", "role": ["attribute"]},
           {"colIndex":2, "colName":"Noise_flag",
            "colType":"integer", "role": ["attribute"]}]
data = encode_json(fname, columns, taskid)
with open('hyper_bands.json', 'w+') as fp:
    fp.write(simplejson.dumps(data, indent=4, sort_keys=True))

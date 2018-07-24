import simplejson
import sys
sys.path.insert(0, "..")
from convert_single_csv import encode_json

fname = 'GroundData/itc_ground_relation_train.csv'
taskid = 2
columns = [{"colIndex":0, "colName": "stem_id",
            "colType":"integer", "role":["attribute"]},
           {"colIndex":1, "colName": "crown_id",
            "colType":"integer", "role":["attribute"]}]
data = encode_json(fname, columns, taskid)
with open('itc_ground_relation_train.json', 'w+') as fp:
    fp.write(simplejson.dumps(data, indent=4, sort_keys=True))

import simplejson
import sys
sys.path.insert(0, "..")
from convert_single_csv import encode_json

fname = 'GroundData/species_id_train.csv'
taskid = 3
columns = [{"colIndex":0, "colName": "crown_id",
            "colType":"integer", "role":["attribute"]},
           {"colIndex":1, "colName": "species",
            "colType":"string", "role":["attribute"]},
           {"colIndex":2, "colName": "genus",
            "colType":"string", "role":["attribute"]},
           {"colIndex":3, "colName": "species_id",
            "colType":"string", "role":["attribute"]},
           {"colIndex":4, "colName": "genus_id",
            "colType":"string", "role":["attribute"]}]
data = encode_json(fname, columns, taskid)
with open('species_id_train.json', 'w+') as fp:
    fp.write(simplejson.dumps(data, indent=4, sort_keys=True))

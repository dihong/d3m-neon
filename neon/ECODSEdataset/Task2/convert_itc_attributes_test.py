import simplejson
import sys
sys.path.insert(0, "..")
from convert_single_csv import encode_json

fname = 'GroundData/itc_attributes_test.csv'
taskid = 2
columns = [{"colIndex":0, "colName": "plot_ID",
            "colType":"string", "role":["attribute"]},
           {"colIndex":1, "colName": "crown_id",
            "colType":"integer", "role":["attribute"]},
           {"colIndex":2, "colName": "ITC_E",
            "colType":"real", "role":["attribute"]},
           {"colIndex":3, "colName": "ITC_N",
            "colType":"real", "role":["attribute"]}]
data = encode_json(fname, columns, taskid)
with open('itc_attributes_test.json', 'w+') as fp:
    fp.write(simplejson.dumps(data, indent=4, sort_keys=True))

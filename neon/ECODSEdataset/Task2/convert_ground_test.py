import simplejson
import sys
sys.path.insert(0, "..")
from convert_single_csv import encode_json

fname = 'GroundData/ground_test.csv'
taskid = 2
columns = [{"colIndex":0, "colName": "stem_id",
            "colType":"integer", "role":["attribute"]},
           {"colIndex":1, "colName": "tag_N",
            "colType":"real", "role":["attribute"]},
           {"colIndex":2, "colName": "tag_E",
            "colType":"real", "role":["attribute"]},
           {"colIndex":3, "colName": "height",
            "colType":"real", "role":["attribute"]},
           {"colIndex":4, "colName": "diameter",
            "colType":"real", "role":["attribute"]},
           {"colIndex":5, "colName": "cr_max",
            "colType":"real", "role":["attribute"]},
           {"colIndex":6, "colName": "cr_perp",
            "colType":"real", "role":["attribute"]}]
data = encode_json(fname, columns, taskid)
with open('ground_test.json', 'w+') as fp:
    fp.write(simplejson.dumps(data, indent=4, sort_keys=True))

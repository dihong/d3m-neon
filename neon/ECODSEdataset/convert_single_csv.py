import simplejson
import sys

assert len(sys.argv)==2, "please specify relative path of csv file."

csv_file = sys.argv[1]
datasetID = 'ECODSE_' + csv_file.split('/')[-1].split('.')[0]
columns = []
data = {
    "about":{
        "datasetID": datasetID,
        "datasetName": datasetID,
        "license": "",
        "approximateSize": "",
        "datasetVersion": "1.0",
        "datasetSchemaVersion": "1.0",
        "redacted": True
    },
    "dataResources":[
        {
            "resID": "0",
            "resPath": csv_file,
            "resType": "table",
            "resFormat": ["text/csv"],
            "isCollection": True,
            "columns":[
                {
                    "colIndex": 0,
                    "colName": "X",
                    "colType": "real",
                    "role": ["attribute"]
                },
                {
                    "colIndex": 1,
                    "colName": "Y",
                    "colType": "real",
                    "role": ["attribute"]
                },
                {
                    "colIndex": 2,
                    "colName": "Z",
                    "colType": "real",
                    "role": ["attribute"]
                }
            ]
        }
    ]
}

for c in collections:
    data = convert(c)
    with open('%s.json'%c, 'w+') as fp:
        fp.write(simplejson.dumps(data, indent=4, sort_keys=True))

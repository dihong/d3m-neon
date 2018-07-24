import simplejson

collections = ['pointCloud']
datasetID_prefix = 'ECODSE_'

def convert(collection):
    data = {
        "about":{
            "datasetID": datasetID_prefix+collection,
            "datasetName": collection,
            "license": "",
            "approximateSize": "",
            "datasetVersion": "1.0",
            "datasetSchemaVersion": "1.0",
            "redacted": True
        },
        "dataResources":[
            {
                "resID": "0",
                "resPath": collection,
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
    return data

for c in collections:
    data = convert(c)
    with open('%s.json'%c, 'w+') as fp:
        fp.write(simplejson.dumps(data, indent=4, sort_keys=True))

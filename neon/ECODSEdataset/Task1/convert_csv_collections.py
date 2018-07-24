import simplejson

collections = ['ITC']
datasetID_prefix = 'ECODSE_Task1_'

def convert():
    data = {
        "about":{
            "datasetID": datasetID_prefix+"ITC",
            "datasetName": "ITC",
            "license": "",
            "approximateSize": "",
            "datasetVersion": "1.0",
            "datasetSchemaVersion": "1.0",
            "redacted": True
        },
        "dataResources":[
            {
                "resID": "0",
                "resPath": "ITC_csv",
                "resType": "table",
                "resFormat": ["text/csv"],
                "isCollection": True,
                "columns":[
                    {
                        "colIndex": 0,
                        "colName": "crown_id",
                        "colType": "integer",
                        "role": ["attribute"]
                    },
                    {
                        "colIndex": 1,
                        "colName": "confidence",
                        "colType": "string",
                        "role": ["attribute"]
                    },
                    {
                        "colIndex": 2,
                        "colName": "Plot_ID",
                        "colType": "string",
                        "role": ["attribute"]
                    },
                    {
                        "colIndex": 3,
                        "colName": "kmlgeometry",
                        "colType": "string",
                        "role": ["attribute"]
                    }
                ]
            }
        ]
    }
    return data

data = convert()
with open('ITC.json', 'w+') as fp:
    fp.write(simplejson.dumps(data, indent=4, sort_keys=True))

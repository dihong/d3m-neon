import simplejson

datasetID = 'ECODSE_Task3_hyper_bands_train'

columns = []

with open('GroundData/hyper_bands_train.csv') as fp:
    fields = fp.read().strip().split('\n')[0].strip().split(',')
for k, f in enumerate(fields):
    columns.append({"colIndex": k, "colName": f,
                    "colType":"real", "role": ["attribute"]})
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
            "resPath": "GroundData/hyper_bands_train.csv",
            "resType": "table",
            "resFormat": ["text/csv"],
            "isCollection": False,
            "columns":columns
        }
    ]
}

with open('hyper_bands_train.json', 'w+') as fp:
    fp.write(simplejson.dumps(data, indent=4, sort_keys=True))


def encode_json(fpath, columns, taskid):
    ## Inputs:
    #  ----------
    #  fpath (string): relative path of csv file, e.g. 'GroundData/species_id_train.csv'
    #  columns (list of dict): fields of csv file.
    #  taskid (integer): task id number, e.g. 1, 2, or 3.
    ## Outputs:
    #  ----------
    #  [1] Dictionary

    fname = fpath.split('/')[-1].split('.')[0]
    datasetID = 'ECODSE_Task%d_%s' % (taskid, fname)
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
                "resPath": fpath,
                "resType": "table",
                "resFormat": ["text/csv"],
                "isCollection": False,
                "columns":columns
            }
        ]
    }
    return data

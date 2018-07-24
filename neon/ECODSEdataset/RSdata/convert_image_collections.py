"""
This script creates a .json d3m data schema for a collection of images.
"""

import simplejson
datasetID_prefix = 'ECODSE_'
collections = [('camera', 'tif'), ('chm', 'tif'), ('hs', 'tif')]


def convert(collection, ext):
    data = {"about":
            {
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
                    "resType": "image",
                    "resFormat": ["image/%s"%ext],
                    "isCollection": True
                }
            ]
           }
    return data

for c,t in collections:
    data = convert(c, t)
    with open('%s.json'%c, 'w+') as fp:
        fp.write(simplejson.dumps(data, indent=4, sort_keys=True))

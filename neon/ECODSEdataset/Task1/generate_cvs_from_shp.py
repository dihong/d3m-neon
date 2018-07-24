import ogr
import csv
import sys
from glob import glob
import os

# Ref: https://gis.stackexchange.com/questions/19163/convert-shapefile-to-csv-including-attributes-and-geometry


def convert_shp_to_csv(shpfile):
    outfile = os.path.join('ITC_csv', shpfile.split('/')[-1].split('.')[0]+".csv")
    csvfile = open(outfile, 'wb')
    ds = ogr.Open(shpfile)
    lyr = ds.GetLayer()
    # Get field names
    dfn = lyr.GetLayerDefn()
    nfields = dfn.GetFieldCount()
    fields = []
    for i in range(nfields):
        fields.append(dfn.GetFieldDefn(i).GetName())
    fields.append('kmlgeometry')
    csvwriter = csv.DictWriter(csvfile, fields)
    try:
        csvwriter.writeheader()  # python 2.7+
    except:
        csvfile.write(','.join(fields) + '\n')
    # Write attributes and kml out to csv
    for feat in lyr:
        attributes = feat.items()
        geom = feat.GetGeometryRef()
        attributes['kmlgeometry'] = geom.ExportToKML()
        csvwriter.writerow(attributes)
    # clean up
    del csvwriter, lyr, ds
    csvfile.close()

for shpfile in glob("ITC/*.shp"):
    convert_shp_to_csv(shpfile)


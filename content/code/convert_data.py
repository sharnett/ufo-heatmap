#!/usr/bin/python2.7

from avro.datafile import DataFileReader
from avro.io import DatumReader
from pandas import DataFrame

avro_file = '/Users/srharnett/Downloads/ufo_data/ufo_awesome.avro'
reader = DataFileReader(open(avro_file, 'r'), DatumReader())
df = DataFrame(list(reader))
df.to_pickle('ufo_data.pkl')
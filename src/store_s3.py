import math, os
import boto
from filechunkio import FileChunkIO
from boto.s3.key import Key

#Enviornment variables are used for access key and pair

boto.set_stream_logger('boto')

#S3 Connection
con = boto.connect_s3()
buck = con.get_bucket('boto-demo-1442166850')


#Get File info
source_path = 'tech.jpg'

k = Key(buck)
k.key = source_path
k.set_contents_from_filename(source_path)

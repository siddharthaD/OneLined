import math, os
import boto
from filechunkio import FileChunkIO


#S3 Connection
con = boto.connect_s3()
buck = con.get_bucket('boto-demo-1442166850')

#Get File info
source_path = 'alamoda.mp4'
source_size = os.stat(source_path).st_size

#create a multipart upload request
mp = buck.initiate_multipart_upload(os.path.basename(source_path))

#Use a chuck size of 1MB
chunk_size = 1024 * 1024
chunk_count = int(math.ceil(source_size / float(chunk_size)))


#Set bytes
for i in range(chunk_count):
	offset = chunk_size * i
	print '*'
	bytes  = min(chunk_size, source_size - offset)
	with FileChunkIO(source_path, 'r', offset=offset,
			bytes=bytes) as fp:
		mp.upload_part_from_file(fp, part_num=i + 1)

mp.complete_upload()

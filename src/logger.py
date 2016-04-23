import math, os, time
import boto
import boto.sqs
from boto.s3.key import Key
from  boto.sqs.message import Message

#Constants
REGION    = 'ap-southeast-1'
LOG_FILE  = ''
LOG_FILE_PATH = ''
LOG_QUEUE = 'LogQueue'
LOG_BUCK  = 'onelinedlogs'

print 'Initializing LOG job', time.strftime("%d/%m/%Y %H:%M")
#initializations
if LOG_FILE == '':
	LOG_FILE = 'olgapp' + time.strftime("%d%m%Y_%H") + '.dat'

if LOG_FILE_PATH == '':
	LOG_FILE_PATH = '/tmp/'
print 'Reading ', LOG_QUEUE
#Connect to SQS and get messages from LOG_QUEUE
sqs_conn = boto.sqs.connect_to_region(REGION)
#print conn.get_all_queues()

my_queue = sqs_conn.get_queue(LOG_QUEUE)

#Write temperary messages to log queue 
#msg      = Message()
#msg.set_body('another test message 2')
#my_queue.write(msg)

print 'Writing Messages to Local file', LOG_FILE
#Read Messages from SQS LogQueue
rs = my_queue.get_messages()
count =  len(rs)
#print count  #number of message

#Get File info
source_path = LOG_FILE_PATH + LOG_FILE

#write each message
#with open(source_path,'a+') as f:
#       for msg in rs:
#               f.write(msg.get_body())
#               my_queue.delete_message(msg)

#write all messages at one go
my_queue.dump(source_path, sep='\n')

print 'Deleting messages read from', LOG_QUEUE
#Delete the messages already read
my_queue.delete_message_batch(rs)

#"After dumping the queue purge it
#my_queue.purge()
#read messages from local file
#with open('test1','r') as rf:
#       print rf.read()
#Enviornment variables are used for access key and pair

#S3 Connection
s3_con = boto.connect_s3()
buck   = s3_con.get_bucket(LOG_BUCK)

print 'Writing Log File to S3 Bucket: %s.', LOG_BUCK
k = Key(buck)
k.key = LOG_FILE
k.set_contents_from_filename(source_path)
print 'Job Completed at: %s', str(time.strftime("%d/%m/%Y %H:%M"))                                                    

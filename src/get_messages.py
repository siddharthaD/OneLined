import boto.sqs
import boto
from  boto.sqs.message import Message

conn = boto.sqs.connect_to_region('ap-southeast-1')
#print conn.get_all_queues()

my_queue = conn.get_queue('LogQueue')

#msg      = Message()
#msg.set_body('another test message 2')
#my_queue.write(msg)

#Read Messages from SQS LogQueue
rs = my_queue.get_messages()
count =  len(rs)
print count  #number of message

#write each message
#with open('test1','a+') as f:
#	for msg in rs:
#		f.write(msg.get_body())
#		my_queue.delete_message(msg)
#write all messages at one go
my_queue.dump('test2.dat', sep='\n')

#"After dumping the queue purge it
#my_queue.purge()
#read messages from local file
#with open('test1','r') as rf:
#	print rf.read()

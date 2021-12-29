import requests
import numpy as np
import csv  
import re

#Add URL here#
url=["https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt","https://raw.githubusercontent.com/pallebone/StrictBlockPAllebone/master/BlockIP.txt","https://raw.githubusercontent.com/ktsaou/blocklist-ipsets/master/firehol_level1.netset","https://www.spamhaus.org/drop/edrop.txt","https://www.spamhaus.org/drop/drop.txt"]
#Don't change this list#
IP_List=[]

#for loop for all the URLs#
for i_url in url:
#Curl the list from the web#
	read = requests.get(i_url)
#Format it to a list format#
	text_read=(read.text)
	Sort_list=text_read.split("\n")
	for item in Sort_list:
			IP_List.append(item)

#Sort the list to new lines#
text = '\n'.join(IP_List)

#Get only IPV4#
IP_V4 = re.findall( r'[0-9]+(?:\.[0-9]+){3}', text )

#Dedup list#
List_Dedup = list(dict.fromkeys(IP_V4))

#Add a line and sort it for the last time#
IP_LIST_GO = '\n'.join(List_Dedup)


# from the numpy module to created a cvs file
rows = [IP_LIST_GO]
# from the numpy module to created a cvs file
with open("Bad_IP.csv", "w") as f:
	np.savetxt(f, 
           rows,
   	      delimiter ="", 
       	   fmt ='% s')

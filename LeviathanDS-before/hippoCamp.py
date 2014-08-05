# MICROSOFT DOCX GENERATOR
# REQUIRMENTS
# https://github.com/mikemaccana/python-docx.git
# pip install lxml PIL

from docx import *
import os
import tarfile
import time
import shutil

fileSeedName = 'clusterTesting_50k_set_'
dataStorageDirectory = 'data'
timeStamp = int(time.time())
tarFilename = fileSeedName + str(timeStamp) + ".tar.gz"
relationships = relationshiplist()
appprops = appproperties()
contenttypes = contenttypes()
websettings = websettings()
wordrelationships = wordrelationships(relationships)

#Create data directory if it does not exists
if not os.path.exists(dataStorageDirectory):
	os.mkdir(dataStorageDirectory)






#File Generator 

for x in range(0,10):
	document = newdocument()
	body = document.xpath('/w:document/w:body', namespaces=nsprefixes)[0]

	#Append two headers and a paragraph
	body.append(heading("Encasereview Clustering Test Document",1))
	body.append(heading("Legal Car Cat <= Search Vectors",2))
	body.append(paragraph('This file was generated using python, no need to  COM, .NET, Java. Keeping it  simple since 90s :).'))

	title = 'Cluster Testing Document'
	subject = 'A test file generated by SQA Don Johnson (Written in Python)'
	creator = 'Don Johnson'
	keywords = ['cluster','testing','python']

	coreprops = coreproperties(title=title, subject=subject, creator=creator, keywords=keywords)



	#save document
	savedocx(document,coreprops, appprops, contenttypes, websettings, wordrelationships,'data/{}_{}.docx'.format(fileSeedName,x))


tar = tarfile.open("{}".format(tarFilename),"w:gz")
tar.add("data/", arcname="{}".format(tarFilename))
tar.close()

#remove Data Directory
shutil.rmtree(dataStorageDirectory)





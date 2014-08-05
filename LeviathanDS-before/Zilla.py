# MICROSOFT XLSX GENERATOR
# REQUIRMENTS
# pip install xlsxwriter
import xlsxwriter
import os
import tarfile
import time
import shutil
import random


fileSeedName = 'ClusterTesting_xlsx_set'
dataStorageDirectory = 'xlsdata'
timeStamp = str(time.time())
tarFilename = fileSeedName + timeStamp + ".tar.gz"


#creating folder if  it does not exist
if not os.path.exists(dataStorageDirectory):
    os.mkdir(dataStorageDirectory)


#File generator

for x in range(0,10000):
    workbook = xlsxwriter.Workbook('{}/{}_{}.xlsx'.format(dataStorageDirectory,fileSeedName, x))
    worksheet = workbook.add_worksheet()

    #some random data to  write to worklist
    expenses = (
        ['Rent', '{}'.format(random.randint(1,2000))],
        ['Gas', '{}'.format(random.randint(20,4000))],
        ['Food', '{}'.format(random.randint(40,1000))],
        ['Gym', '{}'.format(random.randint(100,400))],
        )

    row = 0
    col = 0

    for item, cost in (expenses):
        worksheet.write(row, col, item)
        worksheet.write(row, col + 1, cost)
        row += 1

    worksheet.write(row, 0, 'Total')
    worksheet.write(row, 1, '=SUM(B1:B4)')
    workbook.close()


#Tar Archive
tar = tarfile.open("{}".format(tarFilename),"w:gz")
tar.add("xlsdata",arcname="{}".format(tarFilename))
tar.close()

shutil.rmtree(dataStorageDirectory)
print("XLSX GENERATION COMPLETE")
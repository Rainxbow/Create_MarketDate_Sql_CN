import os
import csv
import sys

f=open('output.txt','w+')
old= sys.stdout
sys.stdout=f


path = r'./name'
for filename in os.listdir(path):
	print(filename.split('.')[0],end='')
	csv_reader = csv.reader(open('/home/funny/Desktop/name/%s'%filename,encoding='KOI8-R'))
	f_list = list(csv_reader)
	fx = f_list[0][1]
	print("_%s"%fx)

f.close()

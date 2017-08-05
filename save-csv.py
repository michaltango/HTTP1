import csv, os.path, socket
url = "http://192.168.100.20:8080/file1.csv"
header_in_csv = True

import sys
#print(sys.argv[1])

def displaycsv(filename):
    #Open CSV file - Source
	with open('file1.csv', 'r') as csvfile, open('outputfile.csv', 'w') as output:
		reader = csv.DictReader(csvfile)
		#writer = csv.DictWriter(output)
		header = reader.fieldnames
		for row in reader:
				print()
				for head in header:
					print(head + ":" + row[head])
		
		#print(header)
	return 1
	
def updatecsv(routername,details):
    #Open CSV file - Source
	with open('file1.csv', 'r') as csvfile, open('outputfile.csv', 'w') as output:
		reader = csv.DictReader(csvfile)
		#writer = csv.DictWriter(output)
		header = reader.fieldnames
		type = "dasdas"
		
		for sysarg in range(2,len(sys.argv)):
			print(sysarg)
			uppdatefield = sys.argv[sysarg]
			updatevalue = sys.argv[sysarg].split()
			sysarg = sysarg + 1
			
			
		if type in header:
			print(type)
		else:
			header.append(type)
		
		
		#for row in reader:
		#	if row[name] == routername:
		#		for head in header:
				
					
		
		print(header)
	return 1

if len(sys.argv) > 1:
	action = sys.argv[1]
	if action == "show":
		displaycsv("file1.csv")
	elif action == "update":
		updatecsv("das","dsadsa")
	else:
		print("Usage: " + sys.argv[0] + " [show|update]")
else:
	print("Usage: " + sys.argv[0] + " [show|update]")
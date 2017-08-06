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
	#os.remove('outputfile.csv')
	with open('file1.csv', 'r') as csvfile, open('outputfile.csv', 'w+') as output:
		reader = csv.DictReader(csvfile)
		header = reader.fieldnames
		
		#Extract argument lists from command line and save to dictionary
		updatefield = {}
		for sysarg in range(3,len(sys.argv)):
			argument = sys.argv[sysarg].split(":")
			updatefield[argument[0]] = argument[1]
			sysarg = sysarg + 1
			
		
		#Append new fields to a header list 
		for field, value in updatefield.items():
			if  field not in header:
				header.append(field)
			

			
				#Save new file to a temp location
		writer = csv.DictWriter(output,fieldnames=header)
		writer.writeheader()
		
		
		#Iterate through CSV file and update router row
		for row in reader:
			if row["name"] == routername:
				for head in header: 
					if head != "name" and head in updatefield.keys():
						row[head] = updatefield[head]
			print(row)
			writer.writerow(row)
		
	output.close()
	csvfile.close()
	os.remove('file1.csv')
	os.rename('outputfile.csv','file1.csv')
						
		#		for head in header:
				
					
		
#		print(header)
	return 1

if len(sys.argv) > 1:
	action = sys.argv[1]
	if action == "show":
		displaycsv("file1.csv")
	elif action == "update":
		updatecsv(sys.argv[2],"dsadsa")
	else:
		print("Usage: " + sys.argv[0] + " [show|update] routername argument:value")
else:
	print("Usage: " + sys.argv[0] + " [show|update] routername argument:value")
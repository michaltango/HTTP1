import csv, os.path, socket
url = "http://192.168.100.20:8080/file1.csv"
header_in_csv = True

import sys
print(sys.argv[1])

def displaycsv(filename):
    #Open CSV file - Source
	with open('file1.csv', 'r') as csvfile, open('outputfile.csv', 'w') as output:
		reader = csv.DictReader(csvfile)
		writer = csv.DictWriter(output)
		header = reader.fieldnames
		print(header)



	return 1

print(displaycsv("file1.csv"))


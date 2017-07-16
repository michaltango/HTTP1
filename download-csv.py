import urllib.request
url = "http://172.16.3.1:8080/file1.csv"

header_in_csv = True
position = list()
csvfilename = url.split('/')[-1] + ".csv"
response = urllib.request.urlopen(url)

file = open("csvfilename",'wb')
content = response.read()
file.write(content)

file.close()


file = open("csvfilename",'r')

if header_in_csv:
   headerline = file.readline()
   headers = headerline.split(',')

for head in headers:
    print("##" + head + "##")
    
for line in file:
    line = line.rstrip()
    print(line)

file.close()

#for line in content:
#    print(line)


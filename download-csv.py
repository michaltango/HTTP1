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
    


for line in file:
     print(line)



#for line in content:
#    print(line)


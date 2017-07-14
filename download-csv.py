import urllib.request
url = "https://github.com/michaltango/Python1/blob/master/file1.csv"

csvfilename = url.split('/')[-1]
response = urllib.request.urlopen(url)

print (csvfilename)



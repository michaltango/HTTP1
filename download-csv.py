import urllib
url = "https://github.com/michaltango/Python1/blob/master/file1.csv"

csvfilename = url.split('/')[-1]
httpsession = urllib.urlretrieve(url)

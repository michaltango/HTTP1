import urllib.request
from urllib.error import URLError, HTTPError
import csv, os.path, socket
url = "http://172.16.3.1:8080/file1.csv"
header_in_csv = True


#Download file from given url and save to current directory 

def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True

def download_csv(url):
    position = list()
    csvfilename = url.split('/')[-1]

    #Try to open URL, return error codes
    try:
        response = urllib.request.urlopen(url)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
        return "Error accessing file."
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
        return "Error connecting."
    else:
        print(response.info())
        csvfile_size = response.getheader("Content-Length")
        print("File size: " + csvfile_size)

        #Define size of buffer
        csvfile_buffer = int(csvfile_size) / 10 
        csvfile_buffer = int(csvfile_buffer)

        #Open file and write content to it
        file = open(csvfilename,'wb')
        content = response.read(csvfile_buffer)
        print("Writing: ",end='')
        while content:
            file.write(content)
            print("#",end='')
            content = response.read(csvfile_buffer)
        file.close()

    return csvfile_size

def displaycsv(filename):
    print("\nDevices:")
    #Open CSV file - Source
    with open(filename,mode='r') as csvfile:
        file = csv.DictReader(csvfile)
        #Open inventory file when we write
        with open('inventory', 'w') as invfile:
                    
            for row in file:    

                port = row['port']
                name = row['name']
                ipaddr = row['IP']
                if port.isdigit() and is_valid_ipv4_address(ipaddr):
                    
                    port = int(port)
                    invfile.write(name + " " + ipaddr + ":" + repr(port) + "\n")
                else:
                    print(name + ": Wrong data type")
                
    return 1

download_csv(url)
print(displaycsv("file1.csv"))

#for line in content:
#    print(line)


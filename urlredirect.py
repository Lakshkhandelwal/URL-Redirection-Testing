from urlparse import urlparse
import urllib2
import socket
import requests
import sys

def check_connectivity(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((str(host), int(port)))
        s.close()
    except socket.timeout:
        print("Failed to connect to %s:%s" %(host,port))
        return False
    except:
        print("Failed to connect to %s:%s" % (host, port))
        return False

    return True

args = sys.argv
inputFile = args[1]
urls = open(str(inputFile),"r")
fileout = open("output.csv","a")
fileout.write("Request Code,Verified or Not,Origin URL,End URL")
fileout.write("\n")

for url in urls:
    port = 80
    if urlparse(url)[0] == "https":
        port = 443
    elif urlparse(url)[0] == "http":
        port = 80
    if check_connectivity(urlparse(url)[1],port):
        try:
            url = url.strip()
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            print "orig url: "+urlparse(url)[1]
            print "redirect url: "+urlparse(response.geturl())[1]
            if str(urlparse(url)[1]) == str(urlparse(response.geturl())[1]):
                r = requests.head(url)
                fileout.write(str(r.status_code)+",Redirect Not Found,"+url+","+str(urlparse(response.geturl())[1]))
                fileout.write("\n")
                print url
            else:
                if str(urlparse(url)[1]) in str(urlparse(response.geturl())[1]):
                    r = requests.head(url)
                    fileout.write(str(r.status_code)+",Redirect Not Found,"+url+","+str(urlparse(response.geturl())[1]))
                    fileout.write("\n")
                else:
                    r = requests.head(url)
                    fileout.write(str(r.status_code)+",Redirect Found,"+url+","+str(urlparse(response.geturl())[1]))
                    fileout.write("\n")
                    print url
        except:
            fileout.write("404"+",Could not connect to the Website,"+url+","+str(urlparse(response.geturl())[1]))
            fileout.write("\n")
            print url

fileout.close()
urls.close()

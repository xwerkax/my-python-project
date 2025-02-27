import os, sys
import urllib.parse
import validators
import requests
from datetime import datetime

print("Number of arguments: ", len(sys.argv))

print("Arguments list: ", sys.argv)

url = "https://duckduckgo.com"
if len(sys.argv) > 1 :
    url = sys.argv[1]

print("Website to download:", url)

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)
print("current working directory:", os.getcwd())

if not os.path.exists("./websites"):
    os.mkdir("websites")

parseURL = urllib.parse.urlparse(url)
print(parseURL)

validFlag = validators.url(url)
if validFlag:
    print("Url:", url, "is valid")
else:
    print("Url:", url, "is not valid.")

response = requests.get(url, allow_redirects=True )
if response.ok == True:
    print("Reponse is ok from server for url:", url)
    now = datetime.now()
    dateString = now.strftime("%d.%m.%Y %H.%M")
    print(dateString)
    fileName = "./websites/" + parseURL.netloc +" "+ dateString + ".html"
    print(fileName)
    fh = open(fileName, "wb")
    fh.write(response.content)
    fh.close()
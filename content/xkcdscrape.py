import urllib.request, urllib.parse
from urllib.request import urlopen
import ssl
import xml.etree.ElementTree as ET
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://xkcd.com/atom.xml"
uh = urllib.request.urlopen(url)
xml = uh.read()
#print(xml.decode())
tree = ET.fromstring(xml)
#print(tree)
imglst=list()
for entry in tree.findall("{http://www.w3.org/2005/Atom}entry"):
    summary = entry.find("{http://www.w3.org/2005/Atom}summary").text
    #print(summary)
    imgsrc = re.findall("(https\S+png)",summary)[0]
    #print(imgsrc)
    imgsrc_str = str(imgsrc)
   # print(type(imgsrc_str))
    imglst.append(imgsrc_str)
pic1 = imglst[0]
urllib.request.urlretrieve(pic1, "xkcd_daily.png")



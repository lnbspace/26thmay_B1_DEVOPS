#!/usr/bin/python3

import  time,cgi,subprocess,os

print("Content-Type: text/html")
print("")

print("<h1> Hello WORLd </h1>")

data="""
<html>
    <h1>  Hye Docker  </h1>
    <input>
    <input>
    <input>
    <input>
    <input>
    <input>
</html>
"""
print(data)
ox=subprocess.getoutput('date')
print("<h1>",ox,"</h1>")

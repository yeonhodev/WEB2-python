#!/usr/bin/env python3

import cgi, os

form = cgi.FieldStorage()
pageId = form["pageId"].value

os.remove('data/'+pageId+'.html')

#Redirection
print("Location: index.py")
print()
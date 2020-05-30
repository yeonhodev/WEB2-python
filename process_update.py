#!/usr/bin/env python3

import cgi, os

form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form["description"].value

opened_file = open('data/'+pageId+'.html', 'w')
opened_file.write(description)

os.rename('data/'+pageId+'.html', 'data/'+title+'.html')

#Redirection
print("Location: index.py?id="+title)
print()
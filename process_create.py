#!/usr/bin/env python3

import cgi

form = cgi.FieldStorage()
title = form["title"].value
description = form["description"].value

opened_file = open('data/'+title+'.html', 'w')
opened_file.write(description)

#Redirection
print("Location: index.py?id="+title)
print()
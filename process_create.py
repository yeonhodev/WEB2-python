#!/usr/bin/env python3
print("content-type:text/html; charset=utf-8\n")

import cgi

form = cgi.FieldStorage()
title = form["title"].value
description = form["description"].value

opened_file = open('data/'+title+'.html', 'w')
opened_file.write(description)

#Redirection

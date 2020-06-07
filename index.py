#!/usr/bin/env python3
print("content-type:text/html; charset=utf-8\n")

import cgi, os, view
from html_sanitizer import Sanitizer
sanitizer = Sanitizer()

form = cgi.FieldStorage()

if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId+'.html', 'r').read()
    # description = description.replace('<', '&lt;')
    # description = description.replace('>', '&gt;')
    # description = sanitizer.sanitize(description)
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    pageId = 'Dev Blog'
    description = 'Hello, blog'
    update_link = ''
    delete_action = ''

print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>yeonhodev.github.io</title>
</head>
<body>
    <h1><a href="index.py">yeonhodev.github.io</a></h1>
    <ol>
        <li>Dev</li>
            <ol>
                <li>OS</li>
                    <ol>
                        <li>Mac</li>
                        <li>Windows</li>
                        <li><a href="index.py?id=linux">Linux</a></li>
                    </ol>
                <li>WEB</li>
                    <ol>
                        <li>HTML</li>
                        <li>CSS</li>
                        <li>JavaScript</li>
                        <li>SQL</li>
                        <li><a href="index.py?id=python">Python</a></li>
                    </ol>
                <li>Mobile</li>
                <li>LANGUAGES</li>
                    <ol>
                        <li>Python</li>
                    </ol>
                <li>Git</li>
            </ol>
    </ol>
    <ol>
        {listStr}
    </ol>
    <a href="create.py">create</a>
    {update_link}
    {delete_action}
    <h2>{title}</h2>
    <p>{desc}</p>
</body>
</html>
'''.format(
    title=pageId, 
    desc=description, 
    listStr=view.getList(), 
    update_link=update_link, 
    delete_action=delete_action
    ))
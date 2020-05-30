#!/usr/bin/env python3
print("content-type:text/html; charset=utf-8\n")

import cgi, os

files = os.listdir('data')
listStr = ''
for item in files:
    file_name = os.path.splitext(item)[0]
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=file_name)

form = cgi.FieldStorage()

if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId+'.html', 'r').read()
else:
    pageId = 'Dev Blog'
    description = 'Hello, blog'

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
    <form action="process_update.py" method="POST">
        <input type="hidden" name="pageId" value="{form_default_title}"
        <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
        <p><textarea name="description" id="" rows="4" placeholder="description">{form_default_description}</textarea></p>
        <p><input type="submit"></p>
    </form>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr, form_default_title=pageId, form_default_description=description))
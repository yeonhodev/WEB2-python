#!/usr/bin/env python3
print("content-type:text/html; charset=utf-8\n")
import cgi
form = cgi.FieldStorage()
pageId = form["id"].value
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
    <h2>{title}</h2>
    <p>I would like to be a programmer.</p>
</body>
</html>
'''.format(title=pageId))
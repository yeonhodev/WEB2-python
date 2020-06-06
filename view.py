import os

def getList():
    files = os.listdir('data')
    listStr = ''
    for item in files:
        file_name = os.path.splitext(item)[0]
        listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=file_name)
    return listStr
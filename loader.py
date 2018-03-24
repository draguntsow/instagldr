import re
import urllib.request
import os

def scan(filename):
    with open(filename) as html:
        raw = html.read()

    link_pattern = r'display_url":".*?.jpg"'
    links = re.findall(link_pattern, raw, re.MULTILINE)

    for i in range(len(links)):
        links[i] = links[i][14:(len(links[i])-1)]

    return links

def load(links, fold=''):
    if fold == '':
        fold = os.getcwd()

    index = 1
    for link in links:
        urllib.request.urlretrieve(link, fold+'\\'+str(index)+'.jpg')
        index+=1

'''
Main package of the instagloader.
Allows to download all photos from the page at the moment.

TODO:
Create a console-launch mode (maybe in other package?);
More precise and scalable loading settings are needed;
Direct load the html-page in-box needed (the authentication support will be required);
Verbose mode also will be helpful;
More than 20 photos per one loading is neccessary;

BUG:
Last one or two downloaded photos are not presented on the page given,
but exist in code and, of course, are downloaded by the utility.
'''

import re
import urllib.request
import os

#Scanning document function for finding direct photos URLs
def scan(filename):
    with open(filename) as html:
        raw = html.read()

    link_pattern = r'display_url":".*?.jpg"'
    links = re.findall(link_pattern, raw, re.MULTILINE)

    for i in range(len(links)):
        links[i] = links[i][14:(len(links[i])-1)]

    return links

#Loading function is used for download photos by links retrieved from scan()
def load(links, fold=''):
    if fold == '':
        fold = os.getcwd() #if the directory is not specified, the current one will be used

    index = 1
    for link in links:
        urllib.request.urlretrieve(link, fold+'\\'+str(index)+'.jpg')
        index+=1

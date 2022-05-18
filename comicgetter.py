# TUI App to get comics from mycomiclist.com
#

# Ask for the comic name

import requests 
import re
import os

comic_name = input("What comic do you want to search for? ")

MainComicURL = "https://mycomiclist.com/comic/" + comic_name

# select the UL element with the class basic list
# and then put each element in a list
ComicList = []
maintext = requests.get(MainComicURL).text
exp = re.compile('''<a class="ch-name" href="(.*?)">(.*?)</a>''')
ComicList = exp.findall(maintext)

# print the list
print("\nHere are the results:")
for i in range(len(ComicList)):
    print(i+1, ComicList[i][1])
    print("\n")

# ask for the comic number
comic_number = int(input("Which comic do you want to download? 0 means all"))

def get_comic(url, ComicName):
    r = requests.get(url)
    exp = re.compile(r'https://2.bp.blogspot.com/[^"]+"')
    # apply the regex to the response
    imgs = exp.findall(r.text)
    if not os.path.exists(ComicName):
        os.mkdir(ComicName)
    # download all images using wget
    for idx,img in enumerate(imgs):
        os.system("wget "+ img[:-1] + " -O "+ComicName+"/img"+str(idx)+".jpg")

if comic_number == 0:
    for i in range(len(ComicList)):
        get_comic(ComicList[i][0], ComicList[i][1])
        os.system("convert -delay 10 -loop 0 {}/*.jpg {}.pdf".format(ComicList[i][1],ComicList[i][1]))
else:
    get_comic(ComicList[comic_number-1][0], ComicList[comic_number-1][1])
    os.system("convert -delay 10 -loop 0 {}/*.jpg {}.pdf".format(ComicList[i][1],ComicList[i][1]))


# convert to pdf

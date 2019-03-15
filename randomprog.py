from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
html= urlopen("https://www.avito.ru/moskva?s_trg=3&q=pivas")
bsObj= BeautifulSoup(html.read())
def GetContent():
    textcontent=bsObj.findAll("div",{"class":"description item_table-description"})
    for contentList in textcontent:
        Newcontent=""
        Newcontent=Newcontent+str(textcontent)
    return textcontent
def GetImageContent():
    imagecontent=bsObj.findAll("img",{"class":"photo-count-show large-picture-img"})
    path=""
    output = [x["src"] for x in imagecontent]
    for image in imagecontent :
    #    imageurl=imagecontent["src"]
    #    path='<img src="https:'+str(imageurl)+'"/>'
    #return path
def Filewriting():
    filename='index.html'
    with open(filename,'w') as file_object:
        file_object.write('<html lang="ru" dir="ltr"><head><meta charset="utf-8">')
        file_object.write(GetContent())
        file_object.write(str(GetImageContent()))
print(GetContent())
print(GetImageContent())

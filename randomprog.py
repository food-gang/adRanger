from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
query=input("Enter value ")
html= urlopen("https://www.avito.ru/moskva?s_trg=3&q="+str(query))
bsObj= BeautifulSoup(html)
#print(bsObj.prettify())
def GetContent():
    textcontent=bsObj.findAll("div",{"class":"description item_table-description"})
    for contentList in textcontent:
        Newcontent=""
        Newcontent=Newcontent+str(textcontent)
    return textcontent
def GetPrice():
    price=bsObj.findAll("span",{"class":"price"})
    return price
def getMetro():
    metro=bsObj.findAll("p",text="м.")
    print(metro)
def GetImageContent():
    imagecontent=bsObj.findAll("img",{"class":"large-picture-img"})
    output = [x["src"] for x in imagecontent]
    return output
def Filewriting():
    filename='index.html'
    with open(filename,'w') as file_object:
        file_object.write('<html lang="ru" dir="ltr"><head><meta charset="utf-8">')
        file_object.write(str(GetContent()))
        imageurl=GetImageContent()
        for image in imageurl:
            file_object.write('<img src ="https:'+str(image)+'"/>\n')
        print("Запись в файл готова")
getMetro()

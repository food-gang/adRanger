from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import json

query=input("Enter value ")
html= urlopen("https://www.avito.ru/moskva?s_trg=3&q="+str(query))
bsObj= BeautifulSoup(html)
#print(bsObj.prettify())
def getPrice():
    prices=bsObj.findAll("span",{"itemprop":"price"})
    price = [x["content"] for x in prices]
    return price
def getMetro():
    place=[]
    metro=bsObj.findAll("div",{"class":"data"})
    for metrolist in metro:
        list=metrolist.findAll("p")
        try:
            place.append(list[1].get_text())
        except:
            break
    return place
def getName():
    names=[]
    name=bsObj.findAll("a",{"class":"item-description-title-link"})
    for namelist in name:
        names.append(namelist.span.get_text())
    return names
def getArray():
    with open("data_file.json", mode='w', encoding='utf-8') as f:
        request={"Запрос":query}
        json.dump(request, f,ensure_ascii=False)
    namespace=getName()
    pricelist=getPrice()
    placelist=getMetro()
    count=-1
    for i in namespace:
        count=count+1
        name=namespace[count]
        price=pricelist[count]
        place=placelist[count]
        place = place.replace(u'\xa0', u' ')
        entry={"name":name,"price":price,"place":place}
        print(entry)
        with open("data_file.json", mode='a',encoding='utf-8') as feedsjson:
            json.dump(entry,feedsjson,ensure_ascii=False)
    return entry
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
print(getArray())

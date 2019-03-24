from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import json

query=input("Enter value ")
query.replace(" ","+")
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
def getHref():
    refs=[]
    href=bsObj.findAll("a",{"class":"item-description-title-link"})
    refs=[x["href"] for x in href]
    return refs
def getArray():
    with open("data_file.json", mode='w', encoding='utf-8') as f:
        request={"Запрос":query}
        json.dump(request, f,ensure_ascii=False)
    namespace=getName()
    pricelist=getPrice()
    placelist=getMetro()
    imageurl=GetImageContent()
    hrefs=getHref()
    count=-1
    for i in namespace:
        count=count+1
        name=namespace[count]
        ref=hrefs[count]
        ref="https://www.avito.ru"+ref
        price=pricelist[count]
        place=placelist[count]
        image=imageurl[count]
        image="https:"+image
        place = place.replace(u'\xa0', u' ')
        entry={"name":name,"ref":ref,"price":price,"place":place,"url":image}
        print(entry)
        with open("data_file.json", mode='a',encoding='utf-8') as feedsjson:
            json.dump(entry,feedsjson,ensure_ascii=False)
    return entry
def GetImageContent():
    out=[]
    imagecontent=bsObj.findAll("ul",{"class":"item-slider-list js-item-slider-list"})
    for image in imagecontent:
        out.append(image.find("img",{"class":"large-picture-img"}))
    output = [x["src"] for x in out]
    return output
print(getArray())

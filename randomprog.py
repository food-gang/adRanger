from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import json
import re
query=input("Enter value ")
query.replace(" ","+")
avito= urlopen("https://www.avito.ru/moskva?s_trg=3&q="+str(query))
youla= urlopen("https://youla.ru/moskva?q="+str(query))
bsAvito= BeautifulSoup(avito)
bsYoula= BeautifulSoup(youla)
#print(bsAvito.prettify())
def getPrice():
    prices=bsAvito.findAll("span",{"itemprop":"price"})
    price = [x["content"] for x in prices]
    return price
def getMetro():
    place=[]
    metro=bsAvito.findAll("div",{"class":"data"})
    for metrolist in metro:
        list=metrolist.findAll("p")
        href=metrolist.findAll("a")
        try:
            list=list[1].get_text()
            list1 = list.replace(u'\xa0', u' ')
            place.append(list1)
        except:
            place.append(href)
    return place
def getName():
    names=[]
    name=bsAvito.findAll("a",{"class":"item-description-title-link"})
    for namelist in name:
        names.append(namelist.span.get_text())
    return names
def getHref():
    refs=[]
    href=bsAvito.findAll("a",{"class":"item-description-title-link"})
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

        entry={"name":name,"ref":ref,"price":price,"place":str(place),"url":image}
        print(entry)
        with open("data_file.json", mode='a',encoding='utf-8') as feedsjson:
            json.dump(entry,feedsjson,ensure_ascii=False)
    namespace=getNameY()
    pricelist=getPriceY()
    placelist=getMetroY()
    imageurl=GetImageContentY()
    hrefs=getHrefY()
    count=-1
    for i in namespace:
        count=count+1
        name=namespace[count]
        ref=hrefs[count]
        ref="https://youla.ru"+ref
        price=pricelist[count]
        place=placelist[count]
        image=imageurl[count]
        #place = place.replace(u'\xa0', u' ')
        entry={"name":name,"ref":ref,"price":price,"place":place,"url":image}
        print(entry)
        with open("data_file.json", mode='a',encoding='utf-8') as feedsjson:
            json.dump(entry,feedsjson,ensure_ascii=False)
    return entry
def GetImageContent():
    out=[]
    imagecontent=bsAvito.findAll("div",{"class":"item-photo"})
    for image in imagecontent:
        out.append(image.find("img",{"src":True}))
    output = [x["src"] for x in out]
    return output
#print(getArray())
def getNameY():
    names=[]
    name=bsYoula.findAll("div",{"class":"product_item__title"})
    for namelist in name:
        names.append(namelist.get_text())
    return names
def getPriceY():
    list=[]
    prices=bsYoula.findAll("div",{"class":"product_item__description"})
    for price in prices:
        listitem=price.find("span",{"class":"rub"}).previous
        listitem=re.sub("\D","",listitem)
        #listitem = listitem.replace(u'\xa0', u' ')
        #listitem = listitem.replace(u" ', '\n ", u' ')
        list.append(int(listitem))
    return list
def getMetroY():
    place=[]
    metro=bsYoula.findAll("span",{"class":"product_item__location"})
    for metrolist in metro:
        list=metrolist.get_text()
        list=re.sub("[^А-Яа-я]","",list)
        place.append(list)
    return place
def getHrefY():
    refs=[]
    href=bsYoula.findAll("li",{"class":"product_item"})
    for ref in href:
        refs.append(ref.find("a",{"title":True}))
    refs=[x["href"] for x in refs]
    return refs
def GetImageContentY():
    out=[]
    imagecontent=bsYoula.findAll("div",{"class":"product_item__image"})
    for image in imagecontent:
        out.append(image.find("img"))
    output = [x["src"] for x in out]
    return output
#print(len(getName()),len(getMetro()),len(getHref()),len(GetImageContent()))
getArray()

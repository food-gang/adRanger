from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import quote
from bs4 import BeautifulSoup
import json
import re
import time
from lxml.html.soupparser import fromstring
#query=input()
def getArray(query,sort,category):
    start_time = time.time()
    #print("--- %s seconds ---" % (time.time() - start_time))
    if int(sort)==2:
        asort="&s=2"
        ysort=""
    elif int(sort)==1:
        asort="&s=1"
        ysort="attributes[sort_field]=price&"
    else:
        asort=""
        ysort=""
    Acategory=""
    Ycategory=""
    categories={0:'transport',1:'nedvizhimost',2:'predlozheniya_uslug',3:'lichnye_veschi',4:'rabota',5:'zhivotnye',6:'dlya_biznesa'}
    for key,value in categories.items():
        if int(key) == int(category):
            Acategory=value
            break;
    avito= urlopen("https://www.avito.ru//moskva/"+quote(str(Acategory))+"?q="+quote(str(query))+quote(str(asort)))
    bsAvito= BeautifulSoup(avito, features = "lxml")
    categories={0:'cars/',1:'nedvijimost?',2:'uslugi?',3:'',4:'rabota?',5:'zhivotnye?',6:'dlya-biznesa?'}
    dc=""
    for key,value in categories.items():
        if int(key) == int(category):
            Ycategory=value
            if Ycategory=='cars/':
                dc="auto."
                if int(sort)==1:
                    ysort="searchOrder=1&"
                elif int(sort)==2:
                    ysort="searchOrder=2&"
            break;
    youla= urlopen("https://"+quote(str(dc))+"youla.ru/moskva/"+quote(str(Ycategory))+"?"+ysort+"q="+quote(str(query)))
    bsYoula= BeautifulSoup(youla, features = "lxml")
    print("--- %s seconds ---" % (time.time() - start_time))
    #with open("static/js/data_file.json", mode='w', encoding='utf-8') as f:
        #request='{ exit:'
    #    json.dump(request, f,ensure_ascii=False)
    namespace=getName(bsAvito)
    pricelist=getPrice(bsAvito)
    placelist=getMetro(bsAvito)
    imageurl=GetImageContent(bsAvito)
    hrefs=getHref(bsAvito)
    count=-1
    entry={}
    for i in namespace:
        count=count+1
        name=namespace[count]
        ref=hrefs[count]
        ref="https://www.avito.ru"+ref
        price=pricelist[count]
        place=placelist[count]
        image=imageurl[count]
        image="https:"+image
        id=1500+count
        entryA={"name":name,"ref":ref,"price":price,"place":str(place),"url":image}
        entry[str(id)]=entryA
        #print(entry)
        #with open("static/js/data_file.json", mode='a',encoding='utf-8') as feedsjson:
            #json.dump(entry,feedsjson,ensure_ascii=False)
    namespace=getNameY(bsYoula)
    pricelist=getPriceY(bsYoula)
    placelist=getMetroY(bsYoula)
    imageurl=GetImageContentY(bsYoula)
    hrefs=getHrefY(bsYoula)
    count=-1
    entryYl=''
    for i in namespace:
        count=count+1
        name=namespace[count]
        ref=hrefs[count]
        ref="https://youla.ru"+ref
        price=pricelist[count]
        place=placelist[count]
        image=imageurl[count]
        #place = place.replace(u'\xa0', u' ')
        id=500+count
        entryY={"name":name,"ref":ref,"price":price,"place":str(place),"url":image}
        entry[str(id)]=entryY
        #print(entry)
    with open("static/js/data_file.json", mode='w',encoding='utf-8') as feedsjson:
        json.dump(entry,feedsjson,ensure_ascii=False)
    #return entry
    #print("--- %s seconds ---" % (time.time() - start_time))
def getPrice(bsAvito):

    prices=bsAvito.findAll("span",{"itemprop":"price"})
    price = [x["content"] for x in prices]

    return price

def getMetro(bsAvito):

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
def getName(bsAvito):

    names=[]
    name=bsAvito.findAll("a",{"class":"item-description-title-link"})
    for namelist in name:
        names.append(namelist.span.get_text())

    return names

def getHref(bsAvito):
    start_time = time.time()
    refs=[]
    href=bsAvito.findAll("a",{"class":"item-description-title-link"})
    refs=[x["href"] for x in href]

    return refs
def GetImageContent(bsAvito):

    out=[]
    imagecontent=bsAvito.findAll("div",{"class":"item-photo"})
    for image in imagecontent:

        out.append(image.find("img",{"src":True}))
    output = [x["src"] for x in out]

    return output

def getNameY(bsYoula):

    names=[]
    name=bsYoula.findAll("div",{"class":"product_item__title"})
    for namelist in name:
        names.append(namelist.get_text())

    return names

def getPriceY(bsYoula):

    list=[]
    prices=bsYoula.findAll("div",{"class":"product_item__description"})
    for price in prices:
        try:
            listitem=price.find("span",{"class":"rub"}).previous
            listitem=re.sub("\D","",listitem)
        #listitem = listitem.replace(u'\xa0', u' ')
        #listitem = listitem.replace(u" ', '\n ", u' ')
            list.append(int(listitem))
        except:
            list.append(int('0'))

    return list
def getMetroY(bsYoula):

    place=[]
    metro=bsYoula.findAll("span",{"class":"product_item__location"})
    for metrolist in metro:
        list=metrolist.get_text()
        list=re.sub("[^А-Яа-я]","",list)
        place.append(list)

    return place

def getHrefY(bsYoula):

    refs=[]
    href=bsYoula.findAll("li",{"class":"product_item"})
    for ref in href:
        refs.append(ref.find("a",{"title":True}))
    refs=[x["href"] for x in refs]

    return refs
def GetImageContentY(bsYoula):

    out=[]
    imagecontent=bsYoula.findAll("div",{"class":"product_item__image"})
    for image in imagecontent:
        out.append(image.find("img"))
    output = [x["src"] for x in out]

    return output

#getArray(query)

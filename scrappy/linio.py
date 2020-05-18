
import requests
from bs4 import BeautifulSoup
import os
import time
import urllib
import urllib.request as urllib
import re
import numpy as np
from PIL import Image, ImageOps
import wget
import csv

os.system('mkdir images')
class Scrapy():

 
    def show(self):
        req = requests.get('https://www.linio.com.pe/p/durex-12pack-condones-extraseguro-36-preservativos--s36y3u')
        statusCode = req.status_code
        soup = BeautifulSoup(req.text, "lxml")


        titulo = soup.find('span',{'class':'product-name'})
        marca = soup.find('span',{'class':'body-base-sm'})

        precio = soup.find('span',{'class':'price-main-md'})

        print(precio.get_text())
        print(marca.get_text())
        print(titulo.get_text())


    def listaProductos(self,urls,categories,nums=0):
        data = {}
        with open('linio.csv', mode='a+') as csv_file:
            fieldnames = ['titulo','precio','categoria','link','img']
            writer = csv.DictWriter(csv_file,fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            i = 0
            for url, num in zip(urls,nums):
                cat = categories[i]
                i +=1
                time.sleep(1)
                if url !="/sp/tiendas-oficiales":
                    if(nums == 0):
                        link = 'https://www.linio.com.pe'+str(url)
                        req = requests.get(link)
                        print('url')
                        print(link)
                        soup = BeautifulSoup(req.text, "lxml")

                        items = soup.findAll('div',{'class':'catalogue-product row'})
                        for item in items:
                            titulo = item.find('span',{'class':'title-section'})
                            #marca = soup.find('span',{'class':'body-base-sm'})
                            link = item.find('a')
                            precio = item.find('span',{'class':'price-main-md'})
                            print(precio.get_text())
                            #print(marca.get_text())
                            print(titulo.get_text())
                            image = item.find('img', attrs = {'src':True})
                            #print(image['data-lazy'])

                            data['titulo'] = titulo.get_text()
                            data['precio'] = precio.get_text()
                            img = self.imgDownload(image['data-lazy'])
                            data['img'] = img
                            data['categoria'] = cat
                            writer.writerow({
                                'titulo': data['titulo'], 
                                'precio': data['precio'], 
                                'categoria': data['categoria'],
                                'link': 'https:'+ data['link'],
                                'img':data['img']
                                })           
                                #print(image['data-lazy'])
                    else:
                        for num in range(1, num):
                            time.sleep(1)
                            link='https://www.linio.com.pe'+str(url)+'?page='+str(num)
                            req = requests.get(link)
                            soup = BeautifulSoup(req.text, "lxml")
                            print('url')
                            print(link)
                            items = soup.findAll('div',{'class':'catalogue-product row'})
                            for item in items:
                                
                                titulo = item.find('span',{'class':'title-section'})
                                #marca = soup.find('span',{'class':'body-base-sm'})

                                precio = item.find('span',{'class':'price-main-md'})
                                link = item.find('a')
                                #print(precio.get_text())
                                #print(marca.get_text())
                                #print(titulo.get_text())

                                image = item.find('img', attrs = {'src':True})
                                #print(image['data-lazy'])

                                data['titulo'] = titulo.get_text()
                                data['precio'] = precio.get_text()
                                data['link'] = link['href']
                                img = self.imgDownload(image['data-lazy'])
                                data['img'] = img
                                data['categoria'] = cat
                                print(cat)
                                
                                    
                                writer.writerow({
                                    'titulo': data['titulo'], 
                                    'precio': data['precio'],
                                    'categoria': data['categoria'],
                                    'link': 'https:'+ data['link'],
                                    'img':data['img']
                                    })
                                    #print(image['data-lazy'])


        
    def getLinks(self,url):
        html_page = urllib.urlopen(url)
        soup = BeautifulSoup(html_page,'lxml')
        links = []
        category = []

        for link in soup.find('ul',{'class':'nav nav-pills nav-stacked menu'}).findAll('a'):
            links.append(link.get('href'))
            category.append(link.get('title'))
        print(category)
        return links, category

    def imgDownload(self, images):
        image = 'https:'+ images
        tit = str(images)
        titulo = tit[16:-4]
        #titulo = re.sub("[ /.:]", "_", image)
        #titulo = re.sub("\s+", "_", titulo.strip())
        """
        fd = urllib.urlopen(image)
        image_file = io.BytesIO(fd.read())
        img = Image.open(image_file)
        print(img)
        img.save('out.jpg')  
        """
        tit = titulo +'.jpg'

        url = image
        #url = requests.get(download, allow_redirects=True)
        wget.download(url,  "images/"+tit)
        return tit
        """
        f = open('images/img.jpg', 'w')
        f.write(str(r.content))
        f.close()
        """
       

#print( getLinks("https://www.linio.com.pe/") )

scrapy = Scrapy()
link, categories = scrapy.getLinks("https://www.linio.com.pe/")
url = np.array(link)
category = np.array(categories)
print(len(url))
nums = [0,0,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16]
scrapy.listaProductos(url,category,nums)







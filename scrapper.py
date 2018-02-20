import requests
from selenium import webdriver
import os,time,base64
from bs4 import BeautifulSoup

thisPath=os.path.dirname( os.path.realpath(__file__) )
picklefile="{}/session.pickle".format(thisPath)
imageFile='{}/images.txt'.format(thisPath)
separator=" "
downloadDirectory='{}/download'.format(thisPath)



headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def getImages():
    with open(imageFile, 'r') as myfile:
        htmltext=myfile.readlines()
        htmltext=[ line.replace('\n',"").split(separator) for line in htmltext]
    return htmltext


def getSimilarImagePageLink(url):
    print("getting simlar")
    selenumdriver.get('https://images.google.com/searchbyimage?image_url={}'.format(url))
    htmltext=selenumdriver.page_source
    soup = BeautifulSoup(htmltext,"lxml")
    a=soup.find('a', attrs={'class': 'iu-card-header'})
    if a:
        print("images site link: https://www.google.com{}".format(a.get("href")))
        return "https://www.google.com{}".format(a.get("href"))
    else:
        return None
    


def saveImg(src,name,count):
    if "data:image" in src[:20]:
        imgdata = base64.b64decode(src.split(",")[1])
        extension=src[:40].split(";")[0].split("/")[1]
    else:
        response = requests.get(src)
        imgdata=response.content
        extension=response.headers['content-type'].split("/")[1]
    filename="{}/{}/{}_{}.{}".format(downloadDirectory,name,name,count,extension)
    print("saved image at ({})".format(filename))
    if imgdata:
        with open(filename, 'wb') as f:
            f.write(imgdata)
        return True


def downloadFromSimilarImagesPage(url,name,maxNo):
    selenumdriver.get(url)
    div={}
    scrollTo=1080
    previous_imgs=0
    while len(div)<maxNo:
        selenumdriver.execute_script("window.scrollTo(0, {})".format(scrollTo))
        time.sleep(2)
        htmltext=selenumdriver.page_source
        soup = BeautifulSoup(htmltext,"lxml")
        div=soup.find("div", attrs={'id': 'search'}).find_all("img")
        scrollTo+=500
        if len(div) ==0 or len(div)==previous_imgs:
            break
        previous_imgs=len(div)

    os.makedirs("{}/{}".format(downloadDirectory,name), exist_ok=True)
    count=0

    for img in div:
        src= img.get("src") if img.get("src") else img.get("data-src")
       
        if src:
            print("saving image {}".format(count))
            try:
                if saveImg(src,name,count):
                    count+=1
            except Exception:
                continue
        if count>maxNo:
            break

    

    
def main():
    global selenumdriver
    selenumdriver = webdriver.Firefox()
    images=getImages()
    for each in images:
        if "#" not in each[0] and len(each)==3:
            name,count,url=each
            print(each)
            similarImagePageLink=getSimilarImagePageLink(url)

            if similarImagePageLink:
                downloadFromSimilarImagesPage(url=similarImagePageLink,name=name,maxNo=int(count))
            else:
                print("cant get similar image search page")

if __name__=="__main__":
    try:
        main()
    except ValueError as e:
        print(str(e))
        print("quiiting")
        print("make sure there is no more than one spaces in {} also at the end".format(imageFile))
    finally:
        #saveSession()
        if 'selenumdriver' in globals():
            selenumdriver.close()
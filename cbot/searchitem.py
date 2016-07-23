from lxml import html
import requests

craigUrl = "craigslist.org"
searchIndex = [
("antiques","craigslist.org/search/ata"),
("appliances","craigslist.org/search/ppa"),
("arts+crafts","craigslist.org/search/ara"),
("atv/utv/sno","craigslist.org/search/sna"),
("auto parts","craigslist.org/search/pta"),
("wheels/tires","craigslist.org/search/wta"),
("baby+kid","craigslist.org/search/baa"),
("barter","craigslist.org/search/bar"),
("beauty+hlth","craigslist.org/search/haa"),
("bikes","craigslist.org/search/bia"),
("bike parts","craigslist.org/search/bip"),
("boats","craigslist.org/search/boo"),
("boat parts","craigslist.org/search/bpa"),
("books","craigslist.org/search/bka"),
("business","craigslist.org/search/bfa"),
("cars+trucks","craigslist.org/search/cta"),
("cds/dvd/vhs","craigslist.org/search/ema"),
("cell phones","craigslist.org/search/moa"),
("clothes+acc","craigslist.org/search/cla"),
("collectibles","craigslist.org/search/cba"),
("computers","craigslist.org/search/sya"),
("computer parts","craigslist.org/search/syp"),
("electronics","craigslist.org/search/ela"),
("farm+garden","craigslist.org/search/gra"),
("free","craigslist.org/search/zip"),
("furniture","craigslist.org/search/fua"),
("garage sale","craigslist.org/search/gms"),
("general","craigslist.org/search/foa"),
("heavy equip","craigslist.org/search/hva"),
("household","craigslist.org/search/hsa"),
("jewelry","craigslist.org/search/jwa"),
("materials","craigslist.org/search/maa"),
("motorcycles","craigslist.org/search/mca"),
("motorcycle parts","craigslist.org/search/mpa"),
("music instr","craigslist.org/search/msa"),
("photo+video","craigslist.org/search/pha"),
("rvs+camp","craigslist.org/search/rva"),
("sporting","craigslist.org/search/sga"),
("tickets","craigslist.org/search/tia"),
("tools","craigslist.org/search/tla"),
("toys+games","craigslist.org/search/taa"),
("trailers","craigslist.org/search/tra"),
("video gaming","craigslist.org/search/vga"),
("wanted","craigslist.org/search/waa") ]


class craigList:
    def __init__(self, sKeyword, sCity = "tallahassee"):
        self.pageLinks = []
        self.cList = []
        self.sCit = "http://" + sCity + "."
        self.sKey = sKeyword
        self.parseLinks()
        self.parsePage()

    def parseLinks(self):
        for entry in searchIndex:
            if self.sKey in entry[0]:
                pagewanted = entry[1]
                break
            else:
                print "page not found"
                exit(0)
        pageNum = 0
        url = self.sCit + pagewanted
        while True:
            if pageNum == 0:
                pass
            else:
                url = self.sCit + pagewanted + "?s=" + str(pageNum)
            pageNum += 100
            cPage = requests.get(url)
            pageTree = html.fromstring(cPage.text)
            pageTable = pageTree.xpath("//a[@class='hdrlnk']/@href")
            if len(pageTable) < 10:
                break
            self.pageLinks.append(pageTable)

    def parsePage(self):
        #control = 0
        for pageLink in self.pageLinks:
            for searchitem in pageLink:
                correctUrl = self.sCit + craigUrl + searchitem
                cItem = craigItem(correctUrl)
                self.cList.append(cItem)
                #if control == 2:
                #   break
                #control += 1
            #break


class craigItem:
    def __init__(self, cPag):
        iUrl = str(cPag)
        itemPage = requests.get(iUrl)
        self.itemPageTree = html.fromstring(itemPage.text)
        self.title = ''
        self.price = ''
        self.descr = ''
        self.setTitle()
        self.setPrice()
        self.setDescr()

    def setTitle(self):
        try:
            self.title = self.itemPageTree.xpath(
                    "//span[@class='postingtitletext']/span[@id='titletextonly']//text()")
        except:
            self.title = "Not Available"
        while '\n' in self.title: self.title.remove('\n')
        if self.title == []:
            self.title = ["Not Available"]

    def setPrice(self):
        try:
            self.price = self.itemPageTree.xpath(
                    "//span[@class='postingtitletext']/span[@class='price']//text()")
        except:
            self.price = "Not Available"
        while '\n' in self.price: self.price.remove('\n')
        if self.price == []:
            self.price = ["Not Available"]

    def setDescr(self):
        try:
            self.descr = self.itemPageTree.xpath(
                    "//section[@id='postingbody']//text()")
        except:
            self.descr = 'Not Available'
        while '\n' in self.descr: self.descr.remove('\n')
        if self.descr == []:
            self.descr = ["Not Available"]

    def __str__(self):
        returnthis = "title:\t" + "".join(self.title)\
        +"\nprice:\t" + "".join(self.price)\
        +"\ndescr:\t" + "".join(self.descr)
        return returnthis.encode('utf-8')



if __name__ == "__main__":
    c = craigList("antiques")
    number = 1
    print "***********************************************"
    for it in c.cList:
        print number
        print it
        print "***********************************************"
        number += 1

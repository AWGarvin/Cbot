from catadata import searchIndex
from lxml import html
import threading
import requests
import sys
craigUrl = "craigslist.org"

class craigList:
    def __init__(self, sRegion, sCatagory, sKeyword, sMinDate):
        self.pageLinks = []
        self.dateTables = []
        self.cList = []
        self.sCit = "http://" + sRegion + "."
        self.sCat = sCatagory
        self.sKey = "?query=" + sKeyword.lower()
        self.MinD = sMinDate
        self.parseLinks()
        self.minY = int(sMinDate[:4])
        self.minM = int(sMinDate[5:7])
        self.minD = int(sMinDate[8:])
        if self.pageLinks == []:
            pass
        else:
            self.parsePage()
    def parseLinks(self):
        for k,v in searchIndex.items():
            if self.sCat in k:
                pagewanted = v
                break
        pageNum = 0

        while True:
            url = self.sCit + pagewanted + self.sKey
            if pageNum == 0:
                pass
            else:
                url += "&s=" + str(pageNum)
            url += "&sort=date"
            #print url
            pageNum += 100
            cPage = requests.get(url)
            pageTree = html.fromstring(cPage.text)
            pageTable = pageTree.xpath("//a[@class='hdrlnk']/@href")
            dateTable = pageTree.xpath("//span[@class='pl']/time/@datetime")
            #print pageTable, len(pageTable)
            #print dateTable, len(dateTable)
            if len(pageTable) < 10 or pageTable == []:
                break
            self.pageLinks.append(pageTable)
            self.dateTables.append(dateTable)
            pageTable = []
    def parsePage(self):
        x = 0
        y = 0
        threads = []
        for pageLink in self.pageLinks:
            for searchitem in pageLink:
                correctUrl = self.sCit + craigUrl + searchitem
                if craigUrl in searchitem: break
                testDate = self.dateTables[x][y]
                testD = testDate[:10]
                Y = int(testD[:4])
                M = int(testD[5:7])
                D = int(testD[8:])
                dateval = lambda y, m, d: y * 365 + m*30 + d
                if dateval(Y, M, D) < dateval(self.minY, self.minM, self.minD):
                    return
                t = threading.Thread(target=self.parseItem, args=(correctUrl, testD,))
                threads.append(t)
                y += 1
            x += 1
        for t in threads: t.start()
        for t in threads: t.join()
    def parseItem(self, cU, tD):
        cItem = craigItem(cU, self.sCit, self.MinD, tD)
        print cItem.getTitle()
        if "none" in cItem.getTitle():
            return
        if 's' in cItem.getDate() or 'N' in cItem.getDate():
            pass
            #continue
        self.cList.append(cItem)
        # print "***********************************************"
        # print type(cItem.getTitle())
        # print type(cItem.getPrice())
        # print type(cItem.getDescr())
        # print type(cItem.getEmail())
        # print type(cItem.getPhone())
        # print type(cItem.getDate())
        # print type(cItem.getUpDate())        
        # print "***********************************************"
        return

class craigItem:
    def __init__(self, cPag, city, minDate, upDte):
        self.minY = int(minDate[:4])
        self.minM = int(minDate[5:7])
        self.minD = int(minDate[8:])
        self.upDate = upDte
        self.cityurl = city
        iUrl = str(cPag)
        #print iUrl
        try:
            itemPage = requests.get(iUrl)
        except:
            self.title = ["none"]
            return
        self.itemPageTree = html.fromstring(itemPage.text)
        self.setTitle()
        self.setPrice()
        self.setDescr()
        self.setContact()
        self.setDate()
        self.setImages()
        #print "complete"
    def getTitle(self):
        return "".join(self.title).encode('utf-8')
    def getPrice(self):
        return "".join(self.price).encode('utf-8')
    def getDescr(self):
        return "".join(self.descr).encode('utf-8')
    def getEmail(self):
        return "".join(self.email).encode('utf-8')
    def getPhone(self):
        return "".join(self.phone).encode('utf-8')
    def getDate(self):
        return str(self.date[0])
    def getUpDate(self):
        return str(self.upDate)
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
            self.price = ["Not Available"]
        while '\n' in self.price: self.price.remove('\n')
        if self.price == []:
            self.price = ["Not Available"]
    def setDescr(self):
        try:
            self.descr = self.itemPageTree.xpath(
                    "//section[@id='postingbody']//text()")
        except:
            self.descr = ['Not Available']
        while '\n' in self.descr: self.descr.remove('\n')
        if self.descr == []:
            self.descr = ["Not Available"]
    def setContact(self):
        replyLink = self.itemPageTree.xpath(
                "//a[@id='replylink']/@href")
        if replyLink == []:
            self.phone = ['Not Available']
            self.email = ['Not Available']
            return
        contactUrl = self.cityurl + craigUrl + replyLink[0]
        contactPage = requests.get(contactUrl)
        contactTree = html.fromstring(contactPage.text)
        try:
            self.phone = contactTree.xpath(
                    "//ul/li/text()")
        except:
            self.phone = ['Not Available']
        try:
            self.email = contactTree.xpath(
                    "//div[@class='anonemail']//text()")
        except:
            self.email = ['Not Available']
        while '\n' in self.email: self.email.remove('\n')
        count = 0
        for entry in self.phone:
            if '(' in entry:
                self.phone = entry[2:]
                break
            if count == len(self.phone)-1:
                self.phone = ['Not Available']
            count += 1
        if self.email == []:
            self.email = ["Not Available"]
        if len(self.phone) > 17 or self.phone == []:
            self.phone = ["Not Available"]
    def setDate(self):
        try:
            self.date = self.itemPageTree.xpath(
                    "//time//text()")
            self.date.pop()
            self.date[0] = self.date[0][:10]
            Y = int(self.date[0][:4])
            M = int(self.date[0][5:7])
            D = int(self.date[0][8:])
            dateval = lambda y, m, d: y * 365 + m*30 + d
            if dateval(Y, M, D) < dateval(self.minY, self.minM, self.minD):
                pass
                #self.date[0] = ['stop']
        except:
            self.date = ['Not Available']
        while '\n' in self.date: self.date.remove('\n')
        if self.date == []:
            self.date = ["Not Available"]
    def __str__(self):
        returnthis = "title:\t" + "".join(self.title)\
        +"\nprice:\t" + "".join(self.price)\
        +"\ndescr:\t" + "".join(self.descr)\
        +"\nemail:\t" + "".join(self.email)\
        +"\nphone:\t" + "".join(self.phone)\
        +"\ndate:\t" + self.date[0]\
        +"\nupDate:\t" + self.upDate
        return returnthis.encode('utf-8')

    def getImages(self):
        return self.images

    def setImages(self):
        try:
            self.images = self.itemPageTree.xpath(
                "//div[@id='thumbs']/a/@href")
        except:
            self.images = ["Not Available"]
                                



if __name__ == "__main__":
    c = craigList("tallahassee","antiques","chair", "2016-07-26")
    number = 1
    print "***********************************************"
    for it in c.cList:
        print number
        print it
        print "***********************************************"
        number += 1

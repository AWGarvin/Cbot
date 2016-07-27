from catadata import searchIndex
from lxml import html
import requests
import sys
craigUrl = "craigslist.org"

class craigList:
    def __init__(self, sRegion, sCatagory, sKeyword, sMinDate):
        self.pageLinks = []
        self.cList = []
        self.sCit = "http://" + sRegion + "."
        self.sCat = sCatagory
        self.sKey = "?query=" + sKeyword
        self.MinD = sMinDate
        self.parseLinks()
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
        url = self.sCit + pagewanted + self.sKey
        while True:
            if pageNum == 0:
                pass
            else:
                url = self.sCit + pagewanted + "?s=" + str(pageNum)
            pageNum += 100
            cPage = requests.get(url)
            pageTree = html.fromstring(cPage.text)
            pageTable = pageTree.xpath("//a[@class='hdrlnk']/@href")
            print pageTable
            if len(pageTable) < 10 or pageTable == []:
                break
            self.pageLinks.append(pageTable)
    def parsePage(self):
        control = 0
        for pageLink in self.pageLinks:
            for searchitem in pageLink:
                #print searchitem
                correctUrl = self.sCit + craigUrl + searchitem
                if craigUrl in searchitem: break
                cItem = craigItem(correctUrl, self.sCit, self.MinD)
                #print cItem.getDate()
                if 's' in cItem.getDate() or 'N' in cItem.getDate():
                    control += 1
                    continue
                self.cList.append(cItem)
                if control == 10:
                   break
                control += 1
            break

class craigItem:
    def __init__(self, cPag, city, minDate):
        self.minY = int(minDate[:4])
        self.minM = int(minDate[5:7])
        self.minD = int(minDate[8:])
        self.cityurl = city
        iUrl = str(cPag)
        itemPage = requests.get(iUrl)
        self.itemPageTree = html.fromstring(itemPage.text)
        self.setTitle()
        self.setPrice()
        self.setDescr()
        self.setContact()
        self.setDate()
    def getTitle(self):
        return str("".join(self.title))
    def getPrice(self):
        return str("".join(self.price))
    def getDescr(self):
        return str("".join(self.descr))
    def getEmail(self):
        return str("".join(self.email))
    def getPhone(self):
        return str("".join(self.phone))
    def getDate(self):
        return str(self.date[0])
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
    def setContact(self):
        replyLink = self.itemPageTree.xpath(
                "//a[@id='replylink']/@href")
        contactUrl = self.cityurl + craigUrl + replyLink[0]
        contactPage = requests.get(contactUrl)
        contactTree = html.fromstring(contactPage.text)
        try:
            self.phone = contactTree.xpath(
                    "//ul/li/text()")
        except:
            self.phone = 'Not Available'
        try:
            self.email = contactTree.xpath(
                    "//div[@class='anonemail']//text()")
        except:
            self.email = 'Not Available'
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
        if len(self.phone) > 17:
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
                self.date[0] = ['stop']
            # print self.date[0]
        except:
            self.date = 'Not Available'
        while '\n' in self.date: self.date.remove('\n')
        if self.date == []:
            self.date = ["Not Available"]
    def __str__(self):
        returnthis = "title:\t" + "".join(self.title)\
        +"\nprice:\t" + "".join(self.price)\
        +"\ndescr:\t" + "".join(self.descr)\
        +"\nemail:\t" + "".join(self.email)\
        +"\nphone:\t" + "".join(self.phone)\
        +"\ndate:\t" + self.date[0]
        return returnthis.encode('utf-8')

if __name__ == "__main__":
    c = craigList("tallahassee","antiques","dolkdfa", "2016-07-10")
    number = 1
    print "***********************************************"
    for it in c.cList:
        print number
        print it
        print "***********************************************"
        number += 1

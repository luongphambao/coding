import requests
import random
import json
import time

class shopeeCmtScraper:
    def __init__(self, sURL):
        if (sURL[:8] == "https://"):
            self.URL = sURL
        else:
            self.URL = "https://" + sURL

        t = self.URL.split("/")

        if (t[3] == "product"):
            self.shopID, self.itemID = t[-2], t[-1]
            return

        t_2 = t[3].split(".")
        self.shopID, self.itemID = t_2[-2], t_2[-1]

    def getAllCmts(self):
        pattern = "qwertyuiopasdfghjklzxcvbnm" + \
            str.upper("qwertyuiopasdfghjklzxcvbnm") + "1234567890"
        token = ""

        for i in range(32):
            token += pattern[random.randint(0, len(pattern) - 1)]

        aHeaders = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
            "Cookie": "csrftoken=" + token
        }

        aPayload = {
                "shopid": self.shopID,
                "itemid": self.itemID,
                "filter": 1,
                "flag": 1,
                "type": 0,
                "offset": 0
            }

        aRes = []

        while(1):
            print("offset=", aPayload["offset"])

            request = requests.get("https://shopee.vn/api/v2/item/get_ratings", params=aPayload, headers=aHeaders)
            request = json.loads(request.text)

            iRating = len(request["data"]["ratings"])

            for i in range(iRating):
                cmt = request["data"]["ratings"][i]["comment"]
                bHidden = request["data"]["ratings"][i]["is_hidden"]
                if (len(cmt) > 0) and (not bHidden):
                    aRes.append(cmt.replace("\n", "\\n"))

            aPayload["offset"] += iRating

            if (iRating < 1):
                break

        return aRes

"""
Accepted format: 
    https://shopee.vn/{itemName}.{shopID}.{itemID}
    https://shopee.vn/product/{shopID}/{itemID}
"""
#111138057.2380707066
#88201679.5873954476
#.48582040.2274665808
#48406301.6751782083
#65589552.4737194401
#277411443.7254565873
sURL = "https://shopee.vn/product/277411443/7254565873"
scraper = shopeeCmtScraper(sURL)

with open(scraper.shopID + "-" + scraper.itemID + ".txt", "w+", encoding="utf8") as file:
    file.write("Date time: " + time.asctime() + "\n")
    file.write("URL: " + scraper.URL + "\n")

    startTime = time.time()
    res = scraper.getAllCmts()
    elapsedTime = time.time() - startTime

    file.write("Time taken: " + str(elapsedTime) + "s\n")
    file.write("Total comments: " + str(len(res)) + "\n\n")
    
    for i in res:
        file.write(i + "\n")
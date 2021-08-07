import bs4
import requests
import jparser
def getLeaderboard(l):
    leaders = l
    formatted = leaders.text.split(')')
    for i in range(len(formatted)):
        formatted[i] = formatted[i].split('(')[0]
    return formatted
class ReplAPI():
    def __init__(self, username):
      self.user = username.replace("@", '')
      amoghthecool = requests.get(f"https://replit.com/data/profiles/{self.user}")
      if amoghthecool.text == '{"message":"user not found","name":"NotFoundError","status":404}':
        exit(f'"{self.user}" does not exist!!')
      self.json = jparser.jparse(amoghthecool.text)
      url = f'https://www.replit.com/@{self.user}'
      reqs = requests.get(url)
      self.soup = bs4.BeautifulSoup(reqs.text,
      'html.parser',parse_only=bs4.SoupStrainer(['span']))
      url = "https://replit.com/leaders?since=all_time"
      page = requests.get(url)
      soup = bs4.BeautifulSoup(page.text,'html.parser',parse_only=bs4.SoupStrainer(['div']))
      leaders = soup.find(class_="jsx-776267233 leaderboard-list-top")
      self.l = leaders
    def getBio(self):
        return self.json["bio"]
    def getOrg(self):
        try:
            return self.json["organization"]
        except:
            return "No orginizations found."
    def getCycles(self):
        return int(eval(self.soup.find(class_="jsx-3139500421").text))
    def getIsHacker(self):
        try:
            return self.json["hacker"]
        except:
            return False
    def getPfp(self):
        try:
            return self.json["icon"]["url"]
        except:
            return "nopfp"
    def getTopLangs(self):
      return self.json["topLanguages"]
    def getFirstName(self):
      try:
        if (self.json["firstName"] != None):
          return self.json["firstName"]
        else:
          raise IndexError("wut")
      except:
        return "null"
    def getLastName(self):
      try:
        if (self.json["lastName"] != None):
          return self.json["lastName"]
        else:
          raise IndexError("wut")
      except:
        return "null"
    def getName(self):
        return self.getFirstName() + ' ' + self.getLastName()
    def mergeListsIntoDict(self, l1, l2):
        dictionary = {}
        for i in range(len(l1)):
            dictionary[l1[i]] = l2[i]
        return dictionary
    def getRepls(self):
      repls2 = self.json["repls"]
      for i in range(len(repls2)):
        val = repls2[i]["title"]
        repls2[i] = {val: f"https://replit.com/@{self.user}/{val.replace(' ', '')}"}
      return repls2
    def isInLeaderboard(self):
        for i in getLeaderboard(self.l):
            if i.upper() == self.user.upper():
                return True
        return False
    def getNotifs(self):
      amoghthecool = requests.get(f"https://replit.com/notifications")
      soup = bs4.BeautifulSoup(amoghthecool.text,'html.parser', parse_only=bs4.SoupStrainer(['div']))
      n = soup.find_all(class_ = "jsx-806891921 item-container has-link")
      p = []
      for i in n:
        p.append(i.text)
      return n
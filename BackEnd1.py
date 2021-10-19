import Pyro4
import json
import urllib
import urllib.request
from datetime import datetime
@Pyro4.expose
class JustHungry1(object):
    def __init__(self):
        self.Orders = []
        self.Menues = [["Nandos", {"starters": [("Spicy Mixed Olives", 4), ("PERi-PERi Nuts", 4)], "mains": [("1/2 Chicken", 7), ("Chicken Butterfly", 12)], "desert": [("Choc-A-Lot Cake", 4.75), ("Carrot Cake", 4.75)]}], ["Lebeneat", {"starters": [("Hummus shawarma chicken", 5), ("Falafl", 5.95)], "mains": [("Shish tauk", 11.95), ("Mixed Grill", 15.65),("Bamieh {V}", 10.95)], "desert": [("Baklava", 3.50), ("Knefeh", 3.50)]}]]

    def GetAllMenus(self, name):
        print("Start Order")
        print("GetAllMenus")
        self.Orders.append([name])
        try:
            BackEnd0.update(self.Orders)
        except:
            pass
        try:
            BackEnd2.update(self.Orders)
        except:
            pass

        return self.Menues

    def GetMenu(self, MNum):
        print("GetMenu number: ", MNum)
        self.Orders[-1].append(self.Menues[MNum][0])
        try:
            BackEnd0.update(self.Orders)
        except:
            pass
        try:
            BackEnd2.update(self.Orders)
        except:
            pass
        return self.Menues[MNum]

    def AddFoodChoice(self, order):
        self.Orders[-1].append(order)
        price=0
        for x in self.Menues:
            if x[0]==self.Orders[-1][-2]:
                price+=x[1]["starters"][order[0]][1]
                price+=x[1]["mains"][order[1]][1]
                price+=x[1]["desert"][order[2]][1]

        self.Orders[-1].append(price)
        try:
            BackEnd0.update(self.Orders)
        except:
            pass
        try:
            BackEnd2.update(self.Orders)
        except:
            pass


        print("AddFoodChoice")

        return order

    def CheckAddress(self, postcode):
        print(postcode)
        postcode=postcode.replace(" ", "")
        print("Called CheckAddress("+ postcode+")")
        try:
            data = urllib.request.urlopen('https://api.postcodes.io/postcodes/' + postcode)
        except:
            return [False]
        decode = data.read().decode('utf-8')
        PostCodeInfo = json.loads(decode)
        print(PostCodeInfo)
        if PostCodeInfo["status"]==200:
            self.Orders[-1].append(postcode)#4
            self.Orders[-1].append(PostCodeInfo["result"]["admin_ward"])#5
            self.Orders[-1].append(PostCodeInfo["result"]["admin_district"])#6
            try:
                BackEnd0.update(self.Orders)
            except:
                pass
            try:
                BackEnd2.update(self.Orders)
            except:
                pass
            return self.Orders[-1]
        else:
            return False


    def ConfirmOrder(self,CorC):
        if CorC==True:
            print("confirm order")
            now = datetime.now()
            CT = str(now)
            self.Orders[-1].append(CT[:16])
            try:
                BackEnd0.update(self.Orders)
            except:
                pass
            try:
                BackEnd2.update(self.Orders)
            except:
                pass
            return "Order is confirmed and will be delivered to " + self.Orders[-1][5]+", "+self.Orders[-1][6]+" POST CODE: "+self.Orders[-1][4]
        elif CorC==False:
            print("Cancel order")
            self.Orders.pop()
            try:
                BackEnd0.update(self.Orders)
            except:
                pass
            try:
                BackEnd2.update(self.Orders)
            except:
                pass

            return "Order has been canceled"


    def GetPastOrders(self, Cname):
        print("past orders")
        print(Cname)
        Corders = []
        for order in self.Orders:
            if order[0] == Cname:
                Corders.append(order)
        print(Corders)
        OldOrders = []
        text=""
        for x in Corders:
            text="You placed a £"+str(x[3])+" order from "+x[1]+" to post code "+x[4]+" on "+x[7]
            OldOrders.append(text)
        print(OldOrders)
        return OldOrders

        #
        # for Count,order in enumerate(Corders):
        #     str="You ordered "
        #     for x in self.Menues:
        #         if x[0]==order[1]:
        #             str+=x[1]["starter"][order[2][0]]
        #             str+=", "
        #             str+=x[1]["mains"][order[2][1]]
        #             str+=" and "
        #             str+=x[1]["desert"][order[2][2]]
        #     str+=" from "+order[1]+" on "+order[7]
        #     OldOrders.append(str)


    def update(self, data):
        self.Orders = data
        print("Updating BackEnd1", self.Orders)


BackEnd1 = Pyro4.Proxy("PYRONAME:BackEnd0")
BackEnd2 = Pyro4.Proxy("PYRONAME:BackEnd2")

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
instance = JustHungry1()
uri = daemon.register(instance)

ns.register("BackEnd1", uri)

print("BackEnd1 Ready.")

daemon.requestLoop()

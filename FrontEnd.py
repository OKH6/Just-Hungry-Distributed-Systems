import Pyro4
import sys
import os
@Pyro4.expose

class JustHungryFront(object):
    def GetAllMenus(self, name):
        try:
            print("Trying to get Menues from BackEnd0")
            return BackEnd0.GetAllMenus(name)
        except Exception as e:
            print(e)
            try:
                print("Trying to get Menues from BackEnd1")
                return BackEnd1.GetAllMenus(name)
            except Exception as e:
                print(e)
                try:
                    print("Trying to get Menues from BackEnd2")
                    return BackEnd2.GetAllMenus(name)
                except Exception as e:
                    print(e)
                    print("No BackEnd running")
                    exit()


    def GetMenu(self, MenNum):
        try:
            print("Trying to get Menu from BackEnd0")
            return BackEnd0.GetMenu(MenNum)
        except Exception as e:
            print(e)
            try:
                print("Trying to get Menu from BackEnd1")
                return BackEnd1.GetMenu(MenNum)
            except Exception as e:
                print(e)
                try:
                    print("Trying to get Menu from BackEnd2")
                    return BackEnd2.GetMenu(MenNum)
                except Exception as e:
                    print(e)
                    print("No BackEnd running")
                    exit()

    def AddFoodChoice(self, order):

        try:
            print("Trying to add order using BackEnd0")
            return BackEnd0.AddFoodChoice(order)
        except Exception as e:
            print(e)
            try:
                print("Trying to add order using BackEnd1")
                return BackEnd1.AddFoodChoice(order)
            except Exception as e:
                print(e)
                try:
                    print("Trying to add order using BackEnd2")
                    return BackEnd2.AddFoodChoice(order)
                except Exception as e:
                    print(e)
                    print("No BackEnd running")
                    exit()

    def CheckAddress(self, postcode):

        try:
            print("Trying to check address using BackEnd0")
            return BackEnd0.CheckAddress(postcode)
        except Exception as e:
            print(e)
            try:
                print("Trying to check address using BackEnd1")
                return BackEnd1.CheckAddress(postcode)
            except Exception as e:
                print(e)
                try:
                    print("Trying to check address using BackEnd2")
                    return BackEnd2.CheckAddress(postcode)
                except Exception as e:
                    print(e)
                    print("No BackEnd running")
                    exit()

    def ConfirmOrder(self, CorC):
        try:
            print("Trying to Confirm order using BackEnd0")
            return BackEnd0.ConfirmOrder(CorC)
        except Exception as e:
            print(e)
            try:
                print("Trying to Confirm order using BackEnd1")
                return BackEnd1.ConfirmOrder(CorC)
            except Exception as e:
                print(e)
                try:
                    print("Trying to Confirm order using BackEnd2")
                    return BackEnd2.ConfirmOrder(CorC)
                except Exception as e:
                    print(e)
                    print("No BackEnd running")
                    exit()
    def GetPastOrders(self, name):
        try:
            print("Trying to get past orders using BackEnd0")
            return BackEnd0.GetPastOrders(name)
        except Exception as e:
            print(e)
            try:
                print("Trying to get past orders using BackEnd1")
                return BackEnd1.GetPastOrders(name)
            except Exception as e:
                print(e)
                try:
                    print("Trying to get past orders using BackEnd2")
                    return BackEnd2.GetPastOrders(name)
                except Exception as e:
                    print(e)
                    print("No BackEnd running")
                    exit()





BackEnd0 = Pyro4.Proxy("PYRONAME:BackEnd0")
BackEnd1 = Pyro4.Proxy("PYRONAME:BackEnd1")
BackEnd2 = Pyro4.Proxy("PYRONAME:BackEnd2")

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()

uri = daemon.register(JustHungryFront)

ns.register("FrontEnd", uri)

print("FrontEnd Ready.")

daemon.requestLoop()

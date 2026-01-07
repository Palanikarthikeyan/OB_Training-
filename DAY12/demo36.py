from datetime import datetime
import time
class vendor:
    '''this is sample trading app'''
    def __init__(self,vN,vGST):
        self.vN = vN
        self.vGST = vGST
        print('Enrollment is done')
    def billing(self,pN,pCost,pQty):
        '''product billing details'''
        self.pN = pN
        self.pCost = pCost
        self.pQty = pQty
        self.total = self.pCost * self.pQty
        self.tax = self.total * 0.18
        self.gs = self.tax + self.total
        self.duration = self.delivery_time()
        self.logs(self.pN,self.pCost,self.gs,self.duration,self.vN,self.vGST)
    def delivery_time(self):
        dispatched = datetime(2026,1,6,14,20,0)
        received = datetime(2026,1,7,19,40,0)
        duration = received - dispatched
        return duration
    def logs(self,*args):
        '''vendor details and product details are appended to file'''
        fobj = open('vendor.log','a')
        s1=f'Product Name:{args[0]}\tCost:{args[1]}\tGS(including Tax):{args[2]}\t'
        s2=f'Vendor Name:{args[4]}\tVendorGST:{args[5]}\t Travel Duration:{args[3]}'
        fobj.write(s1+s2+"\n\n")
        fobj.close()

vobj1 = vendor('V1','VGST1234')
vobj1.billing('pA',1000,5)
time.sleep(2)
vobj1.billing('pB',1230,3)
vobj1.billing('pC',1300,4)

time.sleep(3)
vobj2 = vendor('V3','VGST4313')
vobj2.billing('pS',2290,3)
vobj1.billing('pT',2000,2)

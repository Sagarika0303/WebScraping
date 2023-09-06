class employee:
    employeename = " "
    employeenumber = 0
    
    def __init__(self , employeename , employeenumber):
       self.employeename=employeename
       self.employeenumber=employeenumber
       print(employeename) 
       print(employeenumber) 
    def m1(self,employeename):
        print(employeename)
    def m2(self,employeenumber):
        print(employeenumber)       

class manager(employee):
    def m3(self):
        print("m3")
    def m4(self):
        print("m4")

class accountant(employee):
    def m5(self):
        print("m5") 
 
employee1 = employee("sara",300)
manager2 = manager.m3
acc3 = accountant.m5



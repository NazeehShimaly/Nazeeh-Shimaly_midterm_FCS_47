import datetime
import re
class employee:
    idIncrement=2#static variable


    def __init__(self, userName:str, Timestamp:int ,gender:str,salary:int):
        if employee.idIncrement<10:
            self.id="emp00"+str(employee.idIncrement)
        elif employee.idIncrement>=10 and employee.idIncrement<100 :
            self.id="emp0"+str(employee.idIncrement)
        else:
            self.id="emp"+str(employee.idIncrement)
        employee.idIncrement=employee.idIncrement+1
        self.Timestamp=str(Timestamp)
        self.gender=str(gender)
        self.salary=int(salary)
        self.userName=str(userName)


    
    def menu(self):
        if self.gender=="male" :
            print("Hi Mr."+self.userName)
        else :
            print("Hi Ms."+self.userName)
        choice=0
      
        while choice!="2":
            print("1. Check my Salary")
            print("2. Exit")
            
            choice=input("")
            if(choice=="1"):
              print(self.checkSalary())
            elif choice=="2":
                self.exit()
                return
            else:
                print("wrong input please re enter one of the below operation")


    def checkSalary(self):
        return "your salary = "+str(self.salary)+"$"
    

    def exit(self):
        timeStampFile=open("timeStamp.txt","a")
        timeStamp=datetime.datetime.now()
        timeStampFile.write(self.userName+"  online at " +str(timeStamp)+"\n")
        timeStampFile.close()


    def changeSalary(self):
        salary=input("enter the new salary : ")
        pattern=("[0-9]{1,10}")
        result=re.fullmatch(pattern,salary)
        if result:
            self.salary=int(salary)
        else:
            print("Invalid input")
    def raisePrecentage(self,perc):
        self.salary=int(self.salary+self.salary*perc/100)

            
        
    
        
        



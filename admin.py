from employee import employee
import datetime
import re
class admin:
    def __init__(self,list1[]):
      self.employeeList=list1
    def menu(self):
       choice=0
       while choice!="7":
          print("1. Display Statistics"+"\n"+"2. Add an Employee"+"\n"+
                "3. Display all Employees"+"\n"+"4. Change Employee’s Salary"
                +"\n"+"5. Remove Employee"+"\n"+"6. Raise Employee’s Salary"+"\n"+"7. Exit")
          choice=input("")
          if choice=="1":
             self.displayStatistcs()
          elif choice=="2":
            result=None
            while result==None:
              username=input("specifying the new username")
              Pattern=("[a-zA-z]{3,20}")
              result=re.fullmatch(Pattern,x)
            date1=datetime.datetime.now()
            date1=str(date1)[0:10]
            date1=date1.replace("-","")
            self.addAnEmployee()
          elif choice=="3":
             self.displayAllEmployee()
          elif choice=="4":
             self.changeEmployeeSalary()
          elif choice=="5":
             self.removeEmployee()
          elif choice=="6":
             self.raiseEmployeeSalary()
          elif choice=="6":
             self.exit()
          else:
             print("INVALID INPUT")

    def displayStatistics(self): 
       return None
       
    def addAnEmployee(self,userName, Timestamp ,gender,salary):
       return None
    def displayAllEmployee(self):
       
       return None
    def changeEmployeeSalary(id):
       return None
    def removeEmployee():
       return None
    def raiseEmployeeSalary():
       return None
    def exit():
       return None
    
             
            






from employee import employee
import datetime
import re
class admin:
    def __init__(self,list1:list[employee]):
      self.employeeList=list1
    def menu(self):
       choice=0
       while choice!="7":
          print("1. Display Statistics"+"\n"+"2. Add an Employee"+"\n"+
                "3. Display all Employees"+"\n"+"4. Change Employee’s Salary"
                +"\n"+"5. Remove Employee"+"\n"+"6. Raise Employee’s Salary"+"\n"+"7. Exit")
          choice=input("")
          if choice=="1":
            self.displayStatistics()
          elif choice=="2":
            self.addAnEmployee()
          elif choice=="3":
             self.displayAllEmployee()
          elif choice=="4":
             self.changeEmployeeSalary()
          elif choice=="5":
             self.removeEmployee()
          elif choice=="6":
             self.raiseEmployeeSalary()
          elif choice=="7":
             self.exit()
             return
          else:
             print("INVALID INPUT")

    def displayStatistics(self):
       numOfFemales=0
       total=len(self.employeeList)
       
       for employee1 in self.employeeList:
          
          if employee1.gender=="female":
             numOfFemales=numOfFemales+1
       
       print( "from " +str(total)+" employees "
             +str(numOfFemales)+" is females and "+str(total-numOfFemales)+" is males")
      
       
    def addAnEmployee(self):
      result=None
      count=0
      while result==None and count<4:
         username=input("specifying the new username only letters allowed : ")
         Pattern=("[a-zA-z]{3,10}")
         result=re.fullmatch(Pattern,username)
         count=1+count
         if count==4:
            print("you are entering an unallowed character the process is cancelled")
            return None
         #entering user name


      gender=gender=input("Male or female :").lower()
      count=0
      while gender!="m" and gender!="male" and gender!="f" and gender!="female" and count<3 :
         count=count+1
         print("INVALID INPUT"+"\n"+"enter m or male if the employee is male"+"\n"+
               "enter f of female if she is female")
         gender=input("").lower()
         if count==3:
            print("you are entering an unallowed character the process is cancelled")
            return None
      if gender=="m":
         gender="male"
      elif gender=="f":
         gender="female"
      #specifing the gender
         
          
          
      count=0
      salary=input("enter the employee salary : ")
      pattern=("[0-9]{1,6}")
      result=re.fullmatch(pattern,salary)
      while result==None and count<3:
         count=count+1
         print("invalid input")
         salary=input("enter the employee salary")
         result=re.fullmatch(pattern,salary)
         if count==3:
            print("you are entering an unallowed character the process is cancelled")
            return None
         #salary specified



      date1=datetime.datetime.now()
      date1=str(date1)[0:10]
      date1=int(date1.replace("-","") )
      #timeStamp


      self.employeeList.append(employee(username,date1,gender,salary))
      #adding employee to the list

       
    def displayAllEmployee(self):
      for em in range (len(self.employeeList)-1,-1,-1):
       print ("employee Id : "+self.employeeList[em].id+"\n"+" user name : "+ self.employeeList[em].userName+"\n"+
              " gender : "+self.employeeList[em].gender+"\n"+" salary : "+str(self.employeeList[em].salary)+"\n"+" start working in : "
              +str(self.employeeList[em].Timestamp)+"\n")
       
       
    
    
    def changeEmployeeSalary(self):
      
      id=input("enter the employee id : ")
      index=self.findEmployee(id)
      if index==-1:
         print("no employee with this id")
      else:
         self.employeeList[index].changeSalary()

      

             
    def removeEmployee(self):
      
      id=input("enter the employee id : ")
      index=self.findEmployee(id)
      if index==-1:
         print("no employee with this id")
      else:
         self.employeeList.pop(index)
         print("employee deleted")

      
       
       
    def raiseEmployeeSalary(self):
       id=input("enter employee id : ")
       index=self.findEmployee(id)
       if index >= 0:
         raisepercentage=input("enter the percentage to be raised % : ")
         try:
            self.employeeList[index].raisePrecentage(float(raisepercentage))
            print("the salary was raised by "+raisepercentage+" the new salary is "+
                  str(self.employeeList[index].salary))
         except ValueError:
            print("Invalid percentage")
         
       
       return None
    def exit(self):
       file=open("employeesData.txt","w")
       for employee in self.employeeList:
          file.write(employee.id+","+employee.userName+","+str(employee.Timestamp)
                     +","+employee.gender+","+str(employee.salary)+"\n")
       file.close()
    def findEmployee(self,id):
      pattern=("emp"+"[0-9]{3,1000}")
      
      
      result=re.fullmatch(pattern,id.replace(" ",""))
      if result==None:
         return -1
            
      else:
         start=0
         end=len(self.employeeList)-1
         mid=(start+end)//2
         while mid>=start and mid<=end and start<=end:
            if self.employeeList[mid].id==id:
               
               return mid
            elif int((self.employeeList[mid].id)[3:])>int(id[3:]):
               end=mid-1
               mid=(start+end)//2
            elif int((self.employeeList[mid].id)[3:])<int(id[3:]):
               start=mid+1
               mid=(start+end)//2
         
         return -1
 
    
             
            






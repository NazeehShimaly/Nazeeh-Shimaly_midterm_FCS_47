class employee:
    idIncrement=3
    def __init__(self, userName, Timestamp ,gender,salary):
        if employee.idIncrement<10:
            self.id="emp00"+str(employee.idIncrement)
        elif employee.idIncrement>=10 and employee.idIncrement<100 :
            self.id="emp0"+str(employee.idIncrement)
        else:
            self.id="emp"+str(employee.idIncrement)
        employee.idIncrement=employee.idIncrement+1
        self.Timestamp=Timestamp
        self.gender=gender
        self.salary=int(salary)
        self.userName=userName
    
    def menu(self):
        if self.gender=="male" :
            print("Hi Mr."+self.userName)
        else :
            print("Hi Ms."+self.userName)
        choice=0
      
        while choice!=2:
            print("1. Check my Salary")
            print("2. Exit")
            
            choice=input
            if(choice=="1"):
                self.checkSalary()
            elif choice=="2":
                self.exit()
            else:
                print("wrong input please re enter one of the below operation")
            

            
        
    
        
        



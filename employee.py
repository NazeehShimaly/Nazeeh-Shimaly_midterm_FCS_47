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
        self.salary=salary
        
        



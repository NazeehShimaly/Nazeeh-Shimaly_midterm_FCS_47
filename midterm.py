from employee import employee
from admin import admin

def fileIntoListOfEmp():
    list1=[employee]
    
    filereader=open("employeesData.txt","r")
    for line in filereader:
        list2=line.split(",")
        if len(list2)==5:
            list1.append(employee(list2[1].replace(" ",""),
                                  int(list2[2].replace(" ","")),
                                  list2[3].replace(" ",""),
                                  int(list2[4].replace(" ",""))))
        
    filereader.close()
    list1.pop(0)
    return list1

def empfound(emp,list1:list[employee],passw):
    if passw !="":
        return -1
    else:
        for employee1 in range (0,len(list1)):
            if list1[employee1].userName==emp:
                return employee1
    return -1

employeelist= fileIntoListOfEmp()  

print("Welcome to comapny program"+"\n") 
attemp=0

while attemp<5:
    userName=input("enter your userName : ")
    passw=input("enter your password : ")
    if passw=="admin123123" and userName=="admin":
        Admin=admin(employeelist)    
        Admin.menu()
        attemp=0
    else:
        index=empfound(userName,employeelist,passw)
        if index==-1:
            attemp+=1
            print("No Matches")
        else:
            employeelist[index].menu()
            attemp=0
        

    
    

    
print("Your blocked")
        

                
                

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

employeelist= fileIntoListOfEmp()  
print(employeelist[1].gender)
print("Welcome to comapny program"+"\n") 
attemp=0
while attemp<5:
    userName=input("enter your userName : ")
    passw=input("enter your password : ")
    if passw=="admin123123" and userName=="admin":
        Admin=admin(employeelist)    
        Admin.menu()


    

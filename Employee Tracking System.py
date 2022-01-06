def login():
    if 'password' not in d:
        password=input("Create new password\n")
        d['password']=password
        print("password created")
        return False
    else:
        password=input("Enter password\n")
        if d['password']==password:
            print("login successful")
            return True
        else:
            print("incorrect password")
            return False

def updatePassword():
    d['password']=input("Enter new password\n")

def addEmployee():
    eid=input("Enter unique employee id\n")
    if eid in d:
        print("Name already exists choose another")
    else:
        l=[]
        print("Press enter for blank entry")
        l.append(input("Enter name\n"))
        l.append(input("Enter number\n"))
        l.append(input("Enter email\n"))
        l.append(input("Enter address\n"))
        l.append(input("Enter designation\n"))
        l.append(input("Enter salary\n"))
        d[eid]=l
        
def showEmployees():
    for i in d:
        if i != 'password':
            print(i,d[i][0])
        
def employeeDetails():
    eid=input("Enter employee id to search\n")
    if eid in d:
        print("Name :",d[eid][0])
        print("Contact Number :",d[eid][1])
        print("Email :",d[eid][2])
        print("Address :",d[eid][3])
        print("Designation :",d[eid][4])
        print("Salary :",d[eid][5])
    else:print("Employee Not Found")

def fetch_employees():
    f=open("EmployeesBook.txt","a")
    f.close()
    f=open("EmployeesBook.txt","r")
    l=f.readlines()
    for i in l:
        a=i.split()
        n=a[0]
        a=a[1:]
        a=' '.join(a)
        if n=='password':
            d[n]=a
        else:
            d[n]=eval(a)
    f.close()

def updateEmployeeDetails():
    eid=input("Enter employee id to update details\n")
    if eid not in d:
        print("employee not found")
    else:
        c=input("1.Update name\n2.Update number\n3.Update Email\n4.Update address\n5.Update Designation\n6.Update Salary\n")
        if c=='1':  
              d[eid][0]=input("Enter new name\n")
              print("name Updated")
        if c=='2':
            d[eid][1]=input("Enter new number")
            print("number updated")
        elif c=='3':
            d[eid][2]=input("Enter new email\n")
            print("email Updated")
        elif c=='4':
            d[eid][3]=input("Enter new address\n")
            print("address Updated")
        elif c=='5':
            d[eid][4]=input("Enter new Designation")
            print("Designation updated")
        elif c=='6':
            d[name][5]=input("Enter new Salary\n")
            print("Salary Updated")
        else:
            print("Wrong choice")
             
def modify_file():
    f=open("EmployeesBook.txt","w")
    for i in d:
        s=i+" "+str(d[i])+"\n"
        f.write(s)
    f.close()

def deleteEmployee():
    eid=input("Enter employee id to delete\n")
    if eid in d:
        d.pop(eid)
        print("Employee Deleted")
    else:
        print("Employee not found")

def clearEmployeesBook():
    password=d['password']
    d.clear()
    d['password']=password

d={}

fetch_employees()

while(True):
    log=login()
    if log==False:
        l=input("Enter 1 to login , 2 to exit\n")
        if l=='2':
            break
    else:
        break
while(log):
    print("Menu\n")
    print("1.Add Employee\n2.Delete Employee\n3.Show Employee Details\n4.Show all employees\n5.Update employee details\n6.Clear All employees\n7.Update password\n8.Exit")
    ch=input("Enter your choice\n")
    if (ch=='1'):
        addEmployee()
    elif ch=='2':
        deleteEmployee()
    elif ch=='3':
        employeeDetails()
    elif ch=='4':
        showEmployees()
    elif ch=='5':
        updateEmployeeDetails()
    elif ch=='6':
        clearemployeesBook()
    elif ch=='7':
        updatePassword()
    elif ch=='8':
        break
    else:
        print("Wrong choice try again")
    c=input("If you want to continue enter y else n\n")
    if c=='n':break

modify_file()



                  

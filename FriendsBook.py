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

def addFriend():
    name=input("Enter name\n")
    if name in d:
        print("Name already exists choose another")
    else:
        l=[]
        print("Press enter for blank entry")
        l.append(input("Enter number\n"))
        l.append(input("Enter email\n"))
        l.append(input("Enter address\n"))
        l.append(input("Enter birthday\n"))
        d[name]=l
        
def showFriends():
    for i in d:
        if i != 'password':
            print(i)
        
def friendDetails():
    name=input("Enter name to search\n")
    if name in d:
        print("Name :",name)
        print("Contact Number :",d[name][0])
        print("Email :",d[name][1])
        print("Address :",d[name][2])
        print("BirthDay :",d[name][3])
    else:print("Friend Not Found")

def fetch_friends():
    f=open("FriendsBook.txt","a")
    f.close()
    f=open("FriendsBook.txt","r")
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

def updateFriendDetails():
    name=input("Enter name to update\n")
    if name not in d:
        print("Friend name not found")
    else:
        c=input("1.Update number\n2.Update Email\n3.Update address\n4.Update BirthDay\n")
        if c=='1':  
              d[name][0]=input("Enter new number\n")
              print("number Updated")
        elif c=='2':
            d[name][1]=input("Enter new email\n")
            print("email Updated")
        elif c=='3':
            d[name][2]=input("Enter new address\n")
            print("address Updated")
        elif c=='4':
            d[name][3]=input("Enter new BirthDay\n")
            print("BirthDay Updated")
        else:
            print("Wrong choice")
             
def modify_file():
    f=open("FriendsBook.txt","w")
    for i in d:
        s=i+" "+str(d[i])+"\n"
        f.write(s)
    f.close()

def deleteFriend():
    name=input("Enter friend name to delete\n")
    if name in d:
        d.pop(name)
        print("Friend Deleted")
    else:
        print("Friend not found")

def clearFriendsBook():
    password=d['password']
    d.clear()
    d['password']=password

d={}

fetch_friends()

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
    print("1.Add Friend\n2.Delete Friend\n3.Show Friend Details\n4.Show all friends\n5.Update friend details\n6.Clear All friends\n7.Update password\n8.Exit")
    ch=input("Enter your choice\n")
    if (ch=='1'):
        addFriend()
    elif ch=='2':
        deleteFriend()
    elif ch=='3':
        friendDetails()
    elif ch=='4':
        showFriends()
    elif ch=='5':
        updateFriendDetails()
    elif ch=='6':
        clearFriendsBook()
    elif ch=='7':
        updatePassword()
    elif ch=='8':
        break
    else:
        print("Wrong choice try again")
    c=input("If you want to continue enter y else n\n")
    if c=='n':break

modify_file()



                  

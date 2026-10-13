print("\t***WELCOME TO LIBRARY***")

storybooks=[0,0,0,0,0,1,0,1,0,0,1,0,0,0]     #1-books taken,0-books available
poetrybooks=[0,0,0,1,0,0,1,0,1,0,1,0,]
studybooks=[0,0,1,1,0,1,1,0,1,0,1,0,0,1,0]
generalbooks=[0,0,1,0,1,0,1,0,1,0]

def library_login():
    n=int(input("Enter your ID:"))
    m=1234
    if n==m :
        print("Enjoy your book")
    else:
        print("invalid ID")

def take_book():
    op=input("select\n1.storybooks\n2.poetrybooks\n3.studybooks\n4.generalbooks")
    if op=='1':
        m=int(input("How many books you want?"))
        for i in range(m):
          if m<len(storybooks) and m>0:
            storybooks[i]=1
        print(f"books are {storybooks}")
    elif op=='2':
        m=int(input("How many books you want?"))
        for i in range(m):
          if m<len(poetrybooks) and m>0:
            poetrybooks[i]=1
        print(f"books are {poetrybooks}")
    elif op=='3':
        m=int(input("How many books you want?"))
        for i in range(m):
          if m<len(studybooks) and m>0:
            studybooks[i]=1
        print(f"books are {studybooks}")
    elif op=='4':
        m=int(input("How many books you want?"))
        for i in range(m):
          if m<len(generalbooks) and m>0:
            generalbooks[i]=1
        print(f"books are {generalbooks}")
    else:
          print("no book available")

def add_book():
    a=input("select\n1.storybooks\n2.poetrybooks\n3.studybooks\n4.generalbooks")
    if a=='1':
        storybooks.append(0)
    elif a=='2':    
        poetrybooks.append(0) 
    elif a=='3':
        studybooks.append(0)
    elif a=='4':   
       generalbooks.append(0) 
    else:
        print("no book added")
        return
    print("book added successfully")

def return_book():
    r=input("select\n1.storybooks\n2.poetrybooks\n3.studybooks\n4.generalbooks")
    if r=='1':
      storybooks.append(0)
    elif r=='2':    
        poetrybooks.append(0)
    elif r=='3':
        studybooks.append(0)
    elif r=='4':   
       generalbooks.append(0)
    else:
        print("book not returned")
        return
    print("thank you for returning book")

choice=input("Select:\n1.Librarylogin\n2.takebook\n3.addbook\n4.returnbook")
if choice=='1':
    library_login()
elif choice=='2':
    take_book()
elif choice=='3':
    add_book()
elif choice=='4':
    return_book()
else:
    print("invalid option")


 
    







    
    
    

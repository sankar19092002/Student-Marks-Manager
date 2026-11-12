students=[]
def calculate_grade(percentage):
    if(percentage>=90):
        return "A"
    
    elif(percentage>=75):
        return "B"
    
    elif(percentage>=60):
        return "C"
    
    elif(percentage>=40):
        return "D"
    else:
        return "F"
    
while True:
    print("\nStudent Marks Manager")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Exit")
    choice=input("Enter your choice : ")  

    if(choice=="1"):
        name=input("Enter Student Name : ")
        m1=int(input("Enter marks in Subject 1 : "))
        m2=int(input("Enter marks in Subject 2 : "))
        m3=int(input("Enter marks in Subject 3 : "))
        total=m1+m2+m3
        percentage=total/3
        grade=calculate_grade(percentage)
        students.append([name,m1,m2,m3,total,percentage,grade])
        print("Student added successfully")
        
    elif(choice=="2"):
        if not students:
            print("No records found")
        else:
            print("\nStudent Records")
            print("Name Total Percentage Grade")
            for s in students:
                print(s[0]," ",s[4]," ",round(s[5],2)," ",s[6])
                
    elif(choice=="3"):
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again")
                        
        
    
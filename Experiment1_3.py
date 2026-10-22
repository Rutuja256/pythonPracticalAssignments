#students datails

name=input("enter your name:")
roll=int(input("enter your roll call:"))
marks=float(input("enter your CGPA:"))
address=input("enter your current address:")
hostel=bool(input("are you staying in hostel? answer in True or False:"))

if(marks>=7.0):
    print("aligible students details for sholarship ")
    print("name:", name)
    print("roll call:", roll)
    print("CGPA:", marks)
    print("address:", address)
    print("hostel:", hostel)
else:
    print("there is no student that are eligible for sholarship")
        
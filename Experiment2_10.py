mStatus=int(input("input enter 1 if you are marriied or enter 0 if you are unmarried:"))
age=int(input("enter your age:"))
gender=input("enter m or M if you are a male and enter f or F if you are a female")

if mStatus==1:
    print("insures")
elif mStatus==0 and (gender=='m' or gender=='M') and age>30:
    print("insures")
elif mStatus==0 and (gender=='f' or gender=='F') and age>25:
    print("insures")
else:
    print("you are not aligible")        

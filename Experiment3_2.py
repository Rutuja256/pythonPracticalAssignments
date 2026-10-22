# Frequency of characters:
strs=input("enter a string here:")
count=0
temp=""
for i in strs:
    if i not in temp:
        for j in strs:
            if j==i:
                count=count+1
        print(i,"->",count)
        count=0
        temp=temp+i   
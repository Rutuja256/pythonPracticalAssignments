# Remove Spaces 
strs=input("enter a string")
temp=""
for i in strs:
    if i!=" ":
        temp=temp+i
print(temp)        


#Word count:
# strs=input("enter a string:")
# words=strs.split()
# for i in words:
#     print(i)
#     print()


#Title case:
# strs=input("enter string:")
# ans=""
# words=strs.split()
# for word in words:
#     for i in range(0,len(word)):
#         if i==0:
#             ans=ans+word[i].upper()
#         else:
#             ans=ans+word[i]
#     ans=ans+" "                      
# print(ans)

# strs=input("enter a string:")
# temp=""
# for i in range(0,len(strs)):
#     if strs[i] not in temp:
#         for j in range(i+1,len(strs)):
#             if strs[i]==strs[j]:
#                 temp=temp+strs[j]
#                 temp=temp+" "
#                 break 
# print(temp)
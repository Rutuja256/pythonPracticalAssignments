#Longest Word:
strs=input("enter string:")
words=strs.split()
longest=words[0]
short=words[0]
for word in words:
    print(word,"->",len(word))
    if len(word)>=len(longest):
        longest=word
    if len(word)<=len(short):
        short=word    
print("longest word:",longest) 
print("shortest word:",short) 
string=input("Enter something: ")
char=input("Enter a chacter: ")
i=0
count=0
while(i<len(string)):
  if(string[i]==char):
    count+=1
  i=i+1
print("The character",char,"appears",count,"times in the word",string)
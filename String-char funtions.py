a=input("enter a string: ")
digitcount=0
spacecount=0
alphabetcount=0
for i in a:
   if i.isnumeric():
      digitcount+=1
   elif i.isalpha():
      alphabetcount+=1
   elif i.isspace():
      spacecount+=1
print("Digit count:",digitcount)
print("Alphabet count:",alphabetcount)
print("Space count:",spacecount)

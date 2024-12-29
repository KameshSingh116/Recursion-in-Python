#Radhe Radhe
#Python code for recursion

def factorial(n):
    if(n==1 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
choice='y'
while(choice=='y'):

  a=int(input("Enter the number:"))
  b=factorial(a)

  print(b)
  choice=input("Enter the choice:(y/n)")
  if(choice=='y'):
      continue
  else:
      break
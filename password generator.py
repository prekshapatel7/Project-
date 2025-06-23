import random
import string

letters = list(string.ascii_lowercase + string.ascii_uppercase)

numbers=['0','1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','(',')','+']
print("welcome to password generator")
n1=int(input("how many letters you want?"))
n2=int(input("how many numbers you want?"))
n3=int(input("how many symbols you want?"))
password=[]
for i in range(1,n1+1):
      char= random.choice(letters)
      password=password+[char]
for i in range(1,n2+1):
      char= random.choice(numbers)
      password=password+[char]

for i in range(1,n3+1):
       char=random.choice(symbols)
       password=password+[char]
random.shuffle(password)
password_final=" "
for i in password:
    password_final+=i
print("your password is",password_final)
    



       

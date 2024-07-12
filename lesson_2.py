from random import choice 
simvol="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
long=int(input("enter your password length "))
password=""
for i in range(long):
    password+=choice(simvol)
print(password)
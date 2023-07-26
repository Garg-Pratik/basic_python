# age= int(input("Enter Your age:"))
# print("your age is:",age)
# if(age>18):
#     print("You are eligible")
# else:
#     print("You are not eligible")

Age=int(input("Enter your age:"))
print("Your age is:",Age)
if(Age>=18 and Age<=60):
    print("!!!you are eligible!!!")
elif(Age<=15):
    print("Go To Home Kid")
elif(Age>15 and Age<18):
    print("you are eligible but can't drink")
elif(Age>60 and Age<=100):
    print("you are to old to drink")
else:
    print("You are miracle to live")
print("!!! Have A Great Day !!!")
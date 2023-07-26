
#Break:-
num=int(input("Enter The Value:"))
for i in range(1,15):
    print(num,"X",i,"=",num*(i))
    if(i==10):
        break           #break use to completely break the loop and exit 
print("loop Exit")
#__________________________________________________________________________________________

num=int(input("Enter The Value:"))
for i in range(1,15):
    if(i==10):
        break
    print(num,"X",i,"=",num*(i))    #here its check if-conditon first then print, thats    why value print till "9" becuz after "9" its check if-condition value "10" and stop   there.
#__________________________________________________________________________________________    



#Continue:-
num=int(input("Enter The Value:"))
for i in range(1,15):
    if(i==10):
        print("skip the iteration")
        continue        #contiune use to skip the iteration"(i==10)" and continues the loop
    print(num,"X",i,"=",num*(i))
print("loop Exit")

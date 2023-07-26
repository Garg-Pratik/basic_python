name = "hello my name is pratik"
print(name[0:8])
print(len(name))


Name= "Pratik"
len1=len(Name)
print("Pratik is a",len1,"letter name")
print(Name[0:2])                         #for Function we use (parenthesis) 
print(Name[:])
print(Name[2:])
print(Name[:5])
print(Name[0:-3])
print(Name[0:len(Name)-3])    #when we use [0:-3] its automatically add len() to it
                               # and work as total no. of [__ : len(char) - choosed value]   ex- [0 : len(Name)-3]  = [0:6-3] (logic)
                               # gives output as [0:3]  and will print {pra}   

print(Name[-3:-1])    # same as above ---- [len(Name)-3 : len(Name)-1]  = [3:5]
 

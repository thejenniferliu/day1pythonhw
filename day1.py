#Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

#while the output of n**3 < 1000, 
#print(n**3)
#when n**3 > 1000, break
n = 0
while n**3 < 1000:
    print(n**3,end = " ")
    n+=1

#get first prime numbers up to 100
#only divisible by 1, and divisible by itself. 


#Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors
age = int(input("What is your age?"))
if age < 18:
    print("you are a child")
elif age <= 65:
    print("you are an adult")
else:
    print("you are a senior")
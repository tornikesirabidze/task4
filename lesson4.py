
my_name=input("enter your name: ")
my_surname=input("enter your surname: ")
my_age=int(input("enter your age: "))
print("my name is " "{} my surname is {}" " my age " "{}".format( my_name , my_surname, my_age))
my_age+=5
print("after 5 year im now {} year old ".format(my_age)) 
tent1=int(input("text number: "))
tent2=int(input("text number: "))
tent3=int(input("text number: "))
my_sum=0
#17 19 20
if tent1 % 2 ==1 :
    my_sum+=tent1

if tent2 %2 ==1 : 
   my_sum+=tent2

if tent3 %2 ==1:
    my_sum+=tent3
    print("sum odd numbers is {}".format(my_sum))
text=input("enter text:  ")
text_1 = 0

for char in text:
    if char == "a":
        text_1 += 1
print(" text contains 'a'{} ".format(text_1))
print('"stey hungy, stey foolish" by stive jobs')
num=12
if num >5:
  print("bigger than five")
if num <=47:
  print("between 5 and 47")
name1=input("text some name: ")
name2=input("text some name: ")
name_1=0
name_2=0
for xmovani in name1:
       if xmovani in "aeiou":
            name_1+=1
for xmovani in name2:
   if xmovani in "aeiou":
        name_2+=1
if name_1 > name_2 :
        print("name 1 have more symbols {}".format(name_1))   
elif name_1 < name_2 :
 print("name 2 have more symbols {}".format(name_2))        
else:
 print("tolia")

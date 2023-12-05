import random

alphabet=['a','b','c','d','e','f']
numbers=['1','2','3','4','5','6','7','8','9','0']
special=['/','*','-','+','!']
length=int(input("Enter the lenght of the password you want:"))
ch=int(input("enter the length of the character:"))
number=int(input("enter the lenght of the numbers"))
special_char=int(input("enter the  number of the special character"))


password=""

if (ch+number+special_char)==length:
    for i in range(ch):
        password+=random.choice(alphabet)

    for i in range(number):
        password+=random.choice(numbers)

    for i in range(special_char):
        password+=random.choice(special)

    pass_array=[]

    for i in  password:
        pass_array.append(i)


        
    random.shuffle(pass_array)

    new_pass=""
    for i in pass_array:
        new_pass+=i

    print(new_pass)


else:
    print("Your lenght does not match so please check your lenght and then try again.")

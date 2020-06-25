# PART 1    

# 1. Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7. Make sure to use only higher order function.

a = [i for i in range(1,200) if i%3!=0 and i%7==0]
print(a)

# 2 Write a program in Python to multiple the element of list by itself using a traditional function and pass the function to map to complete the operation.

def a(x): 
    return x * x
  
y = (1, 2, 3, 4,5,6,7,8,9,10) 
result = map(a, y) 
print(list(result))


# 3 Write a program to Python find out the character in a string which is uppercase using list comprehension.

x=[i for i in "ConsultAdd" if i.isupper() ]
print(x)



#4 Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should maps the students with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension. HINT-Use Zip function also
    #● Student = [&#39;Smit&#39;, &#39;Jaya&#39;, &#39;Rayyan&#39;]
    #● capital = [&#39;CSE&#39;, &#39;Networking&#39;, &#39;Operating System&#39;]


students = ["Smit", "Jaya", "Rayyan"] 
subjects = ["CSE","Networking", "Operating System"]
print ("key : " + str(students)) 
print ("value : " + str(subjects)) 
result = dict(zip(students, subjects)) 
print ("Result is : " +  str(result))


#6 Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”

def reverse(string):    
    for i in range(len(string)- 1, -1, -1):
        yield string[i]

for i in reverse("Consultadd Training"):
    print(i)




#7 Write any example on decorators.

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")
pretty = make_pretty(ordinary)
ordinary = make_pretty(ordinary)


@make_pretty
def ordinary():
    print("I am ordinary")



#8 Write a program to handle an error if the user entered the number more than
    #four digits it should return “Please length is too short/long !!! Please provide only four
    #digits”


try:
    x= int(input("Please enter a four digit number : "))
    if x>9999 or x<999:
        print("Please length is too short/long !!! Please provide only four digits ")
    else:
        print("Good to go!!")    
except:
    print("Only numbers are allowed")


#9 Create a login page backend to ask user to enter the UserEmail and password.
    #Make sure to ask Re-Type Password and if the password is incorrect give chance to
    #enter it again but it should not be more than 3 times.


count=0
while count < 3:
    username = input (str('Please enter a username: '))
    password = input('Please enter a password: ')
    if username == 'pratik' and password =='12345':
        print('Good to go!!')
        break
    else:
        print('username/password is incorrect')
        count += 1






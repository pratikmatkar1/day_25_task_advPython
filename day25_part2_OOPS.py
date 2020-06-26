#1 Write a program that calculates and prints the value according to the given formula:
    # Q= Square root of [(2*C*D)/H]
    # Following are the fixed values of C and H:
    # C is 50. H is 30.
    # D is the variable whose values should be input to your program.

import math

numbers = input("Please enter the value of D: ")
numbers = numbers.split(',')

result = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result.append(Q)

print(result)


#2 Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default.




#3 

class py_solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))

#4 What is the output of the following code? Explain your answer as well.

#I
class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        self.y = 1
def main():
    b = Derived_Test()
    print(b.x,b.y)
main()
#Ans in this we will get an error because the variable x here cannot be inherited.


#II 
 
class A:
    def __init__(self, x= 1):
        self.x = x
class der(A):
    def __init__(self,y = 2):
        super().__init__()
        self.y = y
def main():
    obj = der()
    print(obj.x, obj.y)
main()
#Ans here the o/p is 1 2


#III

class A:
    def __init__(self,x):
        self.x = x
    def count(self,x):
        self.x = self.x+1
class B(A):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y
    def count(self):
        self.y += 1     
def main():
    obj = B()
    obj.count()
    print(obj.x, obj.y)
main()
#Ans The o/p of this program is 3 1


#IV

class A:
    def __init__(self):
        self.multiply(15)
        print(self.i)
 
    def multiply(self, i):
        self.i = 4 * i;
class B(A):
    def __init__(self):
        super().__init__()
 
    def multiply(self, i):
        self.i = 2 * i;
obj = B()
#Ans The o/p of this program is 30


#5 Create a Time class and initialize it with hours and minutes.
    # Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
    # Make a method displayTime which should print the time.
    # Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.

class Time():
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(time1, time2):
        time3 = Time(0,0)
        if time1.minutes + time2.minutes > 60:
            time3.hours = (time1.minutes + time2.minutes)/60
        time3.hours = time3.hours + time1.hours + time2.hours
        time3.minutes = (time1.minutes + time2.minutes) - (((time1.minutes + time2.minutes)/60)*60)
        return time3

    def displayTime(self):
        print ("Present time is" , self.hours, "hours and" , self.minutes, "minutes")

    def DisplayMinute(self):
        print((self.hours * 60) + self.minutes)

a = Time(5,40)
b = Time(11,30)
c = Time.addTime(a,b)
c.displayTime()
c.DisplayMinute()


#6 Write a Person class with an instance variable, , and a constructor that takes an integer, , as a parameter. The constructor must assign  to  after confirming the argument passed as  is not negative; if a negative argument is passed as , the constructor should set  to  and print Age is not valid, setting age to 0.. In addition, you must write the following instance methods:
# yearPasses() should increase the  instance variable by .
# amIOld()  should perform the following conditional actions:
# If , print You are young..
# If  and , print You are a teenager..
# Otherwise, print You are old..	
# Sample Input:
# 4
# -1
# 10
# 16
# 18
# Sample Output:
# Age is not valid, setting age to 0.
# You are young.
# You are young.
 
# You are young.
# You are a teenager.
 
# You are a teenager.
# You are old.
 
# You are old.
# You are old.



class Person:
    def __init__(self,initialAge):
        if initialAge <0:
            self.age= 0
            print('Age is not valid, setting age to 0.')
        else:
            self.age=initialAge
    def amIOld(self):
        if self.age<13:
            print('You are young.')
        elif self.age>=13 and self.age<18:
            print('You are a teenager.')
        else:
            print('You are old.')
    def yearPasses(self):
        self.age+=1
y = int(input())
for i in range(0, y):
    age = int(input())         
    x = Person(age)  
    x.amIOld()
    for j in range(0, 3):
        x.yearPasses()       
    x.amIOld()
    print("")












price = 10
price = 20

print(price)

# we check in a patient named John Smith . He's 20 years old and is a new patient
#in this we have 3 variables

full_name = 'John Smith'
age = 20
is_new = True

name = input('what is your name? ')
print( 'welcome  ' +   name)

# two questions
# 1.persons name and favourite colour
# 2.then,print a message like "divya likes red"

name = input('what is your name? ')
colour = input('what is your favourite colour? ')
print(name + ' likes ' + colour)

# calculating age

Birth_year = input('Birth_year: ')
age = 2019 - int(Birth_year)
print(age)

# Ask a user their weight (in pounds), convert it to kilograms and print on the terminal

weight_lbs = input('weight (lbs): ')
#one pound=0.45
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

# string will define with "" quotes or '' quotes

 #if we use ""quotes in starting of the string then in middle of the string we need to use '' quotes
course = "python's course for begginers"
print(course)

#defina a string in multiple lines to send email
course = '''
Hi Sandeep

how are you

i am testing this email

'''

print(course)


#starting characters starts with 0 and
# if we start with ending -1
course = 'python for beginners'
print(course[0])

#if we want more than one character then

course = 'python for beginners'
print(course[0:6])


course = 'python for beginners'
print(len(course))

course = 'python for beginners'
print(course.upper())

course = 'python for beginners'
print(course.find('beginners'))

course = 'python for beginners'
print(course.replace('beginners', 'absolute beginners'))


course = 'python for beginners'
print('python' in course)


#Arithematic operators

print(10 + 2)

x = 10
x = x + 3
print(x)

#operator presedence

x = 10 + 3 * 2
print(x)

#Math functions

x = 2.9
print(round(x))

import math
print(math.ceil(2.9))

import math
print(math.floor(2.9))

#if statements

# 1.if its hot

     #it's a hot day
     #drink plenty of water
# 2.otherwise if it's cold

     #it's a cold day
     #wear warm clothes
# 3.otherwise

     #it's a lovely day

is_hot = False
is_cold = True

if is_hot:
    print("it's hot day")
    print('drink plenty of water')

elif is_cold:
    print("it's a cold day")
    print('wear warm clothes')

else:
    print("it's a lovely day")
    print("enjoy your day")

# price of a house is $1m
#if  buyers has good credit,
   #they need to put down 10%
#otherwise
   #they need to put down 20%
#print the down payment

price = 1000000
has_good_credit = True

if has_good_credit:

down_payment = 0.1 * price

else:
down_payment = 0.2 * price
print(f"down_payment: {down_payment}")

# logical operators (and,or,not)
#and = both conditions should be true
#or = atleast one condition should be true
#not = any bulian value converts in to false

# If applicant have high income AND good credit
       #Eligible for loan

       has_high_income = True
       has_good_credit = False
if has_high_income  and has_good_credit:
    print("Eligible for loan")

# If applicant has good credit AND doesn't have a criminal record
  # Eligible for loan

  has_good_credit = True
  has_criminal_record = False
  if has_good_credit = True and not has_criminal_record :
      print("Eligible for loan")

#comparision operators

# If temperature is greater than 30
 #it's a hot day

 #otherwise' if it's less than 10
#it's a cold day

 #otherwise
 #it's neither hot or cold'
temperature = 30
if temperature  > 30

    print("it's hot day")

else
    print(it's cold day')








# price of a house is $1m
# if  buyers has good credit,
   #they need to put down 10%
# otherwise
   #they need to put down 20%
# print the down payment

house_price = 1000000
has_good_credit = False
# down_payment = 10

if has_good_credit:
    down_payment =(0.1 * house_price)
elif:
    down_payment=(0.2 * house_price)
print(f"down_payment: {down_payment}")
print("Make sure data is uploaded to git")

# comparision operators

# If temperature is greater than 30
# it's a hot day

# otherwise' if it's less than 10
# it's a cold day

# otherwise
# it's neither hot or cold'
temperature = 35
if temperature > 30

    print("it's hot day")

else
    print("it's not a hot day")


    #if name is lessathan 3 characters

    #name must be atleast 3characters long
    #name atleat 3 characters
    #otherwise if it's is more than 50 characters long
    #name can be maximum of 50 characters
    #otherwise name looks good

    name = 3

    if len(name) > 3:

    print("name atleast 3 characters")
elif len(name) > 50:
print("name can be maximum of 50 characters")
else
name looks good

#weight converter:

#weight= 55
#(L)bs or (kg) :k

weight = input('weight: ')
unit = input('(L)bs or (K): ')
if unit.upper( )== "L":
    converted = weight * 0.45
    print(f"you are {converted} kilos")
else:
    converted  = weight / 0.45
    print(f"you are {converted} pounds")


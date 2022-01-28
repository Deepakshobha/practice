# When we have more than 2 conditions to check then we will use if-elif condition

print(''' waiter has given u the menu 

            1. Indain food 

            2. Italian Food 

            3. Russian Food''')

print('waiter is asking me for the choice')

choice = int(input('enter the choice'))  # 5

if choice == 1:

    print('waiter serves me Indian food')

    print('eat it and pay the bill')

elif choice == 2:

    print('waiter serves me Italian food')

    print('eat it and pay the bill')

elif choice == 3:

    print('waiter serves me Russian food')

    print('eat it and pay the bill')

else:

    print('Sir, That item is not available here')

    print('please look for Another Restaurant')


# write a Program to find the Maximum among 3 numbers

''' 

a=int(input('enter a value')) 

b=int(input('enter b value')) 

c=int(input('enter c value')) 

if a>b and a>c: 

    print('a is greater than b,c') 

elif b>c: 

    print('b is greater than a,c) 

else: 

    print('c is greater than a,b)
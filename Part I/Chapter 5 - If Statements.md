#  If Statements

### A Simple Example

```py
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
	print(car.upper())
	else:
	print(car.title())

----------------------
Audi
BMW
Subaru
Toyota
```
<br>

### Conditional Tests

Simplest conditional test checks whether the value of a variable is equal to the value of interest. First set a value to a variable, next equality operator checks if is true.

```py
car = 'bmw'
car == 'bmw'

-------------
True
```

<mark style="background: #FF5582A6;">**Note:**</mark> if you put a function in any variable you will not change the value first added. (ex.: lower (), upper (), title() ... )
<br>

### Checking for Inequality
If you want determine whether 1 values are not equal  ( !=) . 

```py
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
		print("Hold the anchovies!")

----------------------
Hold the anchovies!
```
<br>

### Checking Whether a Value Is in a List or NOT
To find out whether a particular value is already in a list, use the keyword "in" .

```py
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
True
'pepperoni' in requested_toppings
False

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
print(True)
if 'pepperoni' in requested_toppings:
print(True)
```

```PY
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
		print(user.title() + ", you can post a response if you wish.")

------------------------
Marie, you can post a response if you wish.1
```
<br>

### If - Else Statements
There is one thing you need to pay attention, when you use the "Else Statements" there is no way to define a condition. You will only be able in the cases of "If and Elif Statements".
```py
age = 17
if age >= 18:
		print("You are old enough to vote!")
		print("Have you registered to vote yet?")
else:
		print("Sorry, you are too young to vote.")
		print("Please register to vote as soon as you turn 18!")

-----------------------
Sorry, you are too young to vote
Please register to vote as soon as you turn 18!
```
<br>

### The If - Elif - Else Chain

```PY
age = 12
if age < 4:
		print("Your admission cost is $0.")
elif age < 18:
		print("Your admission cost is $5.")
else:
		print("Your admission cost is $10.")

---------------------------
Your admission cost is $5.
```
<br>


### Using Multiple Elif Blocks

```py
age = 12
if age < 4:
		price = 0
elif age < 18:
		price = 5
elif age < 65:
		price = 10
else:
		price = 5
print("Your admission cost is $" + str(price) + ".")

-----------------------------
Your admission cost is $5.
```
**Omitting the else Block:** Python does not require an else block at the end of an "If -  Elif chain". Sometimes an else block is useful, but others it's clearer to use an additional "Elif Statement" that catches the specific condition of interest. So the choice depends on the situation that is going to be applied.
<br>

### Testing Multiple Conditions
This code only works in the "If Statement", because will consider all the possibilities without discarding the other ones, assuming all conditions are the first one.
```py
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
		print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
		print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
		print("Adding extra cheese.")
		print("\nFinished making your pizza!")

--------------------------
Adding mushrooms.
Adding extra cheese.
Finished making your pizza!
```
This code would not work properly if we used an "If- Elif-Else" block, because the code would stop running after only one test passes. It's because in this cases when a one it's true automatically the other ones are false. 
<br>
## Using if Statements with Lists

```py
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
	for requested_topping in requested_toppings:
		 if requested_topping == 'green peppers':
			print("Sorry, we are out of green peppers right now.")

	else:
			print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

------------------
Adding mushrooms.
Sorry, we are out of green peppers right now.
Adding extra cheese.
Finished making your pizza! 

```

### Checking That a List Is Not Empty
```py
requested_toppings = []

	if requested_toppings:
		for requested_topping in requested_toppings:
			print("Adding " + requested_topping + ".")
		print("\nFinished making your pizza!")
	else:
		print("Are you sure you want a plain pizza?")

---------------------
Are you sure you want a plain pizza?

```
In this case if the list is not empty, the output will show each requested topping being added to the pizza.

```py
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

---------------------------
Adding mushrooms.
Sorry, we don't have french fries.
Adding extra cheese.
Finished making your pizza!
```
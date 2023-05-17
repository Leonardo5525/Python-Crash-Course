## How the input() Function Works
```py
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

======================================
Tell me something, and I will repeat it back to you: Hello everyone! Hello everyone!
```

### Using int() to Accept Numerical Input

```PY
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")

=====================================
How tall are you, in inches? 71
You're tall enough to ride!
```

### The Modulo Operator
A useful tool for working with numerical information is the <mark style="background: #FFF3A3A6;">modulo operator (%</mark>), which divides one number by another number and returns the remainder:
```py
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")

============================================
Enter a number, and I'll tell you if it's even or odd: 42
The number 42 is even.
```
<br>

## Introducing while Loops

### The while Loop in Action
```py
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

=============================
1
2
3
4
5
```


### Letting the User Choose When to Quit
```py
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
	while message != 'quit':
		message = input(prompt)
		if message != 'quit':
			print(message)

==========================
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello everyone!
Hello everyone!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello again.
Hello again.

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
```

### Using a flag
A flag is very important, will substitute the use of " While = True" and set to a variable the value "True". This will make possible to and a loop whenever you want easily then before. Just like the example in [[#Filling a Dictionary with User Input]]
```py
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print(message)

============================= 
# In this will not have a result, because the loop will continuing printing the message until input 'quit'.
```

### Using break to Exit a Loop
```py
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!\n")
		
=============================
Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) New York
I'd love to go to New York!
User Input and while Loops 125

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) San Francisco
I'd love to go to San Francisco!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) quit
```


### Using continue in a Loop
This will just keep the coding going normally just like in a loop. It will just discard the necessity of a element or a message after the conditional.

```py
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
print(current_number)

=============================
1
3
5
7
9
```

**Note - Avoiding Infinite Loop:** just need to add a way to count, " x += 1 "
```py
# This code will work
x = 1
while x <= 5:
print(x)
x += 1
==============================

# This loop runs forever!
x = 1
while x <= 5:
print(x)
```
<br>

## Using a while Loop with Lists and Dictionaries

### Moving Items from One List to Another
```py
# Start with users that need to be verified, users.py
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)


# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())


==================================
Verifying user: Candace
Verifying user: Brian
Verifying user: Alice

The following users have been confirmed:
Candace
Brian
Alice
```


### Removing All Instances of Specific Values from a List
In Chapter 3 we used remove() to remove a specific value from a list. The remove() function worked, but just because the value we were interested in appeared only once in the list. So what if you want to remove all instances of a value from a list?

```py
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
	
print(pets)


===========================
['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
['dog', 'dog', 'goldfish', 'rabbit']
```

In this case you can use a " While " or " For " loop to do that, will just pass in each element in the list checking the value if it its compatible.

### Filling a Dictionary with User Input

```py
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
	# Prompt for the person's name and response.
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")
	
	# Store the response in the dictionary:
	responses[name] = response
	
	# Find out if anyone else is going to take the poll.
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == 'no':
		polling_active = False
	
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")
```

## Summary
In this chapter you learned how to:
- Use input();
- Work with both text and numerical input; 
- While loops and how to make your programs run as long as your users want;
- Ways to control the flow of a while loop by setting an active flag;
- Using the break statement, and using the continue statement. You learned how to use a while loop to move items from one list to another and how to remove all instances of a value from a list. You also learned how while loops can be used with dictionaries.

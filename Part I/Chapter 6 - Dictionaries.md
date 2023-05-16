 .
 ### A Simple Dictionary
```py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

------------------------
green
5
```

## Working with Dictionaries
A dictionary in Python is a collection of key-value pairs ( {'color': 'green', 'points': 5} ), it's named pairs because the variable is. Each key is connected to a value, and you can use a key to access the value associated with that key. A key’s value can be a number, a string, a list, or even another dictionary. In fact, you can use any object that you can create in Python as a value in a dictionary. <mark style="background: #FFF3A3A6;">The string 'color' is a key in this dictionary, and its associated value is 'green'. </mark>

```py
alien_0 = {'color': 'green', 'points': 5}
```

You can store as many key-value pairs as you want in a dictionary.

### Accessing Values in a Dictionary
```py
alien_0 = {'color': 'green'}
print(alien_0['color'])

---------------------
green
```

### Adding New Key-Value Pairs
The difference between list and dictionaries, is that list are usually in sorted order and dictionaries in arbitrary.
```py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

----------------------
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5, 'y_position': 25, 'x_position': 0}
```

### Starting with an Empty Dictionary
It is also possible to work with a empty dictionary. Just like in lists start "list = [ ]", but in this case use braces { }.
```py
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

---------------------
{'color': 'green', 'points': 5}
```

### Modifying Values in a Dictionary
```py
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

-----------------------
The alien is green.
The alien is now yellow.
```
This change is going to make the last value to be forgotten, and can't get back. 

```py
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
	if alien_0['speed'] == 'slow':
		x_increment = 1
	elif alien_0['speed'] == 'medium':
		x_increment = 2
	else:
	# This must be a fast alien.
		x_increment = 3
	# The new position is the old position plus the increment.

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

----------------------
Original x-position: 0
New x-position: 2
```
This is a example a something forward in a game.

### Removing Key-Value Pairs
To remove we can use the function "del" too, all del needs is the name of the dictionary and the key that you want to remove.
```py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
u del alien_0['points']
print(alien_0)

------------------------
{'color': 'green', 'points': 5}
{'color': 'green'}
```

### A Dictionary of Similar Objects
You can also use a dictionary to store one kind of information about many objects. 
```py
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

----------------------
Sarah's favorite language is C.
```

**Note:** is case you don't have the key it will cause a "KeyError". And if the key doesn't have a value the code won't work causing a "SyntaxError: invalid syntax", and if is empty will show nothing.
**Note - Finding a key:** in case you don't know if you have a key or don't now the value.
```py
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print(favorite_languages.get ('jenny', 'No such user.'))
print(favorite_languages.get ('jen', 'No such user.'))
----------------------
No such user
python
``` 


## Looping Through a Dictionary
### Looping Through <mark style="background: #CACFD9A6;">All Key-Value Pairs</mark>
This way is not gonna see just he value, but the string too.
<mark style="background: #FFF3A3A6;">Method items() </mark>, which returns a list of key-value pairs. The for loop then stores each of these pairs in the two variables provided.
**Note:** key-value pairs are not returned in the order in which they were stored, even when looping through a dictionary.
```py
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)

----------------------------
Key: last
Value: fermi
Key: first
Value: enrico
Key: username
Value: efermi
```


### Looping Through <mark style="background: #CACFD9A6;">All the Keys</mark> in a Dictionary
The <mark style="background: #FFF3A3A6;">keys() method </mark>is useful when you don’t need to work with all of the values in a dictionary.
```py
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in favorite_languages.keys():
	print(name.title())

---------------------------
Jen
Sarah
Phil
Edward
```
Looping through the keys is actually the default behavior when looping through a dictionary, so this code would have exactly the same output if you wrote without <mark style="background: #FFF3A3A6;">any method</mark>
So if you wrote your code simple like this:
```py
for name in favorite_languages:
```

An example of dictionary  using a conditional 'if' for 'loop':
```py
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

------------------------------
Edward
Phil
Hi Phil, I see your favorite language is Python!
Sarah
Hi Sarah, I see your favorite language is C!
Jen
```

### Looping Through a Dictionary’s Keys <mark style="background: #CACFD9A6;">in Order</mark>
Use the <mark style="background: #FFF3A3A6;">sorted() </mark>function to get a copy of the keys in order:
```py
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

----------------------------
Edward, thank you for taking the poll.
Jen, thank you for taking the poll.
Phil, thank you for taking the poll.
Sarah, thank you for taking the poll.
```


### Looping Through <mark style="background: #CACFD9A6;">All Values</mark> in a Dictionary
Interested in the values that a dictionary contains, you can use the <mark style="background: #FFF3A3A6;">values() method</mark> to return a list of values without any keys.

```py
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

----------------------------
The following languages have been mentioned:
Python
C
Python
Ruby
```

**Special condition:** When you wrap set() around a list that contains duplicate items, this method will pull out the unique and results in a non repetitive list of languages that have been mentioned.
```py
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil':}
'python',
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title()) 

---------------------------------
The following languages have been mentioned:
Python
C
Ruby
```
<br>

## Nesting
Store a set of dictionaries in a list or a list of items as a value in a dictionary.
Can nest a set of dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary.

### A List of Dictionaries
This is a simple example how this function works, in real case is used for so much more information.
This will input a dictionaries inside a list and will make a loop through this list seeing all the dictionaries.
```py
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
u aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
print(alien)

-------------------------------------
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}
```

**Realistic example:**

```py
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

# Show the first 5 aliens:
	for alien in aliens[:5]:
		print(alien)
		print("...")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))


---------------------------------------
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
...
Total number of aliens: 30
```


### A List in a Dictionary
You can nest a list inside a dictionary any time you want more than
one value to be associated with a single key in a dictionary.
```py
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}

#Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['topping']:
	print("\t" + topping)

==============================
You ordered a thick-crust pizza with the following toppings:
	mushrooms
	extra cheese
```

### A Dictionary in a Dictionary
In this case we first define a dictionary called users with two keys: one each for the usernames 'aeinstein' and 'mcurie', so all the dictionaries need to be inside the main one.
```py
users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}
for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']

print("\tFull name: " + full_name.title())
print("\tLocation: " + location.title())

==============================================
Username: aeinstein
Full name: Albert Einstein
Location: Princeton
Username: mcurie
Full name: Marie Curie
Location: Paris
```
If each user’s dictionary had different keys, the code inside the for loop would be more complicated. So for cases with identical or similar cases, is recommended the use, but if you are going to make a bigger distinguish, it's better to use another way. 
# **List**
### Accessing Elements in a List
```py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
# trek
```


### Returning last value on the list or -2 (before the last) -3 (before -2) and continue

```py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
# specialized
```

### Modifying Elements in a List
```py
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)
# ['ducati','honda', 'yamaha', 'suzuki']
```


<br/>
<br/>

## Adding items to a list
### Appending (last)
In this case the new item is going to be added in the end of the list.
```py
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)
# ['honda', 'yamaha', 'suzuki','ducati']
```

### Appending from a empty list
In this case it's going to keep adding a item in the end of the list in the last place each time time.
``` py
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
# ['honda', 'yamaha', 'suzuki','ducati']
```

### Inserting elements into a list (any)
You can add a item on the list in any place of the list you want.
*note:* if you want to add any item in the end of the list you need to use de <mark> index [-1] </mark> 
```py
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1, 'ducati')
print(motorcycles)
# ['honda', 'ducati', 'yamaha', 'suzuki']
```


<br/>
<br/>

## Removing items on the list

### Removing an item using the DEL statement (need to know index)
You can choose what item you want to 'DELETE' from the list, just need to know the <mark> index [0]</mark>
```py
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)
# ['yamaha', 'suzuki']
```


### Removing an Item Using the pop() Method (last, in this case)
This way you can remove the item on the list by inputting the value on a variable.
And is special in the index part, because if you don't add <mark>(index) </mark> you are gong to automatically remove the last item of the list. But if you want you can choose the item you want to remove. 
```py
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)
# ['honda', 'yamaha', 'suzuki']
# yamaha
```


### Removing Using pop() Method (ANY, in this case)
You can choose the exactly item you want to remove of the list by inputting the  <mark> (index) </mark> and adding to a variable.
```py
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
# The first motorcycle I owned was a Honda.
```


### Removing a item by value (any)
This is a special case, it's going to need just the name (value) of the string or number on the list to be removed, so you can choose without knowing the index value like the other ones above.
```py
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)
# ['honda', 'yamaha', 'suzuki']
```

<br/>
<br/>

## Organizing your list

### Organizing a list using SORT()
In this way the list can't go back to his original form.
But you can make the list in alphabetical <u> order  </u>  or in <u> reverse order</u>.
```py
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# ['audi', 'bmw', 'subaru', 'toyota']
cars.sort(reverse= True)
print(cars)
# ['toyota', 'subaru', 'bmw', 'audi']
```


### Organizing a list using SORTED()
In this way the list <mark> can go back to his original order </mark>  and you can sort the list in order or in reverse order, by editing when you print.
```py
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
```


### Organizing a list reverse chronological order REVERSE()

```py
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
```


### Finding the length of a list

```
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
# 4
```

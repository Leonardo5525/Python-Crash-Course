#Try ir Yourself - 3-1. Names: 
names = ['leo', 'vitoria', 'joao', 'lucas']
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[3])

#Try it Yourself - 3-2. Greetings:
names = ['leo naka', 'vitoria', 'joao', 'lucas']
message = (names[0].capitalize())
print(message)

#Try it Yourself - 3-3. Your Own List: 
transportation = ['car', 'motocycle', 'bike', 'airplane']
message = (f'I would like to own a Honda {transportation[0]}')
print(message)

#Try it Yourself 3-4. Guest List: 
name = ['goro', 'sato', 'miyuki']
print(f'Please come to my dinner {name[0]}')
print(f'Please come to my dinner {name[1]}')
print(f'Please come to my dinner {name[2]}')

#Try it Yourself 3-5. Changing Guest List: 
name = ['goro', 'sato', 'miyuki']
cancel_name ='goro'
name.remove(cancel_name)
name.append('shimizu')
print(f'Please come to my dinner {name[0]}')
print(f'Please come to my dinner {name[2]}')
print(f"I understand you can´t make it {cancel_name}")
print(f'Please come to my dinner {name[-1]}')

#Try it Yourself 3-6. More Guests: 
name = ['goro', 'sato', 'miyuki']
cancel_name ='goro'
name.remove(cancel_name)
name.append('shimizu')
print(f'Please come to my dinner {name[0]}'
      )
print(f'Please come to my dinner {name[2]}')
print(f"I understand you can´t make it {cancel_name}")
print(f'Please come to my dinner {name[-1]}')
print(f'I found a bigger table so i am gonna invete some more people')
name.insert(-2, 'mayumura')
name.insert(-2, 'gibson')
name.append('gibson jr')
print(f'Please come to my dinner {name[0]}')
print(f'Please come to my dinner {name[2]}')
print(f"I understand you can´t make it {cancel_name}")
print(f'Please come to my dinner {name[-2]}')
print(f'Please come to my dinner {name[-3]}')
print(f'Please come to my dinner {name[-4]}')
print(f'Please come to my dinner {name[-1]}')

#Try it Yourself 3-7. Shrinking Guest List:
name = ['goro', 'sato', 'miyuki']
cancel_name ='goro'
name.remove(cancel_name)
name.append('shimizu')
print(f'Please come to my dinner {name[0]}')
print(f'Please come to my dinner {name[2]}')
print(f"I understand you can´t make it {cancel_name}")
print(f'Please come to my dinner {name[-1]}')
print(f'I found a bigger table so i am gonna invete some more people')
name.insert(-2, 'mayumura')
name.insert(-2, 'gibson')
name.append('gibson jr')
print(f'Please come to my dinner {name[0]}')
print(f'Please come to my dinner {name[2]}')
print(f'Please come to my dinner {name[-2]}')
print(f'Please come to my dinner {name[-3]}')
print(f'Please come to my dinner {name[-4]}')
print(f'Please come to my dinner {name[-1]}')
print(f"I understand you can´t make it {cancel_name}")
print('I am sorry my table will not be ready on time')
one_name = name.pop(-4)
two_name = name.pop(-3)
three_name = name.pop(-2)
four_name = name.pop(-1)
print(f'I am sorry that i can note invite you to dinner {one_name}')
print(f'I am sorry that i can note invite you to dinner {two_name}')
print(f'I am sorry that i can note invite you to dinner {three_name}')
print(f'I am sorry that i can note invite you to dinner {four_name}')
print(f'My table still have your seat reserved {name[0]}')
print(f'My table still have your seat reserved {name[1]}')
del name[1]
del name[0]
print(name)

#Try it Yourself 3-7. Shrinking Guest List: NEW WAYS TO DO THE SAME
name = ['goro', 'sato', 'miyuki']
cancel_name ='goro'
name.remove(cancel_name)
name.append('shimizu')
print(f'Please come to my dinner {name[0]}')
print(f'Please come to my dinner {name[2]}')
print(f"I understand you can´t make it {cancel_name}")
print(f'Please come to my dinner {name[-1]}')
print(f'I found a bigger table so i am gonna invete some more people')
name.insert(-2, 'mayumura')
name.insert(-2, 'gibson')
name.append('gibson jr')
print(f'Please come to my dinner {name[0]}')
print(f'Please come to my dinner {name[2]}')
print(f'Please come to my dinner {name[-2]}')
print(f'Please come to my dinner {name[-3]}')
print(f'Please come to my dinner {name[-4]}')
print(f'Please come to my dinner {name[-1]}')
print(f"I understand you can´t make it {cancel_name}")
print('I am sorry my table will not be ready on time')
one_name = name.pop(-1)
two_name = name.pop(-1)
three_name = name.pop(-1)
four_name = name.pop(-1)
print(f'I am sorry that i can note invite you to dinner {one_name}')
print(f'I am sorry that i can note invite you to dinner {two_name}')
print(f'I am sorry that i can note invite you to dinner {three_name}')
print(f'I am sorry that i can note invite you to dinner {four_name}')
print(f'My table still have your seat reserved {name[0]}')
print(f'My table still have your seat reserved {name[1]}')
del name[0]
del name[0]
print(name)

#Try it Yourself - 3-8. Seeing the World: 
locals = ['Japan', 'USA', 'Koreia', 'Canada', 'Australia']
print(locals)
print(sorted(locals))
#print(sorted(locals, reverse=True))
print(locals)
locals.reverse()
print(locals)
locals.reverse()
print(locals)
locals.sort()
print(cars)
locals.sort(reverse= True)
print(locals)

# Try it Yourself - 3-9. Dinner Guests: 
name = ['goro', 'sato', 'miyuki']
cancel_name ='goro'
name.remove(cancel_name)
name.append('shimizu')
print(f'Please come to my dinner {name[0]}'
      )
print(f'Please come to my dinner {name[2]}')
print(f"I understand you can´t make it {cancel_name}")
print(f'Please come to my dinner {name[-1]}')
print(f'I found a bigger table so i am gonna invete some more people')
name.insert(-2, 'mayumura')
name.insert(-2, 'gibson')
name.append('gibson jr')
print(f'Please come to my dinner {name[0]}')
print(f'Please come to my dinner {name[2]}')
print(f"I understand you can´t make it {cancel_name}")
print(f'Please come to my dinner {name[-2]}')
print(f'Please come to my dinner {name[-3]}')
print(f'Please come to my dinner {name[-4]}')
print(f'Please come to my dinner {name[-1]}')
print(len(name))

# Try it Yourself - 3-10. Every Function: 
'''Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or any-
thing else you’d like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once.'''

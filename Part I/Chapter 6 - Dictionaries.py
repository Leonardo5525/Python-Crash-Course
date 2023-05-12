'''
Try It Yourse lf
6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
'''
person = {'name': 'leo', 'last': 'nakamura', 'age': 25}
print(person['name'])
print(person['last'])
print(person['age'])

'''
Try It Yourse lf
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.
'''


'''
Try It Yourse lf
6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
    •Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
    • Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

'''
words = {'list': 'listas', 'if': 'condicional', 'while': 'repetição' }

print (f"List: {words['list']}.\n")
print (f"If: {words['if']}.\n")
print (f"While: {words['while']}.\n")


'''
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings should automatically be included in the output.
'''
words = {'list': 'listas', 'if': 'condicional', 'while': 'repetição' }

for key, value in words.items():
    print("\nKey: " + key)
    print("Value: " + value)  

'''
6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
    • Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
    • Use a loop to print the name of each river included in the dictionary.
    • Use a loop to print the name of each country included in the dictionary.
'''
words = {'Nile': 'Egipty', 'Amazonas': 'Brazil', 'Danúbio': 'Europa' }

for key, value in words.items():
    print(f'The river {key} pass through {value}')

'''
6-6. Polling: Use the code in favorite_languages.py (page 104).
    • Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
    • Loop through the list of people who should take the poll. If they have already taken the poll print a message thanking them for responding.If they have not yet taken the poll, print a message inviting them to take the poll.
'''
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
'leo': 'nothing',
'anthony': 'nothing' 
}
friends = ['phil', 'sarah', 'edward', 'jen']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends and favorite_languages:
        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")
    else:
        print(" Hi " + name.title() + ", I see you didn't take the favorite language is pool, SO LETS!")
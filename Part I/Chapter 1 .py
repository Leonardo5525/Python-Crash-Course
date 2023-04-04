#Combining or Concatenating Strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

#Adding Whitespace to Strings with Tabs or Newlines
print('Leonardo \nYuiti \tNakamura \n\t 25 anos')

#Stripping Whitespace
favorite_language = 'python '
favorite_language.rstrip()
print(favorite_language)
favorite_language.lstrip()
' python'
print(favorite_language)
favorite_language.strip()
' python '
print(favorite_language)

#Avoiding Syntax Errors with Strings
message = "\nOne of Python's strengths is its diverse community."
print(message)
#This line is going to fail
'''message = '\nOne of Python's strengths is its diverse community.'
print(message)
'''

#Try Yourself - 
# 2-3. Personal Message:
name =  'Leo'
print(f'“Hello {name}, would you like to learn some Python today?”')
#2-4. Name Cases:
name = 'leonardo nakamura'
print(name.lower())
print(name.upper())
print(name.title())
#2-5. Famous Quote:
quote = "A person who never made a mistake never tried anything new" 
author = "Albert Einstein"
print(f'{author} once Said {quote}')
#2-6. Famous Quote 2:
quote = "A person who never made a mistake never tried anything new" 
famous_person = "Einstein"
message = (f'{famous_person} once Said {quote}')
print(message)
#2-7. Stripping Names:
name = ' Leo '
print(f'\n{name}')
print(f'\t{name}')
print(f'\n\t{name}')
print(f'\n{name.lstrip()}')
print(f'\n{name.rstrip()}')
print(f'\n{name.strip()}')

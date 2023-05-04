# Variables and Datas
## Combining or Concatenating Strings

```py
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)
# Hello, Ada Lovelace!
# Leonardo 
```


## Adding White space to Strings with Tabs or Newlines
The function ' \n ' is going to break the line, going to the next paragraph.
The function ' \t ' is going to create a indetation, just like tab creating a little white space. .
```py
print('Leonardo \nYuiti \tNakamura \n\t 25 anos')
# Leonardo
# Yuiti    Nakamura
#          25 anos
```


## Stripping White space

```py
favorite_language = 'python '
favorite_language.rstrip()
print(favorite_language)
favorite_language.lstrip()
' python'
print(favorite_language)
favorite_language.strip()
' python '
print(favorite_language)
# python 
# python 
# python 
```


## Avoiding Syntax Errors with Strings
If you use quotation mark in the string, you can use apostrophe without cause a Syntax Error in the code.
```py
message = "\nOne of Python's strengths is its diverse community."
print(message)
# One of Python's strengths is its diverse community.
```


## This line is going to fail
The reason to fail in this case it's because when you add a apostrophe in the middle of the sentence you need to use quotation mark. Otherwise the code will have a Syntax Error because doesn't know the end of the string.
```py
message = '\nOne of Python's strengths is its diverse community.'
print(message)
# SyntaxError: unterminated string literal (detected at line 1)
```

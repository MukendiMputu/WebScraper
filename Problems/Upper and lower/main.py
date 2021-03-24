# the list with words from string
# please, do not modify it
some_iterable = input().split()

# use dictionary comprehension to create a new dictionary
dict_modify = {str.upper(words): str.lower(words) for words in some_iterable}
print(dict_modify)

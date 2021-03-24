# put your python code here
usr_input = input().split()
words_input = [str.lower(word) for word in usr_input]
dict_words_occurrence = {str.lower(key): words_input.count(key) for key
                         in words_input}

for key, value in dict_words_occurrence.items():
    print(f"{key} {value}")

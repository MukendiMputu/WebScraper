country_list = ["France\n", "China\n", "Brazil\n"]

country_file = open('countries.txt', 'a', encoding='utf-8')
country_file.writelines("Turkey\n")
country_file.close()

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world", 5//2)
# print("Hello world", word[::-1])

word = 'geeks'
result = True
for i in range(len(word)//2):
    if word[i] != word[len(word)-i-1]:
        result = False
        break
    
statement = 'madam is a palindrome. Racecar is also a palindmore'
list_character = statement.split(' ')    
set_character = set(list_character)    
print("== list_character ", list_character)
print("== set_character ", set_character)

dict_count_character ={}
for item in set_character:
    dict_count_character[item]=list_character.count(item)

print("== dict_count_character ", dict_count_character)
max_value = max(dict_count_character.values())
min_value = min(dict_count_character.values())



result = {
    'max': max_value,
    'words': list(filter(lambda x: x[1]==max_value, dict_count_character.items() ))
}
print('=== result ', result)

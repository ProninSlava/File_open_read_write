import sys
from pprint import pprint
import os

#________________________________________________________
# получкние списка файлов и сортировка по расширению .txt
path = os.getcwd()
files = os.listdir(path)
files_filtered = [x for x in files if x.endswith('.txt')]
#________________________________________________________

dict_name_sum = {}
dict_name_text = {}

for name_file in files_filtered:
    with open(name_file, 'r', encoding='UTF-8') as file:
        count = 0
        for row in file:
            if name_file not in dict_name_text:
                dict_name_text[name_file] = row.strip() + '\n'
            else:
                dict_name_text[name_file] += row.strip() + '\n'
            count += 1
        dict_name_sum[name_file] = count
#_______________________________________________________________________________
#сортировка по значению
dict_name_sort = dict(sorted(dict_name_sum.items(), key=lambda items: items[1]))
#_______________________________________________________________________________

with open('dz_fail.txt', 'w', encoding='UTF-8') as f:
    for name_file in dict_name_sort:
        f.write(name_file + '\n')
        f.write(str(dict_name_sort[name_file]) + '\n')
        f.write(dict_name_text[name_file])

print(dict_name_sum)
print(dict_name_sort)
pprint(dict_name_text)



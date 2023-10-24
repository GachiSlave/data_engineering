import re


f = open('text_1_var_69')

dict = {}
for line in f:
    line = re.split('\?|,|:|!|&| |\n|\.|\'', line)
    for item in line:
        if item in dict:
            dict[item] += 1
        else:
            dict.update({item: 1})
    dict.pop('')
f.close()
sorted(dict.items(), key=lambda x: x[1]).reverse()

for i in dict.items():
    print(i)
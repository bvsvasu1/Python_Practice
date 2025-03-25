import re

# text = 'the cost of each item is $3.85 and 3.89 and $3..89'

# pattern = r'\$[0-9]+\.[0-9]+'

# findalls = re.findall(pattern,text)

# print(findalls)


regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

import re
print("1", re.findall(regex_pattern, "ML"))
print("2", re.match(regex_pattern, "ML"))
print("3", str(bool(re.match(regex_pattern, "ML"))))
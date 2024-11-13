import re

a = "** my name is fareed ** you are *so good*\n *fareed* you are damn"
cleaned_string = re.sub(r'[*\n]', '', a)
print(cleaned_string)

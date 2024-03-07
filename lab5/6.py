import re
text = 'I have a iphone.'
print(re.sub("[ ,.]", ":", text))
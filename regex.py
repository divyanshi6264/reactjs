import re
text = "I am learning Python"
result = re.search("python",text)
print(result)

import re
text = "I am learning python"
result = re.match("python",text)
print(result)

import re
text = "I am learning python"
result = re.findall("python",text)
print(result)

import re
text = "my mobile no. is 987654321"
result = re.findall(r"\d", text)
print(result)

import re
text = "my mobile no. is 987654321"
result = re.findall(r"\d+", text)
print(result)

import re
text = "my mobile no. is 987654321"
result = re.findall(r"\w", text)
print(result)

import re
text = "my mobile no. is 987654321"
result = re.findall(r"\w+", text)
print(result)

import re
text = "my mobile no. is 987654321"
result = re.findall(r"\s", text)
print(result)


import re
text = "my mobile no. is 987654321"
result = re.findall(r"\s+", text)
print(result)

import re
text = "my mobile no. is 987654321"
result = re.findall(r".", text)
print(result)

import re
text = "my mobile no. is 987654321"
result = re.findall("mobil?e", text)
print(result)

import re
text = "my mobile no. is 987654321"
result = re.findall(r"0$", text)
print(result)

import re
text = "my mobile no. is 987654321"
result = re.findall(r"\bcat\b", text)
print(result)

import re
text = "my mobile no. is 987654321"
result = re.findall(r"mobile*", text)
print(result)






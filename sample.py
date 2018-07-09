# cook your dish here
import re

#time = "00:39:12     0      0.00      0.00      0.00      0.00      0.00    100.00"
time = "00:39:12     48      0.00      0.00      0.00      0.00      0.00    100.00"
words = re.split(" +", time)
if re.match('\d', words[1]):
    for s in words:
        print(s)
else:
    print(words[1])

#['Dec', '3', '14:25:33']

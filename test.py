import re

user_input = "-- -- -- --"
a = list(user_input)
print(a)

user_input = "..."
input_lenth = len(user_input)
for i in [".",",","!","?"]:
    if i in user_input:
        input_lenth -= 1
print(input_lenth)
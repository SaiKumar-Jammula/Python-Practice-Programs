
import random , string
abc=string.ascii_lowercase

print(random.choice(abc))
print(random.choices(abc,k=5))
print("".join(random.choices(abc,k=5)))
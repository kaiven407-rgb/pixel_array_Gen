import re

with open('src/utils.ts', 'r') as f:
    text = f.read()

old_move = r'''
 dbMoveFig\(
    inst
    nil
    list\(list\(dx dy\) "R0"\)
 \)
'''

new_move = r'''
   inst~>xy = list(car(inst~>xy)+dx cadr(inst~>xy)+dy)
'''

text = re.sub(old_move, new_move, text, flags=re.VERBOSE)

with open('src/utils.ts', 'w') as f:
    f.write(text)

print("Fixed move logic in Python generator")

with open('src/utils.ts', 'r') as f:
    text = f.read()

text = text.replace('''   dbMoveFig(
      inst
      nil
      list(list(dx dy) "R0")
   )''', '''   inst~>xy = list(car(inst~>xy)+dx cadr(inst~>xy)+dy)''')

with open('src/utils.ts', 'w') as f:
    f.write(text)

print("Fixed move logic in Python generator")

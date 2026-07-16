import re

with open('src/utils.ts', 'r') as f:
    text = f.read()

# Fix segment logic
pattern1 = r'(if seg_purpose\.lower\(\) == rov_purpose\.lower\(\):)'
repl1 = r'if seg_purpose.lower() == rov_purpose.lower() and row == max_active_row:'
text = re.sub(pattern1, repl1, text)

# Fix row logic
pattern2 = r'(if purpose\.lower\(\) == rov_purpose\.lower\(\):)'
repl2 = r'if purpose.lower() == rov_purpose.lower() and row == max_active_row:'
text = re.sub(pattern2, repl2, text)

with open('src/utils.ts', 'w') as f:
    f.write(text)

print("Fixed max_active_row in Python generator")

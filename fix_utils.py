import re

with open('src/utils.ts', 'r') as f:
    text = f.read()

# I want to undo the messy sed swap first.
# Wait, let me just git checkout src/utils.ts!
# I can't, no .git. But I can just download the original file from github.

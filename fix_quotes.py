with open('src/utils.ts', 'r') as f:
    text = f.read()

text = text.replace(r"code.push(\'            \"R0\"\');", r"code.push('          \"R0\"');")

with open('src/utils.ts', 'w') as f:
    f.write(text)

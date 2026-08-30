import re
lines=open('index.html','r',encoding='utf-8').read().splitlines()
count=0
for i,line in enumerate(lines, start=1):
    opens=len(re.findall(r'<div\b', line))
    closes=len(re.findall(r'</div>', line))
    if opens or closes:
        count += opens - closes
        print(f'{i:4}: +{opens} -{closes} => {count} | {line.strip()}')
print('\nFinal unclosed count:', count)

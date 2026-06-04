with open('kdd.html', 'r') as f:
    lines  = f.read().split('\n')

for page in ['overview', 'timeline', 'rules', 'mag240m', 'wikikg90m', 'pcqm4m', 'participate', 'update', 'results', 'workshop']:
    lines_new  = lines.copy()
    for i, line in enumerate(lines_new):
        if page in line:
            print(line)
            lines_new[i] = line.replace('<a href=', "<a class=\"active\" href=")
    
    with open(f'kdd_{page}.html', 'w') as f:
        f.write('\n'.join(lines_new))


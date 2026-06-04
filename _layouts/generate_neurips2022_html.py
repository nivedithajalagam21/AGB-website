with open('neurips2022.html', 'r') as f:
    lines  = f.read().split('\n')

for page in ['overview', 'timeline', 'rules', 'participate', 'update', 'results', 'workshop', 'datasets']:
    lines_new  = lines.copy()
    for i, line in enumerate(lines_new):
        if page in line:
            print(line)
            lines_new[i] = line.replace('<a href=', "<a class=\"active\" href=")
    
    with open(f'neurips2022_{page}.html', 'w') as f:
        f.write('\n'.join(lines_new))


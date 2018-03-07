
def get_file_contents(file_name):
    with open(file_name, 'r') as f:
        return f.read().split('\n')

def parse_flags(flags):
    return ('n' in flags,
            'l' in flags,
            'i' in flags,
            'v' in flags,
            'x' in flags)

def get_comparison_function(v, x, i):
    if v: 
        if x: cmp = lambda x, y: x != y
        else: cmp = lambda x, y: x not in y
    else: 
        if x: cmp = lambda x, y: x == y
        else: cmp = lambda x, y: x in y

    if i: return lambda x, y: cmp(x.lower(), y.lower())

    return cmp


def grep(pattern, files, flags=''):
    
    response = ''
    n, l, i, v, x = parse_flags(flags)

    cmp = get_comparison_function(v, x, i)

    for file_name in files:
        contents = get_file_contents(file_name)

        if l:
            for line in contents:
                if cmp(pattern, line):
                    response += file_name + '\n'
                    break

        else:
            for i, line in enumerate(contents):

                prefix = ''
                if len(files) > 1:
                    prefix += file_name + ':'
                if n:
                    prefix += '{}:'.format(i+1)

                if cmp(pattern, line):
                    response += prefix + line + '\n'

    return response

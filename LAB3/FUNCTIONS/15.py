def putations(string):
    if len(string) <= 1:
        return [string]
    else:
        ps = []
        for i in range(len(string)):
            first_c = string[i]
            remaining_c = string[:i] + string[i+1:]
            for p in putations(remaining_c):
                ps.append(first_c + p)
        return ps

def print_putations(string):
    ps = putations(string)
    for p in ps:
        print(p)


def resolve(c1, c2):
    for literal in c1:
        if literal.startswith('-'):
            opposite = literal[1:]
        else:
            opposite = '-' + literal
        if opposite in c2:
            return (c1 - {literal}) | (c2 - {opposite})
    return None

clause1 = {'-P', 'Q'}

clause2 = {'P'}
result = resolve(clause1, clause2)
print("Resolved Clause:", result)

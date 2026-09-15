VARIABLES = ["csc", "maths", "phy", "che", "tam", "eng", "bio"]
 
DOMAIN = ["Monday", "Tuesday", "Wednesday"]
 
CONSTRAINTS = [
    ("csc", "maths"), ("csc", "phy"), ("maths", "phy"),
    ("maths", "che"), ("maths", "tam"), ("phy", "tam"),
    ("phy", "eng"), ("che", "eng"), ("tam", "eng"),
    ("tam", "bio"), ("eng", "bio")
]
 
def backtrack(assign):
    if len(assign) == len(VARIABLES):
        return assign
 
    var = select(assign)
 
    for day in DOMAIN:
        if consistent(var, day, assign):
            assign[var] = day
            res = backtrack(assign)
            if res:
                return res
            del assign[var]
    return None
 
def select(assign):
    for v in VARIABLES:
        if v not in assign:
            return v
 
def consistent(var, day, assign):
    for a, b in CONSTRAINTS:
        if var == a or var == b:
            other = b if var == a else a
            if other in assign and assign[other] == day:
                              return False
    return True
 
solution = backtrack({})
 
if solution:
    print("Solution:")
    for s, d in solution.items():
        print(s, "->", d)
else:
    print("No solution exists.")


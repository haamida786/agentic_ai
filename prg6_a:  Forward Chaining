def forward_chaining(facts, rules, goal):
    inferred = set(facts)
    while True:
        new_fact = False
        for premise, conclusion in rules:
            if set(premise).issubset(inferred) and conclusion not in inferred:
                inferred.add(conclusion)
                new_fact = True
        if goal in inferred:
            return True
        if not new_fact:
            return False

facts = ['P']
rules = [
(['P'],'Q'),
(['Q'],'R')
]
goal = 'R'
print("Goal Found:", forward_chaining(facts, rules, goal))

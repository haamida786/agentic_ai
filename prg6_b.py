def backward_chaining(facts, rules, goal):
    if goal in facts:
        return True
    for premise, conclusion in rules:
        if conclusion == goal:
            if all(backward_chaining(facts, rules, p) for p in premise):
                return True
            return False

facts = ['P']
rules = [
(['P'], 'Q'),
(['Q'], 'R')
]
goal = 'R'
print("Goal Found:", backward_chaining(facts, rules, goal))

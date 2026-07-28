import itertools
 
def evaluate(expr, model):
    for s, v in model.items():
        expr = expr.replace(s, str(v))
    expr = expr.replace("AND", "and")
    expr = expr.replace("OR", "or")
    expr = expr.replace("NOT", "not")
    expr = expr.replace("=>", "<=")
    return eval(expr)
 
def model_check(kb, query, symbols):
    print("Truth Table:")
    print("-------------------------")
    entails = True
 
    for values in itertools.product([False, True], repeat=len(symbols)):
        model = dict(zip(symbols, values))
        kb_result = evaluate(kb, model)
        query_result = evaluate(query, model)
        print(model, "KB:", kb_result, "Query:", query_result)
 
        if kb_result and not query_result:
            entails = False
 
    return entails
 
symbols = ["P", "Q"]
kb = "P AND Q"
query = "P"
 
if model_check(kb, query, symbols):
    print("\nKB entails Query")
else:
    print("\nKB does NOT entail Query")


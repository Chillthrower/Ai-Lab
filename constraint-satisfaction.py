VARIABLES = ["csc", "maths", "phy", "che", "tam", "eng", "bio"]
DOMAIN = ["Monday", "Tuesday", "Wednesday"]
CONSTRAINTS = [("csc", "maths"), ("csc", "phy"), ("mat", "phy"), ("mat", "che"), 
                ("mat", "tam"), ("phy", "tam"), ("phy", "eng"), ("che", "eng"), 
                ("tam", "eng"), ("tam", "bio"), ("eng", "bio")]

def backtrack(assignment):
    if len(assignment) == len(VARIABLES): 
        return assignment
    
    var = next(v for v in VARIABLES if v not in assignment)
    
    for value in DOMAIN:
        if all(assignment.get(v) != value for v1, v2 in CONSTRAINTS for v in (v1, v2) if var in (v1, v2)):
            assignment[var] = value
            result = backtrack(assignment)
            if result: 
                return result
            assignment.pop(var)
    return None

solution = backtrack({})
print(solution)

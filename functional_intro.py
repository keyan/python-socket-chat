def codeAssign():
    names = ['Mary', 'Isla', 'Sam']
    
    for i in range(len(names)):
        names[i] = hash(names[i])

    print names
    
def functionalCodeAssign():
    names = ['Mary', 'Isla', 'Sam']
    
    codeNames = map(lambda x: hash(x), names)
    
    print codeNames

codeAssign()
functionalCodeAssign()
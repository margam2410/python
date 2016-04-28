""" Dispay resistor colour code values"""
colours = [ "black", "brown", "red", "orange", "yellow",
            "green", "blue", "violet", "grey","white" ]
cv = list (enumerate (colours))
for c in cv:
    print c[0], "\t", c[1]

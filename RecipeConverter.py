print "Welcome to Dom's Recipe Converter", 
print "Enter the amount of Flour (Cups):", 
Flour = raw_input()

print "Enter the amount of Water (Cups):",
Water = raw_input()

print "Enter the amount of Salt (Teaspoons):",
Salt = raw_input()

print "Enter the amount of Yeast (Teaspoons):",
Yeast = raw_input()

print "Enter the Recipe adjustment factor (Ex 2.0 would double the recipe):",
x = raw_input()

print "--- Modified Recipe ---"

print "Flour(Cups): %.2f" % (int(Flour) * (int(x)))
print "Water(Cups): %.2f" % (int(Water) * (int(x)))
print "Salt(Teaspoons): %.2f" % (int(Salt) * (int(x)))
print "Yeast(Teaspoons): %.2f" % (int(Flour)* (int(x)))

print "--- Good Luck With Your New Recipe :) ---"
print "--- Thanks for Using Dom's Recipe Conver! ---"
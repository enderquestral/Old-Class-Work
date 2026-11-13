pdollars = float(input("Price dollars? "))
pcents = float(input("Price cents? "))
tipper = float(input("Tip percentage [0-100]? "))
print((pdollars+(pcents/100)) * tipper/100)
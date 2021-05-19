held = int(input("Enter classes held"))
att = int(input("Enter classes attended"))
percentage = ((att / held) * 100)
if (percentage < 75):
    print("not eligible")
elif (percentage == 75):
    print("Just Eligible")
else:
    print("Eligible")



V = int(input("Enter total number of vehicles: "))
W = int(input("Enter total number of wheels: "))

four_wheelers = (W - 2 * V) // 2
two_wheelers = V - four_wheelers

if W % 2 != 0 or two_wheelers < 0 or four_wheelers < 0:
    print("Invalid input")
else:
    print("Number of two-wheelers =", two_wheelers)
    print("Number of four-wheelers =", four_wheelers)
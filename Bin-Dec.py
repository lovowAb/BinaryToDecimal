"""
  Abdullahi
  lovowAb
  change binary to decimal
"""

binary = int(input("Enter a binary number: "))
sum = 0
counter = 0
while binary > 0:
    y = binary % 10
    binary = binary // 10
    sum = sum + y * (2**counter)
    counter += 1
print("Your result in decimal is: ", sum)

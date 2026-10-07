temp=float(input("Enter the temperature : "))
if temp>35: 
  print("It is very hot")
elif temp>25:
  print("The weather is warm")
elif temp>15:
  print("It is cool and breezy")
elif temp>0:
  print("It is cold")
elif temp>-10:
  print("It is freezing")
else:
  print("Invalid")
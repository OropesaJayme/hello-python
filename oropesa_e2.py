import sys

Sw = float(sys.argv[1])

if Sw >= 220:
    print("Super Typhoon")
elif Sw >= 118 or Sw == 219:
    print("Typhoon")
elif Sw >= 89 or Sw == 117:
    print("Severe Tropical Storm")
elif Sw >= 62 or Sw == 88:
    print("Tropical Storm")
else:
    print("Tropical Depression")

import sys
x = sys.argv[1:]
x = str(x)

dic = {
    "-": "Minus",
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

for key, value in dic.items():
    x = x.replace(key, value)

print(x)

jahr1=int(input("Jahr 1:"))
monat1=int(input("Monat 1:"))
tag1=int(input("Tag 1:"))
jahr2=int(input("Jahr 2:"))
monat2=int(input("Monat 2:"))
tag2=int(input("Tag 2:"))

def zeitlich_vor(jahr1, monat1, tag1, jahr2, monat2, tag2):
    if jahr1<jahr2:
        return 1
    elif jahr1>jahr2:
        return 0
    elif monat1<monat2:
        return 1
    elif monat1>monat2:
        return 0
    elif tag1<tag2:
        return 1
    else:
        return 0

zeitlich_vor(jahr1, monat1, tag1, jahr2, monat2, tag2)

if 1:
    print("Datum 1 liegt zeitlich vor Datum 2")
elif 0:
    print("Datum 2 liegt zeitlich vor Datum 1")

jahr=int(input("Jahr:"))
monat=int(input("Monat:"))
tag=int(input("Tag:"))

def wochentag(jahr,monat,tag):
    if jahr%4==0 and jahr%100!=0 or jahr%400==0:
        if monat==1:
            k=5
        elif monat==2:
            k=1
    if monat==1:
        k=6
    elif monat==2:
        k=2
    elif monat==3:
        k=2
    elif monat==4:
        k=5
    elif monat==5:
        k=0
    elif monat==6:
        k=3
    elif monat==7:
        k=5
    elif monat==8:
        k=1
    elif monat==9:
        k=4
    elif monat==10:
        k=6
    elif monat==11:
        k=2
    elif monat==12:
        k==4

    j=jahr%100
    c=jahr//100
    d=tag+k+j+j//4-2*c%4
    wochentag=d%7
    if wochentag==0:
        print("Sonntag")
    elif wochentag==1:
        print("Montag")
    elif wochentag==2:
        print("Dienstag")
    elif wochentag==3:
        print("Mittwoch")
    elif wochentag==4:
        print("Donnerstag")
    elif wochentag==5:
        print("Freitag")
    elif wochentag==6:
        print("Samstag")

print(wochentag(jahr,monat,tag))   
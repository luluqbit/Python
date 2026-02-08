jahr = int(input("Jahr: "))
monat = int(input("Monat: "))
tag = int(input("Tag: "))

def datum(jahr,monat,tag):
     if monat==12 and tag==31:
          jahr=jahr+1
          monat=1
          tag=1
     elif monat in [1,3,5,7,8,10,12] and tag<31:
          tag=tag+1
     elif monat in [4,6,9,11] and tag<30:
          tag=tag+1
     elif monat==2 and tag<28:
          tag=tag+1
     elif monat==1 or monat==3 or monat==5 or monat==7 or monat==8 or monat==10 or monat==12 and tag==31:
          monat=monat+1
          tag=1
     elif monat==4 or monat==6 or monat==9 or monat==11 and tag==30:
          tag=1
          monat=monat+1
     elif jahr%4==0 and jahr%100!=0 or jahr%400==0:
          if monat==2 and tag<29:
                tag=tag+1
          elif monat==2 and tag==29:
                tag=1
                monat=monat+1
     elif monat==2 and tag==28:
          tag=1
          monat=monat+1
     print("Der nächste Tag ist:", tag,".",monat,".",jahr)
     return
datum(jahr,monat,tag)          
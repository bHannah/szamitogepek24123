from Szamitogep import Szamitogep

def listaba_rendezes():
    f = open("szamitogepek.txt", "r", encoding="utf8")
    f.readline()
    sorok = f.readlines()
    f.close()
    szamitogepek = []
    for i in range(len(sorok)):
        darab = Szamitogep(sorok[i])
        szamitogepek.append(darab)
    return szamitogepek

def listakiiras(szamitogepek):
    for i in range(len(szamitogepek)):
        op_r = szamitogepek[i].op_r
        ram = szamitogepek[i].ram
        print(f"{op_r} ({ram})")

def szamitogepek_szama(szamitogepek):
    ossz = 0
    for i in range(len(szamitogepek)):
        ossz += szamitogepek[i].ram
    vegsoatlag = round(ossz / len(szamitogepek), 3)
    print(f"Átlag: {vegsoatlag}")

def legtobbramos_op_r(szamitogepek):
    max = 0
    for i in range(len(szamitogepek)):
        if szamitogepek[max].ram < szamitogepek[i].ram:
            max = i
    eredmeny = szamitogepek[max].op_r
    print(f"Legtöbb ram-ot tartalmazó oprendszer: {eredmeny}")

def windowsosgepekszama(szamitogepek):
    windowsosgepek = 0
    for i in range(len(szamitogepek)):
        if szamitogepek[i].op_r == "Win":
            windowsosgepek += 1
    print(f"Hány Windowsos gépünk van: {windowsosgepek} db Windowos számítógépünk van")

def ramkereses(szamitogepek):
    vizsgaltram = 16
    print(f"Van-e {vizsgaltram} GB RAM-nál nagyobb windows: ", end="")
    van = False
    for i in range(len(szamitogepek)):
        if szamitogepek[i].ram > vizsgaltram and szamitogepek[i].op_r == "Win":
            van = True

    if van == True:
        print("Van ilyen gép")
    else:
        print("Nincs ilyen gép")
from Szamitogep import Szamitogep

peldany1 = Szamitogep("Win", 32)
peldany2 = Szamitogep("Mac", 16)
peldany3 = Szamitogep("Win", 16)

szamitogepek = []

szamitogepek.append(peldany1)
szamitogepek.append(peldany2)
szamitogepek.append(peldany3)
for i in range(len(szamitogepek)):
    op_r = szamitogepek[i].op_r
    ram = szamitogepek[i].ram
    print(f"{op_r} ({ram})")

print("Átlag: ", end="")
ossz = 0
for i in range(len(szamitogepek)):
    ossz += szamitogepek[i].ram
print(round(ossz / len(szamitogepek), 3))


print("Legtöbb ram-ot tartalmazó oprendszer: ", end="")
max = 0
for i in range(len(szamitogepek)):
    if szamitogepek[max].ram < szamitogepek[i].ram:
        max = i
print(szamitogepek[max].op_r)

print("Hány Windowsos gépünk van: ", end="")
windowsosgepek = 0
for i in range(len(szamitogepek)):
    if szamitogepek[i].op_r == "Win":
        windowsosgepek += 1
print(f"{windowsosgepek} db Windowos számítógépünk van")

vizsgaltram = 16
print(f"Van-e {vizsgaltram} GB-nál nagyobb windows: ", end="")
van = False
for i in range(len(szamitogepek)):
     if szamitogepek[i].ram > vizsgaltram and szamitogepek[i].op_r == "Win":
         van = True

if van == True:
    print("Van ilyen gép")
else:
    print("Nincs ilyen gép")





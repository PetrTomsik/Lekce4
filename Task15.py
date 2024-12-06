jmena = []
text1 = input(f"První prvek")
text2 = input(f"Druhý prvek")
text3 = input(f"Třetí prvek")
jmena.append(text1)                 #prida jen jednu vec
jmena.append(text2)
jmena.append(text3)
print(f"Všechny jmena {jmena}")
print(f"První jmeno {jmena[0]}")
print(f"Druhý jmeno {jmena[1]}")
print(f"Tretí jmeno {jmena[2]}")

print(f" delka  {len(jmena)}")           # 3 celkový počet

dalsi_jmena = ["Karel", "Honza"]         # pridava list do listu
jmena.extend(dalsi_jmena)
jmena.pop()                             # z konce mi to odebere posledni prvek

#druhe reseni
duha = []
duha.append(input("Zadej první barvu duhy"))
duha.append(input("Zadej druhou barvu duhy"))
duha.append(input("Zadej treti barvu duhy"))
print(f"Všechny jmena {duha}")
print(f"První jmeno {duha[0]}")
print(f"Druhý jmeno {duha[1]}")
print(f"Tretí jmeno {duha[2]}")


obr = []
obr.append(["aa","bb"])
obr.append("lek")
obr.append("baf")
print(obr)
print(f"prvek na indexu 0 {obr[0]}")
print(f"prvek na indexu 0 {obr[0]}")
print(f"prvek na indexu 0 {obr[0]}")
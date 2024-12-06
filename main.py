text = "Pomocí speciálního příkazu s operátorem [] můžeme řetězec pčečíst od konce?"
#vypište, kolikrát se vyzkytuje znak "s"
print(f"Kolikrat je v textu zank s: {text.count('s')}")     # pocítá kolikrat je tam a
#vypište, co se vyskytuje od indexu 7 po index 14
#print(f"v {text} je na indexu 1 zank {text[1]}")            # zjisti na daným míste hodnotu
#vypište, co se vyskytuje od indexu 7 po index 14
print(f"v {text} je na indexu 7-14 zank: {text[7:15]}")        # zjisti na daným míste hodnotu  od do  zavorky pravy alt f [ a g ]   trojka neni zahrnuta
#vyřizněte text tak, aby bylovypsano slovo operátorem

print(f"vypis slovo oprator z textu: {text[29:39]}")
print(f'{text.index("operátorem")} a delka {len("operátorem")}')
print(f'slovo je tedy {text[text.index("operátorem"):text.index("operátorem") + len("operátorem")]}')

delka = len(text)
print(f"v {text} je na kazdy druhy zank {text[0:delka:2]}")
#text vypiste naopak
print(f"{text} a obracený text je  {text[::-1]}")



text = "qsxht!trfecdtcbgřáýčerdxdpsěš d21rřcřetčěpe**u?rsS"
#delka = len(text)
text1 = text[5:]
text2 = text1[::-1]
print(f"Ignorujte prvních pět znaků: {text1}")
print(f"Otočte řetězec: {text2}")
print(f"Vypište každý čtvrtý znak: {text2[::4]}")

# lepsí varianta
text = text[5::]
text = text[::-1]
text = text[::4]
print(text)
#na jeden řádek

text = "qsxht!trfecdtcbgřáýčerdxdpsěš d21rřcřetčěpe**u?rsS"

print(f"Ignorujte prvních pět znaků: {text1}")
print(f"Otočte řetězec: {text2}")
print(f"Vypište každý čtvrtý znak: {text2[::4]}")



text2 = "qsxht!trfecdtcbgřáýčerdxdpsěš d21rřcřetčěpe**u?rsS"

print(text2.upper()) # velkýma pismenama
print(text2.lower()) # malýma pismenama

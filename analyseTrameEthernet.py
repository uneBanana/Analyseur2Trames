# Analyseur d'une trame ETHERNET

# La trame doit etre mise dans le fichier './trame'
file = open("trame")
tr = file.read()


# On supprime maintenant les espaces et les retours de lignes
tr2 = ""
for c in tr:
	if(c not in [' ', '\r', '\n']):
		tr2 += c


## Description

# Les 8 premiers bits correpondent au préambules
print("Préambule : ")
print(tr2[0:8])
print()

print("Adresse Dest : ", end='')
print(tr2[8:14])


print("Adresse Source : ", end='')
print(tr2[14:20])

print("\nData : ")
data = tr2[20:-4]
print(data)

# Les 4 derniers bits correspondent au CRC
print("\nCRC : ", end='')
print(tr2[-4:-1], tr2[-1], sep='')



## Analyse des données
print("\n\nLes données sous forme ASCII")
data2 = bytes.fromhex(data)
print(data2)

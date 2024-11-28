#ouvrir (et lire) un fichier .txt non-pythoniquement
fp = open("test.txt")
text = fp.read()
fp.close()
print(text)

#ouvrir (et lire ligne par ligne) un fichier pythoniquement
with open("test.txt") as fp:
    lines = fp.readlines()
print(lines)                    #no need to close the file

#lire les lignes une par une
with open("test.txt") as fp:
    line1 = fp.readline()
    line2 = fp.readline()
print(line1[:-1])       #pour ne pas printer le caractere aui saut la ligne

#ouverture en écriture qui supprime le contenu pré existant
line_to_write = "bonjour monde\n"
with open("test.txt", "w"):
    fp.write(line_to_write)

#ouverture en écriture qui ne supprime pas le contenu mais va "appender"
with open("test.txt","a"):
    fp.write(["sylvain\n","joe\n","lily\n"])
print(lines)
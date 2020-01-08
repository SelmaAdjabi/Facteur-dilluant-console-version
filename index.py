print("--- Facteur dilluant ---\n")
print("1. Calculer le volume initiale")
print("2. Calculer le facteur dilluant")

choix = input("\nEntrer votre choix : ")

if choix == "1" :
	print("\nNB: Veuillez entrer les volumes avec les memes unités !\n")
	fd = float(input("Entrer le facteur dilluant : "))
	vf = float(input("Entrer le volume finale : "))
	vi = vf / fd
	vd = vf - vi
	print("\n*** Resultat ***")
	print("Volume initiale = " + str(vi))
	print("Volume dilluant = " + str(vd))
elif choix == "2" :
	print("\nNB: Veuillez entrer les volumes avec les memes unités !\n")
	vi = float(input("Entrer le volume initiale : "))
	vf = float(input("Entrer le volume finale : "))
	fd = 1 / (vi / vf)
	vd = vf - vi
	print("\n*** Resultat ***")
	print("Facteur dilluant = " + str(fd))
	print("Volume dilluant = " + str(vd))
else :
	print("Veuillez entrer un choix valide !")


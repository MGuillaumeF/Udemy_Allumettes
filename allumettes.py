#-*- coding: utf-8 -*-
from math import floor
def jeuOrdi (nbAllumettes, limite) :
	if (nbAllumettes <= 2) :
		return 1
	elif (nbAllumettes <= (limite + 1)) :
		return nbAllumettes - 1
	elif (nbAllumettes - limite) >= (limite * 2 + 2) :
		return limite
	else :
		return floor((nbAllumettes - 2) / 3) if floor((nbAllumettes - 2) / 3) >= 1 else 1
	
def jeuJoueur (nbAllumettes, limite) :
	result = 0
	while True:
		result = int(input("Combien d'alumette à retirer ?"))
		if (result >= 1 and result <= limite and result <= nbAllumettes) :
			return result

def jeu (nbAllumettes):
	# Initialisation
	limite = 2
	print('le jeu commence avec {} allumettes'.format(nbAllumettes))

	while (nbAllumettes != 0):
		# Tour du joueur
		enter = int(jeuJoueur (nbAllumettes, limite))
		limite = enter * 2
		nbAllumettes -= enter
		print('le joueur retire {} allumettes'.format(enter))
		if (nbAllumettes == 0) :
			print ("Le joueur perd")
			break
		print('Il reste {} alumettes'.format(nbAllumettes))
		
		# Tour de l'ordinateur
		enter = jeuOrdi (nbAllumettes, limite)
		limite = enter * 2
		nbAllumettes -= enter
		print('l\'ordinateur retire {} allumettes'.format(enter))
		if (nbAllumettes == 0) :
			print ("L'ordinateur perd")
			break
		print('Il reste {} alumettes'.format(nbAllumettes))

	# Fin
	print("le jeu est terminé")

def main():
	jeu(30)

main()

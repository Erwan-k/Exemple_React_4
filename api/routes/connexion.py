from flask_restful import Api, Resource, reqparse
import os
from sqlalchemy.engine.url import make_url
import mysql.connector

def getMysqlConnection():
	url = make_url(os.getenv('DATABASE_URL'))
	mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)
	return mydb

def convertir_nbr_vers_base(nbr): 
    base = 26
    liste = list("abcdefghijklmnopqrstuvwxyz")
    if not nbr:
        return "a"
    elif nbr == 1:
        return "b"
    else:
        mot = ""
        compteur = 0
        while nbr>=base**compteur: #Recherche de du plus grand c tel que base**c<=nbr
            compteur += 1
        compteur -=1
        for i in range(compteur,-1,-1):     #Pour i allant de c à 0 : 
            val = nbr//(base**i)            #On regarde la valeur du i-ème bit (le nombre d'apparition du multiple base**c dans nbr)
            nbr -= val*base**i              #On ampute cette valeur à nbr
            mot += liste[val]               #Et on l'ajoute à notre mot
        return mot

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

def recuperer_structure_tex_rb():
	chemin = os.getcwd()
	chemin = chemin[:chemin.index("src/app")]+"src/app"

	os.chdir(chemin)
	fichier = open("structure.tex",'rb')
	structure = fichier.read()
	fichier.close()

	return structure

def enregistrer_un_fichier_wb(nom,contenu):
	fichier = open(nom,'wb')
	fichier.write(contenu)
	fichier.close()

def lire_un_fichier_rb(nom_fichier):
	fichier = open(nom_fichier,'rb')
	data = fichier.read()
	fichier.close()
	return data

def rechercher_la_prochaine_ref():
	chemin = os.getcwd()
	chemin = chemin[:chemin.index("src/app")]+"src/app"
	os.chdir(chemin+"/fichiers")

	fichiers = os.listdir()
	compteur = 0
	while convertir_nbr_vers_base(compteur) in fichiers:
		compteur += 1

	return convertir_nbr_vers_base(compteur)

def ecrire_objet(reference,objet):
	chemin = os.getcwd()
	chemin = chemin[:chemin.index("src/app")]+"src/app"
	os.chdir(chemin+"/fichiers")

	with open(reference,'wb') as fichier:
		pickle.dump(objet, fichier)

def recuperer_objet(reference):
	chemin = os.getcwd()
	chemin = chemin[:chemin.index("src/app")]+"src/app"
	os.chdir(chemin+"/fichiers")

	with open(reference, 'rb') as fichier:
		return pickle.load(fichier)

def supprimer_objet(reference):
	chemin = os.getcwd()
	chemin = chemin[:chemin.index("src/app")]+"src/app"
	os.chdir(chemin+"/fichiers")

	os.remove(reference)

def envoyer_email(adresse_mail,message):
	pass

from random import choice,shuffle
from time import time

from ajouter_valeurs import *

connexion1_post_args = reqparse.RequestParser()
connexion1_post_args.add_argument("adresse_mail",type=str,required=True)
connexion1_post_args.add_argument("mot_de_passe",type=str,required=True)
connexion1_post_args.add_argument("nom",type=str,required=True)
connexion2_post_args = reqparse.RequestParser()
connexion2_post_args.add_argument("adresse_mail",type=str,required=True)
connexion2_post_args.add_argument("code",type=str,required=True)
connexion3_post_args = reqparse.RequestParser()
connexion3_post_args.add_argument("adresse_mail",type=str,required=True)
connexion4_post_args = reqparse.RequestParser()
connexion4_post_args.add_argument("adresse_mail",type=str,required=True)
connexion5_post_args = reqparse.RequestParser()
connexion5_post_args.add_argument("adresse_mail",type=str,required=True)
connexion5_post_args.add_argument("code",type=str,required=True)
connexion5_post_args.add_argument("nouveau_mdp",type=str,required=True)
connexion6_post_args = reqparse.RequestParser()
connexion6_post_args.add_argument("adresse_mail",type=str,required=True)
connexion6_post_args.add_argument("mot_de_passe",type=str,required=True)
connexion6_post_args.add_argument("nouveau_mdp",type=str,required=True)
connexion7_post_args = reqparse.RequestParser()
connexion7_post_args.add_argument("adresse_mail",type=str,required=True)
connexion7_post_args.add_argument("mot_de_passe",type=str,required=True)

class connexion1(Resource):
	def post(self): #s_inscrire
		body = connexion1_post_args.parse_args()
		[adresse_mail,mot_de_passe,nom] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que l'adresse mail n'est pas déjà dans la table Users.	
		mycursor.execute("SELECT count(*) FROM Users WHERE adresse_mail = \""+adresse_mail+"\"")
		if mycursor.fetchall()[0][0]:
			return {"retour":"l'adresse mail est déjà enregistrée'"}

		#Je vérifie que le format des informations renseignées est conforme.
		if not adresse_mail.count("@"):
			return {"retour":"l'adresse mail doit au moins comporter le symbole @"}
		if len(nom) <= 3:
			return {"retour":"le nom doit faire au moins 3 caractères"}
		if len(mot_de_passe) <= 6:
			return {"retour":"le mot de passe doit faire au moins 6 caractères"}
		nombre_maj = 0
		for i in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
			if mot_de_passe.count(i):
				nombre_maj+= mot_de_passe.count(i)
		nombre_min = 0
		for i in list("abcdefghijklmnopqrstuvwxyz"):
			if mot_de_passe.count(i):
				nombre_min+= mot_de_passe.count(i)
		nombre_chiffre = 0
		for i in list("0123456789"):
			if mot_de_passe.count(i):
				nombre_chiffre+= mot_de_passe.count(i)
		if not nombre_maj:
			return {"retour":"le mot de passe doit contenir une majuscule"}
		if not nombre_min:
			return {"retour":"le mot de passe doit contenir une minuscule"}
		if not nombre_chiffre:
			return {"retour":"le mot de passe doit contenir un chiffre"}
		if not nombre_maj+nombre_min+nombre_chiffre< len(mot_de_passe):
			return {"retour":"le mot de passe doit contenir un caractère spécial"}

		#Je crée un code que j'envoie par mail et l'enregistre dans la table adresse_mail_non_verif.
		lettres = list("abcdefghijklmnopqrstuvwxyz")
		nombres = list("0123456789")
		caracteres = list("éè_àù")
		n_l,n_n,n_c = choice(range(5,8)),choice(range(3,6)),choice(range(1,3))
		code = [choice(lettres) for i in range(n_l)]+[choice(nombres) for i in range(n_n)]+[choice(caracteres) for i in range(n_c)]
		shuffle(code)
		code = "".join(code)
		#Envoie par mail 
		envoyer_email(adresse_mail,"Pour vérifier votre adresse mail, veuillez renseigner le code : "+code+" à la page https://exemple_messagerie.erwankerbrat.com/verif_mail")
		ajouter_Adresse_mail_non_verif(adresse_mail,code,mycursor,mydb)

		#J'ajoute une ligne à la table professeur.
		ajouter_Users(adresse_mail,nom,mot_de_passe,mycursor,mydb)

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}

class connexion2(Resource):
	def post(self): #verifier_son_adresse_mail
		body = connexion2_post_args.parse_args()
		[adresse_mail,code] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que l'adresse mail existe dans la table professeur.
		mycursor.execute("SELECT count(*) FROM Users WHERE adresse_mail = \""+adresse_mail+"\"")
		if not mycursor.fetchall()[0][0]:
			return {"retour":"l'adresse mail specifiee n'est pas connue de notre bdd"}

		#Je vérifie que l'adresse mail existe toujours dans la table adresse_mail_non_verif.
		mycursor.execute("SELECT count(*) FROM Adresse_mail_non_verif WHERE adresse_mail = \""+adresse_mail+"\"")
		if not mycursor.fetchall()[0][0]:
			return {"retour":"l'adresse mail est déjà vérifiée"}

		#Je vérifie que le code est le bon.
		mycursor.execute("SELECT code FROM Adresse_mail_non_verif WHERE adresse_mail = \""+adresse_mail+"\"")
		code_dans_la_table = mycursor.fetchall()[0][0]
		if code != code_dans_la_table:
			return {"retour":"le code spécifiée n'est pas le bon"}

		#Je supprime la valeur dans la table adresse_mail_non_verif.
		mycursor.execute("DELETE FROM Adresse_mail_non_verif WHERE adresse_mail = \""+adresse_mail+"\"")
		mydb.commit()

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}

class connexion3(Resource):
	def post(self): #demander_un_nouvel_email_de_confirmation
		body = connexion3_post_args.parse_args()
		[adresse_mail] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que l'adresse mail existe dans la table professeur.
		mycursor.execute("SELECT count(*) FROM Users WHERE adresse_mail = \""+adresse_mail+"\"")
		if not mycursor.fetchall()[0][0]:
			return {"retour":"l'adresse mail specifiee n'est pas connue de notre bdd"}

		#Je vérifie que l'adresse mail existe toujours dans la table adresse_mail_non_verif.
		mycursor.execute("SELECT count(*) FROM Adresse_mail_non_verif WHERE adresse_mail = \""+adresse_mail+"\"")
		if not mycursor.fetchall()[0][0]:
			return {"retour":"l'adresse mail est déjà vérifiée"}

		#Je récupère le code et le renvoie par mail.
		mycursor.execute("SELECT code FROM Adresse_mail_non_verif WHERE adresse_mail = \""+adresse_mail+"\"")
		code = mycursor.fetchall()[0][0]

		envoyer_email(adresse_mail,"Pour vérifier votre adresse mail, veuillez renseigner le code : "+code+" à la page https://exemple_messagerie.erwankerbrat.com/verif_mail")

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}

class connexion4(Resource):
	def post(self): #demander_un_code_pour_changer_son_mdp
		body = connexion4_post_args.parse_args()
		[adresse_mail] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que l'adresse_mail existe dans la table professeur.
		mycursor.execute("SELECT count(*) FROM Users WHERE adresse_mail = \""+adresse_mail+"\"")
		if not mycursor.fetchall()[0][0]:
			return {"retour":"l'adresse mail specifiee n'est pas connue de notre bdd"}

		#Je vérifie que l'adresse_mail n'existe plus dans la table adresse_mail_non_verif.
		mycursor.execute("SELECT count(*) FROM Adresse_mail_non_verif WHERE adresse_mail = \""+adresse_mail+"\"")
		if mycursor.fetchall()[0][0]:
			return {"retour":"l'adresse mail n'a pas été vérifiée"}

		#Je vérifie qu'un code n'existe pas déjà.
		mycursor.execute("SELECT count(*) FROM Changer_de_mdp_code WHERE adresse_mail = \""+adresse_mail+"\"")

		#Si oui, je le récupère et le renvoie par mail.
		if mycursor.fetchall()[0][0]:

			mycursor.execute("SELECT code FROM Changer_de_mdp_code WHERE adresse_mail = \""+adresse_mail+"\"")
			code = mycursor.fetchall()[0][0]
			envoyer_email(adresse_mail,"Pour changer votre mot de passe, veuillez renseigner le code : "+code+" à la page https://exemple_messagerie.erwankerbrat.com/gestion_mdp")

		#Si non, j'en crée un et l'envoie par mail.
		else:
			lettres = list("abcdefghijklmnopqrstuvwxyz")
			nombres = list("0123456789")
			caracteres = list("éè_àù")
			n_l,n_n,n_c = choice(range(5,8)),choice(range(3,6)),choice(range(1,3))
			code = [choice(lettres) for i in range(n_l)]+[choice(nombres) for i in range(n_n)]+[choice(caracteres) for i in range(n_c)]
			shuffle(code)
			code = "".join(code)

			ajouter_Changer_de_mdp_code(adresse_mail,code,mycursor,mydb)
			envoyer_email(adresse_mail,"Pour changer votre mot de passe, veuillez renseigner le code : "+code+" à la page http://195.154.118.79:9874/gestion_mdp")

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}

class connexion5(Resource):
	def post(self): #changer_son_mdp_a_l_aide_d_un_code
		body = connexion5_post_args.parse_args()
		[adresse_mail,code,nouveau_mdp] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que l'adresse_mail existe dans la table professeur.
		mycursor.execute("SELECT count(*) FROM Users WHERE adresse_mail = \""+adresse_mail+"\"")
		if not mycursor.fetchall()[0][0]:
			return {"retour":"l'adresse mail specifiee n'est pas connue de notre bdd"}

		#Je vérifie que l'adresse_mail n'existe plus dans la table adresse_mail_non_verif.
		mycursor.execute("SELECT count(*) FROM Adresse_mail_non_verif WHERE adresse_mail = \""+adresse_mail+"\"")
		if mycursor.fetchall()[0][0]:
			return {"retour":"l'adresse mail n'a pas été vérifiée"}

		#Je vérifie que le format du nouveau mot_de_passe est valide.
		if len(nouveau_mdp) <= 6:
			return {"retour":"le mot de passe doit faire au moins 6 caractères"}
		nombre_maj = 0
		for i in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
			if nouveau_mdp.count(i):
				nombre_maj+= nouveau_mdp.count(i)
		nombre_min = 0
		for i in list("abcdefghijklmnopqrstuvwxyz"):
			if nouveau_mdp.count(i):
				nombre_min+= nouveau_mdp.count(i)
		nombre_chiffre = 0
		for i in list("0123456789"):
			if nouveau_mdp.count(i):
				nombre_chiffre+= nouveau_mdp.count(i)
		if not nombre_maj:
			return {"retour":"le mot de passe doit contenir une majuscule"}
		if not nombre_min:
			return {"retour":"le mot de passe doit contenir une minuscule"}
		if not nombre_chiffre:
			return {"retour":"le mot de passe doit contenir un chiffre"}
		if not nombre_maj+nombre_min+nombre_chiffre< len(nouveau_mdp):
			return {"retour":"le mot de passe doit contenir un caractère spécial"}

		#Je vérifie qu'un code ait bien été enregistré.
		mycursor.execute("SELECT count(*) FROM Changer_de_mdp_code WHERE adresse_mail = \""+adresse_mail+"\"")
		if not mycursor.fetchall()[0][0]:
			return {"retour":"aucune demande de changement de mot de passe n'a été trouvée dans notre BDD"}

		#Je vérifie que le code correspond puis je le supprime de changer_de_mdp_code.
		mycursor.execute("SELECT code FROM Changer_de_mdp_code WHERE adresse_mail = \""+adresse_mail+"\"")
		code_dans_la_table = mycursor.fetchall()[0][0]
		if code_dans_la_table != code:
			return {"retour":"le code spécifié n'est pas bon"}

		mycursor.execute("DELETE FROM Changer_de_mdp_code WHERE adresse_mail = \""+adresse_mail+"\"")
		mydb.commit()

		#Je modifie le mot_de_passe dans la table professeur.
		mycursor.execute("UPDATE Users SET mdp = \""+nouveau_mdp+"\" WHERE adresse_mail = \""+adresse_mail+"\"")
		mydb.commit()

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}

class connexion6(Resource):
	def post(self): #changer_son_mdp_a_l_aide_du_mdp_actuel
		body = connexion6_post_args.parse_args()
		[adresse_mail,mot_de_passe,nouveau_mdp] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que l'adresse_mail existe dans la table professeur.
		mycursor.execute("SELECT count(*) FROM Users WHERE adresse_mail = \""+adresse_mail+"\"")
		if not mycursor.fetchall()[0][0]:
			return {"retour":"l'adresse mail specifiee n'est pas connue de notre bdd"}

		#Je vérifie que l'adresse_mail n'existe plus dans la table adresse_mail_non_verif.
		mycursor.execute("SELECT count(*) FROM Adresse_mail_non_verif WHERE adresse_mail = \""+adresse_mail+"\"")
		if mycursor.fetchall()[0][0]:
			return {"retour":"l'adresse mail n'a pas été vérifiée"}

		#Je vérifie que le format du nouveau mot_de_passe est valide.
		if len(nouveau_mdp) <= 6:
			return {"retour":"le mot de passe doit faire au moins 6 caractères"}
		nombre_maj = 0
		for i in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
			if nouveau_mdp.count(i):
				nombre_maj+= nouveau_mdp.count(i)
		nombre_min = 0
		for i in list("abcdefghijklmnopqrstuvwxyz"):
			if nouveau_mdp.count(i):
				nombre_min+= nouveau_mdp.count(i)
		nombre_chiffre = 0
		for i in list("0123456789"):
			if nouveau_mdp.count(i):
				nombre_chiffre+= nouveau_mdp.count(i)
		if not nombre_maj:
			return {"retour":"le mot de passe doit contenir une majuscule"}
		if not nombre_min:
			return {"retour":"le mot de passe doit contenir une minuscule"}
		if not nombre_chiffre:
			return {"retour":"le mot de passe doit contenir un chiffre"}
		if not nombre_maj+nombre_min+nombre_chiffre< len(nouveau_mdp):
			return {"retour":"le mot de passe doit contenir un caractère spécial"}

		#Je vérifie que l'ancien mot_de_passe est le bon.
		mycursor.execute("SELECT mdp FROM Users WHERE adresse_mail = \""+adresse_mail+"\"")
		mdp_dans_la_table = mycursor.fetchall()[0][0]
		if mdp_dans_la_table != mot_de_passe:
			return {"retour":"le code spécifié n'est pas bon"}

		#Je change le mot_de_passe.
		mycursor.execute("UPDATE Users SET mdp = \""+nouveau_mdp+"\" WHERE adresse_mail = \""+adresse_mail+"\"")
		mydb.commit()

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}

class connexion7(Resource):
	def post(self): #se_connecter
		body = connexion7_post_args.parse_args()
		[adresse_mail,mot_de_passe] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que l'adresse mail existe dans la table professeur.
		mycursor.execute("SELECT count(*) FROM Users WHERE adresse_mail = \""+adresse_mail+"\"")
		if not mycursor.fetchall()[0][0]:
			return {"retour":"l'adresse mail specifiee n'est pas connue de notre bdd"}

		#Je vérifie que l'adresse mail n'existe plus dans la table adresse_mail_non_verif.
		mycursor.execute("SELECT count(*) FROM Adresse_mail_non_verif WHERE adresse_mail = \""+adresse_mail+"\"")
		if mycursor.fetchall()[0][0]:
			return {"retour":"l'adresse mail n'est pas vérifiée"}

		#Je vérifie que le mot de passe est le bon.
		mycursor.execute("SELECT mdp FROM Users WHERE adresse_mail = \""+adresse_mail+"\"")
		mdp = mycursor.fetchall()[0][0]
		if mdp != mot_de_passe:
			return {"retour":"le mot de passe specifie n'est pas le bon"}

		#Je supprime les enventuels anciens token.
		mycursor.execute("DELETE FROM Token WHERE adresse_mail = \""+adresse_mail+"\"")
		mydb.commit()

		#Je génére un token et l'enregistre dans la table token.
		lettres = list("abcdefghijklmnopqrstuvwxyz")
		nombres = list("0123456789")
		caracteres = list("éè_àù")
		n_l,n_n,n_c = choice(range(5,8)),choice(range(3,6)),choice(range(1,3))
		token = [choice(lettres) for i in range(n_l)]+[choice(nombres) for i in range(n_n)]+[choice(caracteres) for i in range(n_c)]
		shuffle(token)
		token = "".join(token)
		ajouter_Token(adresse_mail,token,mycursor,mydb)

		mycursor.close()
		mydb.close()

		return {"retour":"ok","token":token}



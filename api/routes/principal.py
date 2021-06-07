from flask_restful import Api, Resource, reqparse
import os
from sqlalchemy.engine.url import make_url
import mysql.connector
from time import time

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

principal1_post_args = reqparse.RequestParser()
principal1_post_args.add_argument("token",type=str,required=True)
principal1_post_args.add_argument("nom_conv",type=str,required=True)
principal2_post_args = reqparse.RequestParser()
principal2_post_args.add_argument("token",type=str,required=True)
principal2_post_args.add_argument("ref_conv",type=int,required=True)
principal2_post_args.add_argument("ref_user",type=str,required=True)
principal3_post_args = reqparse.RequestParser()
principal3_post_args.add_argument("token",type=str,required=True)
principal3_post_args.add_argument("ref_conv",type=int,required=True)
principal4_post_args = reqparse.RequestParser()
principal4_post_args.add_argument("token",type=str,required=True)
principal4_post_args.add_argument("ref_conv",type=int,required=True)
principal4_post_args.add_argument("message",type=str,required=True)
principal5_post_args = reqparse.RequestParser()
principal5_post_args.add_argument("token",type=str,required=True)
principal6_post_args = reqparse.RequestParser()
principal6_post_args.add_argument("token",type=str,required=True)
principal6_post_args.add_argument("ref_conv",type=int,required=True)

class principal1(Resource):
	def post(self): #Créer une conversation avec d'autres membres
		body = principal1_post_args.parse_args()
		[token,nom_conv] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que le token existe et je récupère l'adresse mail du pelo
		if True:
			mycursor.execute("SELECT count(*) FROM Token WHERE token_ = \""+token+"\"")
			if not mycursor.fetchall()[0][0]:
				return {"retour":"le token n'est pas connu de notre BDD"}
			mycursor.execute("SELECT adresse_mail FROM Token WHERE token_ = \""+token+"\"")
			adresse_mail = mycursor.fetchall()[0][0]

		#Je vérifie que le nom est conforme
		if True:
			if not len(nom_conv):
				nom_conv = "Sans nom"

		#J'ajoute une conversation
		if True:
			mycursor.execute("SELECT count(*) FROM Conversation")
			if not mycursor.fetchall()[0][0]:
				id_conv = 0
			else:
				mycursor.execute("SELECT max(id_conv) FROM Conversation")
				id_conv = mycursor.fetchall()[0][0]+1

			ajouter_Conversation(id_conv,nom_conv,mycursor,mydb)
			ajouter_Relation_conv_membre(id_conv,adresse_mail,mycursor,mydb)

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}

class principal2(Resource):
	def post(self): #Ajouter un utilisateur à une conversation
		body = principal2_post_args.parse_args()
		[token,ref_conv,ref_user] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que le token existe et je récupère l'adresse mail du pelo
		if True:
			mycursor.execute("SELECT count(*) FROM Token WHERE token_ = \""+token+"\"")
			if not mycursor.fetchall()[0][0]:
				return {"retour":"le token n'est pas connu de notre BDD"}
			mycursor.execute("SELECT adresse_mail FROM Token WHERE token_ = \""+token+"\"")
			adresse_mail = mycursor.fetchall()[0][0]

		#Je vérifie que la conversation est bien celle de mon pelo
		if True:
			mycursor.execute("SELECT count(*) FROM Relation_conv_membre WHERE id_conv = "+str(ref_conv)+" AND id_membre = \""+adresse_mail+"\"")
			if not mycursor.fetchall()[0][0]:
				return {"retour":"navre, vous ne faites pas parti de cette conversation"}

		#Je vérifie que le gars que l'on veut ajouter existe bien
		if True:
			mycursor.execute("SELECT count(*) FROM Users WHERE adresse_mail = \""+ref_user+"\"")
			if not mycursor.fetchall()[0][0]:
				return {"retour":"navre, l'utilisateur que vous voulez ajouter n'existe pas"}

		#J'ajoute le gars
		if True:
			ajouter_Relation_conv_membre(ref_conv,ref_user,mycursor,mydb)

		mycursor.close()

		return {"retour":"ok"}

class principal3(Resource):
	def post(self): #Quitter une conversation
		body = principal3_post_args.parse_args()
		[token,ref_conv] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que le token existe et je récupère l'adresse mail du pelo
		if True:
			mycursor.execute("SELECT count(*) FROM Token WHERE token_ = \""+token+"\"")
			if not mycursor.fetchall()[0][0]:
				return {"retour":"le token n'est pas connu de notre BDD"}
			mycursor.execute("SELECT adresse_mail FROM Token WHERE token_ = \""+token+"\"")
			adresse_mail = mycursor.fetchall()[0][0]

		#Je vérifie que la conversation est bien celle de mon pelo
		if True:
			mycursor.execute("SELECT count(*) FROM Relation_conv_membre WHERE id_conv = "+str(ref_conv)+" AND id_membre = \""+adresse_mail+"\"")
			if not mycursor.fetchall()[0][0]:
				return {"retour":"navre, vous ne faites pas parti de cette conversation"}

		#Je retire mon pelo
		if True:
			mycursor.execute("DELETE FROM Relation_conv_membre WHERE id_conv = "+str(ref_conv)+" AND id_membre = \""+adresse_mail+"\"")
			mydb.commit()

		#Si la conversation ne compte plus de membres, je la supprime de la BDD
		if True:
			mycursor.execute("SELECT count(*) FROM Relation_conv_membre WHERE id_conv = "+str(ref_conv))
			if not mycursor.fetchall()[0][0]:
				mycursor.execute("DELETE FROM Conversation WHERE id_conv = "+str(ref_conv))
				mycursor.execute("DELETE FROM Messages WHERE id_conversation = "+str(ref_conv))
				mydb.commit()

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}

class principal4(Resource):
	def post(self): #Envoyer un message
		body = principal4_post_args.parse_args()
		[token,ref_conv,message] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que le token existe et je récupère l'adresse mail du pelo
		if True:
			mycursor.execute("SELECT count(*) FROM Token WHERE token_ = \""+token+"\"")
			if not mycursor.fetchall()[0][0]:
				return {"retour":"le token n'est pas connu de notre BDD"}
			mycursor.execute("SELECT adresse_mail FROM Token WHERE token_ = \""+token+"\"")
			adresse_mail = mycursor.fetchall()[0][0]

		#Je vérifie que la conversation est bien celle de mon pelo
		if True:
			mycursor.execute("SELECT count(*) FROM Relation_conv_membre WHERE id_conv = "+str(ref_conv)+" AND id_membre = \""+adresse_mail+"\"")
			if not mycursor.fetchall()[0][0]:
				return {"retour":"navre, vous ne faites pas parti de cette conversation"}

		#J'ajoute mon message
		if True:
			ajouter_Messages(ref_conv,adresse_mail,message,int(time()),mycursor,mydb)

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}

class principal5(Resource):
	def post(self): #Récupérer la liste des conversations
		body = principal5_post_args.parse_args()
		[token] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que le token existe et je récupère l'adresse mail du pelo
		if True:
			mycursor.execute("SELECT count(*) FROM Token WHERE token_ = \""+token+"\"")
			if not mycursor.fetchall()[0][0]:
				return {"retour":"le token n'est pas connu de notre BDD"}
			mycursor.execute("SELECT adresse_mail FROM Token WHERE token_ = \""+token+"\"")
			adresse_mail = mycursor.fetchall()[0][0]

		#Je récupère la liste des conversations de mon pelo
		if True:
			mycursor.execute("SELECT id_conv FROM Relation_conv_membre WHERE id_membre = \""+adresse_mail+"\"")
			id_convs = [i[0] for i in mycursor.fetchall()]
			stock = []
			for i in id_convs:
				mycursor.execute("SELECT nom,id_conv FROM Conversation WHERE id_conv = "+str(i))
				resultat = mycursor.fetchall()[0]
				stock += [{"nom":resultat[0],"id_conv":resultat[1]}]

		mycursor.close()
		mydb.close()

		return {"retour":"ok","valeurs":stock}

class principal6(Resource):
	def post(self): #Récupérer les 100 derniers messages d'une conv
		body = principal6_post_args.parse_args()
		[token,ref_conv] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que le token existe et je récupère l'adresse mail du pelo
		if True:
			mycursor.execute("SELECT count(*) FROM Token WHERE token_ = \""+token+"\"")
			if not mycursor.fetchall()[0][0]:
				return {"retour":"le token n'est pas connu de notre BDD"}
			mycursor.execute("SELECT adresse_mail FROM Token WHERE token_ = \""+token+"\"")
			adresse_mail = mycursor.fetchall()[0][0]

		#Je vérifie que la conversation est bien celle de mon pelo
		if True:
			mycursor.execute("SELECT count(*) FROM Relation_conv_membre WHERE id_conv = "+str(ref_conv)+" AND id_membre = \""+adresse_mail+"\"")
			if not mycursor.fetchall()[0][0]:
				return {"retour":"navre, vous ne faites pas parti de cette conversation"}

		#Je récupère les messages de la conversation
		if True:
			mycursor.execute("SELECT ref_envoyeur,message FROM Messages WHERE id_conversation = "+str(ref_conv)+" ORDER BY date DESC LIMIT 100")
			resultat = []
			for i in mycursor.fetchall():
				[ref_envoyeur,message] = i
				mycursor.execute("SELECT nom FROM Users WHERE adresse_mail = \""+adresse_mail+"\"")
				nom = mycursor.fetchall()[0][0]
				resultat += [{"nom":nom,"message":message}]
			resultat.reverse()

		mycursor.close()
		mydb.close()

		return {"retour":"ok","valeurs":resultat}

















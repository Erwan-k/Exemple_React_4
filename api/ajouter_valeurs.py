def ajouter_Users(adresse_mail,nom,mdp,mycursor,mydb):
	val = (adresse_mail,nom,mdp)
	try:
		mycursor.execute("INSERT INTO Users (adresse_mail,nom,mdp) VALUES ("+",".join(["%s"]*len(val))+")", val)
	except Exception as e:
		return {"statut":False,"erreur":"pas reussi a insert into"}
	try:
		mydb.commit()
	except:
		return {"statut":False,"erreur":"pas reussi a commit"}
	return {"statut":True}

def ajouter_Token(adresse_mail,token_,mycursor,mydb):
	val = (adresse_mail,token_)
	try:
		mycursor.execute("INSERT INTO Token (adresse_mail,token_) VALUES ("+",".join(["%s"]*len(val))+")", val)
	except Exception as e:
		return {"statut":False,"erreur":"pas reussi a insert into"}
	try:
		mydb.commit()
	except:
		return {"statut":False,"erreur":"pas reussi a commit"}
	return {"statut":True}

def ajouter_Adresse_mail_non_verif(adresse_mail,code,mycursor,mydb):
	val = (adresse_mail,code)
	try:
		mycursor.execute("INSERT INTO Adresse_mail_non_verif (adresse_mail,code) VALUES ("+",".join(["%s"]*len(val))+")", val)
	except Exception as e:
		return {"statut":False,"erreur":"pas reussi a insert into"}
	try:
		mydb.commit()
	except:
		return {"statut":False,"erreur":"pas reussi a commit"}
	return {"statut":True}

def ajouter_Changer_de_mdp_code(adresse_mail,code,mycursor,mydb):
	val = (adresse_mail,code)
	try:
		mycursor.execute("INSERT INTO Changer_de_mdp_code (adresse_mail,code) VALUES ("+",".join(["%s"]*len(val))+")", val)
	except Exception as e:
		return {"statut":False,"erreur":"pas reussi a insert into"}
	try:
		mydb.commit()
	except:
		return {"statut":False,"erreur":"pas reussi a commit"}
	return {"statut":True}

def ajouter_Conversation(id_conv,nom,mycursor,mydb):
	val = (id_conv,nom)
	try:
		mycursor.execute("INSERT INTO Conversation (id_conv,nom) VALUES ("+",".join(["%s"]*len(val))+")", val)
	except Exception as e:
		return {"statut":False,"erreur":"pas reussi a insert into"}
	try:
		mydb.commit()
	except:
		return {"statut":False,"erreur":"pas reussi a commit"}
	return {"statut":True}

def ajouter_Messages(id_conversation,ref_envoyeur,message,date,mycursor,mydb):
	val = (id_conversation,ref_envoyeur,message,date)
	try:
		mycursor.execute("INSERT INTO Messages (id_conversation,ref_envoyeur,message,date) VALUES ("+",".join(["%s"]*len(val))+")", val)
	except Exception as e:
		return {"statut":False,"erreur":"pas reussi a insert into"}
	try:
		mydb.commit()
	except:
		return {"statut":False,"erreur":"pas reussi a commit"}
	return {"statut":True}

def ajouter_Relation_conv_membre(id_conv,id_membre,mycursor,mydb):
	val = (id_conv,id_membre)
	try:
		mycursor.execute("INSERT INTO Relation_conv_membre (id_conv,id_membre) VALUES ("+",".join(["%s"]*len(val))+")", val)
	except Exception as e:
		return {"statut":False,"erreur":"pas reussi a insert into"}
	try:
		mydb.commit()
	except:
		return {"statut":False,"erreur":"pas reussi a commit"}
	return {"statut":True}


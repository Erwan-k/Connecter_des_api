def ajouter_nom_de_la_table_2(attribut1,attribut2,mycursor,mydb):
	val = (attribut1,attribut2)
	try:
		mycursor.execute("INSERT INTO nom_de_la_table_2 (attribut1,attribut2) VALUES ("+",".join(["%s"]*len(val))+")", val)
	except Exception as e:
		return {"statut":False,"erreur":"pas reussi a insert into"}
	try:
		mydb.commit()
	except:
		return {"statut":False,"erreur":"pas reussi a commit"}
	return {"statut":True}

def ajouter_nom_de_la_table_2(attribut1,attribut2,mycursor,mydb):
	val = (attribut1,attribut2)
	try:
		mycursor.execute("INSERT INTO nom_de_la_table_2 (attribut1,attribut2) VALUES ("+",".join(["%s"]*len(val))+")", val)
	except Exception as e:
		return {"statut":False,"erreur":"pas reussi a insert into"}
	try:
		mydb.commit()
	except:
		return {"statut":False,"erreur":"pas reussi a commit"}
	return {"statut":True}


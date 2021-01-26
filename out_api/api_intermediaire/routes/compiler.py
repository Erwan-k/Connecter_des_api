from flask_restful import Api, Resource, reqparse
import os
from sqlalchemy.engine.url import make_url
import mysql.connector
import requests


compiler2_post_args = reqparse.RequestParser()
compiler2_post_args.add_argument("token",type=str,required=True)

class compiler2(Resource):
	def post(self): #compiler
		body = compiler2_post_args.parse_args()
		[token] = [body[i] for i in body]


		fichier = open("sortie.tex","rb")
		data = fichier.read()
		fichier.close()

		x = requests.post("http://127.0.0.1:8624/compiler1",data={"fichier":b"1"})


		return {"retour":x}



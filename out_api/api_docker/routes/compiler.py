from flask_restful import Api, Resource, reqparse
import os
from sqlalchemy.engine.url import make_url
import mysql.connector

compiler1_post_args = reqparse.RequestParser()
compiler1_post_args.add_argument("fichier",type=bytes,required=False)

class compiler1(Resource):
	def post(self): #compiler
		body = compiler1_post_args.parse_args()
		return body
		[fichier] = [body[i] for i in body]

		try:
			fichier = open("a_compiler.tex",'wb')
			fichier.write(fichier)
			fichier.close()

			os.system("pdflatex a_compiler.tex")

			fichier = open("a_compiler.pdf",'rb')
			data = fichier.read()
			fichier.close()

			return {"retour":"ok","data":data}

			
		except:
			return {"retour":"pas ok"}



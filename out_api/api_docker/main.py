from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

from routes.compiler import compiler1

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(compiler1,"/compiler1") #&2

if __name__ == "__main__":
	app.run(debug=True,port=5000,host='0.0.0.0')
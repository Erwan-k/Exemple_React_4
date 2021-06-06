from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

from routes.connexion import connexion1,connexion2,connexion3,connexion4,connexion5,connexion6,connexion7

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(connexion1,"/connexion1") 
api.add_resource(connexion2,"/connexion2") 
api.add_resource(connexion3,"/connexion3") 
api.add_resource(connexion4,"/connexion4") 
api.add_resource(connexion5,"/connexion5") 
api.add_resource(connexion6,"/connexion6") 
api.add_resource(connexion7,"/connexion7") 

if __name__ == "__main__":
	app.run(debug=True,port=5000,host='0.0.0.0')
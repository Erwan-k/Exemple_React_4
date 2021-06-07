from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

from routes.connexion import connexion1,connexion2,connexion3,connexion4,connexion5,connexion6,connexion7
from routes.principal import principal1,principal2,principal3,principal4,principal5,principal6

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
api.add_resource(principal1,"/principal1") 
api.add_resource(principal2,"/principal2") 
api.add_resource(principal3,"/principal3") 
api.add_resource(principal4,"/principal4") 
api.add_resource(principal5,"/principal5") 
api.add_resource(principal6,"/principal6") 

if __name__ == "__main__":
	app.run(debug=True,port=5000,host='0.0.0.0')
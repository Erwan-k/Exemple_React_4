import requests
url = "http://127.0.0.1:1234/"

def testeur(route,arguments,type_):
	global url
	if type_ == "get":
		response = requests.get(url+route,arguments)
	if type_ == "put":
		response = requests.put(url+route,arguments)
	if type_ == "post":
		response = requests.post(url+route,arguments)
	if type_ == "delete":
		response = requests.delete(url+route,arguments)
	return response.json()


##############################   connexion   ##############################

s = testeur("connexion1",{"user":"string","mdp":"string"},"post")
print(s)

s = testeur("connexion2",{"rien":"string"},"post")
print(s)

s = testeur("connexion3",{"token":"string"},"post")
print(s)

s = testeur("connexion4",{"token":"string"},"post")
print(s)


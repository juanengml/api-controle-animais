from requests import get,post,put,delete
import requests 

endpoint = "https://StormyShoddyWorkplace.juanengml.repl.co/"

status = get(endpoint).json()

print(status)

endpoint_crud = "https://StormyShoddyWorkplace.juanengml.repl.co/api/v1/crud/"

data = {'nome':"lora",
		    'dt_nascimento':"05/02/2019",
		    'especie':"gato",
		    'insta':"@lora"
}
r = post(endpoint_crud,data).json()
print("POST: ",r)

data = {"nome":"lora"}
r = get(endpoint_crud,data).json()
print("GET: ",r)


data = {"nome":"lora","dt_nascimento":"02/02/2019"}
r = put(endpoint_crud,data).json()
print("PUT: ",r)

#data = {"nome":"lora"}
#r = requests.delete(url=endpoint_crud,data={"nome":"lora"}).json()
#print("DELETE: ",r)

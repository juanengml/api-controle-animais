from requests import get,post,put,delete
import requests 

endpoint = "http://firmadataflavor.ddns.net:8080/"

status = get(endpoint).json()

print(status)

endpoint_crud = "{}api/v1/crud/".format(endpoint)
data = [{'nome':"lora",
		    'dt_nascimento':"05/02/2019",
		    'especie':"gato",
		    'insta':"@lora"
},
{'nome':"ada",
		    'dt_nascimento':"01/11/2019",
		    'especie':"gato",
		    'insta':"@lora"
},
{'nome':"sam",
		    'dt_nascimento':"01/11/2019",
		    'especie':"gato",
		    'insta':"@lora"
},
{'nome':"uly",
		    'dt_nascimento':"01/11/2019",
		    'especie':"gato",
		    'insta':"@lora"
}
]
for value in data:
  r = post(endpoint_crud,value).json() 
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

from flask import Flask
from flask_restful import Resource, Api, reqparse
from datetime import datetime as dt 
import dataset 
import os 


app = Flask(__name__)
api = Api(app)

#---------- connectando db --------------- #  

url_db = os.getenv("DATABASE_URL")

db = dataset.connect(url_db)
table = db['tbl_pets_animais']

#--------------------CRUD ------------------#
class CRUD(Resource):
   def post(self):
		    #
		    # AQUI CODIGO PARA CADASTRAR DADOS
		    parser = reqparse.RequestParser()
		    parser.add_argument('nome')
		    parser.add_argument('dt_nascimento')
		    parser.add_argument('especie')
		    parser.add_argument('insta')
		    dados = parser.parse_args()
		    ID = table.insert(dados)
		    return {"status":"CREATE","dados":dados,"dt":str(dt.now())}  
		
   def get(self):
		    # busca os dados 
		    parser = reqparse.RequestParser()
		    parser.add_argument('nome')
		    dados = parser.parse_args()
		    user = table.find_one(nome=dados['nome'])
		    return {"status":"READ","dados":dict(user)}
		    
   def put(self):
		    # codigo para atualizar registros
		    parser = reqparse.RequestParser()
		    parser.add_argument('nome')
		    parser.add_argument('dt_nascimento')
		    dados = parser.parse_args()
		    user = dict(table.find_one(nome=dados['nome']))
		    data = dict(id=user['id'], nome=user['nome'], dt_nascimento=user['dt_nascimento'])
		    r = table.update(data, ['id'])
		    return {"status":"UPDATE",'result':r,"dados":user}    
		
   def delete(self):
        # codigo para deletar registros
        parser = reqparse.RequestParser()
        parser.add_argument('nome')
        dados = parser.parse_args() 
        print(dados['nome'])
        r = table.delete(nome=dados['nome'])
        return {"status":"DELETE","result":r, "dados":dados}    

#------------status check------------------#
class status(Resource):
   def get(self):
        return {"status":str(dt.now())} 

api.add_resource(CRUD, '/api/v1/crud/')
api.add_resource(status, '/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
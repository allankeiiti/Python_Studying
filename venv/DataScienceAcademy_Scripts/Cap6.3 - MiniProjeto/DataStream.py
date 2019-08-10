from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
from datetime import datetime
from pymongo import MongoClient
import json as j
import pandas as pd

# Chaves de autenticação do Twitter
consumer_key = "vTtCva0Bjh8kX33w90FJhr4JH"
consumer_secret = "LWadLqJLPZ6BvxYwTPE0yZQqNshxeODWvDRvgwprv1BVKIIdNW"

access_token = "1157083378165919744-m8FgZsZ1UOLBAyY27cMP8Ns9QUJ3nN"
access_token_secret = "ZyQ94fIgblptARVYTjAtPrczCGFFVxrTX2QWsPXMbDxZ3"

# Criando chaves de autenticação
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Criando uma classe para capturar os streams de dados do Twitter e armazenar no MongoDB
class MyListener(StreamListener):
  def on_data(self, dados):
    tweet = j.loads(dados)
    created_at = tweet["created_at"]
    id_str = tweet["id_str"]
    text = tweet["text"]
    obj = {"created_at": created_at, "id_str": id_str, "text": text,}
    tweetind = col.insert_one(obj).inserted_id
    print(obj)
    return True

# Criando o objeto MyListener
mylistener = MyListener()
myStream = Stream(auth, listener= mylistener)

# Preparando conexão com o MongoDB
client = MongoClient('localhost', 27017)
db = client.twitterdb
col = db.tweets

palavras_chave = ['Capcom', 'StreetFighter', 'Megaman', 'Rockman']

# Realizando a coleta dos Posts do Twitter, filtrando com base nas palavras_chave
myStream.filter(track=palavras_chave)

# Desconectando o Stream
myStream.disconnect()

# Verificando o documento no collection no DB twitterdb do MongoDB
print(col.find_one())

'''
#     Análise de Dados com Pandas e Scikit-Learn
#     Criar Dataset - importar Pandas - Criar Dataframe
'''

dataSet = [{'created_at': item['created_at'], 'text': item['text'],} for item in col.find()]
dataFrame = pd.DataFrame(dataSet)
print(dataFrame)



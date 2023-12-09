# Ira receber o arquivo de imagem da API JAVA @app.route("localhost/nome_endpoint/<int:array_do_usuario>")
# Irá comparar a imagem com o blob storage
# Irá retornar com o id da pessoa e passar para API JAVA  @app.route("localhost/nome_endpoint/<int:array_do_usuario>")

<<<<<<< HEAD
from azure.storage.blob import BlobClient,BlobServiceClient
=======

from azure.storage.blob import BlobClient
import requests
>>>>>>> 6b48de117b432c7b2eea3e71ebb3b25fe9c818d2
from flask import Flask, jsonify, request
import conexao

#Fazendo conexão com o blob diretamente

blob = conexao

#listagem de blobs no container, necessário para fazer comparação

def listar_blobs(self, blob_service_client: BlobServiceClient, container_name):
    container_client = blob_service_client.get_container_client(container=container_name)

    blob_list = container_client.list_blobs()

    for blob in blob_list:
        print(f"Nome: {blob.name}")

<<<<<<< HEAD


def get_clients_with_connection_string():
    connection_string, container_name = get_details()
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client,get_container_client(container_name)

    listar_blobs = container_client.list_blobs_names()

    for imagem in listar_blobs:
        blob_client = container_client.get_blob_client(imagem)

        imagem_baixada = blob_client.download_blob().content_as_bytes()

        print(imagem)
        
    print()
    
app = Flask(__name__)

=======
app = Flask(__name__)

#Fazendo conexão com o blob diretamente
blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=blobsecurepass1;AccountKey=LWoDmpn551J3KaMj5FVKpWZqc3EPStbewzbNLSFCbWxgu+Y1hw6SAMAcHVXbM4cHNi3Ua1SsgqGO+ASt+WZRQQ==;EndpointSuffix=core.windows.net'", 
container_name="containersecure7",
blob_name="blobsecurepass1")

def lista_blobs(self, blob_service_client: BlobServiceClient, container_name):
    container_client = blob_service_client.get_container_client(container=container_name)

    blob_list = container_client.list_blobs()

    for blob in blob_list:
        print(f"Name: {blob.name}")






>>>>>>> 6b48de117b432c7b2eea3e71ebb3b25fe9c818d2
app.run(port=8080, host='localhost', debug=True)
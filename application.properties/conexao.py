import os
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError

#determinando a conexão com o blob
def dados():
    storage_connection_string = 'DefaultEndpointsProtocol=https;AccountName=blobsecurepass1;AccountKey=LWoDmpn551J3KaMj5FVKpWZqc3EPStbewzbNLSFCbWxgu+Y1hw6SAMAcHVXbM4cHNi3Ua1SsgqGO+ASt+WZRQQ==;EndpointSuffix=core.windows.net'    
    blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
    container_id = 'containersecure7'
print (dados)

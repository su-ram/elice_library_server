import os
from azure.storage.blob import BlobServiceClient

def upload_image(filename):
    try:

        blob_service_client = BlobServiceClient.from_connection_string(os.environ["AZURE_STORAGE_CONNECTION_STRING"])
        filepath = os.path.abspath(os.path.curdir)
        filepath = os.path.join(filepath,'elice_library','images',filename)
        file = open(filepath,"rb")
        container_client = blob_service_client.get_container_client("user")
        blob_client = container_client.get_blob_client(filename)

        with file as data:
            blob_client.upload_blob(data, blob_type="BlockBlob")

        os.remove(filepath)

    except Exception as ex:
        print('Exception:')
        print(ex)

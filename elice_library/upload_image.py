import os
from azure.storage.blob import *

class ProfileImage():

    blob_service_client = BlobServiceClient.from_connection_string(os.environ["AZURE_STORAGE_CONNECTION_STRING"])
    container_client = blob_service_client.get_container_client("user")

    def upload_image(self,filename):
        try:

            filepath = os.path.abspath(os.path.curdir)
            filepath = os.path.join(filepath,'elice_library','images',filename)
            file = open(filepath,"rb")
            blob_client = self.container_client.get_blob_client(filename)

            with file as data:
                blob_client.upload_blob(data, blob_type="BlockBlob")

            os.remove(filepath)

        except Exception as ex:
            print('Exception:')
            print(ex)

        return blob_client.url



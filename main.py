from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import random
from datetime import datetime

# Azure Blob Storage connection string
connection_string = "DefaultEndpointsProtocol=https;AccountName=wavely;AccountKey=/54X85Sm4bZpidx+6KqthsZkm7epqRQnsNdAbRNOSZRHieHSj+kvm/a4PkAHp3TzujmwqPmh8q+R+AStURU/pg==;EndpointSuffix=core.windows.net"

# Name of the container
container_name = "wavely-container"

# Name of blob in the container
blob_name = "wavely"

# Local file path of the file
local_file_path = "sample.wav"

# Function to download a blob from Azure Blob Storage
def download_blob_from_storage():
    try:
        blob_service_client = BlobServiceClient.from_connection_string(conn_str=connection_string)
        container_client = blob_service_client.get_container_client(container_name)
        blob_client = container_client.get_blob_client(blob_name)

        # Download the blob to a local file
        with open("downloaded_sample.wav", "wb") as my_blob:
            download_stream = blob_client.download_blob()
            my_blob.write(download_stream.readall())

        print("Blob downloaded successfully.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Function to detect mood based on the time of the day
def detect_mood():
    current_time = datetime.now().time()
    if current_time < datetime.strptime("12:00:00", "%H:%M:%S").time():
        return "Happy"
    elif current_time < datetime.strptime("18:00:00", "%H:%M:%S").time():
        return "Calm"
    else:
        return "Sad"

def upload_file_to_blob():
    try:
        blob_service_client = BlobServiceClient.from_connection_string(conn_str=connection_string)
        container_client = blob_service_client.get_container_client(container_name)

        # Create a blob client to upload the file
        blob_client = container_client.get_blob_client(blob_name)

        with open(local_file_path, "rb") as data:
            blob_client.upload_blob(data)

        print(f"File '{local_file_path}' uploaded to Azure Blob Storage successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Function to detect mood based on the time of the day
def detect_mood():
    current_time = datetime.now().time()

    if current_time < datetime.strptime("12:00:00", "%H:%M:%S").time():
        return "Happy"
    elif current_time < datetime.strptime("18:00:00", "%H:%M:%S").time():
        return "Calm"
    else:
        return "Sad"

if __name__ == "__main__":
    # Upload audio file to Azure DB
    upload_file_to_blob()

    # Download audio file from Azure and detect mood
    download_blob_from_storage()
    mood = detect_mood()
    print(f"Mood: {mood}")


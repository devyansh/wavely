# Wavely Assesment

### Architecture
Here we are using Microsoft Azure Services as the cloud provider. The code is developed in python and uses Azure Python SDK. 

### Installation 
Install Azure Python SDK 
```
pip install azure-storage-blob
```

Login into your azure account by running 

```
az login
```

### Instructions
Find the connection string of the storage account and replace in main.py


Run main.py

## Things to note
For production environment create proper methods with name input parameters to resuse the methods. 

The mood detection algorithm can also run on the cloud instead of running locally. Create APIs to call the python methods and fetch mood. 

Code improvements for cases when a file with selected name already exists. Delete uploaded 'sample.wav' in azure blob before running scrip again. Delete 'downloaded_sample.wav' and then run the script.



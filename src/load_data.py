from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFDirectoryLoader




BDC_PATH = "bdc"



def load_documents():
    
    documents = []

    loader = PyPDFDirectoryLoader("bdc/")  # Charge tous les PDF d'un dossier
    documents = loader.load()

    return documents









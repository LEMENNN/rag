from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFDirectoryLoader




BDC_PATH = "bdc"



def load_documents():
    
    documents = []

    loader = PyPDFDirectoryLoader("bdc/")  # Charge tous les PDF d'un dossier
    documents = loader.load()


    # for file in os.listdir(BDC_PATH):
    #      if file.endswith(".pdf"):
    #          loader = PyPDFLoader(file)
    #          documents.extend(loader.load())
    # print(f"✅ {len(documents)} documents chargé")

    return documents






# texts = load_document()

# chunks = split_text([doc.page_content for doc in texts], chunk_size=200, chunk_overlap=20)


# # Afficher les résultats
# for i, chunk in enumerate(chunks[:5]):  # Afficher les 5 premiers chunks
#     print(f"Chunk {i+1}:\n{chunk}\n{'-'*50}")

# print(f"Total chunks générés : {len(chunks)}")



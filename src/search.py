import chromadb
from sentence_transformers import SentenceTransformer


embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

chroma_client = chromadb.PersistentClient(path="db")
collection = chroma_client.get_or_create_collection(name="rag_bdc")

def lexical_search():
    return None


def search(query, top_k=3):
    """Recherche les chunks les plus pertinents à partir d'une requête."""
    
    # recherche lexicale 

    # recherche sémantique
    query_embedding = embedding_model.encode([query]).tolist()  # Convertir la requête en vecteur
    semantic_results = collection.query(query_embeddings=query_embedding, n_results=top_k)
    
    # Afficher les résultats
    for i, (doc, score) in enumerate(zip(semantic_results["documents"][0], semantic_results["distances"][0])):
        print(f"🔎 Résultat {i+1}: (Score: {score:.4f})\n{doc}\n{'-'*50}")


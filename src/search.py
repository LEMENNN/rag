import chromadb
from sentence_transformers import SentenceTransformer


embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

chroma_client = chromadb.PersistentClient(path="db")
collection = chroma_client.get_or_create_collection(name="rag_bdc")


def search(query, top_k=3):
    """Recherche les chunks les plus pertinents à partir d'une requête."""
    
    query_embedding = embedding_model.encode([query]).tolist()  # Convertir la requête en vecteur
    results = collection.query(query_embeddings=query_embedding, n_results=top_k)
    
    # Afficher les résultats
    for i, (doc, score) in enumerate(zip(results["documents"][0], results["distances"][0])):
        print(f"🔎 Résultat {i+1}: (Score: {score:.4f})\n{doc}\n{'-'*50}")

# Exemple de requête
search("Quels sont les documents liés à la facturation ?")
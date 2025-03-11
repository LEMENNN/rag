from src.load_data import load_documents
from src.chunking import split_text
from src.index_data import index_chunks
from src.search import search



texts = load_documents()

chunks = split_text([doc.page_content for doc in texts], chunk_size=800, chunk_overlap=80)


index_chunks(chunks)

search("C'est quoi Micropole ?")
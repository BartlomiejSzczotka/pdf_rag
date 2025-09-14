from langchain_community.embeddings.ollama import OllamaEmbeddings

EMBEDDING_MODEL_NAME = "embeddinggemma:300m"
# EMBEDDING_MODEL_NAME = "mxbai-embed-large:latest"
# EMBEDDING_MODEL_NAME = "nomic-embed-text:latest"


def get_embedding_function():
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL_NAME)
    return embeddings

from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings

# Planner model
planner_llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0.2
)

# Coding model
coder_llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0.1
)

# Debug model
debug_llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0
)

# Research model
research_llm = ChatOllama(
    model="mistral:latest",
    temperature=0.3
)

# Vision model
vision_llm = ChatOllama(
    model="qwen3-vl:4b",
    temperature=0.2
)

# Embeddings
embedding_model = OllamaEmbeddings(
    model="nomic-embed-text"
)
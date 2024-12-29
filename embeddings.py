from typing import Sequence
import ollama

def getEmbedding(sentence: str) -> Sequence[float]:
    embedResponse = ollama.embed(
        model='all-minilm',
        input=sentence
    )
    
    return embedResponse.embeddings[0]

def getEmbeddings(sentences: Sequence[str]) -> Sequence[Sequence[float]]:
    embedResponse = ollama.embed(
        model='all-minilm',
        input=sentences
    )

    return embedResponse.embeddings
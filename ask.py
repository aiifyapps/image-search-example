#!/usr/bin/env python

import ollama
from pymilvus import Hit
import db
import embeddings
from langchain_community.document_loaders import PyPDFLoader

# Database connect
db.connect()

# select collection
knowledge = db.Collection("images")
knowledge.load()


def search(term: str) -> None:
    embedding = embeddings.getEmbedding(term)

    search_params = {"metric_type": "COSINE", "params": {"nprobe": 10}}

    searchResults = knowledge.search(
        data=[embedding],
        anns_field="embedding",
        param=search_params,
        limit=3,
        output_fields=['representation']  
    )

    context = ""
    for hits in searchResults:
        for hit in hits:    
            context += "\r\n" + hit.entity.get('representation') + "\r\n"            
    print(context)

print("Please, enter the search query and hit Enter key. \r\n")
print("To exit the app type 'quit' and hit Enter key. \r\n")

while True:
    term = input('Your search query: ')

    if 'quit' == term:
        print("\r\nThank you for using this example app.\r\n")
        break

    search(term)

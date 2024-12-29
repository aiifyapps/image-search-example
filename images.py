#!/usr/bin/env python

from email.mime import image
import db
import embeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import captioning

# Database connect
db.connect()

# Create and select collection
db.createCollection("images")
knowledge = db.Collection("images")


images = []
images.append('https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg')
images.append('https://bagelsyourwaycafe.com/wp-content/uploads/2021/05/Fresh-Squeezed-Lemonade.png')
images.append('https://www.cdc.gov/healthy-pets/media/images/2024/04/Cat-on-couch.jpg')
images.append('https://www.animalfriends.co.uk/siteassets/media/images/article-images/cat-articles/51_afi_article1_the-secret-language-of-cats.png')

imageEmbeddings = []

for image in images:
    imageEmbeddings.append({
        "representation": image,
        "embedding": embeddings.getEmbedding(captioning.getCaption(image))
    })


print("Inserting into database")
db.insertEmbeddings(knowledge, imageEmbeddings)

print("Loading the collection")
knowledge.load()


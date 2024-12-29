## Semantic image search example

In this example, you will find a very simple app that allows you to search through your images by typing a keyword.

### Running the example
- Ensure you have Python 3 and pip installed on your machine.

- Install Ollama and ensure the `all-minilm` model is available on your machine:
```bash
# Pulling the model
ollama pull all-minilm
```

- Navigate to the project folder.

- Use the provided Docker Compose file (with Milvus standalone and Attu) located in the project root:

```bash
# Running the docker
docker compose up -d
```

- Create a Python virtual environment:

```bash
# Create virtual environment (-m is for python module)
mkdir -p .venv
python -m venv .venv
```

- Activate the Python virtual environment:

```bash
# Activate virtual environment
source .venv/bin/activate
```

- Install Python dependencies:

```bash
# Install dependecies from requirements.txt
pip install -r requirements.txt
```

- Create a .env file in the project root
```bash
# You have an example of env file name .env.dist you can start from it
cp .env.dist .env
```

### Running the scripts

1. Run the images.py script

This script captions the images, creates embeddings, and inserts the embeddings into the database:

```bash
# Running the script
./images.py
```

2. Run the ask.py script

This script performs a search against the database:
```bash
# Running the script
./ask.py
```

###### HAPPY CODING!
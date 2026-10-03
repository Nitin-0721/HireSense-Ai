import fitz  # PyMuPDF
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load the model only when it is actually needed
model = None


def get_model():
    global model

    if model is None:
        model = SentenceTransformer("all-MiniLM-L6-v2")

    return model


# This is for only one resume at a time
index = None
documents = []
resume_text = ""


def extract_text(pdf_path):
    text = ""

    doc = fitz.open(pdf_path)

    for page in doc:
        text += page.get_text()

    doc.close()

    return text


def chunk_text(text, chunk_size=500):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


def create_vector_store(text):

    global index
    global documents
    global resume_text

    resume_text = text

    documents = chunk_text(text)

    # Load model only when resume is uploaded
    embedding_model = get_model()

    embeddings = embedding_model.encode(documents)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(
        np.array(embeddings).astype("float32")
    )


def retrieve(query, k=3):

    global index

    if index is None:
        return ""

    # Load model only when chat/search is actually used
    embedding_model = get_model()

    query_embedding = embedding_model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        k
    )

    result = []

    for idx in indices[0]:

        if idx < len(documents):
            result.append(documents[idx])

    return "\n".join(result)
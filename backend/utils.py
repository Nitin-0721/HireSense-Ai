import fitz
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

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

    embeddings = model.encode(documents)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings).astype("float32"))


def retrieve(query, k=3):

    global index

    if index is None:
        return ""

    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        k
    )

    result = []

    for idx in indices[0]:
        if idx < len(documents):
            result.append(documents[idx])

    return "\n".join(result)
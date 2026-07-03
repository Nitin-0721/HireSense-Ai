import fitz #reads pdf it is PyMuPDF
import faiss
import numpy as np #to pass vector to faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

#this is for only one resume
index = None
documents = []
resume_text = ""

#everything here is a function becoz every files need them

# extracts text from pdf and returns it as string sexy function
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

#sbse jaruri function, it creates vector store from the resume text and stores it in faiss index
#this function calls only once, by upload.py
def create_vector_store(text):

    global index
    global documents
    global resume_text

    resume_text = text

    documents = chunk_text(text)
    
    
#step 4:where AI starts
    embeddings = model.encode(documents)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
#faiss stores vector in flat32
    index.add(np.array(embeddings).astype("float32"))


def retrieve(query, k=3):

    global index

    if index is None: #if user not uploads any resume and ask question, then empty string will be returned
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

#it contains the RAG engine, heart of the project
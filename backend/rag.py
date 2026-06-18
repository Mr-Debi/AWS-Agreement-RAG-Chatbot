import os

from huggingface_hub import InferenceClient

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import PyPDFLoader

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv
import os

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
# print(HF_TOKEN)

VECTOR_PATH = "vectorstore"

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

client = InferenceClient(
    # model="mistralai/Mistral-7B-Instruct-v0.3",
    token=HF_TOKEN

)


def ingest_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    vectorstore = FAISS.from_documents(
        chunks,
        embedding_model
    )

    vectorstore.save_local(VECTOR_PATH)

    return len(chunks)


def ask_question(question):

    db = FAISS.load_local(
        VECTOR_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )

    docs = db.similarity_search(
        question,
        k=3
    )

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Answer ONLY using the context.

If answer is unavailable say:
Information not found in document.

Context:
{context}

Question:
{question}
"""

    # answer = client.text_generation(
    #     prompt,
    #     max_new_tokens=200
    # )

    response = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",
    messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=200
    )

    answer = response.choices[0].message.content


    return {
        "answer": answer,
        "sources": [
            doc.page_content[:300]
            for doc in docs
        ]
    }
import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
import requests
from bs4 import BeautifulSoup

def simple_splitter(text, chunk_size=1500, overlap=200):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def extract_job_posting():
    load_dotenv()
    print(">>> Entering extract_job_posting")

    url = "https://www.naukri.com/ai-ml-jobs?k=ai%20ml%20jobs"
    print(">>> Fetching page")
    resp = requests.get(url, headers={"User-Agent": os.getenv("USER_AGENT")})
    soup = BeautifulSoup(resp.text, "html.parser")
    text = soup.get_text()

    chunks = simple_splitter(text)
    print(">>> Split into", len(chunks), "chunks")

    llm = ChatOllama(model="mistral", temperature=0, num_predict=500)

    summaries = []
    for i, chunk in enumerate(chunks[:5]):  # limit to 5 chunks
        print(f"\n--- Summarizing chunk {i+1} ---\n")
        completion = llm.invoke(f"Summarize job posting:\n{chunk}")
        print(completion.content)
        summaries.append(completion.content)

    final = llm.invoke("\n".join(summaries))
    print("\n=== Final Summary ===\n")
    print(final.content)

if __name__ == "__main__":
    extract_job_posting()

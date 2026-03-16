import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_community.document_loaders import PlaywrightURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def extract_job_posting():
    

    load_dotenv()
    print(">>> Entering extract_job_posting")

    user_agent = os.getenv("USER_AGENT")
    print(">>> USER_AGENT:", user_agent)

    # Step 1: Load the job posting page
    aiml_job_link = (
        "https://www.naukri.com/ai-ml-jobs?k=ai%20ml%20jobs"
    )

    print(">>> Entering Playwright loader")
   
    loader = PlaywrightURLLoader(
    urls=[aiml_job_link],
    remove_selectors=["header", "footer"],
    timeout=30000  # 30 seconds
    )

    docs = loader.load()

    print(">>> Loaded page, length:", len(docs[0].page_content))

    # Step 2: Split into smaller chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_text(docs[0].page_content)
    print(">>> Split into", len(chunks), "chunks")

    # Step 3: Initialize Ollama model (use smaller one for speed)
    llm = ChatOllama(
        model="mistral",   # make sure this model is pulled in Ollama
        temperature=0,
        num_predict=300    # restrict output length
    )

    # Step 4: Summarize each chunk
    chunk_summaries = []
    for i, chunk in enumerate(chunks[:2]):  # limit to first 2 chunks for testing
        print(f"\n--- Summarizing chunk {i+1} ---\n")
        completion = llm.invoke(f"""
        Summarize the following job posting content in a structured bullet list:
        - Job title
        - Company name
        - Location
        - Employment Type
        - Salary/compensation (if available)
        - Required qualifications/skills
        - Primary responsibilities
        - Benefits offered
        - Application instructions
        - Posting date (if available)

        Content:
        {chunk}
        """)
        print(completion.content)
        chunk_summaries.append(completion.content)

    # Step 5: Combine summaries into a final structured summary
    print(">>> Combining chunk summaries")
    final_summary = llm.invoke(f"""
    Combine the following chunk summaries into one concise, structured job posting summary:

    {"\n".join(chunk_summaries)}
    """)
    print("\n=== Final Summary ===\n")
    print(final_summary.content)

if __name__ == "__main__":
    extract_job_posting()

import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools import tool

@tool
def extract_job_posting():
    """
    Extracts structured information from a a job posting at the provided URL.

    Arg:
    aiml_job_link (str): The URL of the job posting

    Returns (str):
        str: A structured summary o fhte job posting key details
    """
    load_dotenv()
    print(">>> Entering extract_job_posting")

    print("USER_AGENT:", os.getenv("USER_AGENT"))

    # Step 1: Load the job posting page
    aiml_job_link = (
        "https://www.naukri.com/ai-ml-jobs?k=ai%20ml%20jobs"
    )
    loader = WebBaseLoader(aiml_job_link,header_template={"User-Agent": os.getenv("USER_AGENT")})
    docs = loader.load()

    # Step 2: Split into manageable chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=200)
    chunks = splitter.split_text(docs[0].page_content)

    # Step 3: Initialize Ollama model (use a smaller one for speed)
    llm = ChatOllama(
        model="mistral",   # or "llama2:7b", "qwen:3-8b" if installed
        temperature=0,
        num_predict=500    # restrict output length
    )

    # Step 4: Summarize each chunk
    chunk_summaries = []
    for i, chunk in enumerate(chunks[:5]):  # limit to first 5 chunks
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
                                
        Format
            - Respond with a clear , structured bullet-point list.
            - Use exact factual infromatin from the posting , no rewording beyond making it concise.
            - If the posting is missing, inaccessible, or contains no job details, respond with : 
            "Job posting unavailable or contains no job details."

            Do's
            - Ensure all extracted details are accurate and directly taken from the posting.
            - Kepp descriptions short, professional, and easy to scan.
            - Use consistent formatting for all fields (e.g., "Job Title: ...").
            Don'ts
            - Do not include filler language, speculation or personal opinions.
            - Do not rewrite or interpret details-only report facutaul information form the posting.

        Content:
        {chunk}
        """)
        print(completion.content)
        chunk_summaries.append(completion.content)

    # Step 5: Combine summaries into a final structured summary
    final_summary = llm.invoke(f"""
    Combine the following chunk summaries into one concise, structured job posting summary:

    {"\n".join(chunk_summaries)}
    """)

    print("\n=== Final Summary ===\n")
    print(final_summary.content)

if __name__ == "__main__":
    extract_job_posting()

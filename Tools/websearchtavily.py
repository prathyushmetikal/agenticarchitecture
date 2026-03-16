import os
from dotenv import load_dotenv
#from langchain_openai import ChatOpenAI
# from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_tavily import TavilySearch
from langchain.tools import tool
from langchain_ollama import ChatOllama
@tool
def search_with_tavily():
    """
    Extracts structured information for a job posting from the internet

    Arg:
    query (str): The area or field based on which the tavily search has to work

    Returns (str):
        str: A structured summary of the job posting key details
    """
    # Load environment variables
    load_dotenv()
    print(">>> Entering serach with tavily")
    openai_key = os.getenv("OPENAI_API_KEY")
    tavily_key = os.getenv("TAVILY_API_KEY")

    # # Initialize LLM
    # llm = ChatOpenAI(
    #     api_key=openai_key,
    #     model="gpt-4",   # or "gpt-3.5-turbo"
    #     temperature=0
    # )

    # Initialize Ollama chat model (replace "llama2" with your installed model name)
    llm = ChatOllama(
        model='mistral',   # or "mistral", "gemma", etc.
        temperature=0
    )


    # # Initialize Tavily search tool
    # tavily_search = TavilySearchResults(
    #     max_results=5,
    #     api_key=tavily_key
    # )

    # # Run a search query
    # query = "Artificial Intelligence Architect jobs in India"
    # results = tavily_search.run(query)
    # print(f"tavily resutls {results}")

     # Initialize Tavily search
    tavily_search = TavilySearch(
        max_results=2,
        api_key=tavily_key
    )

    # Run a search query
    query = "Artificial Intelligence Architect jobs in India"
    results = tavily_search.run(query)
    print(f"Tavily results: {results}")



    # # Ask GPT to summarize the results
    # completion = llm.invoke(
    #     f"Summarize these job postings in a structured bullet list:\n{results}"
    # )

    # Ask Ollama to summarize the results
    # completion = llm.invoke(
    #     f"Summarize these job postings in a structured bullet list:\n{results}"
    # )

    #print(completion.content)

    # completion_stream = llm.stream(
    # f"Summarize these job postings in a structured bullet list:\n{results}"
    # )

    # for chunk in completion_stream:
    #     print(chunk.content, end="", flush=True)
    # Extract snippets only (avoid passing the full JSON)
    # Extract snippets from Tavily results
    snippets = [res["content"] for res in results if "content" in res]
    joined_text = "\n".join(snippets)

    # Build the instruction prompt as a triple-quoted string
    instruction = f"""
    Summarize the key details in a clear and concise format, including:
    - Job title
    - Company name
    - Location
    - Employment Type (full-time, part-time, contract, etc.)
    - Salary or compensation (if available)
    - Required qualification / skills
    - Primary responsibilities
    - Benefits offered
    - Application instructions
    - Posting date (if available)

    Format:
    - Respond with a clear, structured bullet-point list.
    - Use exact factual information from the posting, no rewording beyond making it concise.
    - If the posting is missing, inaccessible, or contains no job details, respond with:
    "Job posting unavailable or contains no job details."

    Do's:
    - Ensure all extracted details are accurate and directly taken from the posting.
    - Keep descriptions short, professional, and easy to scan.
    - Use consistent formatting for all fields.

    Don'ts:
    - Do not include filler language, speculation or personal opinions.
    - Do not rewrite or interpret details — only report factual information from the posting.

    {joined_text}
    """

    # Stream the summarization
    for chunk in llm.stream(instruction):
        print(chunk.content, end="", flush=True)


if __name__ == "__main__":
    search_with_tavily()
    print(">>> Exiting search_with_tavily")

import os
from dotenv import load_dotenv
#from langchain_openai import ChatOpenAI
# from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_tavily import TavilySearch
from langchain_ollama import ChatOllama

def search_with_tavily():
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


#  uv run .\Tools\websearchtavilyTest.py
# E:\HexawareGENAIProjects\Learning March\agenticarchitecture\.venv\Lib\site-packages\langchain_core\_api\deprecation.py:25: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
#   from pydantic.v1.fields import FieldInfo as FieldInfoV1
# >>> Entering serach with tavily
# Tavily results: {'query': 'Artificial Intelligence Architect jobs in India', 'follow_up_questions': None, 'answer': None, 'images': [], 'results': [{'url': 'https://in.linkedin.com/jobs/ai-architect-jobs', 'title': '4,000+ Ai Architect jobs in India (175 new) - LinkedIn', 'content': '4,000+ Ai Architect Jobs in India (175 new) · Chief Architect - Gen AI · Full stack Architect · Trainee Architect · Senior Principal Architect · AI Architect.', 'score': 0.9999757, 'raw_content': None}, {'url': 'https://www.glassdoor.co.in/Job/india-ai-architect-jobs-SRCH_IL.0,5_IN115_KO6,18.htm', 'title': '8,399 ai architect jobs in India, January 2026 | Glassdoor', 'content': 'Search Ai architect jobs in India with company ratings & salaries. 8399 open ... ₹4L - ₹9L (Glassdoor Est.) & AI/ML skillsShould have string communication skills', 'score': 0.9999318, 'raw_content': None}], 'response_time': 1.35, 'request_id': 'b31eda3b-23e8-4074-9cf9-9a498352e58d'}
#  Job Title: Senior Software Engineer
# Company Name: XYZ Corporation
# Location: New York, NY
# Employment Type: Full-time
# Salary or Compensation: Not specified in the job posting
# Required Qualification / Skills:
# - Bachelor's degree in Computer Science or related field
# - 5+ years of experience in software development
# - Proficiency in Java, Python, and React
# - Strong understanding of cloud computing (AWS preferred)
# - Experience with microservices architecture
# Primary Responsibilities:
# - Design, develop, and maintain high-quality software solutions
# - Collaborate with cross-functional teams to define, design, and ship new features
# - Ensure the performance, quality, and responsiveness of applications
# - Identify and correct bottlenecks and fix bugs
# Benefits Offered:
# - Health, dental, and vision insurance
# - 401(k) retirement plan with company match
# - Paid time off (PTO)
# - Flexible working hours
# Application Instructions:
# - Submit resume and cover letter to [careers@xyzcorp.com](mailto:careers@xyzcorp.com)
# - Include the job title in the subject line of your email
# Posting Date (if available): Not specified in the job posting>>> Exiting search_with_tavily
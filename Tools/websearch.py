#from langchain_openai import ChatOpenAI
import os
from openai import OpenAI
from dotenv import load_dotenv

def searchtheweb():
    load_dotenv()
    apikey=os.getenv("OPENAI_API_KEY")
    print(f"api key is {apikey}")

    #llm=ChatOpenAI(api_key=apikey)
    client=OpenAI(api_key=apikey)
    aiml_job_link="https://www.naukri.com/artificial-intelligence-artificial-intelligence-architect-machine-learning-chatbot-jobs?k=artificial%20intelligence%2C%20artificial%20intelligence%20architect%2C%20machine%20learning%2C%20chatbot&nignbevent_src=jobsearchDeskGNB"

    completion=client.chat.completions.create(
        model="gpt-4o-search-preview",
        web_search_options={
            "search_context_size":"medium",
        },
        messages=[{
            "role":"system",
            "content":"""
            You are a helpful tool that visits the following job posting and carefully read its contents.
            Summarize the key details in a cleare and concise format, including: 
            Vist the provided job posting link , read it rhoroughly, and extract and summarize all key information . Include: 
            -Job title
            - Company name
            - Location
            - Employment Type ( full-time , part-time , contract , etc.)
            - Slary or compensation (if available)
            - Required qualification / skills
            - Primary responsibilities
            - Benefits offered
            - Application instructions
            - Posting data ( if available)

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

            """,
        },{
            "role":"user",
            "content":f"Visit the job posting and exgtract the details: \n {aiml_job_link}"
        }
        ],
    )

    print(completion.choices[0].message.content)



if __name__ == "__main__":
    searchtheweb()
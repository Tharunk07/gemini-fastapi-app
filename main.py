from fastapi import FastAPI
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from fastapi.responses import JSONResponse
import os
load_dotenv()
app = FastAPI(swagger_ui_parameters={"syntaxHighlight": {"theme": "obsidian"}})



@app.post("/chat")
async def llm_chat(user_query):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        google_api_key = os.getenv("GEMINI_API_KEY")
        # other params...
    )

    prompt = ChatPromptTemplate.from_messages([("user","{question}")])

    chain = prompt | llm
    response = chain.invoke({"question":user_query})
    print("Response>>",response.content)
    return JSONResponse({"type":"text","content":response.content})

@app.get("/")
async def home_page():
    return JSONResponse("Welcome to the LLM API, New commit")
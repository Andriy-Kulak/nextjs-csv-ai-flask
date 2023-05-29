from flask import Flask
import os
from dotenv import load_dotenv

from langchain.llms import OpenAI

from langchain.agents import create_csv_agent

load_dotenv()

app = Flask(__name__)

csvPath = "https://nextjs-csv-ai-flask.vercel.app/weeklyGoals.csv"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/test")
def hello_test():
    print("OPENAI_API_KEY", OPENAI_API_KEY)
    agent = create_csv_agent(
        OpenAI(openai_api_key=OPENAI_API_KEY), "titanic.csv", verbose=True
    )
    test = agent.run("how many rows are there?")
    return "<p>{test}</p>"
    # return "<p>Hello, World 222!</p>"

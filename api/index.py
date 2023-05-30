from flask import Flask
import os
from dotenv import load_dotenv

from langchain.llms import OpenAI

from langchain.agents import create_csv_agent

load_dotenv()

app = Flask(__name__)

csvPath = "./files/weeklyGoals.csv"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/test")
def hello_test():
    print("OPENAI_API_KEY --------------------------------", OPENAI_API_KEY)
    agent = create_csv_agent(
        OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY),
        csvPath,
        verbose=True,
    )
    test = agent.run(
        "This is my csv file with weekly goals. What is my completion rate for each goal?"
    )
    print("test --------------------------------", test)

    return test


if __name__ == "__main__":
    app.run(port=5328)

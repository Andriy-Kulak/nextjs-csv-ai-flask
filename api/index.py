from flask import Flask

# from langchain.llms import OpenAI
# from langchain.agents import create_csv_agent

app = Flask(__name__)

OPENAI_API_KEY = "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"


@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"


# @app.route("/api/test")
# def hello_test():
#     agent = create_csv_agent(
#         OpenAI(openai_api_key=OPENAI_API_KEY), "titanic.csv", verbose=True
#     )
#     test = agent.run("how many rows are there?")
#     return "<p>{test}</p>"
#     # return "<p>Hello, World!</p>"

#env build_mcp_12

from langchain_openai import ChatOpenAI
from langchain.sql_database import SQLDatabase
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
import os
os.environ["OPENAI_API_KEY"] = "key"


db = SQLDatabase.from_uri(
    "postgresql+psycopg2://paresh:paresh@localhost:5432/searates2"
)

if db:
    print("connection succesfull")

else:
    print("connection not successfulll")

llm = ChatOpenAI(
model="gpt-4o-mini", 
temperature=0
)


agent = create_sql_agent(
    llm=llm,
    db=db,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    max_iterations=5,
    handle_parsing_errors=True,
    verbose=True,  
)


response = agent.run("give me all customer name who paid their bills")
print(response)
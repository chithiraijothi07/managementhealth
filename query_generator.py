from langchain import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.chat_models import ChatOpenAI

catalog = "main"  # Replace with your catalog
schema = "ai_chatbot"  # Replace with your schema
server_hostname = "adb-7701630258100873.13.azuredatabricks.net"
api_token="dapidbe48c124b0e8fd83d88080a2ed34034-3"
# Specify the warehouse_id or cluster_id based on your setup
# For example, let's use warehouse_id
warehouse_id = "d02a308bd9e9096c"  # Replace with your warehouse ID

# Create a Databricks SQLDatabase connection
db_databricks = SQLDatabase.from_databricks(
    catalog=catalog,
    schema=schema,
    host=server_hostname,
    api_token=api_token,
    warehouse_id=warehouse_id,
)

# Now you can use db_databricks to execute SQL queries

print(db_databricks)

# Set up the OpenAI instance
OPENAI_API_KEY = "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"
# llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

db_chain = SQLDatabaseChain.from_llm(llm=ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo-16k',openai_api_key=OPENAI_API_KEY), db=db_databricks, verbose=True)


# Create an instance of SQLDatabaseChain
# db_chain = SQLDatabaseChain.from_llm(llm=llm, db=db_databricks, verbose=True)

# Maintain conversation history here
conversation_history = []

# ... (your existing code)

def run_query(user_input):
    global conversation_history

    # Add user input to the conversation history
    conversation_history.append(f"User: {user_input}")

    # Join the conversation history
    conversation_text = "\n".join(conversation_history)

    # Run the conversation with memory
    response = db_chain.run(conversation_text)

    # Add AI response to the conversation history
    conversation_history.append(f"MediBot: {response}")

    return response, conversation_history  # Return both response and updated conversation history.
#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


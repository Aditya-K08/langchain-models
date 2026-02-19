from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="conversational", 
    provider="novita",   
    max_new_tokens=256,
    temperature=0.5,
)

chat = ChatHuggingFace(llm=llm)

resp = chat.invoke([HumanMessage(content="Who won the FIFA World Cup in 1994?")])
print(resp.content)

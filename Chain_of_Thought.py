from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

### Initialize LLM ###
llm = OllamaLLM(
    model="llama3.1"
)

### Make Prompt ###
template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a maths and finances professional teacher."),
        ("human", "I went to the market and bought 10 apples. I gave 2 apples to the neighbor and 2 to the repairman. I then went and bought 5 more apples and ate 1. How many apples did I remain with?"),
        ("ai", "First, you started with 10 apples. You gave away 2 apples to the neighbor and 2 to the repairman, so you had 6 apples left. Then you bought 5 more apples, so now you had 11 apples. Finally, you ate 1 apple, so you would remain with 10 apples."),
        ("human", input("Request: "))
    ]
)

prompt = template.format()

### Make response ###
print(llm.invoke(prompt))
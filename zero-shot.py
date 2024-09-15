from langchain_ollama import OllamaLLM

### LLM setting ###
llm = OllamaLLM(
    model="llama3.1",
    temperature=0
)

### Template setting ###
template = """
Answer Yes or No if the following sentence is related to food.
Sentence: I like cookies.
Answer:
"""

print(llm.invoke(template))
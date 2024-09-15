from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

### LLM setting ###
llm = OllamaLLM(
    model="llama3.1",
    temperature=0
)

### Template setting ###
template = PromptTemplate.from_template("""
- 'abc' is a traditional dish in Mexico
                                        
Answer Yes or No if the following sentence is related to food.
Sentence: {sentence}.
Answer:
""")

### If you remove the abc context above, if you input 'the abc is tasy' is going to answer 'No'
### Otherwise, it would output 'Yes'

prompt = template.format(
    sentence = input("Sentence: ")
)

print(llm.invoke(prompt))
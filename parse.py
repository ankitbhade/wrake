from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are an AI assistant tasked with extracting and formatting information from text content. "
    "Here is the content to analyze: {dom_content}\n\n"
    "Instructions:\n"
    "1. Extract ONLY the information that matches this description: {parse_description}\n"
    "2. Format your response in a clear, natural way using proper sentences and paragraphs\n"
    "3. If no matching information exists, you must return EXACTLY an empty string '' with no other text\n"
    "4. Never include phrases like 'no information found' or similar meta-commentary\n"
    "5. Never explain what you're doing or why information is missing\n"
    "6. Focus on readability and natural language flow when information exists"
)

model = OllamaLLM(model="llama3.2")

def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)
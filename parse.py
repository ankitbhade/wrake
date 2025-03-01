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
    "6. Focus on readability and natural language flow when information exists\n"
    "7. Answer in no more than 5-6 sentences. Do not make answers longer than that.\n"
    "8. IMPORTANT: Only provide unique information. Do not repeat information that has already been mentioned.\n"
    "9. If you find only information that repeats what was already found in previous chunks, return an empty string ''\n"
)

model = OllamaLLM(model="llama3.2")

def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    # Combine all chunks into one for processing
    combined_content = "\n".join(dom_chunks)
    
    # Process the combined content in one go
    response = chain.invoke(
        {"dom_content": combined_content, "parse_description": parse_description}
    )
    
    return response

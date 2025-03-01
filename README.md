# 🍁 Wrake  

Your web rake for gathering data in the vast forest of the internet!  

## Description  
Wrake is a tool that helps you extract and parse specific information from web pages using natural language queries.  

## Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/wrake.git
   cd wrake
   ```  

2. Create a virtual environment:  
   ```bash
   python3 -m venv wrake
   source wrake/bin/activate  # On Windows use: wrake\Scripts\activate
   ```  

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

4. Install and start Ollama:  
   - Follow instructions at [Ollama](https://ollama.ai) to install Ollama  
   - **Open a new terminal tab and run:**  
     ```bash
     ollama serve
     ```  
   - Pull the required model:  
     ```bash
     ollama pull llama3.2
     ```  

## Usage  

1. Start the application:  
   ```bash
   streamlit run main.py
   ```  

2. Enter a website URL and click **"Wrake it! 🚀"**  

3. Once the content is extracted, describe what information you want to parse in natural language.  

## Requirements  
- Python 3.9+  
- Ollama  
- Chrome/Chromium browser  

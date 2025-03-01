# 🍁 Wrake - Your Web Rake for Data 🌐🔍  

Wrake is a simple tool powered by Llama 3.2 that helps you extract and parse specific information from web pages using natural language queries. It simplifies web scraping, making data retrieval seamless and user-friendly. 

## **📜 Features**  
✔️ **Natural Language Querying** – Extract data with simple text prompts  
✔️ **Automated Parsing** – No manual filtering required  
✔️ **Fast & Efficient** – Optimized for quick web data retrieval on small webpages  
✔️ **Easy to Use** – Streamlined setup and usage  

![wrake-demo](https://github.com/user-attachments/assets/cda9c2b6-2e30-4eb1-b6e9-a85b27921d51)

## **⚙️ Installation & Setup**  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/ankitbhade/wrake.git
   cd wrake
   ```  

2. **Create a Virtual Environment**  
   ```bash
   python3 -m venv wrake
   source wrake/bin/activate
   ```  

3. **Install Dependencies**  
   ```bash
   pip3 install -r requirements.txt
   ```  

4. **Install and Start Ollama**  
   - Follow instructions at [Ollama](https://ollama.com) to install Ollama  
   - **Open a new terminal tab and run:**  
     ```bash
     ollama serve
     ```  
   - Pull the required model:  
     ```bash
     ollama pull llama3.2
     ```  

## **🚀 Usage**  

1. **Start the Application**  
   ```bash
   streamlit run main.py
   ```  

2. **Extract Data**  
   - Enter a website URL and click **"wrake it"**  
   - Describe the data you want to extract in natural language.
   - Get your results!

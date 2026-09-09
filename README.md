# AI-Student-Support-Assistant

   A terminal-based AI assistant that helps     
   college students with academic and college-
   related information.

FEATURES

   📚 Retrieves information from college 
   documents using RAG

   🧠 Remembers basic student learning topics 
   and progress

   🛠️ Generates quizzes

   📅 Creates study plans

   🤖 Uses Llama 3.2 locally through Ollama

   💬 Simple terminal-based interface


REQUIREMENTS

   Before running the project, install:
      1.Python 3.10 or later

      2.Ollama

      3.Llama 3.2


INSTALLATION 

   1. Install Python

      Download Python from:
         https://www.python.org/downloads/

      Check the installation:
         python --version

   2. Install Ollama

      Download Ollama from:
         https://ollama.com/

      Check the installation:
         ollama --version

   3. Install Llama 3.2

      Open a terminal and run:
         ollama pull llama3.2

      Check that the model is installed:
         ollama list

   4. Install Project Dependencies

      Open the project folder in the terminal
      and run:
         pip install -r requirements.txt

         Run the Project

RUN:

   python main.py

   The AI Student Support Assistant will start     in the terminal.

HOW TO USE 

   Enter a college-related question in the   
   terminal.

   For example:

      What subjects are in Semester 3?

      To generate a quiz:
         quiz Data Structures

      To create a study plan:
         study plan Data Structures

      To save a learning topic:
         I want to learn Data Structures

      To save completed progress:
         I completed Data Structures

      To exit the assistant:
         exit

PROJECT STRUCTURE 

'''text
   AI-Student-Support-Assistant/
   │
   ├── main.py
   ├── agent.py
   ├── rag.py
   ├── memory.py
   ├── tools.py
   ├── requirements.txt
   │
   ├── documents/
   │   ├── college_info.txt
   │   └── college_faq.txt
   │
   └── memory.json
'''

IMPORTANT NOTE 

   The college information included in this   
   project is sample/demo information.

   For important college information such as 
   examination dates, regulations, or official 
   announcements, users should verify the 
   information with official college sources.

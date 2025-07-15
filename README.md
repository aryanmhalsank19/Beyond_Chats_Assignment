# Beyond_Chats — Reddit User Persona Generator (LLM-Powered)

**Beyond_Chats** is an intelligent command-line tool that takes a Reddit user’s profile URL and generates a psychologically-informed **user persona** based on their public posts and comments.

The output is a clean `.txt` file that includes:
- Personality traits  
- Topic interests  
- Writing style  
- Cited quotes from their content  
- A generated summary paragraph  

Powered by a lightweight local LLM (like `phi`) running via **Ollama**, this tool works offline — with no cloud dependencies or rate limits.

---

## What It Does

Reddit URL ➝ Scrape Posts & Comments ➝ Clean & Chunk ➝ Send to LLM ➝ Generate Persona ➝ Save to .txt

For each Reddit user:
- Scrapes their latest **100 posts** and **200 comments**
- Cleans and chunks the text using `nltk`
- Sends each chunk to a local LLM using **Ollama**
- Generates a structured persona per chunk:
  - 2 personality traits
  - Writing style
  - Topic interests
  - 2 quotes
  - Summary paragraph
- Saves everything in `examples/<username>_persona.txt`

---

## Example Use Case

### Command:
```bash
python main.py --url https://www.reddit.com/user/kojied/ --limit 2
Output File:
examples/kojied_persona.txt

Sample Output:

--- Persona Block 1 ---
Username: u/kojied

Personality Traits:
1. Strongly values decentralization and autonomy.
2. Skeptical of mainstream systems and authorities.

Writing Style:
Direct, informal, sometimes confrontational.

Topic Interests:
Crypto, privacy, digital rights, censorship.

Quotes:
- "I’ve stopped trusting traditional banks."
- "Monero is the only true private currency."

Generated Summary:
u/kojied frequently contributes to discussions around crypto and privacy.
Their tone is sharp, independent, and opinionated — reflecting a mindset
that values control and freedom through technology.
Setup Instructions
1. Clone the Project
git clone https://github.com/yourusername/Beyond_Chats.git
cd Beyond_Chats

2. Install Python Dependencies
pip install -r requirements.txt
python -m nltk.downloader punkt

3. Configure Reddit API Credentials
Visit: https://www.reddit.com/prefs/apps

Create a new app → choose script

Create a .env file in the root directory:

REDDIT_CLIENT_ID=your_reddit_app_id
REDDIT_CLIENT_SECRET=your_reddit_secret
REDDIT_USER_AGENT=BeyondChatsUserAgent

4. Install & Run Ollama (for Local LLM)
If you don't have Ollama:

brew install ollama
Then pull and start the model:

ollama pull phi
ollama serve
This runs a local LLM server at:

http://localhost:11434
Running the Tool

python main.py --url https://www.reddit.com/user/GallowBoob/ --limit 3
--url : Reddit profile URL

--limit : (optional) number of content chunks to process

Output saved to:

examples/GallowBoob_persona.txt
Project Structure
bash
Copy
Edit
Beyond_Chats/
├── main.py
├── .env
├── requirements.txt
├── examples/                 # Output persona files
└── persona_builder/
    ├── scraper.py           # Reddit scraping logic
    ├── utils.py             # Text cleaning and chunking
    ├── llm_persona.py       # Persona generation using Ollama
    └── formatter.py         # Output formatting and saving
Model Customization
In llm_persona.py, you can switch models:

OLLAMA_MODEL = "mistral"
Then run:

ollama pull mistral
Test With These Reddit Profiles

https://www.reddit.com/user/GallowBoob/
https://www.reddit.com/user/Unidan/
https://www.reddit.com/user/spez/
https://www.reddit.com/user/BernieSandersFan/
https://www.reddit.com/user/Hungry-Move-6603/
Error Handling
Scenario	What Happens
No posts/comments	[INFO] No data found for user
Ollama not running	[ERROR] Connection refused
Model not pulled yet	Run ollama pull phi again
Invalid Reddit URL	[ERROR] Invalid Reddit URL format

Highlights
Private and offline (no tokens, no API rate limits)

Powered by local LLMs via Ollama

Human-readable, psychology-style persona output

Modular design — easy to extend (web, JSON, HTML, etc.)

Author
Aryan Mhalsank
Built for a Generative AI Internship Assessment
With focus on: real-world NLP, local AI systems, and persona intelligence.

Want to understand someone’s mindset from just their Reddit profile?
This tool lets you do that — quickly, privately, and intelligently.

License
MIT License — free to use, fork, remix, and improve.

# 🧠 Beyond_Chats — Reddit User Persona Generator (LLM-Powered)

**Beyond_Chats** is an intelligent command-line tool that takes a Reddit user’s profile URL and generates a psychologically-informed **user persona** based on their public posts and comments.  
The result is a readable text file that includes:
- Personality traits  
- Topic interests  
- Writing style  
- Cited quotes  
- A generated summary — all backed by real content  

It uses a lightweight **LLM (like Phi)** running **locally via Ollama**, with zero cloud dependency or rate limits.

---

## 🔍 What It Does

Reddit URL → Scrape Posts + Comments → Clean & Chunk → Send to LLM → Generate Full Persona Block → Save to .txt

For each Reddit profile:
- Scrapes latest 100 posts and 200 comments
- Cleans & breaks text into chunks
- Sends each chunk to a local model via Ollama
- Generates a detailed user persona for each chunk:
  - ✅ 2 personality traits
  - ✅ Writing style
  - ✅ Topic interests
  - ✅ Quote examples
  - ✅ Paragraph summary
- Saves output to `examples/<username>_persona.txt`

---

## 🧠 Example Use Case

> Input:
```bash
python main.py --url https://www.reddit.com/user/kojied/ --limit 2
📂 Output:
File: examples/kojied_persona.txt

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
u/kojied frequently contributes to discussions around crypto and privacy. Their tone is sharp, independent, and opinionated — reflecting a mindset that values control and freedom through technology.

Setup Instructions
1. Clone the Project
git clone https://github.com/yourusername/Beyond_Chats.git
cd Beyond_Chats
2. Install Python Dependencies

pip install -r requirements.txt
python -m nltk.downloader punkt
3. Configure Reddit API Access
Go to https://www.reddit.com/prefs/apps

Create a new app → script

Add a .env file in the root directory:

REDDIT_CLIENT_ID=your_reddit_app_id
REDDIT_CLIENT_SECRET=your_reddit_secret
REDDIT_USER_AGENT=BeyondChatsUserAgent

4. Install & Run Ollama
If not installed:

brew install ollama
Then pull the model and serve:

ollama pull phi
ollama serve
✅ Ollama will host a local LLM server at http://localhost:11434.

▶️ Running the Script

python main.py --url https://www.reddit.com/user/GallowBoob/ --limit 3

--url : Reddit profile URL

--limit : (Optional) number of text chunks to process (useful for testing)

The full persona will be saved to:


examples/GallowBoob_persona.txt

Folder Structure
bash
Copy
Edit
Beyond_Chats/
├── main.py
├── .env
├── requirements.txt
├── examples/
└── persona_builder/
    ├── scraper.py        # Scrapes posts/comments
    ├── utils.py          # Cleans + chunks text
    ├── llm_persona.py    # Persona generation via Ollama
    └── formatter.py      # Formats and saves output

Model Customization (Advanced)
You can swap phi with mistral or another local model in llm_persona.py:

OLLAMA_MODEL = "mistral"
Just make sure to:

ollama pull mistral
Tested Reddit Profiles
Try out these real users:

https://www.reddit.com/user/GallowBoob/
https://www.reddit.com/user/Unidan/
https://www.reddit.com/user/spez/
https://www.reddit.com/user/BernieSandersFan/
https://www.reddit.com/user/Hungry-Move-6603/

🧩 Error Handling
If Reddit user has no content → you'll see: No data found for user
If Ollama is not running → you'll see: Connection refused
If model is missing → run: ollama pull phi again

📌 Highlights
No external API costs or limits

Private and offline

Fully explainable: traits are cited with real quotes

Modifiable for JSON, HTML, or web UI output

Author
Aryan Mhalsank
Built for a Generative AI Internship Assessment — focused on real-world AI tools, privacy, and LLM integration.

Need a fast, private way to analyze a user's public online presence?
Beyond_Chats is your plug-and-play solution.

License
MIT License — use freely, improve endlessly.

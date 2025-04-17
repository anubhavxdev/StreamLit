# 🎵 AI Music Assistant

**AI Music Assistant** is a smart web app built using Streamlit that combines Spotify's powerful music data with Google's Gemini AI to create a dynamic and intelligent music experience. Get personalized recommendations, search music, analyze lyrics, explore music theory, and listen to previews—all from one place.

---

## 🚀 Features

- 🎧 **Personalized Music Recommendations** based on mood and genre
- 🔍 **Music Search** by track name
- 📝 **Lyrics Analysis** using Google's Gemini AI
- 🎼 **Music Theory Helper** for chord progressions, concepts, and more
- ▶️ **Play Song Previews** using Spotify API
- ✨ **Beautiful UI** with animations and custom styles

---

## 🛠️ Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io/)
- **AI Integration**: [Google Generative AI (Gemini)](https://ai.google.dev/)
- **Music Data**: [Spotify Web API](https://developer.spotify.com/)
- **API Wrapper**: [Spotipy](https://spotipy.readthedocs.io/)
- **Environment Management**: [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📂 Project Structure

📁 ai-music-assistant/ │ ├── app.py # Main Streamlit application ├── .env # Environment variables (not pushed to repo) ├── requirements.txt # Python dependencies └── README.md # Project documentation


---

## 📦 Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ai-music-assistant.git
cd ai-music-assistant
```
2. **Create a virtual environment (optional)**
   ```bash
   python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.**Install the required packages**
```bash
  pip install -r requirements.txt
```
4. Create a .env file in the root directory
   ```bash
     SPOTIPY_CLIENT_ID=your_spotify_client_id
    SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
    GOOGLE_API_KEY=your_google_api_key
   ```

5. **Run the app**
    ```bash
    streamlit run app.py
   ```


💡 Usage
Use the sidebar to navigate between features:

Music Recommendations

Music Search

Lyrics Analysis

Music Theory Helper

Play a Song Preview

Enter your mood, genre, or lyrics depending on the section.

Click buttons to interact with Gemini or Spotify.

Enjoy the results presented in a clean, music-themed UI!

🖼️ UI Highlights
Gradient background with animated music notes

Floating music cards with hover effects

Custom-styled buttons and inputs

Embedded Spotify player if no audio preview is available

🧠 Sample Prompts
Recommend 5 songs for someone who feels happy and likes indie music.

Analyze the emotional tone of the lyrics pasted below.

What is a dominant seventh chord and how is it used in jazz?

📄 License
This project is licensed under the MIT License. Feel free to fork, use, or modify.

🙋‍♂️ Author
Developed with ❤️ by Your Name

🌟 Acknowledgments
Spotify Developer Platform

Google Generative AI (Gemini)

Streamlit Community

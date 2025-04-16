import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get credentials from .env
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
google_api_key = os.getenv("GOOGLE_API_KEY")

# Authenticate Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
))

# Configure Google Gemini API
genai.configure(api_key=google_api_key)
model = genai.GenerativeModel('gemini-1.5-pro')

# Streamlit UI setup
st.set_page_config(page_title="AI Music Assistant", page_icon="🎵", layout="wide")

# Styling
st.markdown("""
    <style>
    body, .main {
        background: linear-gradient(135deg, #f0f4f7, #e0eafc, #cfdef3);
        font-family: 'Segoe UI', sans-serif;
    }

    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/stardust.png");
        background-size: cover;
    }

    .stTextInput>div>div>input,
    .stTextArea>div>textarea,
    .stSelectbox>div>div>div {
        background-color: rgba(255, 255, 255, 0.9);
        color: #000;
        border-radius: 10px;
        padding: 8px;
    }

    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        font-weight: bold;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #388e3c;
        transform: scale(1.05);
    }

    .music-card {
        background-color: rgba(255, 255, 255, 0.85);
        color: black;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        transition: 0.3s;
    }

    .music-card:hover {
        transform: scale(1.01);
    }
    
    

    /* Floating notes animation */
    @keyframes floatNotes {
        0% {
            transform: translateY(100vh) rotate(0deg);
            opacity: 0;
        }
        50% {
            opacity: 1;
        }
        100% {
            transform: translateY(-10vh) rotate(360deg);
            opacity: 0;
        }
    }
    
    
    .note {
        position: fixed;
        color: #ff69b4;
        font-size: 24px;
        animation: floatNotes 10s linear infinite;
        pointer-events: none;
    }        

    .note:nth-child(1) { left: 5%; animation-delay: 0s; }
    .note:nth-child(2) { left: 25%; animation-delay: 2s; }
    .note:nth-child(3) { left: 45%; animation-delay: 4s; }
    .note:nth-child(4) { left: 65%; animation-delay: 6s; }
    .note:nth-child(5) { left: 85%; animation-delay: 8s; }
    </style>

    <div class="note">🎵</div>
    <div class="note">🎶</div>
    <div class="note">🎼</div>
    <div class="note">🎵</div>
    <div class="note">🎶</div>
""", unsafe_allow_html=True)

# Header
st.title("🎵 AI Music Assistant")
st.markdown("Discover music, get recommendations, and learn about music theory with AI!")

# Gemini response
def get_gemini_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Spotify search
def search_music(query):
    results = sp.search(q=query, limit=5, type='track')
    tracks = results['tracks']['items']
    formatted_results = []

    for track in tracks:
        formatted_results.append({
            "title": track['name'],
            "artist": track['artists'][0]['name'],
            "genre": "Unknown",  # Spotify API does not provide genre at track level
            "year": track['album']['release_date'][:4]
        })
    return formatted_results

# Sidebar Navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.radio("Choose a feature:", 
                           ["Music Recommendations", 
                            "Music Search", 
                            "Lyrics Analysis",
                            "Music Theory Helper",
                            "Play a Song Preview"])  # New section added

# Music Recommendations
if app_mode == "Music Recommendations":
    st.header("🎧 Personalized Music Recommendations")
    mood = st.text_input("How are you feeling or what mood are you in?,(e.g., happy, relaxed, energetic)")
    genre = st.text_input("Any specific genre you prefer? (e.g., rock, jazz, hip-hop)?")

    if st.button("Get Recommendations"):
        if mood or genre:
            prompt = f"Recommend 5 songs for someone who is feeling {mood}"
            if genre:
                prompt += f" and likes {genre} music"
            prompt += ". Include diverse artists. Format as a numbered list with artist names."

            with st.spinner("Finding perfect recommendations..."):
                recommendations = get_gemini_response(prompt)
                st.subheader("Here are your recommendations:")
                st.markdown(recommendations)
        else:
            st.warning("Please provide at least a mood or genre for recommendations.")

# Music Search
elif app_mode == "Music Search":
    st.header("🔍 Music Search")
    search_query = st.text_input("Enter your search query:")

    if st.button("Search"):
        if search_query:
            with st.spinner("Searching music..."):
                results = search_music(search_query)

                st.subheader("Search Results")
                for idx, song in enumerate(results, 1):
                    with st.container():
                        st.markdown(f"""
                        <div class="music-card">
                            <h3>{idx}. {song['title']}</h3>
                            <p><strong>Artist:</strong> {song['artist']}</p>
                            <p><strong>Genre:</strong> {song['genre']}</p>
                            <p><strong>Year:</strong> {song['year']}</p>
                        </div>
                        """, unsafe_allow_html=True)
        else:
            st.warning("Please enter a search query.")

# Lyrics Analysis
elif app_mode == "Lyrics Analysis":
    st.header("📝 Lyrics Analysis")
    lyrics = st.text_area("Paste song lyrics here:", height=200)
    analysis_type = st.selectbox("What would you like to analyze?", 
                                 ["Overall Meaning", "Themes", "Literary Devices", "Emotional Tone"])

    if st.button("Analyze Lyrics"):
        if lyrics:
            with st.spinner("Analyzing lyrics..."):
                prompt = f"Analyze these song lyrics for {analysis_type.lower()}:\n\n{lyrics}\n\nProvide a detailed analysis."
                analysis = get_gemini_response(prompt)
                st.subheader("Lyrics Analysis")
                st.write(analysis)
        else:
            st.warning("Please paste some lyrics to analyze.")

# Music Theory Helper
elif app_mode == "Music Theory Helper":
    st.header("🎼 Music Theory Helper")
    theory_query = st.text_input("Ask a music theory question")
    st.write("Get help with music theory concepts, chord progressions, and more")

    if st.button("Get Answer"):
        if theory_query:
            with st.spinner("Researching music theory..."):
                response = get_gemini_response(f"Explain this music theory concept in simple terms with examples: {theory_query}")
                st.subheader("Music Theory Explanation")
                st.write(response)
        else:
            st.warning("Please enter a music theory question.")

# ▶️ Play a Song Preview (New Section)
elif app_mode == "Play a Song Preview":
    st.header("▶️ Play a Song Preview")
    song_name = st.text_input("Enter the name of a song to preview:")

    if st.button("Play Preview"):
        if song_name:
            results = sp.search(q=song_name, limit=10, type='track')
            tracks = results['tracks']['items']
            track_found = False

            for track in tracks:
                preview_url = track.get('preview_url')
                if preview_url:
                    st.subheader(f"{track['name']} by {track['artists'][0]['name']}")
                    st.audio(preview_url, format='audio/mp3')
                    track_found = True
                    break

            if not track_found:
                if tracks:
                    first_track = tracks[0]
                    track_id = first_track['id']
                    st.warning("No preview available for this track. But you can listen on Spotify:")
                    st.markdown(f"""
                        <iframe src="https://open.spotify.com/embed/track/{track_id}" 
                                width="300" height="80" frameborder="0" allowtransparency="true" 
                                allow="encrypted-media"></iframe>
                    """, unsafe_allow_html=True)
                else:
                    st.warning("No matching tracks found.")
        else:
            st.warning("Please enter a song name.")

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: gray;">
        <p>AI Music Assistant powered by Gemini and Streamlit</p>
    </div>
""", unsafe_allow_html=True)
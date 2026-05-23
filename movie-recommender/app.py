import streamlit as st
import pandas as pd
import pickle
import requests
from pathlib import Path

# ── Page config ──────────────────────────────────────────
st.set_page_config(
    page_title="CineMatch",
    page_icon="🎬",
    layout="wide",
)

# ── TMDB API Key ──────────────────────────────────────────
# Get a free key at: https://www.themoviedb.org/settings/api
TMDB_API_KEY = "YOUR_TMDB_API_KEY_HERE"

# ── Load Data ─────────────────────────────────────────────
@st.cache_data
def load_data():
    base = Path(__file__).parent
    with open(base / "movie_dict.pkl", "rb") as f:
        movies = pd.DataFrame(pickle.load(f))
    with open(base / "similarity.pkl", "rb") as f:
        similarity = pickle.load(f)
    return movies, similarity

# ── Fetch Poster ──────────────────────────────────────────
@st.cache_data(show_spinner=False, ttl=86400)
def fetch_poster(movie_id):
    """Returns poster URL or None if unavailable."""
    if TMDB_API_KEY == "YOUR_TMDB_API_KEY_HERE":
        return None  # no key set, skip silently

    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        path = r.json().get("poster_path")
        if path:
            return f"https://image.tmdb.org/t/p/w500{path}"
    except Exception:
        pass  # fail silently — poster is optional
    return None

# ── Recommend ─────────────────────────────────────────────
def recommend(movie, movies_df, similarity_matrix):
    if movie not in movies_df["title"].values:
        return []

    idx = movies_df[movies_df["title"] == movie].index[0]
    scores = list(enumerate(similarity_matrix[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]

    results = []
    for i, score in scores:
        row = movies_df.iloc[i]
        results.append({
            "title": row["title"],
            "movie_id": row["movie_id"],
            "score": round(score * 100, 1),
        })
    return results

# ── UI ────────────────────────────────────────────────────
st.title("🎬 CineMatch — Movie Recommender")
st.caption("Select a movie you love and get 5 similar recommendations.")
st.divider()

# Load
try:
    movies, similarity = load_data()
except FileNotFoundError as e:
    st.error(
        f"Missing file: {e}\n\n"
        "Make sure `movie_dict.pkl` and `similarity.pkl` are in the same folder as `app.py`."
    )
    st.stop()

# Input
col1, col2 = st.columns([4, 1], gap="medium")

with col1:
    selected = st.selectbox(
        "🔍 Pick a movie",
        options=sorted(movies["title"].values),
        index=None,
        placeholder="Type to search...",
    )

with col2:
    st.write("")  # spacer to align button
    clicked = st.button("🎯 Recommend", use_container_width=True, type="primary")

# Results
if clicked:
    if not selected:
        st.warning("Please select a movie first.")
        st.stop()

    results = recommend(selected, movies, similarity)

    if not results:
        st.error("Movie not found in the database.")
        st.stop()

    st.subheader(f"Because you liked **{selected}**:")
    st.write("")

    cols = st.columns(5, gap="medium")

    for col, movie in zip(cols, results):
        poster = fetch_poster(movie["movie_id"])
        with col:
            if poster:
                st.image(poster, use_container_width=True)
            else:
                # Fallback tile when no poster available
                st.markdown(
                    f"""
                    <div style="
                        background:#1e1e2e;
                        border-radius:8px;
                        aspect-ratio:2/3;
                        display:flex;
                        align-items:center;
                        justify-content:center;
                        padding:1rem;
                        text-align:center;
                        color:#888;
                        font-size:0.85rem;
                    ">🎬<br><br>{movie['title']}</div>
                    """,
                    unsafe_allow_html=True,
                )
            st.markdown(f"**{movie['title']}**")
            st.caption(f"Match score: {movie['score']}%")
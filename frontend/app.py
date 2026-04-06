import streamlit as st
import requests
import time

st.set_page_config(
    page_title="DocMind AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=Outfit:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* Hide streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main background */
.stApp {
    background: #0a0a0f;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #0f0f1a;
    border-right: 1px solid #1e1e2e;
}

[data-testid="stSidebar"] * {
    color: #c9c9e0 !important;
}

/* Title */
.main-title {
    font-family: 'Outfit', sans-serif;
    font-size: 2.2rem;
    font-weight: 700;
    background: linear-gradient(135deg, #7c6bff, #4fc3f7, #7c6bff);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shine 3s linear infinite;
    margin-bottom: 0;
}

@keyframes shine {
    to { background-position: 200% center; }
}

.subtitle {
    color: #6b6b8a;
    font-size: 0.9rem;
    margin-top: 4px;
    margin-bottom: 2rem;
}

/* Status badge */
.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #0d1f0d;
    border: 1px solid #1a3a1a;
    color: #4caf50;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 500;
    margin-bottom: 1.5rem;
}

.status-dot {
    width: 6px;
    height: 6px;
    background: #4caf50;
    border-radius: 50%;
    animation: pulse 2s infinite;
    display: inline-block;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.3; }
}

/* Chat messages */
[data-testid="stChatMessage"] {
    background: #13131f !important;
    border: 1px solid #1e1e30 !important;
    border-radius: 16px !important;
    padding: 1rem !important;
    margin-bottom: 0.75rem !important;
}

/* User message */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background: #0f0f2a !important;
    border-color: #2a2a4a !important;
}

/* Input */
[data-testid="stChatInput"] {
    background: #13131f !important;
    border: 1px solid #2a2a40 !important;
    border-radius: 16px !important;
    color: #e0e0f0 !important;
}

[data-testid="stChatInput"]:focus {
    border-color: #7c6bff !important;
    box-shadow: 0 0 0 2px rgba(124,107,255,0.2) !important;
}

/* Metric cards */
.metric-card {
    background: #13131f;
    border: 1px solid #1e1e30;
    border-radius: 12px;
    padding: 1rem;
    text-align: center;
}

.metric-value {
    font-family: 'Outfit', sans-serif;
    font-size: 1.8rem;
    font-weight: 700;
    color: #7c6bff;
}

.metric-label {
    font-size: 0.75rem;
    color: #6b6b8a;
    margin-top: 2px;
}

/* Feature pills */
.feature-pill {
    display: inline-block;
    background: #1a1a2e;
    border: 1px solid #2a2a4a;
    color: #9090c0;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    margin: 3px;
}

/* Source box */
.source-box {
    background: #0d0d1a;
    border-left: 3px solid #7c6bff;
    border-radius: 0 8px 8px 0;
    padding: 10px 14px;
    margin-top: 10px;
    font-size: 0.8rem;
    color: #6b6b8a;
}

/* Scrollbar */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #0a0a0f; }
::-webkit-scrollbar-thumb { background: #2a2a4a; border-radius: 4px; }

/* Spinner color */
.stSpinner > div { border-top-color: #7c6bff !important; }

/* Divider */
hr { border-color: #1e1e30 !important; }

/* Text colors */
p, li, span { color: #c9c9e0; }
h1, h2, h3 { color: #e0e0f0; }

/* File uploader */
[data-testid="stFileUploader"] {
    background: #13131f;
    border: 1px dashed #2a2a4a;
    border-radius: 12px;
    padding: 1rem;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #7c6bff, #5b4fd4);
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 500;
    padding: 0.5rem 1.5rem;
    transition: all 0.2s;
}

.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 20px rgba(124,107,255,0.4);
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding: 1rem 0'>
        <div style='font-family: Outfit; font-size: 1.3rem; font-weight: 700; color: #e0e0f0;'>🧠 DocMind AI</div>
        <div style='font-size: 0.75rem; color: #6b6b8a; margin-top: 4px;'>RAG-Powered Document Chat</div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("**📄 Document**")
    st.markdown("""
    <div style='background:#0d1a2a; border:1px solid #1a2a3a; border-radius:10px; padding:10px 14px; margin-bottom:1rem;'>
        <div style='font-size:0.8rem; color:#4fc3f7;'>✓ sample.pdf loaded</div>
        <div style='font-size:0.7rem; color:#6b6b8a; margin-top:2px;'>FAISS index ready</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**⚙️ Model Settings**")
    model = st.selectbox("LLM", ["mistral", "llama3", "qwen2.5:7b"], label_visibility="collapsed")
    top_k = st.slider("Retrieved chunks (k)", 1, 6, 3)
    st.markdown(f"""
    <div style='font-size:0.75rem; color:#6b6b8a; margin-top:4px;'>
        Embedding: all-MiniLM-L6-v2<br>
        Vector DB: FAISS
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("**🛠 Tech Stack**")
    for tech in ["LangChain", "FastAPI", "FAISS", "Ollama / Mistral", "HuggingFace Embeddings", "Streamlit"]:
        st.markdown(f"<span class='feature-pill'>{tech}</span>", unsafe_allow_html=True)

    st.divider()

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ── Main area ────────────────────────────────────────────
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("<div class='main-title'>DocMind AI</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Ask anything about your documents — powered by RAG + Mistral</div>", unsafe_allow_html=True)

with col2:
    try:
        r = requests.get("http://127.0.0.1:8000", timeout=2)
        if r.status_code == 200:
            st.markdown("<div class='status-badge'><span class='status-dot'></span> API Online</div>", unsafe_allow_html=True)
    except:
        st.markdown("<div class='status-badge' style='border-color:#3a1a1a;color:#f44336;background:#1f0d0d;'><span style='width:6px;height:6px;background:#f44336;border-radius:50%;display:inline-block;'></span> API Offline</div>", unsafe_allow_html=True)

# Stats row
if "messages" in st.session_state and st.session_state.messages:
    q_count = len([m for m in st.session_state.messages if m["role"] == "user"])
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='metric-card'><div class='metric-value'>{q_count}</div><div class='metric-label'>Questions Asked</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='metric-card'><div class='metric-value'>{top_k}</div><div class='metric-label'>Chunks Retrieved</div></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='metric-card'><div class='metric-value'>local</div><div class='metric-label'>Running Mode</div></div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

# ── Chat ─────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    st.markdown("""
    <div style='text-align:center; padding: 3rem 0;'>
        <div style='font-size:3rem; margin-bottom:1rem;'>🧠</div>
        <div style='font-family:Outfit; font-size:1.2rem; color:#e0e0f0; font-weight:600;'>Ready to answer your questions</div>
        <div style='color:#6b6b8a; font-size:0.85rem; margin-top:8px;'>Try asking something about your document below</div>
        <div style='margin-top:1.5rem; display:flex; gap:8px; justify-content:center; flex-wrap:wrap;'>
    """, unsafe_allow_html=True)
    suggestions = ["What is RAG?", "Explain machine learning", "What is LangChain?", "What is deep learning?"]
    cols = st.columns(len(suggestions))
    for i, s in enumerate(suggestions):
        with cols[i]:
            if st.button(s, key=f"sug_{i}"):
                st.session_state.messages.append({"role": "user", "content": s})
                st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question about your document..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Retrieving context and generating answer..."):
            start = time.time()
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/ask",
                    json={"question": prompt},
                    timeout=120
                )
                data = response.json()
                answer = data.get("answer", "No answer returned.")
                elapsed = round(time.time() - start, 1)
            except Exception as e:
                answer = f"⚠️ Could not reach the API. Make sure FastAPI is running.\n\n`{str(e)}`"
                elapsed = 0

        st.markdown(answer)

        if elapsed > 0:
            st.markdown(f"""
            <div class='source-box'>
                ⚡ Generated in {elapsed}s &nbsp;·&nbsp; Model: {model} &nbsp;·&nbsp; Chunks: {top_k} &nbsp;·&nbsp; Vector DB: FAISS
            </div>
            """, unsafe_allow_html=True)

    st.session_state.messages.append({"role": "assistant", "content": answer})
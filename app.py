import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Sambung Kata - Predator Mode",
    page_icon="⚔️",
    layout="wide"
)

# Load database
@st.cache_data
def load_databases():
    with open("kbbi.txt", "r", encoding="utf-8") as f:
        words = [line.strip().lower() for line in f if line.strip()]
    return words

all_words = load_databases()
rare_letters = set("qxzvf")

if 'used_words' not in st.session_state:
    st.session_state.used_words = set()
if 'last_word' not in st.session_state:
    st.session_state.last_word = None

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');

* { font-family: 'Poppins', sans-serif !important; }

.stApp {
    background: #0f0c29;
    background: linear-gradient(160deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    min-height: 100vh;
}

/* Header */
.hero {
    text-align: center;
    padding: 30px 0 10px 0;
}
.hero h1 {
    font-size: 2.8rem;
    font-weight: 800;
    color: #ffffff;
    text-shadow: 0 0 30px rgba(255,71,87,0.6), 0 0 60px rgba(255,71,87,0.3);
    letter-spacing: 2px;
    margin: 0;
}
.hero p {
    color: #a29bfe;
    font-size: 1rem;
    margin-top: 6px;
    letter-spacing: 3px;
    text-transform: uppercase;
}

/* Input override */
.stTextInput input {
    background: #1e1b4b !important;
    color: #ffffff !important;
    border: 2px solid rgba(162,155,254,0.4) !important;
    border-radius: 12px !important;
    padding: 14px 18px !important;
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    caret-color: #a29bfe !important;
}
.stTextInput input:focus {
    border-color: #a29bfe !important;
    box-shadow: 0 0 0 3px rgba(162,155,254,0.2) !important;
}
.stTextInput input::placeholder {
    color: rgba(162,155,254,0.4) !important;
}
.stTextInput label { display: none !important; }

/* Stat cards */
.stat-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 14px;
    padding: 16px;
    text-align: center;
    margin: 6px 0;
}
.stat-number {
    color: #a29bfe;
    font-size: 1.8rem;
    font-weight: 800;
}
.stat-label {
    color: rgba(255,255,255,0.5);
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Buttons - word cards */
.stButton > button {
    background: rgba(255,255,255,0.04) !important;
    color: white !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    letter-spacing: 1px !important;
    text-align: left !important;
    padding: 12px 18px !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    background: rgba(162,155,254,0.15) !important;
    border-color: rgba(162,155,254,0.4) !important;
    transform: translateX(4px) !important;
    box-shadow: none !important;
}
.stButton > button:active {
    background: rgba(162,155,254,0.3) !important;
}

/* Hide streamlit default elements */
.used-chip {
    display: inline-block;
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.12);
    color: #dfe6e9;
    padding: 5px 14px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 600;
    margin: 4px;
}

/* Section title */
.section-title {
    color: #a29bfe;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin: 20px 0 12px 0;
    padding-bottom: 8px;
    border-bottom: 1px solid rgba(162,155,254,0.2);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(15,12,41,0.95) !important;
    border-right: 1px solid rgba(255,255,255,0.08) !important;
}
section[data-testid="stSidebar"] * { color: #dfe6e9 !important; }

/* Hide streamlit default elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
section[data-testid="stSidebar"] {display: none !important;}

.copyright {
    text-align: center;
    color: rgba(255,255,255,0.3);
    font-size: 0.8rem;
    margin-top: 40px;
    padding: 20px 0;
    border-top: 1px solid rgba(255,255,255,0.06);
    letter-spacing: 1px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="hero">
    <h1>⚔️ PREDATOR MODE ⚔️</h1>
    <p>Sambung Kata · Strategi Huruf Langka</p>
</div>
""", unsafe_allow_html=True)

# Hitung statistik sekali, dipakai sidebar + main panel
used_count = len(st.session_state.used_words)
predator_count = sum(1 for w in st.session_state.used_words if w[-1] in rare_letters)

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    # Stats row - selalu tampil
    st.markdown(f"""
    <div style="display:flex; gap:10px; margin-bottom:12px; flex-wrap:wrap;">
        <div style="flex:1; min-width:80px; background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.12);
                    border-radius:14px; padding:12px; text-align:center;">
            <div style="color:#a29bfe; font-size:1.6rem; font-weight:800;">{used_count}</div>
            <div style="color:rgba(255,255,255,0.4); font-size:0.7rem; text-transform:uppercase; letter-spacing:1px;">Terpakai</div>
        </div>
        <div style="flex:1; min-width:80px; background:rgba(255,71,87,0.1); border:1px solid rgba(255,71,87,0.25);
                    border-radius:14px; padding:12px; text-align:center;">
            <div style="color:#ff6b81; font-size:1.6rem; font-weight:800;">{predator_count}</div>
            <div style="color:rgba(255,255,255,0.4); font-size:0.7rem; text-transform:uppercase; letter-spacing:1px;">🔥 Predator</div>
        </div>
        <div style="flex:1; min-width:80px; background:rgba(85,239,196,0.08); border:1px solid rgba(85,239,196,0.2);
                    border-radius:14px; padding:12px; text-align:center;">
            <div style="color:#55efc4; font-size:1.6rem; font-weight:800;">{used_count - predator_count}</div>
            <div style="color:rgba(255,255,255,0.4); font-size:0.7rem; text-transform:uppercase; letter-spacing:1px;">Biasa</div>
        </div>
        <div style="flex:1; min-width:80px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08);
                    border-radius:14px; padding:12px; text-align:center;">
            <div style="color:#fdcb6e; font-size:1.6rem; font-weight:800;">{len(all_words)//1000}K</div>
            <div style="color:rgba(255,255,255,0.4); font-size:0.7rem; text-transform:uppercase; letter-spacing:1px;">Database</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Reset button di main page juga
    if st.session_state.used_words:
        if st.button("🔄 Reset Semua Kata", use_container_width=True, key="reset_main"):
            st.session_state.used_words = set()
            st.session_state.last_word = None
            st.rerun()

# Search box + results dalam satu kolom
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.markdown('<div class="search-label">🔍 Masukkan awalan kata</div>', unsafe_allow_html=True)
    prefix = st.text_input(
        "prefix",
        key="prefix_input",
        placeholder="Ketik awalan... contoh: kam, ter, men",
        label_visibility="collapsed"
    ).lower().strip()
    if prefix:
        candidates = sorted(
            [w for w in all_words if w.startswith(prefix) and w not in st.session_state.used_words],
            key=lambda w: (w[-1] not in rare_letters, w)
        )

        if candidates:
            st.markdown(f'<div class="section-title">🎯 {len(candidates)} kata ditemukan</div>', unsafe_allow_html=True)

            predator_shown = [w.upper() for w in candidates[:50] if w[-1] in rare_letters]

            for idx, word in enumerate(candidates[:50]):
                if st.button(word.upper(), key=f"btn_{idx}_{word}", use_container_width=True):
                    st.session_state.used_words.add(word)
                    st.session_state.last_word = word
                    st.rerun()

            if predator_shown:
                components.html(f"""
                <script>
                (function() {{
                    var predators = new Set({predator_shown});
                    function applyStyles() {{
                        var buttons = window.parent.document.querySelectorAll('[data-testid="stBaseButton-secondary"]');
                        buttons.forEach(function(btn) {{
                            var text = btn.innerText.trim();
                            if (predators.has(text)) {{
                                btn.style.setProperty('background', 'rgba(255,71,87,0.18)', 'important');
                                btn.style.setProperty('border', '1px solid rgba(255,71,87,0.55)', 'important');
                                btn.style.setProperty('color', '#ff6b81', 'important');
                            }}
                        }});
                    }}
                    applyStyles();
                    setTimeout(applyStyles, 100);
                    setTimeout(applyStyles, 400);
                    setTimeout(applyStyles, 900);
                }})();
                </script>
                """, height=0)

            if len(candidates) > 50:
                st.markdown(f'<div style="color:rgba(255,255,255,0.4); text-align:center; font-size:0.85rem; padding:10px;">+ {len(candidates) - 50} kata lainnya tersedia, ketik lebih spesifik</div>', unsafe_allow_html=True)

        else:
            st.markdown('<div style="text-align:center; color:#ff6b81; padding:30px; font-size:1rem;">⚠️ Tidak ada kata tersedia dengan awalan tersebut</div>', unsafe_allow_html=True)

    # Used words
    if st.session_state.used_words:
        st.markdown('<div class="section-title">📝 Kata Terpakai</div>', unsafe_allow_html=True)
        chips_html = "".join([
            f'<span class="used-chip">{"🔥" if w[-1] in rare_letters else "✅"} {w}</span>'
            for w in sorted(st.session_state.used_words)
        ])
        st.markdown(f'<div style="line-height:2.5;">{chips_html}</div>', unsafe_allow_html=True)

# Copyright
st.markdown('<div class="copyright">© 2026 yuambubulabu · Sambung Kata Predator Mode</div>', unsafe_allow_html=True)

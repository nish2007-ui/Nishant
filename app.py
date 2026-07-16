import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Nishant — Profile",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# ---- EDIT THESE VALUES ----
# ============================================================
NAME = "Nishant"

BIO = (
    "I'm a student at IIT Bombay who likes building tech-related things and "
    "learning how they work under the hood. Right now I'm deep into machine "
    "learning — I find it fascinating how a machine can learn to predict "
    "decisions from data instead of being told exactly what to do."
)

# Photo: point this at a raw GitHub URL once you've pushed the image to your repo.
# Example: if your repo is github.com/yourname/portfolio and the file is
# assets/photo.jpg on the main branch, the raw URL is:
# https://raw.githubusercontent.com/yourname/portfolio/main/assets/photo.jpg
PHOTO_URL = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/assets/photo.jpg"

CITY = ""              # TODO: add your city
STUDENT_STATUS = ""    # TODO: e.g. "Undergraduate, IIT Bombay" or "2nd Year B.Tech"

# Skills: (name, confidence out of 100)
SKILLS = [
    ("Python", 85),
    ("C++", 65),
    ("Fusion 360", 60),
    ("Scikit-learn", 75),
    ("PyTorch", 70),
    ("Matplotlib", 75),
    ("Pandas", 80),
]

# Projects: (name, one-line description, tech used, link or "")
PROJECTS = [
    (
        "Diffusion Model on CelebA",
        "Implemented the forward noising process and verified the closed-form Gaussian marginal numerically.",
        "PyTorch, Torchvision, KaggleHub",
        "",  # TODO: add your repo link, e.g. "https://github.com/you/diffusion-celeba"
    ),
    (
        "Face VAE",
        "Built a convolutional variational autoencoder to encode and reconstruct face images into a latent space.",
        "PyTorch, NumPy, Matplotlib",
        "",  # TODO: add link
    ),
    (
        "ML Fundamentals Mini-Projects",
        "A set of course assignments covering regression, classification, and model evaluation from scratch.",
        "Python, Scikit-learn, Pandas",
        "",  # TODO: add link
    ),
]

# Contact links: (label, url)
CONTACT_LINKS = [
    ("GitHub", "https://github.com/YOUR_USERNAME"),
    ("LinkedIn", "https://linkedin.com/in/YOUR_USERNAME"),
    ("Email", "mailto:your.email@example.com"),
]

# ============================================================
# STYLES — blueprint / schematic theme
# ============================================================
st.markdown(
    """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #0A1929;
            --panel: #0F2438;
            --line: rgba(125, 211, 232, 0.14);
            --grid: rgba(125, 211, 232, 0.05);
            --cyan: #7DD3E8;
            --amber: #E8A23D;
            --paper: #EAF2F8;
            --slate: #8FA5B8;
        }

        .stApp {
            background-color: var(--bg);
            background-image:
                linear-gradient(var(--grid) 1px, transparent 1px),
                linear-gradient(90deg, var(--grid) 1px, transparent 1px);
            background-size: 32px 32px;
        }

        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

        h1, h2, h3 { font-family: 'Space Grotesk', sans-serif !important; color: var(--paper) !important; }

        .mono { font-family: 'JetBrains Mono', monospace; }

        /* --- Fig labels for each section --- */
        .fig-label {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.78rem;
            letter-spacing: 0.12em;
            color: var(--cyan);
            text-transform: uppercase;
            margin-bottom: 0.2rem;
        }
        .section-rule {
            border: none;
            border-top: 1px solid var(--line);
            margin: 0.4rem 0 1.6rem 0;
        }

        /* --- Hero --- */
        .hero-name {
            font-size: 3.2rem;
            font-weight: 700;
            line-height: 1.05;
            margin: 0;
        }
        .hero-meta {
            font-family: 'JetBrains Mono', monospace;
            color: var(--slate);
            font-size: 0.92rem;
            margin-top: 0.6rem;
        }
        .hero-meta span.tag {
            border: 1px solid var(--line);
            padding: 3px 10px;
            border-radius: 3px;
            margin-right: 8px;
            display: inline-block;
            margin-top: 6px;
        }
        .bio-box {
            border-left: 2px solid var(--cyan);
            padding-left: 1rem;
            margin-top: 1.2rem;
            color: var(--paper);
            font-size: 1.02rem;
            line-height: 1.65;
        }

        /* --- Photo: specimen-frame treatment --- */
        [data-testid="stImage"] {
            position: relative;
            padding: 10px;
            border: 1px solid var(--cyan);
            background: var(--panel);
        }
        [data-testid="stImage"] img { display: block; width: 100%; }
        .specimen-tag {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.72rem;
            color: var(--cyan);
            letter-spacing: 0.1em;
            margin-top: 0.5rem;
            text-align: center;
        }

        /* --- Skill gauges --- */
        .skill-row { margin-bottom: 1.1rem; }
        .skill-top {
            display: flex;
            justify-content: space-between;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            color: var(--paper);
            margin-bottom: 4px;
        }
        .skill-top .pct { color: var(--amber); }

        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, var(--cyan), var(--amber));
        }
        .stProgress > div > div > div {
            background-color: rgba(143, 165, 184, 0.15);
        }

        /* --- Project cards --- */
        .project-card {
            border: 1px solid var(--line);
            background: var(--panel);
            padding: 1.3rem 1.4rem;
            border-radius: 4px;
            height: 100%;
            margin-bottom: 1rem;
        }
        .project-name {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 600;
            font-size: 1.15rem;
            color: var(--paper);
            margin-bottom: 0.35rem;
        }
        .project-desc {
            color: var(--slate);
            font-size: 0.92rem;
            line-height: 1.5;
            margin-bottom: 0.6rem;
        }
        .project-tech {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.75rem;
            color: var(--cyan);
            margin-bottom: 0.8rem;
        }

        /* --- Buttons (st.link_button) --- */
        .stLinkButton a {
            background-color: transparent !important;
            border: 1px solid var(--cyan) !important;
            color: var(--cyan) !important;
            font-family: 'JetBrains Mono', monospace !important;
            font-size: 0.82rem !important;
            border-radius: 3px !important;
        }
        .stLinkButton a:hover {
            background-color: var(--cyan) !important;
            color: var(--bg) !important;
        }

        footer, #MainMenu { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# HERO SECTION
# ============================================================
col_photo, col_text = st.columns([1, 2], gap="large")

with col_photo:
    st.image(PHOTO_URL, use_container_width=True)
    st.markdown('<div class="specimen-tag">FIG. 00 — SUBJECT</div>', unsafe_allow_html=True)

with col_text:
    st.markdown('<div class="fig-label">PROFILE</div>', unsafe_allow_html=True)
    st.markdown(f'<h1 class="hero-name">{NAME}</h1>', unsafe_allow_html=True)

    city_display = CITY if CITY else "City — add yours"
    status_display = STUDENT_STATUS if STUDENT_STATUS else "Status — add yours"
    st.markdown(
        f"""
        <div class="hero-meta">
            <span class="tag">📍 {city_display}</span>
            <span class="tag">🎓 {status_display}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(f'<div class="bio-box">{BIO}</div>', unsafe_allow_html=True)

st.markdown('<hr class="section-rule">', unsafe_allow_html=True)

# ============================================================
# SKILLS SECTION
# ============================================================
st.markdown('<div class="fig-label">FIG. 01 — SKILLS</div>', unsafe_allow_html=True)
st.markdown('<h2>Technical skills</h2>', unsafe_allow_html=True)

skill_cols = st.columns(2, gap="large")
for i, (skill, level) in enumerate(SKILLS):
    with skill_cols[i % 2]:
        st.markdown(
            f"""
            <div class="skill-row">
                <div class="skill-top">
                    <span>{skill}</span>
                    <span class="pct">{level}%</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.progress(level / 100)

st.markdown('<hr class="section-rule">', unsafe_allow_html=True)

# ============================================================
# PROJECTS SECTION
# ============================================================
st.markdown('<div class="fig-label">FIG. 02 — PROJECTS</div>', unsafe_allow_html=True)
st.markdown('<h2>Selected work</h2>', unsafe_allow_html=True)

proj_cols = st.columns(len(PROJECTS), gap="medium")
for col, (pname, pdesc, ptech, plink) in zip(proj_cols, PROJECTS):
    with col:
        st.markdown(
            f"""
            <div class="project-card">
                <div class="project-name">{pname}</div>
                <div class="project-desc">{pdesc}</div>
                <div class="project-tech">{ptech}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if plink:
            st.link_button("View project ↗", plink, use_container_width=True)
        else:
            st.button("Link coming soon", disabled=True, use_container_width=True, key=f"disabled_{pname}")

st.markdown('<hr class="section-rule">', unsafe_allow_html=True)

# ============================================================
# CONTACT SECTION
# ============================================================
st.markdown('<div class="fig-label">FIG. 03 — CONTACT</div>', unsafe_allow_html=True)
st.markdown('<h2>Get in touch</h2>', unsafe_allow_html=True)

contact_cols = st.columns(len(CONTACT_LINKS))
for col, (label, url) in zip(contact_cols, CONTACT_LINKS):
    with col:
        st.link_button(label, url, use_container_width=True)

st.markdown(
    """
    <div style="margin-top: 2.5rem; text-align: center; color: var(--slate);
                font-family: 'JetBrains Mono', monospace; font-size: 0.75rem;">
        BUILT WITH STREAMLIT · 8-WEEK ML PORTFOLIO
    </div>
    """,
    unsafe_allow_html=True,
)

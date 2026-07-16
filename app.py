import streamlit as st

# ==========================================
# 1. PAGE SETUP & CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="My Portfolio | Space Mission", 
    page_icon="🚀", 
    layout="centered"
)

# ==========================================
# 2. FULL-PAGE INTERACTIVE SPACE BACKGROUND & MOUSE-TRACKING ROCKET
# ==========================================
# This HTML block injects a global space theme and tracks mouse movement to fly the rocket
space_theme_html = """
<style>
/* 1. Target the entire Streamlit main container to make it transparent */
.stApp {
    background-color: #03030c !important; /* Deep dark space background */
    color: #f0f4f8 !important;
}

/* 2. Global background container for moving stars */
#space-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-image: 
        radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 40px),
        radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 30px),
        radial-gradient(white, rgba(255,255,255,.1) 2px, transparent 40px);
    background-size: 550px 550px, 350px 350px, 250px 250px;
    background-position: 0 0, 40px 60px, 130px 270px;
    z-index: -10;
    transition: background-position 0.2s ease-out, background-size 0.2s ease-out;
}

/* 3. The floating rocket at the bottom */
#rocket-ship {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 50px;
    z-index: 100;
    pointer-events: none; /* Allows user to click buttons behind the rocket */
    transition: transform 0.1s ease-out, bottom 0.2s ease-out;
    filter: drop-shadow(0 0 10px rgba(255,255,255,0.2));
}

/* 4. Flame exhaust effect on the rocket */
#rocket-ship::after {
    content: "⚡";
    position: absolute;
    bottom: -25px;
    left: 12px;
    font-size: 20px;
    transform: rotate(180deg);
    opacity: 0;
    transition: opacity 0.2s ease, transform 0.1s linear;
}

/* Active flight class added by JavaScript when mouse moves low */
.rocket-boosting::after {
    opacity: 1 !important;
}

/* Make Streamlit text clean and readable against the dark background */
h1, h2, h3, p, span, li {
    color: #e2e8f0 !important;
    text-shadow: 0 2px 4px rgba(0,0,0,0.5);
}

/* Make Streamlit tabs look great in dark mode */
.stTabs [data-baseweb="tab-list"] {
    background-color: rgba(255, 255, 255, 0.05) !important;
    border-radius: 8px;
    padding: 5px;
}
.stTabs [data-baseweb="tab"] {
    color: #94a3b8 !important;
}
.stTabs [aria-selected="true"] {
    color: #3b82f6 !important;
    font-weight: bold !important;
}
</style>

<!-- Background elements in DOM -->
<div id="space-bg"></div>
<div id="rocket-ship">🚀</div>

<!-- Interactive JavaScript to track cursor and drive background zoom + rocket engine -->
<script>
const spaceBg = document.getElementById('space-bg');
const rocket = document.getElementById('rocket-ship');

document.addEventListener('mousemove', (e) => {
    const screenHeight = window.innerHeight;
    const screenWidth = window.innerWidth;
    const mouseY = e.clientY;
    const mouseX = e.clientX;

    // Calculate how close the mouse is to the bottom of the screen (0 to 1)
    const closenessToBottom = mouseY / screenHeight;
    
    // 1. Move background faster downwards to simulate speed zoom
    const bgOffset = closenessToBottom * 150;
    spaceBg.style.backgroundPosition = `0px ${bgOffset}px, 40px ${bgOffset * 1.5}px, 130px ${bgOffset * 2}px`;
    
    // 2. Adjust rocket tilt slightly towards the cursor on X-axis
    const tilt = ((mouseX / screenWidth) - 0.5) * 30; // Max tilt 15 degrees
    rocket.style.transform = `translateX(-50%) rotate(${tilt}deg)`;

    // 3. If cursor is in the lower 40% of the screen, ignite thrusters!
    if (closenessToBottom > 0.6) {
        rocket.classList.add('rocket-boosting');
        // Push rocket slightly up as it gets closer
        rocket.style.bottom = `${20 + (closenessToBottom * 15)}px`;
    } else {
        rocket.classList.remove('rocket-boosting');
        rocket.style.bottom = '20px';
    }
});
</script>
"""

# Inject the space engine into the app
st.markdown(space_theme_html, unsafe_allow_html=True)


# ==========================================
# 3. HERO HEADER SECTION
# ==========================================
st.title("Hi, I'm a Machine Learning Builder! 👋")
st.caption("Documenting my coding trajectory, core theories, and physical deployments.")

# Create Navigation Tabs to organize your profile neatly
tab1, tab2, tab3 = st.tabs(["👤 About Me & Skills", "🚀 Projects Gallery", "✉️ Get in Touch"])


# ==========================================
# TAB 1: ABOUT ME & INTERACTIVE SKILLS FOLD
# ==========================================
with tab1:
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3242/3242257.png", use_container_width=True)
        
    with col2:
        st.subheader("My Mission Control")
        st.write(
            """
            Over the past 8 weeks, I have transitioned from basic syntax to designing machine learning pipelines.
            I focus heavily on **conceptual frameworks**—like mathematical shortcuts in diffusion models 
            or multi-dimensional tensor processing—so I can architect real solutions.
            """
        )
        
    st.divider()
    
    # INTERACTIVE FOLDING SKILLS SECTION
    st.subheader("🛠️ My Tech Stack (Hover to Reveal!)")
    st.write("Move your mouse over any skill to peel back the cover and reveal the engine underneath!")

    # CSS and HTML for the "Peel/Fold Page" effect on individual skill cards
    skills_peel_html = """
    <style>
    /* Grid layout for the skills */
    .skills-grid {
      display: flex;
      justify-content: center;
      gap: 15px;
      flex-wrap: wrap;
      margin-top: 20px;
      margin-bottom: 30px;
    }

    /* Individual skill card structure */
    .skill-card {
      position: relative;
      width: 160px;
      height: 120px;
      background-color: #111827;
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 4px 10px rgba(0,0,0,0.3);
      cursor: pointer;
    }

    /* Underneath Layer: The Hidden Image */
    .skill-bg-image {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 1;
    }
    
    .skill-bg-image img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    /* Top Layer: The solid blue cover page containing the text */
    .skill-peel-layer {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: linear-gradient(135deg, #2563eb, #1d4ed8);
      color: white !important;
      display: flex;
      justify-content: center;
      align-items: center;
      font-weight: bold;
      font-size: 18px;
      font-family: sans-serif;
      z-index: 2;
      transition: transform 0.6s cubic-bezier(0.25, 1, 0.5, 1), opacity 0.5s ease;
      transform-origin: top left;
    }

    /* Hover effect: Peels up and slides away */
    .skill-card:hover .skill-peel-layer {
      transform: rotate(-15deg) translate(-100%, -100%);
      opacity: 0;
    }
    </style>

    <div class="skills-grid">

      <!-- SKILL 1: PYTHON -->
      <div class="skill-card">
        <div class="skill-bg-image">
          <img src="https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=200&q=80" alt="Python Code">
        </div>
        <div class="skill-peel-layer">
          Python 🐍
        </div>
      </div>

      <!-- SKILL 2: SQL -->
      <div class="skill-card">
        <div class="skill-bg-image">
          <img src="https://images.unsplash.com/photo-1544383835-bda2bc66a55d?auto=format&fit=crop&w=200&q=80" alt="Database">
        </div>
        <div class="skill-peel-layer">
          SQL 🗄️
        </div>
      </div>

      <!-- SKILL 3: PANDAS -->
      <div class="skill-card">
        <div class="skill-bg-image">
          <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=200&q=80" alt="Data Sheet">
        </div>
        <div class="skill-peel-layer">
          Pandas 🐼
        </div>
      </div>

      <!-- SKILL 4: PYTORCH -->
      <div class="skill-card">
        <div class="skill-bg-image">
          <img src="https://images.unsplash.com/photo-1507668077129-56e32842fceb?auto=format&fit=crop&w=200&q=80" alt="Neural Network">
        </div>
        <div class="skill-peel-layer">
          PyTorch 🔥
        </div>
      </div>

    </div>
    """
    st.markdown(skills_peel_html, unsafe_allow_html=True)


# ==========================================
# TAB 2: PROJECTS GALLERY
# ==========================================
with tab2:
    st.header("Active Payloads")
    st.write("Here is the cargo of systems I've put together during this sprint:")
    
    # Project 1 Container
    with st.container(border=True):
        st.subheader("Project 1: Data Analytics Platform")
        st.write(
            "An interactive program analyzing dataset anomalies, using Pandas workflows to clean, "
            "re-index, and transform data for business decisions."
        )
        p1_col1, p1_col2 = st.columns([1, 1])
        with p1_col1:
            st.markdown("[💻 GitHub Repository](https://github.com/)")
        with p1_col2:
            st.markdown("`Pandas` `Seaborn` `Streamlit`")

    st.write("") 
    
    # Project 2 Container
    with st.container(border=True):
        st.subheader("Project 2: Supervised ML Predictor")
        st.write(
            "Constructed a Scikit-Learn regression framework evaluating variable interactions and coefficients "
            "to perform accurate continuous predictions."
        )
        p2_col1, p2_col2 = st.columns([1, 1])
        with p2_col1:
            st.markdown("[💻 GitHub Repository](https://github.com/)")
        with p2_col2:
            st.markdown("`Scikit-Learn` `Feature Engineering`")


# ==========================================
# TAB 3: CONTACT FORM
# ==========================================
with tab3:
    st.header("Transmission Channel")
    st.write("Send an electronic signal to establish contact.")
    
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        
        submit_button = st.form_submit_button("Launch Message")
        
        if submit_button:
            if name and email and message:
                st.success(f"Transmission successful, {name}! Connection coordinates logged.")
            else:
                st.warning("All input registers must be filled before launching!")

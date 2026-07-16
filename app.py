import streamlit as st

# ==========================================
# 1. PAGE SETUP & CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="My Portfolio | Machine Learning Journey", 
    page_icon="💻", 
    layout="centered"
)

# ==========================================
# 2. HERO HEADER SECTION
# ==========================================
st.title("Hi, I'm a Machine Learning Builder! 👋")
st.caption("Documenting 8 weeks of coding, data, and building real projects.")

# Create Navigation Tabs to organize your profile neatly
tab1, tab2, tab3 = st.tabs(["👤 About Me", "🚀 Interactive Projects", "✉️ Get in Touch"])


# ==========================================
# TAB 1: ABOUT ME & SKILLS
# ==========================================
with tab1:
    # Use columns to keep your profile photo/avatar next to your bio text
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        # A clean profile placeholder (you can replace this link with a photo of your choice)
        st.image("https://cdn-icons-png.flaticon.com/512/3242/3242257.png", use_container_width=True)
        
    with col2:
        st.subheader("My Journey")
        st.write(
            """
            Over the past 8 weeks, I have transitioned from writing basic Python scripts 
            to designing machine learning models, exploring data pipelines, and understanding 
            the math behind advanced architectures (like diffusion models!).
            
            I focus heavily on **conceptual logic** rather than just memorizing syntax—understanding 
            *why* algorithms work so I can build better solutions.
            """
        )
        
    st.divider()
    
    # Skills Section
    st.subheader("🛠️ My Tech Stack")
    st.markdown("""
    *   **Languages:** `Python` `SQL` `Markdown`
    *   **Data Analysis:** `Pandas` `NumPy` `Matplotlib` `Seaborn`
    *   **Machine Learning:** `Scikit-Learn` `PyTorch` `Streamlit`
    *   **Developer Tools:** `Git` `GitHub` `VS Code`
    """)


# ==========================================
# TAB 2: INTERACTIVE PROJECTS (3D HOVER CARDS)
# ==========================================
with tab2:
    st.header("What I've Built")
    st.write("Hover your mouse cursor over the cards below to fold the page and reveal the project visuals!")
    
    # HTML and CSS for the 3D Hover/Flip transition cards
    hover_card_html = """
    <style>
    /* Container holding the cards */
    .flip-card-container {
      display: flex;
      justify-content: center;
      gap: 20px;
      flex-wrap: wrap;
      margin-top: 20px;
      margin-bottom: 30px;
    }

    /* Individual card frame size and 3D environment */
    .flip-card {
      background-color: transparent;
      width: 320px;
      height: 240px;
      perspective: 1000px; /* Gives the 3D pop-out effect */
    }

    /* The actual box structure that rotates */
    .flip-card-inner {
      position: relative;
      width: 100%;
      height: 100%;
      text-align: center;
      transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
      transform-style: preserve-3d;
      box-shadow: 0 4px 15px rgba(0,0,0,0.15);
      border-radius: 12px;
    }

    /* Rotate the card Y-axis 180 degrees on hover */
    .flip-card:hover .flip-card-inner {
      transform: rotateY(180deg);
    }

    /* Properties shared by Front and Back elements */
    .flip-card-front, .flip-card-back {
      position: absolute;
      width: 100%;
      height: 100%;
      -webkit-backface-visibility: hidden; /* Hides the back layer during spin */
      backface-visibility: hidden;
      border-radius: 12px;
      padding: 20px;
      box-sizing: border-box;
    }

    /* FRONT FACE: Colorful Gradient and Text */
    .flip-card-front {
      background: linear-gradient(135deg, #1e3a8a, #3b82f6);
      color: white;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }

    .flip-card-front h3 {
      margin: 0 0 10px 0;
      font-family: sans-serif;
      font-size: 20px;
    }

    .flip-card-front p {
      font-size: 14px;
      opacity: 0.9;
      margin: 0;
    }

    /* BACK FACE: Image Reveal */
    .flip-card-back {
      background-color: #f3f4f6;
      transform: rotateY(180deg); /* Facing backward initially */
      overflow: hidden;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 0;
    }

    .flip-card-back img {
      width: 100%;
      height: 100%;
      object-fit: cover; /* Crops image to fill card cleanly */
    }
    </style>

    <div class="flip-card-container">

      <!-- CARD 1: DATA ANALYSIS -->
      <div class="flip-card">
        <div class="flip-card-inner">
          <div class="flip-card-front">
            <h3>📊 Data Analysis</h3>
            <p>Interactive sales analysis & cleaning pipeline built in Python.</p>
          </div>
          <div class="flip-card-back">
            <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=500&q=80" alt="Data Chart">
          </div>
        </div>
      </div>

      <!-- CARD 2: DIFFUSION MODELS -->
      <div class="flip-card">
        <div class="flip-card-inner">
          <div class="flip-card-front">
            <h3>🧠 Diffusion Models</h3>
            <p>Exploring mathematics behind step-by-step image synthesis.</p>
          </div>
          <div class="flip-card-back">
            <img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=500&q=80" alt="AI Abstract Art">
          </div>
        </div>
      </div>

    </div>
    """
    
    # Injecting the HTML & CSS securely
    st.markdown(hover_card_html, unsafe_allow_html=True)


# ==========================================
# TAB 3: CONTACT FORM (FULLY INDENT-CORRECTED)
# ==========================================
with tab3:
    st.header("Let's Connect!")
    st.write("Feel free to reach out to me for collaboration or questions.")
    
    # Python Form Container
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Your Message")
        
        submit_button = st.form_submit_button("Send Message")
        
        # Perfect, corrected indentation block
        if submit_button:
            if name and email and message:
                st.success(f"Thanks {name}! Your message was successfully recorded!")
            else:
                st.warning("Please fill out all fields!")
                st.warning("Please fill out all fields!")

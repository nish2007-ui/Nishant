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
tab1, tab2, tab3 = st.tabs(["👤 About Me & Skills", "🚀 Projects Gallery", "✉️ Get in Touch"])


# ==========================================
# TAB 1: ABOUT ME & INTERACTIVE SKILLS FOLD
# ==========================================
with tab1:
    # Use columns to keep your profile photo/avatar next to your bio text
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
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
    
    # INTERACTIVE FOLDING SKILLS SECTION
    st.subheader("🛠️ My Tech Stack (Hover to Reveal!)")
    st.write("Move your mouse over any skill to peel back the solid color and reveal the tool's visual representation!")

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
      background-color: #f3f4f6;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 4px 6px rgba(0,0,0,0.05);
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

    /* Top Layer: The solid color page containing the text */
    .skill-peel-layer {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: linear-gradient(135deg, #2563eb, #1d4ed8); /* Deep tech blue */
      color: white;
      display: flex;
      justify-content: center;
      align-items: center;
      font-weight: bold;
      font-size: 18px;
      font-family: sans-serif;
      letter-spacing: 0.5px;
      z-index: 2;
      
      /* Smooth slide and fold transition */
      transition: transform 0.6s cubic-bezier(0.25, 1, 0.5, 1), opacity 0.5s ease;
      transform-origin: top left; /* Folds upwards and leftwards */
    }

    /* The actual hover effect: Peels up and slides away */
    .skill-card:hover .skill-peel-layer {
      transform: rotate(-15deg) translate(-100%, -100%);
      opacity: 0;
    }

    /* Little corner fold shadow effect on hover */
    .skill-card::after {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 0;
      height: 0;
      background: rgba(255, 255, 255, 0.4);
      z-index: 3;
      transition: width 0.4s, height 0.4s;
    }
    
    .skill-card:hover::after {
      width: 30px;
      height: 30px;
      box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
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
          <img src="https://images.unsplash.com/photo-1544383835-bda2bc66a55d?auto=format&fit=crop&w=200&q=80" alt="Database Storage">
        </div>
        <div class="skill-peel-layer">
          SQL 🗄️
        </div>
      </div>

      <!-- SKILL 3: PANDAS -->
      <div class="skill-card">
        <div class="skill-bg-image">
          <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=200&q=80" alt="Data Sheet Dashboard">
        </div>
        <div class="skill-peel-layer">
          Pandas 🐼
        </div>
      </div>

      <!-- SKILL 4: PYTORCH -->
      <div class="skill-card">
        <div class="skill-bg-image">
          <img src="https://images.unsplash.com/photo-1507668077129-56e32842fceb?auto=format&fit=crop&w=200&q=80" alt="Artificial Neural Network concept">
        </div>
        <div class="skill-peel-layer">
          PyTorch 🔥
        </div>
      </div>

    </div>
    """
    
    # Injecting the folding skills into the layout
    st.markdown(skills_peel_html, unsafe_allow_html=True)


# ==========================================
# TAB 2: PROJECTS GALLERY
# ==========================================
with tab2:
    st.header("Projects Showroom")
    st.write("A deep dive into some of the primary projects I constructed from scratch:")
    
    # Project Card 1
    with st.container(border=True):
        st.subheader("Project 1: Data Analysis Dashboard")
        st.write(
            "An interactive dashboard that cleans and analyzes large datasets, "
            "showing key business metrics using Pandas and Seaborn."
        )
        p1_col1, p1_col2 = st.columns([1, 1])
        with p1_col1:
            st.markdown("[💻 GitHub Repository](https://github.com/)")
        with p1_col2:
            st.markdown("`Pandas` `Seaborn` `Streamlit`")

    st.write("") # Spacer
    
    # Project Card 2
    with st.container(border=True):
        st.subheader("Project 2: Machine Learning Predictor")
        st.write(
            "Built a Scikit-Learn regression model to predict housing prices. "
            "Analyzed feature correlation and optimized hyperparameters."
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
    st.header("Let's Connect!")
    st.write("Feel free to reach out to me for collaboration or questions.")
    
    # Form Container
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Your Message")
        
        submit_button = st.form_submit_button("Send Message")
        
        if submit_button:
            if name and email and message:
                st.success(f"Thanks {name}! Your message was successfully recorded!")
            else:
                st.warning("Please fill out all fields!")

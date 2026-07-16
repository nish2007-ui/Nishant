import streamlit as st

# 1. Page Configuration (Sets the browser tab title and icon)
st.set_page_config(
    page_title="My Portfolio | Machine Learning Journey", 
    page_icon="💻", 
    layout="centered"
)

# 2. Top Header (Minimalist & Clean)
st.title("Hi, I'm a Machine Learning Builder! 👋")
st.caption("Documenting 8 weeks of coding, data, and building real projects.")

# 3. Create Navigation Tabs to make the site feel like a real web app
tab1, tab2, tab3 = st.tabs(["👤 About Me", "🚀 Projects Gallery", "✉️ Get in Touch"])

# ==================== TAB 1: ABOUT ME ====================
with tab1:
    # Use columns to keep your photo/avatar next to your bio
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        # A clean profile placeholder (or use a URL of a real photo)
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
    
    # Skills Section using colored markdown "badges"
    st.subheader("🛠️ My Tech Stack")
    
    st.markdown("""
    *   **Languages:** `Python` `SQL` `Markdown`
    *   **Data Analysis:** `Pandas` `NumPy` `Matplotlib` `Seaborn`
    *   **Machine Learning:** `Scikit-Learn` `PyTorch` `Streamlit`
    *   **Developer Tools:** `Git` `GitHub` `VS Code` `Jupyter`
    """)

# ==================== TAB 2: PROJECTS GALLERY ====================
with tab2:
    st.header("What I've Built")
    st.write("Here are some of the key projects I've developed during my 8-week sprint:")
    
    # Project 1 (Enclosed in a clean card container)
    with st.container(border=True):
        st.subheader("Project 1: Data Analysis Dashboard")
        st.write(
            "An interactive dashboard that cleans and analyzes large datasets, "
            "showing key business metrics using Pandas and Seaborn."
        )
        # Using columns inside the card to keep it tight
        p1_col1, p1_col2 = st.columns([1, 1])
        with p1_col1:
            st.markdown("[💻 GitHub Repository](https://github.com/)")
        with p1_col2:
            st.markdown("`Pandas` `Seaborn` `Streamlit`")

    st.write("") # Add spacing
    
    # Project 2 (Enclosed in a clean card container)
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

# ==================== TAB 3: CONTACT FORM ====================
with tab3:
    st.header("Let's Connect!")
    st.write("Feel free to reach out to me for collaboration or questions.")
    
    # A clean, centered contact form
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Your Message")
        
        submit_button = st.form_submit_button("Send Message")
        
        if submit_button:
            if name and email and message:
                st.success(f"Thanks {name}! Your mock message has been sent successfully.")
            else:
                st.warning("Please fill out all fields!")

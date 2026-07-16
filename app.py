import streamlit as st

st.set_page_config(page_title="Interactive Portfolio", layout="centered")

st.title("My Interactive Projects")
st.write("Hover your mouse over the cards below to fold the page and reveal the project visuals!")

# 1. Define the HTML and CSS for the folding hover card
hover_card_html = """
<style>
/* Container to give 3D perspective to the flip effect */
.flip-card-container {
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
  margin-top: 30px;
}

/* The individual card frame */
.flip-card {
  background-color: transparent;
  width: 300px;
  height: 250px;
  perspective: 1000px; /* Essential for 3D depth */
}

/* The inner element that actually rotates */
.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
  transform-style: preserve-3d;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  border-radius: 12px;
}

/* TRIGGER THE FOLD/FLIP ON HOVER */
.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

/* Common properties for both front and back faces */
.flip-card-front, .flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden; /* Hide the back of elements when turned */
  backface-visibility: hidden;
  border-radius: 12px;
  padding: 20px;
  box-sizing: border-box;
}

/* FRONT FACE (Text description) */
.flip-card-front {
  background: linear-gradient(135deg, #1e3a8a, #3b82f6); /* Deep blue gradient */
  color: white;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.flip-card-front h3 {
  margin: 0 0 10px 0;
  font-family: sans-serif;
}

.flip-card-front p {
  font-size: 14px;
  opacity: 0.9;
}

/* BACK FACE (Image Reveal) */
.flip-card-back {
  background-color: #f3f4f6;
  transform: rotateY(180deg); /* Pre-rotate back side so it aligns correctly on flip */
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0;
}

.flip-card-back img {
  width: 100%;
  height: 100%;
  object-fit: cover; /* Crop and scale image to fit card perfectly */
}
</style>

<div class="flip-card-container">

  <!-- CARD 1 -->
  <div class="flip-card">
    <div class="flip-card-inner">
      <!-- Front (What you see first) -->
      <div class="flip-card-front">
        <h3>📊 Data Analysis</h3>
        <p>Interactive sales analysis & cleaning pipeline built in Python.</p>
      </div>
      <!-- Back (What appears on hover) -->
      <div class="flip-card-back">
        <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=500&q=80" alt="Data Chart">
      </div>
    </div>
  </div>

  <!-- CARD 2 -->
  <div class="flip-card">
    <div class="flip-card-inner">
      <!-- Front -->
      <div class="flip-card-front">
        <h3>🧠 Diffusion Models</h3>
        <p>Exploring mathematics behind step-by-step image synthesis.</p>
      </div>
      <!-- Back -->
      <div class="flip-card-back">
        <img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=500&q=80" alt="AI abstract art">
      </div>
    </div>
  </div>

</div>
"""

# 2. Inject the code into Streamlit
st.markdown(hover_card_html, unsafe_allow_html=True)
            else:
                st.warning("Please fill out all fields!")

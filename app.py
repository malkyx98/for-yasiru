import streamlit as st
import time

# Set page config for a vibrant feel
st.set_page_config(page_title="Our Forever Colors", page_icon="🌈")

# Advanced CSS for a Rainbow Gradient and Glowing Buttons
st.markdown("""
    <style>
    /* Animated Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: white;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Styling the Main Card */
    .main-card {
        background-color: rgba(255, 255, 255, 0.2);
        padding: 30px;
        border-radius: 25px;
        backdrop-filter: blur(10px);
        border: 2px solid rgba(255, 255, 255, 0.3);
    }

    /* Heading Style */
    h1 {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: white;
        text-shadow: 3px 3px #ff4b4b;
        text-align: center;
    }

    /* Glowing Button */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border: none;
        box-shadow: 0 0 15px rgba(255, 75, 75, 0.6);
        transition: 0.3s;
    }

    .stButton>button:hover {
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.8);
        transform: scale(1.02);
    }
    
    /* Text Color Fixes */
    .stMarkdown, p, span {
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Wrap everything in a "Glass" card for better readability
with st.container():
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    
    st.title("Yasiru, A Message from My Heart")

    st.write("""
    I know things have been difficult lately, and the 'weather' between us has been a bit stormy. 
    I made this because I want to remind you that no matter the situation, **my commitment to you is permanent.**
    """)

    # Interactive Memory Lane with vibrant metrics
    st.markdown("### 📊 Our Forever Stats")
    col1, col2 = st.columns(2)
    col1.metric("Days Together", "∞", delta="Always")
    col2.metric("Love Level", "100%", delta="Rising")

    st.write("---")

    # The Apology/Peace Offering
    st.subheader("My Promise to You")
    st.info("I value us more than any argument. I am here, I am listening, and I am not going anywhere.")

    if st.button("Click for a Burst of Love"):
        st.balloons()
        st.snow()
        st.success("I love you. More than anything.")
        st.write("I'm waiting for you with open arms.")

    st.markdown('</div>', unsafe_allow_html=True)

# A permanent 'Contract'
st.divider()
st.caption("Version 1.0 - The 'Permanent Love' Edition")
import streamlit as st
import time

st.set_page_config(
    page_title="Diva Turns 22 🕯️",
    page_icon="💸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,600;1,400&family=Great+Vibes&display=swap');
    
    #MainMenu, footer, header {visibility: hidden;}
    
    .stApp {
        background: linear-gradient(180deg, #1a0f0a 0%, #2d1b12 50%, #1a0f0a 100%);
    }
    
    /* Golden particles */
    .gold-dust {
        position: fixed;
        width: 3px;
        height: 3px;
        background: radial-gradient(circle, #ffd700, transparent);
        border-radius: 50%;
        pointer-events: none;
        animation: rise 10s infinite;
        opacity: 0;
    }
    
    @keyframes rise {
        0% { transform: translateY(100vh); opacity: 0; }
        20% { opacity: 0.8; }
        80% { opacity: 0.8; }
        100% { transform: translateY(-10vh); opacity: 0; }
    }
    
    /* Main Title - Elegant Script */
    .diva-title {
        font-family: 'Great Vibes', cursive;
        font-size: 4.5rem;
        text-align: center;
        color: #f4e4c1;
        text-shadow: 0 0 30px rgba(255,215,0,0.5), 0 4px 10px rgba(0,0,0,0.8);
        margin: 2rem 0 0.5rem;
        letter-spacing: 3px;
    }
    
    .subtitle {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.3rem;
        text-align: center;
        color: #d4af37;
        letter-spacing: 4px;
        margin-bottom: 3rem;
        font-style: italic;
    }
    
    /* Candlelit Cake Scene */
    .cake-scene {
        width: 320px;
        height: 380px;
        margin: 2rem auto;
        position: relative;
        background: radial-gradient(ellipse at center, rgba(255,215,0,0.1) 0%, transparent 70%);
        border-radius: 50%;
    }
    
    /* Elegant Cake - Cream/Ivory */
    .cake-layer {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        border-radius: 8px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    .layer-bottom {
        width: 260px;
        height: 85px;
        bottom: 20px;
        background: linear-gradient(135deg, #f5f5dc 0%, #e6d5b8 100%);
        border: 1px solid #d4af37;
    }
    
    .layer-middle {
        width: 190px;
        height: 70px;
        bottom: 105px;
        background: linear-gradient(135deg, #fff8dc 0%, #f0e6d2 100%);
        border: 1px solid #d4af37;
    }
    
    .layer-top {
        width: 130px;
        height: 55px;
        bottom: 175px;
        background: linear-gradient(135deg, #faf0e6 0%, #e8dcc4 100%);
        border: 1px solid #d4af37;
    }
    
    /* Frosting */
    .frosting {
        position: absolute;
        top: -5px;
        left: 0;
        right: 0;
        height: 12px;
        background: linear-gradient(90deg, #fff, #f4e4c1, #fff);
        border-radius: 50px;
        opacity: 0.9;
    }
    
    /* Multiple Candles */
    .candle-group {
        position: absolute;
        bottom: 230px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        gap: 8px;
    }
    
    .candle {
        width: 8px;
        height: 40px;
        background: linear-gradient(90deg, #f4e4c1, #fff, #f4e4c1);
        border-radius: 2px;
        position: relative;
    }
    
    .flame {
        position: absolute;
        top: -12px;
        left: 50%;
        transform: translateX(-50%);
        width: 8px;
        height: 14px;
        background: radial-gradient(ellipse at bottom, #fff 0%, #ffd700 40%, #ff8c00 80%, transparent);
        border-radius: 50% 50% 30% 30%;
        animation: flicker 0.4s infinite alternate;
        box-shadow: 0 0 10px rgba(255,215,0,0.8);
    }
    
    @keyframes flicker {
        0% { transform: translateX(-50%) scale(1) rotate(-2deg); }
        100% { transform: translateX(-50%) scale(1.1) rotate(2deg); }
    }
    
    /* Age */
    .age-number {
        position: absolute;
        bottom: 120px;
        left: 50%;
        transform: translateX(-50%);
        font-family: 'Great Vibes', cursive;
        font-size: 3.5rem;
        color: #d4af37;
        text-shadow: 0 0 20px rgba(212,175,55,0.8);
    }
    
    /* Message Cards - Dark Elegant */
    .message-card {
        background: rgba(30,20,15,0.8);
        border: 1px solid #d4af37;
        border-radius: 15px;
        padding: 2rem;
        margin: 1.5rem 0;
        color: #f4e4c1;
        font-family: 'Cormorant Garamond', serif;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    .card-title {
        font-family: 'Great Vibes', cursive;
        font-size: 1.8rem;
        color: #ffd700;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #d4af37, #b8956a) !important;
        color: #1a0f0a !important;
        border: none !important;
        border-radius: 30px !important;
        padding: 0.8rem 2rem !important;
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        width: 100%;
        box-shadow: 0 5px 20px rgba(212,175,55,0.3) !important;
    }
    
    /* Secret Vault - Same colors */
    .vault-box {
        background: rgba(20,15,10,0.9);
        border: 2px solid #d4af37;
        border-radius: 20px;
        padding: 2.5rem;
        margin: 2rem 0;
        text-align: center;
        box-shadow: 0 0 40px rgba(212,175,55,0.2);
    }
    
    .vault-title {
        font-family: 'Great Vibes', cursive;
        font-size: 2.2rem;
        color: #ffd700;
        margin-bottom: 1.5rem;
    }
    
    .stTextInput > div > div > input {
        background: rgba(0,0,0,0.5) !important;
        border: 1px solid #d4af37 !important;
        border-radius: 30px !important;
        color: #f4e4c1 !important;
        text-align: center !important;
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 1.1rem !important;
    }
    
    /* Lizard Gift Box */
    .gift-scene {
        background: rgba(40,30,20,0.8);
        border: 2px dashed #d4af37;
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        text-align: center;
    }
    
    .lizard-emoji {
        font-size: 4rem;
        animation: crawl 3s infinite;
        display: inline-block;
    }
    
    @keyframes crawl {
        0%, 100% { transform: translateX(-10px) rotate(-5deg); }
        50% { transform: translateX(10px) rotate(5deg); }
    }
</style>

<!-- Golden Dust Particles -->
<div class="gold-dust" style="left: 15%; animation-delay: 0s;"></div>
<div class="gold-dust" style="left: 35%; animation-delay: 2s;"></div>
<div class="gold-dust" style="left: 55%; animation-delay: 4s;"></div>
<div class="gold-dust" style="left: 75%; animation-delay: 1s;"></div>
<div class="gold-dust" style="left: 90%; animation-delay: 3s;"></div>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="diva-title">Diva Turns 22</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">✨ Sanah • The Original Diva • Est. 2004 ✨</p>', unsafe_allow_html=True)

# Cake Scene
st.markdown("""
<div class="cake-scene">
    <div class="cake-layer layer-bottom">
        <div class="frosting"></div>
    </div>
    <div class="cake-layer layer-middle">
        <div class="frosting"></div>
    </div>
    <div class="cake-layer layer-top">
        <div class="frosting"></div>
    </div>
    <div class="age-number">22</div>
    <div class="candle-group">
        <div class="candle"><div class="flame"></div></div>
        <div class="candle"><div class="flame"></div></div>
        <div class="candle"><div class="flame"></div></div>
        <div class="candle"><div class="flame"></div></div>
        <div class="candle"><div class="flame"></div></div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# About Sanah Section
st.markdown('<h2 style="text-align: center; font-family: Great Vibes; color: #ffd700; font-size: 2.5rem;">About The Diva</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="message-card">
    <h3 class="card-title">👑 Sanah 101</h3>
    <p style="font-size: 1.1rem; line-height: 1.8;">
        Name: <b>Sanah</b> (not Sana, not Sanaa, not "hey you")<br>
        Age: <b>22</b> (finally legal to... rent a car without extra fees)<br>
        Occupation: <b>Future Lawyer</b> (currently professional overthinker)<br>
    </p>
</div>
""", unsafe_allow_html=True)

# Comedy Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("🦎 The Lizard Story"):
        st.markdown("""
        <div class="message-card">
            <h3 class="card-title">The Legend of Sanah & The Lizard</h3>
            <p style="font-size: 1.1rem; line-height: 1.8;">
                Our diva once found a lizard in her room and screamed so loud 
                that the neighbors thought someone was being murdered. 
                <br><br>
                She then stood on a chair for 3 hours waiting for "someone brave" 
                (aka anyone else) to remove it. 
                <br><br>
                <b>The lizard now pays rent and lives there permanently.</b> 
                They've reached an understanding. 🦎☕
            </p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    if st.button("⚖️ Law School Diaries"):
        st.markdown("""
        <div class="message-card">
            <h3 class="card-title">Exhibit A: Sanah in Court</h3>
            <p style="font-size: 1.1rem; line-height: 1.8;">
                Survives 4 hours of Contracts lecture, 
                memorizes 50 case names, 
                argues about everything... 
                <br><br>
                ...but still can't decide what to order for dinner. 
                <br><br>
                <b>Objection: Her Honor is hungry.</b> ⚖️🍕
            </p>
        </div>
        """, unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    if st.button("📱 Instagram vs Reality"):
        st.markdown("""
        <div class="message-card">
            <h3 class="card-title">The Aesthetic Lie</h3>
            <p style="font-size: 1.1rem; line-height: 1.8;">
                Instagram: Golden hour, perfect angles, "casual" coffee shot<br>
                Reality: Took 47 photos, spilled coffee on notes, 
                screamed at the sun for being too bright.
                <br><br>
                <b>Still iconic though.</b> 📸✨
            </p>
        </div>
        """, unsafe_allow_html=True)

with col4:
    if st.button("🎁 Special Delivery"):
        st.markdown("""
        <div class="gift-scene">
            <h3 style="font-family: Great Vibes; color: #ffd700; font-size: 1.8rem;">Your Gift Has Arrived</h3>
            <br>
            <span class="lizard-emoji">🦎</span>
            <br><br>
            <p style="color: #f4e4c1; font-size: 1.1rem;">
                <b>A lizard.</b><br>
                Because every diva needs an emotional support reptile.<br>
                <i>(He's trained in legal research and emotional damage)</i>
            </p>
            <br>
            <p style="color: #d4af37; font-size: 0.9rem;">
                *No lizards were harmed. He volunteered for this position.*
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Secret Vault
st.markdown("""
<div class="vault-box">
    <h2 class="vault-title">🔐 The Secret Vault</h2>
    <p style="color: #f4e4c1; font-family: Cormorant Garamond;">Enter the sacred initials...</p>
</div>
""", unsafe_allow_html=True)

password = st.text_input("Vault Code:", type="password", placeholder="Two letters, one legend...", label_visibility="collapsed")

if password:
    if password == "G.I":
        st.success("🔓 Access Granted")
        time.sleep(1)
        
        st.markdown("""
        <div class="vault-box" style="border-color: #ffd700; box-shadow: 0 0 50px rgba(255,215,0,0.3);">
            <h2 style="font-family: Great Vibes; color: #ffd700; font-size: 2rem;">
                Welcome to the secret vault, nasty girl! 🔓🤫🔥
            </h2>
            <br>
            <p style="font-family: Cormorant Garamond; font-size: 1.2rem; color: #f4e4c1; line-height: 2; text-align: left;">
                Since you unlocked this, here's our ultimate truth: 
                We might look innocent on the outside, but our taste in men is purely refined... 
                <b style="color: #ffd700;">No young boys allowed in our world, strictly hot, rich, and old men with top-tier daddy energy!</b> 
                👴🏼💸✨ 
                <br><br>
                Stay nasty, stay iconic, and let's keep being absolute legends together. 
                <b style="color: #ffd700;">Happy Birthday to my favorite partner in crime!</b> 
                👑🎂💖
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.balloons()
        time.sleep(0.5)
        st.snow()
        
    else:
        st.error("❌ Wrong code. The lizard is disappointed in you.")

st.markdown("""
<p style="text-align: center; color: rgba(212,175,55,0.6); margin-top: 3rem; font-family: Cormorant Garamond; letter-spacing: 3px;">
    SANAH • THE DIVA • 22 & BEYOND • G.I
</p>
""", unsafe_allow_html=True)

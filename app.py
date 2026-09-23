import streamlit as st
import time

st.set_page_config(
    page_title="Diva Turns 22 🕯️",
    page_icon="🥂",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS كامل
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,600;1,400&family=Great+Vibes&display=swap');
    
    #MainMenu, footer, header {visibility: hidden;}
    
    .stApp {
        background: linear-gradient(180deg, #1a0f0a 0%, #2d1b12 50%, #1a0f0a 100%);
    }
    
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
    
    .cake-scene {
        width: 320px;
        height: 380px;
        margin: 2rem auto;
        position: relative;
        background: radial-gradient(ellipse at center, rgba(255,215,0,0.1) 0%, transparent 70%);
        border-radius: 50%;
    }
    
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
        transition: all 0.5s;
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
        transition: opacity 0.5s, height 0.5s;
    }
    
    @keyframes flicker {
        0% { transform: translateX(-50%) scale(1) rotate(-2deg); }
        100% { transform: translateX(-50%) scale(1.1) rotate(2deg); }
    }
    
    /* Class for extinguished candles */
    .candle.extinguished {
        background: linear-gradient(90deg, #555, #777, #555);
    }
    
    .candle.extinguished .flame {
        opacity: 0;
        height: 0;
        animation: none;
    }
    
    .smoke {
        position: absolute;
        top: -20px;
        left: 50%;
        transform: translateX(-50%);
        width: 4px;
        height: 20px;
        background: linear-gradient(to top, rgba(200,200,200,0.5), transparent);
        border-radius: 50%;
        animation: smoke-rise 2s ease-out forwards;
        opacity: 0;
    }
    
    @keyframes smoke-rise {
        0% { opacity: 0.8; transform: translateX(-50%) translateY(0) scale(1); }
        100% { opacity: 0; transform: translateX(-50%) translateY(-30px) scale(2); }
    }
    
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
    
    .star {
        position: fixed;
        width: 4px;
        height: 4px;
        background: #ffd700;
        border-radius: 50%;
        pointer-events: none;
        animation: star-fall 3s linear infinite;
        box-shadow: 0 0 10px #ffd700;
        z-index: 9999;
    }
    
    @keyframes star-fall {
        0% { transform: translateY(-10vh) translateX(0); opacity: 1; }
        100% { transform: translateY(100vh) translateX(50px); opacity: 0; }
    }
    
    .falling-lizard {
        position: fixed;
        font-size: 2.5rem;
        pointer-events: none;
        animation: lizard-fall 3s linear infinite;
        z-index: 9999;
        top: -50px;
    }
    
    @keyframes lizard-fall {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(110vh) rotate(360deg); opacity: 0; }
    }
    
    .vault-image {
        border-radius: 15px;
        border: 2px solid #ffd700;
        margin: 1rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        max-width: 100%;
    }
    
    .image-container {
        display: flex;
        justify-content: center;
        gap: 1rem;
        flex-wrap: wrap;
        margin: 2rem 0;
    }
    
    .countdown-number {
        font-family: 'Great Vibes', cursive;
        font-size: 4rem;
        color: #ffd700;
        text-align: center;
        text-shadow: 0 0 30px rgba(255,215,0,0.8);
    }
    
    .blow-text {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.3rem;
        color: #d4af37;
        text-align: center;
        margin: 1rem 0;
        font-style: italic;
    }
    
    .wish-text {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.2rem;
        color: #d4af37;
        text-align: center;
        margin: 1rem 0;
        font-style: italic;
        opacity: 0;
        transition: opacity 1s;
    }
    
    .wish-text.show {
        opacity: 1;
    }
</style>

<div class="gold-dust" style="left: 15%; animation-delay: 0s;"></div>
<div class="gold-dust" style="left: 35%; animation-delay: 2s;"></div>
<div class="gold-dust" style="left: 55%; animation-delay: 4s;"></div>
<div class="gold-dust" style="left: 75%; animation-delay: 1s;"></div>
<div class="gold-dust" style="left: 90%; animation-delay: 3s;"></div>
""", unsafe_allow_html=True)

# Initialize session state
if 'candles_state' not in st.session_state:
    st.session_state.candles_state = 'lit'  # lit, counting, out

st.markdown('<h1 class="diva-title">Diva Turns 22</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">✨ Sanah • The Original Diva • Est. 2004 ✨</p>', unsafe_allow_html=True)

# SINGLE CAKE - changes based on state
if st.session_state.candles_state == 'lit':
    # Cake with lit candles
    st.markdown("""
    <div class="cake-scene" id="cake-scene">
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
    
    # Button to start countdown
    if st.button("🕯️ Blow The Candles", use_container_width=True):
        st.session_state.candles_state = 'counting'
        st.rerun()

elif st.session_state.candles_state == 'counting':
    # Show countdown text
    st.markdown('<p class="blow-text">Blowing the candles...</p>', unsafe_allow_html=True)
    
    # Countdown placeholder
    countdown_placeholder = st.empty()
    
    # Show cake with candles still lit during countdown
    st.markdown("""
    <div class="cake-scene" id="cake-scene">
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
    
    # Countdown 3, 2, 1
    for i in range(3, 0, -1):
        countdown_placeholder.markdown(f'<h1 class="countdown-number">{i}</h1>', unsafe_allow_html=True)
        time.sleep(1)
    
    countdown_placeholder.empty()
    st.session_state.candles_state = 'out'
    st.rerun()

else:  # candles_state == 'out'
    # Cake with extinguished candles and smoke
    st.markdown("""
    <div class="cake-scene" id="cake-scene">
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
            <div class="candle extinguished"><div class="smoke" style="animation-delay: 0s;"></div></div>
            <div class="candle extinguished"><div class="smoke" style="animation-delay: 0.2s;"></div></div>
            <div class="candle extinguished"><div class="smoke" style="animation-delay: 0.4s;"></div></div>
            <div class="candle extinguished"><div class="smoke" style="animation-delay: 0.6s;"></div></div>
            <div class="candle extinguished"><div class="smoke" style="animation-delay: 0.8s;"></div></div>
        </div>
    </div>
    <p class="wish-text show">✨ Make a wish... ✨</p>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown('<h2 style="text-align: center; font-family: Great Vibes; color: #ffd700; font-size: 2.5rem;">About The Diva</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="message-card">
    <h3 class="card-title">👑 Sanah 101</h3>
    <p style="font-size: 1.1rem; line-height: 1.8;">
        Name: <b>Sanah</b> (not Sana, not Sanaa, not "hey you")<br>
        Age: <b>22</b> (finally ready to... 💍😅🏳️)<br>
        Occupation: <b>Future Lawyer</b> (currently professional overthinker)<br>
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("💎 Why You're My Unbiological Sister"):
        st.markdown("""
        <div class="star" style="left: 10%; animation-delay: 0s;"></div>
        <div class="star" style="left: 30%; animation-delay: 0.5s;"></div>
        <div class="star" style="left: 50%; animation-delay: 1s;"></div>
        <div class="star" style="left: 70%; animation-delay: 1.5s;"></div>
        <div class="star" style="left: 90%; animation-delay: 2s;"></div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="message-card">
            <h3 class="card-title">The Language of Us</h3>
            <p style="font-size: 1.1rem; line-height: 1.8;">
                Honestly, I swear talking to you is my main source of dopamine. 
                I love how I can just be 100% myself around you—no filter, no pressure, and zero judgment. 
                We can text whenever, talk about the most random things, gossip endlessly, 
                and just be completely weird together. 
                <br><br>
                Our chat is literally my safe space and my favorite part of the day. 
                Also, big shoutout to your parents for raising such a masterpiece. 
                Honestly, they deserve an award for bringing you into this world. 
                <br><br>
                <b>You're truly one of a kind. 💎</b>
            </p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    if st.button("🎁 Special Gift From Zeinah"):
        # Lizard rain
        lizard_html = ""
        for i in range(15):
            left = 5 + (i * 6)
            delay = i * 0.2
            lizard_html += f'<div class="falling-lizard" style="left: {left}%; animation-delay: {delay}s;">🦎</div>'
        
        st.markdown(lizard_html, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="gift-scene">
            <h3 style="font-family: Great Vibes; color: #ffd700; font-size: 1.8rem;">A Gift From Me To You</h3>
            <br>
            <span class="lizard-emoji">🦎</span>
            <br><br>
            <p style="color: #f4e4c1; font-size: 1.1rem; text-align: left; line-height: 1.8;">
                Congratulations, your personal emotional support Gecko has officially arrived—a quiet, 
                cold-blooded chaos entity with zero morals who spends his nights plotting society's downfall, 
                judging your toxic decisions from the highest corner of the wall, and serving as a tactical 
                biological weapon ready to inflict pure psychological damage on anyone who dares to annoy you... 
                <br><br>
                Side effect: he feeds on the fear of your enemies, stares directly into your soul at 3:00 AM, 
                and comes with absolutely no refunds if he accidentally drops on your face while you're sleeping. 
                <br><br>
                <i>No lizards were harmed in the making of this gift. He volunteered for this position.</i>
            </p>
        </div>
        """, unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    if st.button("☕ Law School Survival"):
        st.markdown("""
        <div class="star" style="left: 15%; animation-delay: 0.2s;"></div>
        <div class="star" style="left: 35%; animation-delay: 0.7s;"></div>
        <div class="star" style="left: 55%; animation-delay: 1.2s;"></div>
        <div class="star" style="left: 75%; animation-delay: 1.7s;"></div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="message-card">
            <h3 class="card-title">Caffeine & Chaos</h3>
            <p style="font-size: 1.1rem; line-height: 1.8;">
                Months of law school chaos summarized in endless all-nighters. 
                We don't read books on time, we telepathically download months of missed lectures 
                right before the exam. 
                <br><br>
                <b>Is this legal? Absolutely not. Do we care? Also no.</b> ☕⚖️
            </p>
        </div>
        """, unsafe_allow_html=True)

with col4:
    if st.button("✨ Manifesting"):
        st.markdown("""
        <div class="star" style="left: 20%; animation-delay: 0.3s;"></div>
        <div class="star" style="left: 40%; animation-delay: 0.8s;"></div>
        <div class="star" style="left: 60%; animation-delay: 1.3s;"></div>
        <div class="star" style="left: 80%; animation-delay: 1.8s;"></div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="message-card">
            <h3 class="card-title">Dear Universe...</h3>
            <p style="font-size: 1.1rem; line-height: 1.8; font-style: italic;">
                Here is my official order for the upcoming year:<br><br>
                
                A man who is pure, respectful, and emotionally mature, 
                but with a bank account that never struggles.<br>
                Handsome? Extremely. Charismatic? Unmatched.<br>
                Must have his life completely together, travel the world with me spontaneously, 
                and treat me like an absolute queen.<br><br>
                
                He needs to love me obsessively, text back in 0.5 seconds, 
                and never make me question my worth.<br><br>
                
                Basically: if he doesn't worship the ground I walk on, 
                he can keep scrolling. <b>Period.</b> ✨👑
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Secret Vault
st.markdown("""
<div class="vault-box">
    <h2 class="vault-title">🔐 The Secret Vault</h2>
    <p style="color: #f4e4c1; font-family: Cormorant Garamond;">Guess the code...</p>
</div>
""", unsafe_allow_html=True)

password = st.text_input("Vault Code:", type="password", placeholder="????", label_visibility="collapsed")

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
        
        # Images
        st.markdown("""
        <div class="image-container">
            <img src="https://raw.githubusercontent.com/zeinahh949-ship-it/Sanah/main/IMG_5156.jpeg" class="vault-image" width="300">
            <img src="https://raw.githubusercontent.com/zeinahh949-ship-it/Sanah/main/IMG_5157.jpeg" class="vault-image" width="300">
            <img src="https://raw.githubusercontent.com/zeinahh949-ship-it/Sanah/main/IMG_5158.jpeg" class="vault-image" width="300">
        </div>
        
        <p style="text-align: center; color: #d4af37; font-family: Cormorant Garamond; font-style: italic; margin-top: 2rem;">
            The exact specifications we discussed... 👀💪
        </p>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="star" style="left: 10%; animation-delay: 0s;"></div>
        <div class="star" style="left: 30%; animation-delay: 0.3s;"></div>
        <div class="star" style="left: 50%; animation-delay: 0.6s;"></div>
        <div class="star" style="left: 70%; animation-delay: 0.9s;"></div>
        <div class="star" style="left: 90%; animation-delay: 1.2s;"></div>
        """, unsafe_allow_html=True)
        
    else:
        st.error("❌ Wrong code. Try again.")

st.markdown("""
<p style="text-align: center; color: rgba(212,175,55,0.6); margin-top: 3rem; font-family: Cormorant Garamond; letter-spacing: 3px;">
    SANAH • THE DIVA • 22 & BEYOND • G.I
</p>
""", unsafe_allow_html=True)

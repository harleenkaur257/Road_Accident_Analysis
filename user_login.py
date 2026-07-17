import streamlit as st

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="wide",
    # initial_sidebar_state="collapsed"
)

# ---------------- Session ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# If already logged in
if st.session_state.logged_in:
    st.switch_page("index.py")

# ---------------- CSS ----------------

st.markdown("""
<style>

/* Hide Streamlit Menu */
#MainMenu{
visibility:hidden;
}
header{
visibility:hidden;
}
footer{
visibility:hidden;
}

/* Background */
.stApp{
background:linear-gradient(135deg,#081B33,#0E2A4E,#17457A);
}

/* Heading */
.title{
text-align:center;
font-size:42px;
font-weight:bold;
color:"#FFD700";
margin-bottom:5px;
}

.subtitle{
text-align:center;
font-size:18px;
color:#D6E4FF;
margin-bottom:30px;
}

/* Login Card */
.login-box{
background:rgba(255,255,255,0.08);
padding:35px;
border-radius:18px;
backdrop-filter:blur(10px);
box-shadow:0px 10px 25px rgba(0,0,0,.45);
}

/* Labels */
label{
color:white !important;
font-weight:bold;
}

/* Text Input */
.stTextInput input{
background:white;
color:black;
border-radius:10px;
border:2px solid #4A90E2;
padding:10px;
}

/* Focus */
.stTextInput input:focus{
border:2px solid #00D4FF;
box-shadow:0px 0px 12px #00D4FF;
}

/* Login Button */
div[data-testid="stFormSubmitButton"] button{

width:100%;
background:#1E88E5;
color:white;
font-size:18px;
font-weight:bold;
padding:12px;
border-radius:10px;
border:none;
transition:0.4s;
}

/* Hover */
div[data-testid="stFormSubmitButton"] button:hover{

background:#00BFFF;
transform:scale(1.03);
box-shadow:0px 0px 15px #00BFFF;
}

/* Image */
img{
border-radius:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- UI ----------------

st.markdown("<h1 class='title'> User Login</h1>", unsafe_allow_html=True)

st.markdown("<p class='subtitle'>Road Accident Analysis System</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

with col1:

    # st.markdown("<div class='login-box'>", unsafe_allow_html=True)

    with st.form("login_form"):

        username = st.text_input("Username")

        password = st.text_input("Password", type="password")

        login = st.form_submit_button("Login")

    st.markdown("</div>", unsafe_allow_html=True)

    if login:

        if username == "admin" and password == "1234":

            st.session_state.logged_in = True

            st.success("Login Successful!")

            st.switch_page("index.py")

        else:

            st.error("Invalid Username or Password")

with col2:

    st.video("login.mp4")

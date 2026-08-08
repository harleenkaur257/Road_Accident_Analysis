import streamlit as st
from datetime import datetime

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="User Login",
    page_icon="🔐",
    layout="wide"
)

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "users" not in st.session_state:
    st.session_state.users = {}

if "login_history" not in st.session_state:
    st.session_state.login_history = []


# ---------------------------------------------------
# IF ALREADY LOGGED IN
# ---------------------------------------------------
if st.session_state.logged_in:
    st.switch_page("pages/index.py")


# ---------------------------------------------------
# CSS
# ---------------------------------------------------
st.markdown("""
<style>

.stApp {
    background-color: #061A2E;
}

.login-title {
    font-size: 42px;
    font-weight: bold;
    color: white;
    text-align: center;
    margin-top: 20px;
}

.subtitle {
    font-size: 20px;
    color: #B8C7D9;
    text-align: center;
    margin-bottom: 30px;
}

.login-box {
    background-color: #0B2742;
    padding: 35px;
    border-radius: 18px;
    box-shadow: 0px 0px 20px rgba(0,0,0,0.4);
}

.history-title {
    color: white;
    font-size: 28px;
    font-weight: bold;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.markdown(
    "<div class='login-title'>User Login</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Road Accident Analysis System</div>",
    unsafe_allow_html=True
)


# ---------------------------------------------------
# TWO COLUMNS
# ---------------------------------------------------
col1, col2 = st.columns([1, 1])


# ===================================================
# LEFT COLUMN
# ===================================================
with col1:

    st.markdown(
        "<div class='login-box'>",
        unsafe_allow_html=True
    )

    login_tab, signup_tab = st.tabs(
        [" Login", "📝 Sign Up"]
    )


    # =================================================
    # LOGIN
    # =================================================
    with login_tab:

        st.subheader("Login")

        with st.form("login_form"):

            username = st.text_input(
                "Username",
                placeholder="Enter your username"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password"
            )

            login = st.form_submit_button(
                " Login",
                use_container_width=True
            )

        if login:

            username = username.strip()

            if username == "" or password == "":
                st.warning(
                    "Please enter username and password."
                )

            elif username in st.session_state.users:

                if st.session_state.users[username] == password:

                    # Save login history
                    st.session_state.login_history.append({
                        "Username": username,
                        "Status": "Successful",
                        "Time": datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        )
                    })

                    st.session_state.logged_in = True
                    st.session_state.username = username

                    st.success("Login Successful!")

                    st.switch_page("pages/index.py")

                else:

                    st.session_state.login_history.append({
                        "Username": username,
                        "Status": "Failed",
                        "Time": datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        )
                    })

                    st.error("Invalid password.")

            else:

                st.session_state.login_history.append({
                    "Username": username,
                    "Status": "Failed",
                    "Time": datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                })

                st.error(
                    "Username does not exist. Please Sign Up first."
                )


    # =================================================
    # SIGN UP
    # =================================================
    with signup_tab:

        st.subheader("Create Account")

        with st.form("signup_form"):

            new_username = st.text_input(
                "Create Username",
                placeholder="Enter username"
            )

            new_password = st.text_input(
                "Create Password",
                type="password",
                placeholder="Enter password"
            )

            confirm_password = st.text_input(
                "Confirm Password",
                type="password",
                placeholder="Enter password again"
            )

            signup = st.form_submit_button(
                "📝 Create Account",
                use_container_width=True
            )

        if signup:

            new_username = new_username.strip()

            if (
                new_username == ""
                or new_password == ""
                or confirm_password == ""
            ):

                st.warning(
                    "Please fill all fields."
                )

            elif new_password != confirm_password:

                st.error(
                    "Passwords do not match."
                )

            elif new_username in st.session_state.users:

                st.error(
                    "Username already exists."
                )

            else:

                st.session_state.users[new_username] = new_password

                st.success(
                    "Account created successfully! "
                    "Now go to Login."
                )


    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# ===================================================
# RIGHT COLUMN
# ===================================================
with col2:

    st.video("login.mp4")


# ===================================================
# LOGIN HISTORY
# ===================================================
st.markdown(
    "<div class='history-title'>📜 Login History</div>",
    unsafe_allow_html=True
)

if st.session_state.login_history:

    st.dataframe(
        st.session_state.login_history,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No login activity yet.")

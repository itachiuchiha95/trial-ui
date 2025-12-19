import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "login"
def login_page():
    st.markdown("## Login")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Log in")

    if submit:
        # REALISTIC mock auth (replace later)
        if username == "demo" and password == "demo":
            st.session_state.logged_in = True
            st.session_state.page = "dashboard"
            st.rerun()
        else:
            st.error("Invalid username or password")
def login_page():
    st.markdown("## Login")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Log in")

    if submit:
        # REALISTIC mock auth (replace later)
        if username == "demo" and password == "demo":
            st.session_state.logged_in = True
            st.session_state.page = "dashboard"
            st.rerun()
        else:
            st.error("Invalid username or password")

st.set_page_config(
    page_title="Trial UI",
    page_icon="🔐",
    layout="wide"
)
PURPLE = "#3b0a78"

st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {PURPLE};
        }}

        .container {{
            max-width: 560px;
            margin: 0 auto;
            padding-top: 70px;
        }}

        .title {{
            text-align: center;
            font-family: Georgia, serif;
            font-style: italic;
            font-size: 64px;
            color: white;
            margin-bottom: 60px;
        }}

        .label {{
            font-size: 34px;
            color: white;
            margin: 28px 0 12px;
        }}

        div[data-baseweb="input"] > div {{
            background: white;
            border-radius: 6px;
            height: 54px;
        }}

        .stButton > button {{
            width: 100%;
            height: 70px;
            background: white;
            color: black;
            font-size: 34px;
            font-weight: 800;
            letter-spacing: 2px;
            border-radius: 8px;
            margin-top: 42px;
        }}

        header, footer {{
            visibility: hidden;
        }}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown('<div class="title">Trial UI</div>', unsafe_allow_html=True)

with st.form("login_form"):
    st.markdown('<div class="label">Username</div>', unsafe_allow_html=True)
    username = st.text_input("", label_visibility="collapsed")

    st.markdown('<div class="label">Password</div>', unsafe_allow_html=True)
    password = st.text_input("", type="password", label_visibility="collapsed")

    submit = st.form_submit_button("LOG IN")

st.markdown("</div>", unsafe_allow_html=True)


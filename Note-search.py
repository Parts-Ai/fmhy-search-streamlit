## Streamlit code
import streamlit as st
import pandas as pd
import gspread
from google.oauth2 import service_account

st.set_page_config(
    page_title="Search Note",
    page_icon="https://www.go-parts.com.au/cdn/shop/files/Asset_5_250x.png?v=1642131890",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://github.com/Rust1667/fmhy-search-streamlit',
        'Report a bug': "https://github.com/Rust1667/fmhy-search-streamlit/issues",
        'About': "https://github.com/Rust1667/fmhy-search-streamlit"
    }
)

st.title("Search Note")

with st.sidebar:
    st.image("https://www.go-parts.com.au/cdn/shop/files/Asset_5_250x.png?v=1642131890", width=200)
    st.text("Search Engine for Note")
    st.markdown("Links:")
    st.markdown("* Wiki: [Reddit](https://www.reddit.com/r/FREEMEDIAHECKYEAH/wiki/index/), [.net](https://fmhy.net/) / [.pages](https://fmhy.pages.dev/), [.tk](https://www.fmhy.tk/) / [.vercel](https://fmhy.vercel.app/), [raw](https://raw.githubusercontent.com/nbats/FMHYedit/main/single-page)")
    st.markdown("* [Github Repo (web-app)](https://github.com/Rust1667/fmhy-search-streamlit)")
    st.markdown("* [Github Repo (script)](https://github.com/Rust1667/a-FMHY-search-engine)")
    st.markdown("* [Other Search Tools for FMHY](https://www.reddit.com/r/FREEMEDIAHECKYEAH/comments/105xraz/howto_search_fmhy/)")

queryInputFromBox = st.text_input(label=" ", value="", help="Search for links in the Wiki.")

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"
    ],
)
conn = connect(credentials=credentials)
client=gspread.authorize(credentials)

sheet_id = '1DzznFoBDHVozt9JpaLcGb6VqDoPHIyPFX9WkhIN5FAk'
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
database_df = pd.read_csv(csv_url, on_bad_lines='skip')

for row in df.itertuples():
    st.write(f"{row.VIN}")

if st.button("Search"):
    queryInput = queryInputFromBox
#     doASearch(queryInput)
#     put_query_in_URL(queryInput)
#     search_from_URL_query()

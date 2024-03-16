## Streamlit code
import streamlit as st
from streamlit_gsheets import GSheetsConnection

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


conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(
    worksheet="Sheet1",
    ttl="10m",
    usecols=[0, 1],
    nrows=3,
)

df = conn.read()

for row in df.itertuples():
    st.write(f"{row.VIN}")

if st.button("Search"):
    queryInput = queryInputFromBox
#     doASearch(queryInput)
#     put_query_in_URL(queryInput)
#     search_from_URL_query()
import streamlit as st
import importlib
import os

from PIL import Image
from streamlit_option_menu import option_menu
from utils import apply_background,custom_navbar
from st_pages import Page, show_pages, add_page_title
from pathlib import Path

root_path = Path(__file__).parent
media_path = root_path.joinpath("media")
pages_path = root_path.joinpath('Pages')

# Set page configuration
st.set_page_config(
    page_title="Book Info Hub",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)
 
    # Apply the background image
apply_background(image_path="./app/media/book4.jpg")





# Main content (previously in the sidebar)
st.subheader("Tools Available")
st.write("""
 **URL Summarization:** 
 Welcome to the URL Summarizer! Paste up to three URLs, and this tool will quickly generate concise summaries of the content using advanced language models. Perfect for when you want to grasp the key points of articles, reviews, or any online content without reading through lengthy texts. Ask specific questions or get an overall summary in seconds!.Provide a URL related to any book or literary content, and our tool will summarize the key points for you.
 
""")
# Add links to book resources or related pages
st.markdown("""
For more information and about the project, check out my profile:

- [LinkedIn](https://www.linkedin.com/in/swathy-ramakrishnan/)
- [GitHub](https://github.com/swaty06)
""")

# Footer
st.markdown("---")
st.markdown(
    """
    **About:** This application is designed to help you explore books, get recommendations, and find your next favorite read. Stay tuned for more updates!
    """
)

show_pages(
    [
        Page(str(root_path.joinpath("main.py")), "Home", "🏠"),
        Page(str(pages_path.joinpath("page1.py")), "Url Summarisor", ":books:"),
      
       
    ]
)

add_page_title(layout="wide")
apply_background()

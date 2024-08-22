import streamlit as st
from utils import apply_background  # Import the function from utils.py

# Set the page configuration
st.set_page_config(
    page_title="Book Info Hub",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply the background image
apply_background(image_path="./app/media/book4.jpg")

# Title and introductory message
st.title("Book Info Hub 📚")
st.markdown("""
Welcome to the Book Info Hub, your gateway to a richer reading experience. Our application offers two powerful tools designed to enhance how you interact with books and reading material: URL Summarization and the Book Chatbot.
""")

# Sidebar content
st.sidebar.title("Sidebar")
st.sidebar.write("This is the expanded sidebar.")

# Main content in the sidebar
st.sidebar.subheader("Tools Available")
st.sidebar.write("""
1. **URL Summarization:** Provide a URL related to any book or literary content, and our tool will summarize the key points for you.
2. **Book Chatbot:** Ask any book-related questions, and get insightful responses from our AI-powered assistant.
""")

# Display Image (Make sure the image path is correct)
# st.image("./app/media/books.jpg", use_column_width=True)

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

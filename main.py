# main.py
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
apply_background(image_path="./media/book4.jpg")

# Title and introductory message
st.title("Book Info Hub 📚")
st.markdown("""
Welcome to the Book Info Hub, your gateway to a richer reading experience. Our application offers two powerful tools designed to enhance how you interact with books and reading material: URL Summarization and the Book Chatbot.

**URL Summarization**
\n In today's fast-paced world, sifting through vast amounts of information to find relevant insights can be daunting. Our URL Summarization tool is here to assist you. Simply provide a URL related to any book or literary content, and our tool will summarize the key points for you. Whether it’s a book review, an article about a book, or any related material, this feature distills the essence of the text, saving you time and helping you decide if the content is worth exploring further. Additionally, if you have specific questions about the content in the URL, our system is equipped to answer them directly, providing you with a more targeted understanding of the text.

**Book Chatbot**
\n Dive deeper into the world of literature with our innovative Book Chatbot. Designed to answer questions about books, genres, authors, and more, this AI-powered assistant is like having a personal librarian at your fingertips. Whether you're looking for recommendations, exploring new genres, or seeking insights into a particular book, our chatbot is ready to assist. It can provide background information on your favorite books, discuss themes and characters, and even help you discover new titles that match your interests.

Our app is designed to make your reading journey more enjoyable and efficient, offering personalized insights and enhancing your understanding of literary content. Join us on this journey to explore and discover the world of books like never before. Whether you're a casual reader or a literary enthusiast, the Book Info Hub is your ultimate companion for all things books.
""")

# Display Image
#st.image("./media/books.jpg", use_column_width='auto')


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

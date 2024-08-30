import os
import streamlit as st
import pickle
import time
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from utils import apply_background, custom_navbar
from dotenv import load_dotenv
from st_pages import add_page_title
from pathlib import Path
from langchain.chat_models import ChatOpenAI

root_path = Path(__file__).parent.parent
media_path = root_path.joinpath("media")

def app():
    load_dotenv()
    vectorstore_openai = None

    st.title("Book Search Tool 📚")
    apply_background(image_path="./app/media/book4.jpg")

    st.sidebar.title("Book Search Tool 📚")
    st.sidebar.write("Enter up to three URLs related to a book or article. Process the URLs to ask questions about the content.")
    
    st.sidebar.markdown(
        """
        <style>
        .stTextInput {
            max-width: 250px;
            padding: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    urls = [st.sidebar.text_input(f"URL {i+1}", key=f"url_{i}", placeholder="Enter URL here") for i in range(3)]
    process_url_clicked = st.sidebar.button("Process URLs")

    file_path = "vector_index.pkl"
    main_placeholder = st.empty()

    # Initialize ChatOpenAI LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.8, max_tokens=500)
    
    if process_url_clicked:
        try:
            loader = UnstructuredURLLoader(urls=urls)
            main_placeholder.text("Data Loading... Started...✅✅✅")
            data = loader.load()

            text_splitter = RecursiveCharacterTextSplitter(separators=['\n\n', '\n', '.', ','], chunk_size=1000)
            main_placeholder.text("Text Splitting... Started...✅✅✅")
            docs = text_splitter.split_documents(data)

            embeddings = OpenAIEmbeddings()
            vectorstore_openai = FAISS.from_documents(docs, embeddings)
            main_placeholder.text("Embedding Vector Started Building...✅✅✅")
            time.sleep(2)
            
            # Save FAISS index
            vectorstore_openai.save_local("vectorstore")
            with open(file_path, "wb") as f:
                pickle.dump(vectorstore_openai, f)
                
        except Exception as e:
            st.error(f"Error processing URLs: {str(e)}")

    st.header("Ask a Question Related to the Links Provided")
    query = st.text_input("Enter your question: ")

    if query:
        try:
            if os.path.exists(file_path):
                with open(file_path, "rb") as f:
                    vectorstore = pickle.load(f)
                    vectorstore = FAISS.load_local("vectorstore", OpenAIEmbeddings())
                    chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
                    result = chain({"question": query}, return_only_outputs=True)

                    st.header("Answer")
                    st.write(result.get("answer", "No answer found."))

                    sources = result.get("sources", "")
                    if sources:
                        st.subheader("Sources:")
                        for source in sources.split("\n"):
                            st.write(source)
            else:
                st.error("No FAISS index file found. Please process URLs first.")
        except Exception as e:
            st.error(f"Error processing query: {str(e)}")

custom_navbar()
add_page_title(layout="wide")
app()


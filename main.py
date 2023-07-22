import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
from tempfile import NamedTemporaryFile

def main():
    # Your Code goes in here
    load_dotenv()

    st.set_page_config(page_title= "ChatDoc Application 📃")

    st.header("ChatDoc Application 📃")

    user_document = st.file_uploader(label="Upload your document", type="csv")

    if user_document is not None:

        with NamedTemporaryFile(suffix ='.csv', delete=False) as f: # Create temporary file
            f.write(user_document.getvalue())
            f.flush()
        
        user_question = st.text_input("Ask a question about your document: ")

        llm = OpenAI(temperature=0)
        agent = create_csv_agent(llm, f.name, verbose=True)

        if user_question is not None and user_question.strip() != "":
            response = agent.run(user_question)
            st.write(response)


if __name__ == "__main__":
    main()
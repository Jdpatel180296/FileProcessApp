import streamlit as st

st.title("Files in Uploaded Folder")

if "uploaded_files" in st.session_state:
    for file in st.session_state["uploaded_files"]:
        st.write(f"📄 {file}")
else:
    st.warning("No folder uploaded yet. Go to 'Upload Folder' first.")

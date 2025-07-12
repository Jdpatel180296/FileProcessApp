import streamlit as st

st.title("Process Files")

if "uploaded_files" in st.session_state:
    selected_files = st.multiselect("Select files to process", st.session_state["uploaded_files"])

    if selected_files:
        st.success(f"You selected {len(selected_files)} file(s).")
        for file in selected_files:
            st.write(f"✅ {file}")
    else:
        st.info("Select files from the list to process.")
else:
    st.warning("No folder uploaded yet.")

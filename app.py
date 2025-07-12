import streamlit as st
import os
import zipfile
import shutil

st.set_page_config(page_title="Folder Uploader App", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
st.sidebar.page_link("app.py", label="📁 Upload Folder", icon="📤")
st.sidebar.page_link("pages/view_files.py", label="📂 View Files")
st.sidebar.page_link("pages/process_files.py", label="⚙️ Process Files")

# Main layout
st.title("📦 Folder Upload and File Preview")

# Two side-by-side columns
col1, col2 = st.columns(2)

upload_dir = "uploaded_data"

# === LEFT COLUMN: Upload ZIP ===
with col1:
    st.header("📁 Upload Folder")
    uploaded_folder = st.file_uploader("Upload a .zip file", type=["zip"])

    if uploaded_folder:
        # Clear previous data
        if os.path.exists(upload_dir):
            shutil.rmtree(upload_dir)

        with zipfile.ZipFile(uploaded_folder, "r") as zip_ref:
            zip_ref.extractall(upload_dir)

        file_list = []
        for root, dirs, files in os.walk(upload_dir):
            for file in files:
                relative_path = os.path.relpath(os.path.join(root, file), upload_dir)
                file_list.append(relative_path)

        # Store in session state
        st.session_state["uploaded_files"] = file_list
        st.success(f"✅ Uploaded and extracted {len(file_list)} files.")

# === RIGHT COLUMN: Show Files ===
with col2:
    st.header("📄 Files in Folder")
    if "uploaded_files" in st.session_state:
        if st.session_state["uploaded_files"]:
            st.code("\n".join(st.session_state["uploaded_files"]))
        else:
            st.info("No files found in the folder.")
    else:
        st.warning("Upload a zipped folder from the left panel to view files.")

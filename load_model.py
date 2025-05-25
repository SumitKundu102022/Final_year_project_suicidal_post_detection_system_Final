import streamlit as st
import tensorflow as tf
import os
from dotenv import load_dotenv
import requests

load_dotenv()

DROPBOX_DIRECT_URL = os.getenv("DROPBOX_DIRECT_URL")  # Replace with your direct link
LOCAL_MODEL_PATH = "model.keras"

def download_model_from_dropbox():
    if not os.path.exists(LOCAL_MODEL_PATH):
        try:
            st.info("Downloading model...")
            response = requests.get(DROPBOX_DIRECT_URL)
            with open(LOCAL_MODEL_PATH, "wb") as f:
                f.write(response.content)
            st.success("Model downloaded successfully.")
        except Exception as e:
            st.error(f"Failed to download model: {e}")
            st.stop()
    else:
        st.info("Model already downloaded.")

def load_model():
    try:
        download_model_from_dropbox()
        model = tf.keras.models.load_model(LOCAL_MODEL_PATH)
        st.success("Model loaded successfully.")
        return model
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        st.stop()



# import streamlit as st
# import tensorflow as tf
# import os
# from dotenv import load_dotenv
# import dropbox

# load_dotenv()
# ACCESS_TOKEN = os.getenv("DROPBOX_ACCESS_TOKEN")

# DROPBOX_PATH = '/model.h5'
# LOCAL_MODEL_PATH = 'model.h5'

# def download_model_from_dropbox():
#     if not os.path.exists(LOCAL_MODEL_PATH):
#         try:
#             dbx = dropbox.Dropbox(ACCESS_TOKEN)
#             metadata, res = dbx.files_download(DROPBOX_PATH)
#             with open(LOCAL_MODEL_PATH, 'wb') as f:
#                 f.write(res.content)
#             # st.success("Model downloaded from Dropbox.")
#         except Exception as e:
#             st.error(f"Failed to download model: {e}")
#             st.stop()
#     # else:
#     #     st.info("Model already exists locally.")

# def load_model():
#     try:
#         download_model_from_dropbox()
#         model = tf.keras.models.load_model(LOCAL_MODEL_PATH)
#         # st.success("Model loaded successfully.")
#         return model
#     except Exception as e:
#         st.error(f"Failed to load model: {e}")
#         st.stop()




# import streamlit as st
# import os
# from dotenv import load_dotenv
# import dropbox
# import tensorflow as tf

# load_dotenv()
# ACCESS_TOKEN = os.getenv("DROPBOX_ACCESS_TOKEN")
# DROPBOX_PATH = "/model.keras"
# LOCAL_MODEL_PATH = "model.keras"

# def download_model():
#     if not os.path.exists(LOCAL_MODEL_PATH):
#         try:
#             with open(LOCAL_MODEL_PATH, 'wb') as f:
#                 metadata, res = dropbox.Dropbox(ACCESS_TOKEN).files_download(DROPBOX_PATH)
#                 f.write(res.content)
#             st.success("Model downloaded from Dropbox.")
#         except Exception as e:
#             st.error(f"Failed to download model: {e}")
#             st.stop()
#     else:
#         st.info("Model already exists locally.")

# def load_model_from_dropbox():
#     try:
#         download_model()
#         model = tf.keras.models.load_model(LOCAL_MODEL_PATH)
#         st.success("Model loaded successfully.")
#         return model
#     except Exception as e:
#         st.error(f"Failed to load model: {e}")
#         st.stop()



# import streamlit as st
# import os
# import requests
# import tempfile
# import tensorflow as tf
# from dotenv import load_dotenv

# load_dotenv()

# # Dropbox direct download link (force download)
# DROPBOX_DIRECT_URL = os.getenv("DROPBOX_DIRECT_URL")  # e.g., https://www.dropbox.com/s/abc123xyz/model.h5?dl=1

# @st.cache_resource
# def load_model_from_dropbox():
#     try:
#         # Create a temporary file
#         with tempfile.NamedTemporaryFile(delete=False, suffix=".h5") as tmp_file:
#             tmp_path = tmp_file.name

#             # Download from Dropbox
#             response = requests.get(DROPBOX_DIRECT_URL)
#             if response.status_code != 200:
#                 st.error("Failed to download model. Check Dropbox link or internet connection.")
#                 st.stop()

#             tmp_file.write(response.content)

#         # Load the model from temp path
#         model = tf.keras.models.load_model(tmp_path)
#         return model

#     except Exception as e:
#         st.error(f"Failed to load model: {e}")
#         st.stop()




# import os
# import streamlit as st
# import dropbox
# import tensorflow as tf
# from dotenv import load_dotenv

# load_dotenv()

# ACCESS_TOKEN = os.getenv("DROPBOX_ACCESS_TOKEN")
# DROPBOX_PATH = '/model.h5'         # Path of model in Dropbox
# LOCAL_MODEL_PATH = 'model.h5'      # Where to save locally

# # Initialize Dropbox client
# dbx = dropbox.Dropbox(ACCESS_TOKEN)

# # Function to download the model from Dropbox
# def download_model():
#     if not os.path.exists(LOCAL_MODEL_PATH):
#         try:
#             with open(LOCAL_MODEL_PATH, 'wb') as f:
#                 metadata, res = dbx.files_download(DROPBOX_PATH)
#                 f.write(res.content)
#             # st.success("Model downloaded successfully.")
#         except Exception as e:
#             st.error(f"Failed to download model: {e}")
#             st.stop()
#     # else:
#     #     st.info("Model already exists locally. Skipping download.")

# # Function to load the model
# def load_model():
#     try:
#         download_model()
#         model = tf.keras.models.load_model(LOCAL_MODEL_PATH)
#         # st.success("Model loaded successfully.")
#         return model
#     except Exception as e:
#         st.error(f"Failed to load model: {e}")
#         st.stop()

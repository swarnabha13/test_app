import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.title("Drone Webcam live feed")
st.write("Testing")

ctx = webrtc_streamer(
    key="example",
    rtc_configuration={  # Add this line
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
)
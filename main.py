import streamlit as st
from llm import GenerativeAIClient
from get_sub import get_transcript
st.image('image.png', width=700)

st.title("Youtube Summy")
st.write("Enter the YouTube video link below:")
st.sidebar.markdown("# About US")
st.sidebar.markdown("## สร้างโดยทีมงาน #AI \n\n #AI for people \n\nเพจที่รวบรวมข่าวสารที่เกี่ยวข้อง และแชร์เทคนิคๆ ต่างของ AI")
st.sidebar.markdown("## สามารถติดตามเราได้ที่ ")
st.sidebar.image('logo.png', width=100)
st.sidebar.link_button("Facebook Page #AI", url='https://www.facebook.com/profile.php?id=61560597801592')
st.sidebar.markdown("สามารถใช้งานได้ฟรี และไม่มีค่าใช้จ่ายเพิ่มเติม \nโดย Google AI Studio \n\n")

# Get user input
link = st.text_input("YouTube video link")

if st.button("Summarize"):
    if link:

        # Get transcript from YouTube video
        srt = get_transcript(link)
#
        # Initialize LLM client
        client = GenerativeAIClient()

        # Generate summary using LLM
        summary = client.generate_summary(srt)
        # Display summary
        st.subheader("Video Summary")
        st.write(summary)

    else:
        st.write("Please enter a YouTube video link")
        

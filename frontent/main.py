import streamlit as st
import requests

st.set_page_config(page_title="YouTube Comment Analyzer", layout="centered")
st.title("Analyze YouTube Video Comments")

st.markdown(
    """
    ### Instructions:
    1. Enter the YouTube video link in the field below.
    2. Click on the "Submit" button.
    3. View and analyze the video along with an overview of its comments.
    """
)

link = st.text_input("Paste the YouTube video link here:")

if st.button("Submit"):
    if "youtube.com/watch" not in link and "youtu.be/" not in link:
        st.error("Please enter a valid YouTube video link.")
    else:
        with st.spinner("Analyzing the video..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:5001/predict", json={"url": link}
                )

                if response.status_code == 200:
                    st.success("Analysis complete!")
                    results = response.json()

                    st.video(link)

                    negative_comments = results.get("Negative", [])
                    positive_comments = results.get("Positive", [])

                    total_comments = len(negative_comments) + len(positive_comments)
                    negative_count = len(negative_comments)
                    positive_count = len(positive_comments)

                    st.subheader("Analysis Overview:")
                    st.markdown(
                        f"""
                        - **Total Comments Analyzed:** {total_comments}
                        - **Positive Comments:** {positive_count} ({(positive_count / total_comments) * 100:.2f}%)
                        - **Negative Comments:** {negative_count} ({(negative_count / total_comments) * 100:.2f}%)
                        """
                    )

                    st.subheader("Detailed Comment Analysis:")

                    st.write("### Negative Comments:")
                    for i, comment in enumerate(negative_comments):
                        st.write(f"**{i + 1}.** {comment}")

                    st.write("### Positive Comments:")
                    for i, comment in enumerate(positive_comments):
                        st.write(f"**{i + 1}.** {comment}")

                else:
                    st.error("Error: Unable to fetch analysis. Try again later.")
            except requests.exceptions.RequestException as e:
                st.error(f"Request failed: {e}")

st.markdown("---")
st.markdown("🔍 Powered by Streamlit and a sentiment analysis backend.")

import streamlit as st
import pickle
import re

from fact_checker import fact_check

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def clean_text(text):

    text = str(text).lower()

    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"www\S+", "", text)
    text = re.sub(r"[^a-zA-Z ]", "", text)

    return text

st.set_page_config(
    page_title="AI Fake News Verification",
    page_icon="📰",
    layout="wide"
)

st.title("📰 AI-Powered Real-Time Fake News Verification")

news = st.text_area(
    "Enter News Headline or Claim",
    height=200
)

results = []

if st.button("Verify News"):

    if news.strip() == "":
        st.warning("Please enter news text.")
    else:

        cleaned = clean_text(news)

        vector = vectorizer.transform([cleaned])

        prediction = model.predict(vector)[0]

        probability = model.predict_proba(vector)[0]

        fake_score = probability[0] * 100
        real_score = probability[1] * 100

        st.subheader("Machine Learning Prediction")

        if prediction == 1:
            st.success(
                f"✅ Likely Real News ({real_score:.2f}%)"
            )
        else:
            st.error(
                f"❌ Likely Fake News ({fake_score:.2f}%)"
            )

        st.write(f"Real Score : {real_score:.2f}%")
        st.write(f"Fake Score : {fake_score:.2f}%")

        st.progress(int(max(real_score, fake_score)))

        st.subheader("Google Fact Check Results")

        st.write("INPUT:", news)

        results = fact_check(news)

        st.write("RESULTS:", results)
        st.write("Results Found:", len(results))
        if results:

            st.subheader("🔍 Google Fact Check Results")

            for item in results:

                st.write("### Claim")
                st.write(item["claim"])

                st.write("Publisher:", item["publisher"])

                st.write("Rating:", item["rating"])

                st.write("Source:", item["url"])

                st.markdown("---")

        else:

            st.warning("No verified fact-check results found.")

st.markdown("---")

st.write(
    "Built using Python, NLP, Scikit-Learn, Streamlit and Google Fact Check API"
)
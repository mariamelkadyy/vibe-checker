import streamlit as st
from transformers import pipeline

st.title("🧠 The Vibe Checker")
st.write("Enter any text below, and I'll use AI to tell you if it's **Positive** or **Negative**.")


# LOAD THE BRAIN:
# Loading an AI model uses time and memory. If the model loads every time someone clicks a button, the app will run very slowly.
# To solve this, we use a special decorator called @st.cache_resource. It runs the function once to load the model and keeps it in memory.
# The model only reloads if the app restarts:


@st.cache_resource()
def load_model():
    # We use a standard 'sentiment-analysis' pipeline from Hugging Face.
    # It downloads a small, efficient model
    return pipeline("sentiment-analysis")

#load the model instantly
with st.spinner('Loading AI Brain...'):
    classifier = load_model()

user_text = st.text_area("What's on your mind?",
                         placeholder="Type something like: '2k26 summer is the best'")


# The Logic and Display
# Finally, we’ll connect the input to the model and add a button to start the analysis:


if st.button("Analyze The Vibe"):
    if user_text.strip():  #check if text isn't empty
        result = classifier(user_text)

        # The model returns a list like [{'label': 'POSITIVE', 'score': 0.99}]
        label = result[0]['label']
        score = result[0]['score']

        # Display the result with some dynamic flair
        if label == "POSITIVE":
            st.success(f"**Positive Vibe Detected!** (Confidence: {score:.2f})")
            st.balloons()   #fun animation

        else:
            st.error(f"**Negative Vibe Detected!** (Confidence: {score:.2f})")

    else:
        st.warning("Please enter some text first!")


















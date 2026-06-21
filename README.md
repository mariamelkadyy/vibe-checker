# The Vibe Checker 🎭

An AI-powered sentiment analysis web application built using **Python**, **Streamlit**, and **Hugging Face Transformers**.
The app allows users to enter any text and instantly predicts whether the sentiment is **Positive** or **Negative**, along with a confidence score.

---

## 🚀 Features

* Real-time sentiment analysis
* Detects **Positive** or **Negative** sentiment
* Displays prediction confidence score
* Interactive and beginner-friendly UI
* Cached AI model for faster loading using Streamlit caching
* Fun UI feedback (success/error messages and balloons animation)

---

## 🛠 Tech Stack

* **Python**
* **Streamlit** — Web app framework
* **Hugging Face Transformers** — Pretrained NLP models
* **PyTorch / TensorFlow** — Model backend

---

## 📌 How It Works

1. User enters text in the input box
2. The app sends the text to a pretrained sentiment analysis model
3. The model classifies the sentiment as:

   * **POSITIVE**
   * **NEGATIVE**
4. The result is displayed with a confidence score

Example output:

Positive Vibe Detected! (Confidence: 0.99)

or

Negative Vibe Detected! (Confidence: 0.97)

---

## 📂 Project Structure

```bash
vibe-checker/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙ Installation & Setup

Clone the repository:

```bash
git clone https://github.com/your-username/vibe-checker.git
```

Move into the project folder:

```bash
cd vibe-checker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

---

## 📦 Requirements

Example `requirements.txt`:

```txt
streamlit
transformers
torch
tensorflow
```

---

## 🧪 Example Inputs

### Positive Examples

* I got accepted into my dream internship!
* Today was amazing and I feel so happy
* I love spending time with my friends

### Negative Examples

* I had a terrible day
* Everything is going wrong
* I feel exhausted and frustrated

### Tricky Examples

* Today's exam cooked me
* I hate how much I love this song
* I'm fine.

---

## ⚠ Limitations

This project also highlights real-world limitations of NLP models:

* May struggle with **slang**
* May misinterpret **sarcasm**
* Mixed emotions can confuse predictions
* Context-dependent phrases may be classified incorrectly

Example:

* “Today's exam cooked me” → Humans understand this as negative slang, but the model may not.
* “I hate how much I love this song” → Contains both positive and negative sentiment, making classification difficult.

---

## 🔮 Future Improvements

Possible upgrades for future versions:

* Add **Neutral** sentiment class
* Support **Arabic sentiment analysis**
* Add sentiment history dashboard
* Visualize predictions with charts
* Use larger or more advanced LLMs
* Deploy with analytics and user tracking

---

## 🌐 Deployment

This app can be deployed for free using:

* Streamlit Community Cloud
* Hugging Face Spaces
* Render

Once deployed, users can access it through a public URL from any device.

---

## 📷 Demo Screenshot

(Add screenshots of your app here after deployment)

---

## 🎯 Learning Outcomes

This project helped me learn:

* How to build AI-powered web apps
* How to use pretrained NLP models
* Streamlit UI development
* Model caching and optimization
* AI limitations in real-world text understanding

---

## 👩‍💻 Author

Built by **Mariam Elkady** as part of my AI and software development learning journey.

# ChatOllama

[![LinkedIn][linkedin-shield]][linkedin-url]
[![Outlook][outlook-shield]][outlook-url]

![Ollama](https://github.com/danjour/ChatOllama/assets/28869251/aba59983-affe-48c0-8832-fc7ac32bf085)


<!-- PROJECTS -->

# About The Project
![image](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![image](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![image](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![image](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![image](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![image](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

The project emerged with the proposal of being a clone of Chat GPT, but obviously with less processing power. For the Large Language Model (LLM) function, I use Ollama, utilizing the [mistral:7b-instruct-v0.2-q4_K_S](https://ollama.com/library/mistral:7b-instruct-v0.2-q4_K_S) base.

The project features a login screen, a main screen, and a registration screen. All are integrated with the database, so when you log in, a query is made to the database. The messages are stored, so even if you leave the chat, the conversations are saved when you log back into your account. The same applies to the registration screen; everything is connected to the database.

# How does the LLM language model work?

## 1. Pre-training Phase

At th first moment, our primary objective is to gather the most diverse collection of textual data possible, like books, articles, and virtually any other form of written information. This comprehensive dataset is pivotal in enabling LLMs to develop a understanding of human language.

Check out the [AI Vs Human Text Detection 🧑🤖 on Kaggle](https://www.kaggle.com/eduardod/ai-vs-human-text-detection?cellIds=17&kernelSessionId=161300091) for an interactive exploration of how AI models distinguish between text written by humans and AI-generated text.

## 2. Context encoding

Term Frequency-Invese Document Frequency

The tf–idf value (short for term frequency–inverse document frequency, which means term frequency–inverse document frequency), is a statistical measure that aims to indicate the importance of a word in a document in relation to a collection of documents or a linguistic corpus. It is often used as a weighting factor in information retrieval and data mining.

$$IDF_t=log(\frac{N}{df_t})$$

$$TFIDF_{tid}=TF_{tid}\times IDF_t$$

Where N = Number of documents and dft = Number of documents where term t appears

[term frequency–inverse document frequency](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)

In the end, we will have this representation:

|          | 1ª Text | 2ª Text | 3ª Text | ... | Nª Text |
|----------|-------------|-------------|-------------|-----|-------------|
| 1ª Word | 0.01           | 0.08        | 0.18        | ... | 0.12        |
| 2ª Word | 0           | 0.06        | 0.19        | ... | 0.13        |
| 3ª Word | 0.05           | 0.06        | 0.19        | ... | 0.1         |
| Nª Word | 0           | 0.1         | 0.2         | ... | 0.2         |

After that, we can assume that this values will pass in a neural network like as shown below

![image](https://github.com/danjour/ChatOllama/assets/28869251/6042a5ad-c563-4ab1-ad34-6a61ecc8a041)

# Login Screen

![image](https://github.com/danjour/ChatOllama/assets/28869251/332eb96a-cf15-45b5-8318-4da49ffd129f)

# Main Screen

![image](https://github.com/danjour/ChatOllama/assets/28869251/16379394-1f71-4b06-9552-af53611f6e7c)

# Register Screen

![image](https://github.com/danjour/ChatOllama/assets/28869251/7e507ec9-8f47-4457-b63a-8767a3eafe94)

# Requirements

To run this project, you'll need to install the following packages:

- `httpx==0.27.0`
- `Flask==3.0.2`
- `psycopg2-binary==2.9.9`
- `bcrypt==4.1.2`
- `python-dotenv==1.0.1`
- `Jinja2==3.1.2`
- `Werkzeug==3.0.1`
- `itsdangerous==2.1.2`
- `click==8.1.7`
- `MarkupSafe==2.1.3`

You can install all required packages with the following command:

```bash
pip install -r requirements.txt
```

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/eduardodanjour/
[facebook-shield]:	https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=555
[facebook-url]: https://www.facebook.com/eduardo.danjour/
[outlook-shield]:https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=555
[outlook-url]: https://www.facebook.com/eduardo.danjour/

import streamlit as st
import openai  # for chatbot implementation (replace with your API key)

# Sidebar or header with contact info
# st.sidebar.title("Contact Information")
# st.sidebar.write("""
# **Sundareswar Pullela**  
# 📞 (458)272-7796  
# 📧 [psundareswar@gmail.com](mailto:psundareswar@gmail.com)  
# 💼 [LinkedIn](https://linkedin.com/in/psundareswar)  
# 📂 [GitHub](https://github.com/sundareswarpullela)
# """)

# # Main content of the portfolio
# st.title("Sundareswar Pullela's AI & ML Portfolio")
# st.write("""
# AI and Machine Learning Engineer with expertise in developing and deploying scalable AI models, fine-tuning large language models (LLMs), and optimizing machine learning pipelines.  
# Graduating with an M.Sc. in Computer Science from Oregon State University in December 2024.
# """)

# # Education Section
# st.header("Education")
# st.write("""
# **Master of Science (M.Sc.) in Computer Science**  
# Oregon State University (Expected Dec 2024)  
# - GPA: 3.7/4.0  
# - Minor in AI (Coursework: Artificial Intelligence, Deep Learning, Machine Learning, etc.)

# **Bachelor of Technology (B.Tech.) in Computer Science**  
# Raghu Engineering College (2018 - 2022)  
# - GPA: 8.9/10.0  
# - Coursework: Data Structures, Computer Networks, Object-Oriented Programming
# """)

# # Skills Section
# st.header("Technical Skills")
# st.write("""
# - **AI/ML Tools**: Fine-Tuning LLMs (GPT-4, Llama-3), OpenAI API, LangChain, MLFlow  
# - **Programming Languages**: Python, R, C++, Java, SQL, Neo4j Cypher  
# - **Cloud & DevOps**: Docker, Kubernetes, AWS, GCP, Azure  
# - **Web Technologies**: HTML, CSS, JavaScript, Angular, Django, RESTful APIs
# """)

# # Work Experience Section
# st.header("Work Experience")
# st.write("""
# **Graduate Research Assistant, Oregon State University** (Sept 2022 - Present)  
# - Developed large-scale biomedical knowledge graphs with sub-second response times using Neo4j on AWS.
# - Streamlined deployment pipelines, reducing graph generation time by 50%.

# **ML Technology Full-Stack Intern, RIA Advisory** (Jun 2023 - Sept 2023)  
# - Developed an end-to-end machine learning pipeline for financial services applications, increasing model accuracy by 10%.

# **Software Developer Intern, Juspay Technologies** (Sept 2021 - Apr 2022)  
# - Developed secure digital payment solutions for major clients, handling over $20 million in revenue.

# **Machine Learning Research Intern, Akrivia Automation** (Dec 2020 - Feb 2021)  
# - Created advanced text parsing algorithms, increasing accuracy by 90%.
# """)

# # Projects Section
# st.header("Projects")
# st.write("""
# **RADIANT Rare Disease Chat**  
# A QA system utilizing fine-tuned LLaMa-3.1 70B parameter LLM for answering questions about rare genetic diseases.  
# [Project Demo](https://radiant.rarepath.ai)

# **Post-training Quantization of Vision Language Model**  
# Implemented PTQ4CLIP, improving quantized vision-language model performance.  
# [Project Report](https://github.com/VLQuant/PTQ4CLIP/blob/main/Post_Training_Quantization_on_the_CLIP_Vision_Language_Model.pdf)

# **Facial Tracking Accessibility Control**  
# Developed a prototype enabling individuals with disabilities to control a computer mouse using facial movements.  
# [GitHub Link](https://github.com/sundareswarpullela/AccessibilityFT)
# """)

# # Publications Section
# st.header("Publications")
# st.write("""
# **Machine Learning Techniques for Heart Disease Prediction**  
# Published in IJSTRE, Nov 2019. Achieved 98% accuracy for coronary heart disease risk prediction.
# """)

# Chat Box Section
st.header("Ask Me Anything!")

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

def fetch_latest_resume_details():
    from PyPDF2 import PdfReader
    text = ""
    reader = PdfReader("~/resume.pdf")
    number_of_pages = len(reader.pages)
    for p_no in range(number_of_pages):
        text.append(page.extract_text())
    return text

def get_response_from_chatbot(question):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system", 
                "content": "You're an AI assistant designed to answer questions about my resume. Do not answer questions about anything else except my resume and profile."
            },
            {
                "role": "system",
                "content": f"Here are the details of my resume. {fetch_latest_resume_details()}"
            },
            {
                
                "role": "user",
                "content": f"{question}"
            }
        ]
    )


def ask_question():
    user_question = st.text_input("Ask a question about my profile:")
    if st.button("Send"):
        # Here you'd normally integrate with OpenAI or another backend
        st.session_state.messages.append({"role": "user", "content": user_question})
        response = get_response_from_chatbot(user_question)
        st.session_state.messages.append({"role": "bot", "content": response})

ask_question()
# if "messages" not in st.session_state:
#     st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).write(msg["content"])

# if prompt := st.chat_input():
#     if not openai_api_key:
#         st.info("Please add your OpenAI API key to continue.")
#         st.stop()

#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.chat_message("user").write(prompt)
#     response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
#     msg = response.choices[0].message.content
#     st.session_state.messages.append({"role": "assistant", "content": msg})
#     st.chat_message("assistant").write(msg)

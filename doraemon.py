#---- RUN THESE COMMANDS BEFORE RUNNING APP ----#
# pip install dotenv
# pip install streamlit
# pip install google-generativeai

# ---- RUN THE APP ----#
# streamlit run doraemon.py

# importing open-source python framework streamlit
import streamlit as st

# importing generativeai from google
import google.generativeai as genai

API_KEY = "AIzaSyC3hIj0XYS0RGY7RNYFeYeh5a1MD2xYmA0"

# configuring our API key to our generativeAI
genai.configure(api_key=API_KEY)

# requring our AI model gemini-pro
model = genai.GenerativeModel("gemini-pro")

# initializing conversation
chat = model.start_chat(history=[])

# functinon to speak with our model
def get_gemini_response(prompt):

    response = chat.send_message(prompt, stream=True)

    return response

# setting title of our frontend page
st.set_page_config(page_title="Doraemon.ai")

st.header("🐾Doraemon - Generative AI")

# setting chat-history if it is not exist in session_state
if "chat_history" not in st.session_state:

    st.session_state["chat_history"] = []

# taking prompt from Nobita, users we are the Nobita :)
input = st.text_input("Your prompt:",key="input")

# submit button
submit = st.button("Ask Doraemon")

# if prompt is given and pressed the submit button
if input and submit:

    # invoking function which helps us to speak with model alse passing user prompt as arg
    response = get_gemini_response(input)

    # setting chat_history with user message
    st.session_state["chat_history"].append(("Nobita",input))

    st.subheader("Doraemon's reply")

    # our model may return chunks of responses so loop through it 
    for msg in response:

        # writing the message to streamlit
        st.info(msg.text)

        # setting chat_history with doraemons response
        st.session_state["chat_history"].append(("Doraemon",msg.text))

# checking whether chat_history has atleast a element
if len(st.session_state["chat_history"]) > 0:

    # if yes then show this heading
    st.subheader("Chat history🤗")

else:

    # else show this heading
    st.subheader("No conversation yet😕")

# running loop on chat_history
for role,text in st.session_state["chat_history"]:
    
    # writing into streamlit to show chat_history convo
    st.write(f"{role}:{text}")

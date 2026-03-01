import streamlit as st

st.set_page_config(page_title="AI Legal Advisor", layout="centered")

st.title("⚖️ AI Legal Advisor")
st.caption("Educational purposes only. Not a substitute for a lawyer.")

# Memory for chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def legal_agent(question):
    question = question.lower()

    if "divorce" in question:
        return "Divorce can be filed under mutual consent or contested grounds under the Hindu Marriage Act."

    elif "fir" in question:
        return "You can file an FIR at any police station. Police must register it if it is a cognizable offence."

    elif "consumer" in question:
        return "You can approach Consumer Court if a product/service is defective or unfair."

    elif "property" in question:
        return "Property disputes are handled in civil court. Ensure ownership documents are clear."

    elif "cyber" in question or "online fraud" in question:
        return "You can report cyber crimes on the National Cyber Crime Portal or nearest police station."

    elif "arrest" in question:
        return "You have the right to know the reason for arrest and the right to contact a lawyer."

    elif "contract" in question:
        return "A valid contract requires offer, acceptance, lawful consideration, and free consent."

    else:
        return "This is general legal information. Please consult a qualified lawyer for specific advice."

# User input
user_input = st.text_input("Ask your legal question:")

if st.button("Send") and user_input:

    response = legal_agent(user_input)

    # Save to history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("AI", response))

# Display chat history
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 {sender}:** {message}")
    else:
        st.markdown(f"**🤖 {sender}:** {message}")
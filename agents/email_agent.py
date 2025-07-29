import streamlit as st
import google.generativeai as genai

def generate_email_response(email_text, tone):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

        model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

        prompt = f"""
        You are an AI assistant specialized in drafting professional and effective email replies.
        Your goal is to provide a concise and appropriate response.

        Please draft an email reply with a "{tone.lower()}" tone to the following email:

        Email Content to Reply To:
        "{email_text}"

        Draft your response here:
        """

        gemini_response = model.generate_content(prompt)

        if gemini_response.candidates and gemini_response.candidates[0].content.parts:
            generated_text = "".join(part.text for part in gemini_response.candidates[0].content.parts if hasattr(part, 'text'))
            return generated_text
        else:
            return "Failed to generate a response from Gemini. No content in response."

    except Exception as e:
        st.error(f"An error occurred with the Gemini API. Please check your API key and model access: {e}")
        return f"Error: Could not generate email response. Details: {e}"
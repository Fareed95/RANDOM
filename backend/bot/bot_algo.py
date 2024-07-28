import textwrap
import google.generativeai as genai
from IPython.display import display, Markdown
import re
from dotenv import load_dotenv
import os



load_dotenv()
# Function to convert text to Markdown format
def bot_gemini(user_input):
    def to_markdown(text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

    # Set your API key directly (replace with your actual API key)
    
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

    if not GOOGLE_API_KEY:
        raise ValueError("No API key found. Please set the GOOGLE_API_KEY environment variable.")

    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

    try:
        # Generate content based on user input
        response = model.generate_content(user_input)

        # Extract and display the generated text content
        content = response.candidates[0].content.parts[0].text

        cleaned_string = re.sub(r'[*\n]', '', content)
        # print(cleaned_string)

        return cleaned_string

    except Exception as e:
        print(f"Error generating content: {e}")
if __name__ == "__main__":
    print(bot_gemini("What is water?"))
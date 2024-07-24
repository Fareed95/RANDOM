import textwrap
import google.generativeai as genai
from IPython.display import display, Markdown

# Function to convert text to Markdown format
def bot_gemini(user_input):
    def to_markdown(text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

    # Set your API key directly (replace with your actual API key)
    GOOGLE_API_KEY = 'AIzaSyDLW0ZzUp32rgwCYVMsnTGNwuhn1ZOTels'

    genai.configure(api_key=GOOGLE_API_KEY)

    # List available models (optional)
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                # print(m.name)
                pass
    except Exception as e:
        print(f"Error listing models: {e}")
        

    # Initialize the generative model
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Prompt user for input
    # user_input = input("Enter the data that Gemini should generate: ")

    try:
        # Generate content based on user input
        response = model.generate_content(user_input)

        # Extract and display the generated text content
        content = response.candidates[0].content.parts[0].text
        return content
        # display(to_markdown(content))

    except Exception as e:
        print(f"Error generating content: {e}")
if __name__ == "__main__":
    print(bot_gemini("What is water?"))
# client_test.py
# --------------------------------------------------
# This file is used ONLY for testing and learning AI integration.
# I created this file to understand how AI APIs work independently
# before integrating them into the main Jarvis project.
#
# This helps in:
# - Testing API responses
# - Understanding request/response structure
# - Experimenting without breaking the main code
# --------------------------------------------------


# NOTE: Replace the placeholder key with your own API key before running



# Using Groq AI for fast and free (limited) inference during testing

# Simple test prompt to confirm the AI integration works correctly
from groq import Groq

client = Groq(api_key="Groq_API_Key")

response = client.chat.completions.create(
    model="openai/gpt-oss-120b", # Model name can be checked on Groq's website
                                 # Other models can also be used
    messages=[
        {"role": "system", "content": "You are Jarvis, a helpful assistant."},
        {"role": "user", "content": "Who is the President of India?"}
    ]
)

# Print AI response to verify integration
print(response.choices[0].message.content)





# --------------------------------------------------
# Google Gemini API (for learning and comparison)
# NOTE:
# Gemini has strict rate limits and usage restrictions.
# This code is kept for reference and experimentation only.
# --------------------------------------------------




## OPTIONAL (Highly Recommended):

## List available models supported by your API key

# from google import genai

# client = genai.Client(api_key="Google_Cloud_API_Key")

# try:
#     models = list(client.models.list())
#     print("Models visible to this key:")
#     for m in models:
#         print(m.name)
# except Exception as e:
#     print("ERROR:", e)


# Example usage of Gemini text generation
# This was tested to understand prompt formatting and responses

# from google import genai

# client = genai.Client(api_key="Google_Cloud_API_Key")

# SYSTEM_PROMPT = "You are Jarvis, a helpful assistant."
# USER_INPUT = "Who is president of India?"

# response = client.models.generate_content(
#     model="models/gemini-2.5-pro", # Any supported model can be used
#     contents=f"{SYSTEM_PROMPT}\n\nUser: {USER_INPUT}"
# )

# print(response.text)




# --------------------------------------------------
# OpenAI API (PAID)
# This section is kept for learning purposes only.
# OpenAI APIs require billing to be enabled.
# --------------------------------------------------


# from openai import OpenAI
# # client = OpenAI() 
# # defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# # if you need the key under different environment variable name,you can do smothing like:


# client = OpenAI(
#     api_key="YOUR_OPENAI_API_KEY"
# )

# response = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant."
#         },
#         {
#             "role": "user",
#             "content": "What is coding?"
#         }
#     ]
# )

# print(response.choices[0].message.content)

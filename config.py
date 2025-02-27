import google.generativeai as genai
from api_read import GEMINI_API_KEY

# Gemini API'yi yapılandır
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")
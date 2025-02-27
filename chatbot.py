from config import model
from file_utils import read_file
from url_utils import read_from_url


def chatbot_interface(message, file, url, chat_history):
    """Chatbot’un ana mantığı."""
    if chat_history is None:
        chat_history = []

    user_input = message if message else "Dosya veya URL’yi analiz et"
    file_content = ""
    url_content = ""

    if url:
        url_content = read_from_url(url)

    if file:
        file_content = read_file(file.name)

    prompt = f"Kullanıcı: {user_input}\n"
    if file_content:
        prompt += f"Dosya içeriği: {file_content}\n"
    if url_content:
        prompt += f"URL içeriği: {url_content}\n"

    if not user_input and not file and not url:
        prompt = "Merhaba, ne yapmamı istersin?"

    if chat_history:
        history_text = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in chat_history])
        prompt = f"Önceki sohbet:\n{history_text}\n\n{prompt}"

    response = model.generate_content([prompt])

    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": response.text})

    return chat_history, None, ""  # Dosya ve URL alanlarını sıfırlamak için
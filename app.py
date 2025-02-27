import gradio as gr
from chatbot import chatbot_interface

# 📌 **Arayüz (Gradio)**
with gr.Blocks(title="📜 Gelişmiş Sohbet ve Dosya Analiz Botu", css="body { background-color: #f4f4f4; }") as interface:
    gr.HTML(
        """
        <h1 style='text-align: center; color: #333;'>💬 Gelişmiş Sohbet ve Analiz Botu</h1>
        <p style='text-align: center; font-size: 16px; color: #555;'>Dosya veya URL yükleyerek analiz et, akıllı asistanın cevaplasın!</p>
        """
    )

    with gr.Row():
        chatbot = gr.Chatbot(
            label="💬 Sohbet Geçmişi",
            type="messages",
            height=450,
            bubble_full_width=False,
            avatar_images=("https://cdn-icons-png.flaticon.com/512/9131/9131529.png",
                           "https://cdn-icons-png.flaticon.com/512/2995/2995626.png"),
        )
        chat_history = gr.State([])

    with gr.Row():
        message = gr.Textbox(
            placeholder="💡 Sorunu sor veya talimat ver...",
            label="Mesaj",
            interactive=True,
            elem_id="message_input"
        )

    with gr.Accordion("📂 Dosya ve URL Yükleme", open=False, elem_id="file_section"):
        file_input = gr.File(label="📄 **Dosya Yükle** (TXT, PDF, DOCX, MP3, WAV, M4A, PNG, JPG)")
        url_input = gr.Textbox(
            placeholder="🔗 URL gir (https://example.com)",
            label="URL",
            interactive=True,
            elem_id="url_input"
        )

    with gr.Row():
        submit_btn = gr.Button("🚀 **Gönder**", variant="primary", elem_id="submit_btn")
        clear_btn = gr.Button("🗑 **Temizle**", variant="secondary", elem_id="clear_btn")

    submit_btn.click(
        fn=chatbot_interface,
        inputs=[message, file_input, url_input, chat_history],
        outputs=[chatbot, file_input, url_input]
    )

    clear_btn.click(lambda: ([], None, ""), inputs=[], outputs=[chatbot, file_input, url_input])

# 📌 **Özel CSS Stilleri**
interface.css = """
#message_input, #url_input {
    border-radius: 8px;
    padding: 12px;
    font-size: 16px;
}
#submit_btn, #clear_btn {
    border-radius: 6px;
    font-size: 18px;
    padding: 12px 20px;
    transition: 0.3s;
}
#submit_btn:hover {
    background-color: #4CAF50 !important;
    color: white;
}
#clear_btn:hover {
    background-color: #f44336 !important;
    color: white;
}
#file_section {
    border-radius: 10px;
    background-color: #ffffff;
    padding: 10px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}
"""

if __name__ == "__main__":
    interface.launch()
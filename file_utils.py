import fitz
import docx
from pydub import AudioSegment
import os
from config import model


def read_file(file_path):
    """Dosya türüne göre içeriği okur."""
    if not file_path:
        return ""

    ext = file_path.split(".")[-1].lower()

    if ext == "txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    elif ext == "pdf":
        doc = fitz.open(file_path)
        return "\n".join([page.get_text() for page in doc])

    elif ext == "docx":
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])

    elif ext in ["mp3", "wav", "m4a"]:
        return transcribe_audio(file_path)

    else:
        return "Bu dosya formatı desteklenmiyor!"


def transcribe_audio(file_path):
    """Ses dosyasını metne çevirir."""
    audio = AudioSegment.from_file(file_path)
    wav_path = "temp.wav"
    audio.export(wav_path, format="wav")

    with open(wav_path, "rb") as f:
        audio_bytes = f.read()

    os.remove(wav_path)

    response = model.generate_content(
        ["Bu ses kaydını metne çevir:", {"mime_type": "audio/wav", "data": audio_bytes}]
    )

    return response.text
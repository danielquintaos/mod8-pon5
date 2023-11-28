from gtts import gTTS
import os

def text_to_speech(text, language='en'):
    """
    Converte o texto fornecido em fala e salva como um arquivo MP3.

    Args:
    text (str): O texto a ser convertido em fala.
    language (str): O idioma da fala (padrão é inglês 'en').

    Returns:
    str: O caminho do arquivo de áudio gerado.
    """
    tts = gTTS(text, lang=language)
    audio_file = "speech.mp3"
    tts.save(audio_file)
    return audio_file

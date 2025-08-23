import gradio as gr
from chatbot import ai_chatbot

PAGE_TITLE = "Caramel AI Chatbot !"
LOGO_URL = "https://raw.githubusercontent.com/hereandnowai/images/refs/heads/main/logos/logo-of-here-and-now-ai.png"
ASSISTANT_AVATAR_URL = "https://raw.githubusercontent.com/hereandnowai/images/refs/heads/main/logos/caramel-face.jpeg"

description_md = f"""<img src='{LOGO_URL}' width='500' style='display: block; margin: auto;'>
                     <br>Your friendly AI teacher for learning the basics of Artificial Intelligence!"""

gr.ChatInterface(
    fn=ai_chatbot,
    chatbot=gr.Chatbot(type='messages', avatar_images=[None, ASSISTANT_AVATAR_URL]),
    title=PAGE_TITLE,
    description=description_md,
    examples=["What is AI?", "What does GPT stand for?", "Explain Neural Network!", "What is RLHF"],
    type='messages'
).queue().launch()
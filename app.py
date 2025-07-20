# Add to your repository
import gradio as gr
from main import RoboTeacher

teacher = RoboTeacher()

def chat(input_text):
    if "exit" in input_text.lower():
        return "Goodbye!"
    return teacher.planner.generate_response(input_text)

interface = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(label="Ask Robo Teacher"),
    outputs=gr.Textbox(label="Response"),
    title="🤖 Robo Teacher Cloud Edition"
)

interface.launch(share=True)  # Creates public URL
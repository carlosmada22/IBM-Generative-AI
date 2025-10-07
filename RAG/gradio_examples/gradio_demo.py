import gradio as gr

def add_sentences(Txt1, Txt2):
    return Txt1 + "/" + Txt2

# Define the interface
demo = gr.Interface(
    fn=add_sentences, 
    inputs=[gr.Textbox(), gr.Textbox()],
    outputs=gr.Textbox()
)

# Launch the interface
demo.launch(server_name="127.0.0.1", server_port= 7880)
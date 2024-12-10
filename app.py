# from g4f.client import Client

# client = Client()
# response = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "Tell me most useful gadget of Doraemon other than pocket and why?"}],
# )
# print(response.choices[0].message.content)


#inporting necessary libraries
from g4f.client import Client
import gradio as gr

#Initialize the gf4 client
client = Client()

#define chatbot response fuction

def chatbot_response(user_input):
    response = client.chat.completions.create( 
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}],
    )
    return response.choices[0].message.content

#Gradio userinterface

interface = gr.Interface( 
    fn=chatbot_response,
    inputs=gr.Textbox(lines=2, placeholder="Type your question here..."),
    outputs="text",
    title="My First Chatbot",
    description="Your Personalised Assistant"
)

#launch the interface
if __name__ == "__main__": 
    interface.launch()
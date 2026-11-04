import gradio as gr
import os

def my_tool(input_text: str) -> str:
    """Do something with input.
    
    Args:
        input_text: The input
    
    Returns:
        The result
    """
    return f"Processed: {input_text}"

demo = gr.Interface(fn=my_tool, inputs="text", outputs="text")

if __name__ == "__main__":
    # Get the port specified by Render (defaults to 10000)
    server_port = int(os.environ.get("PORT", 7860))
    demo.launch(mcp_server=True, server_name="0.0.0.0", server_port=server_port)

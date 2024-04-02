import os
from extract_msg import Message

def msg_to_text(msg_path, output_dir):
    msg = Message(msg_path)
    text = msg.body
    
    # Generate the output file name
    file_name = os.path.splitext(os.path.basename(msg_path))[0] + ".txt"
    output_path = os.path.join(output_dir, file_name)
    
    # Save the text content to a file
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)

def convert_folder(folder_path, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".msg"):
            msg_path = os.path.join(folder_path, file_name)
            msg_to_text(msg_path, output_dir)

# Usage example
folder_path = ".\"
output_dir = ".\txt"
convert_folder(folder_path, output_dir)

# eml-to-txt

A Python script for converting .eml files to plain text (.txt) while preserving UTF-8 encoding.

## Purpose

The `eml-to-txt` script is designed to automate the conversion of email files from .eml to .txt format. This utility is particularly useful for professionals who need to extract and manipulate large sets of email data for archiving, analysis, or integration into knowledge bases and NLP (Natural Language Processing) systems.

## Functionality

- **Batch Processing**: Convert multiple .eml files in one go.
- **UTF-8 Encoding**: Maintain international character and symbol integrity post-conversion.
- **Attachment Handling**: Choose to ignore or save email attachments.
- **Header Customization**: Include or exclude email headers as needed.
- **Search and Filter**: Convert only emails containing specific keywords or patterns.
- **Integration Ready**: Easy to incorporate into data processing pipelines.

## Use Cases

- **Data Migration**: Transfer emails to different platforms in a readable format.
- **Machine Learning**: Create datasets for NLP model training.
- **Compliance and Archiving**: Archive emails for compliance with data retention policies.
- **Text Analytics**: Prepare clean text for analytics and processing tasks.

## Prerequisites

While not necessary, it is always recommended to use a virtual environment for Python projects to avoid conflicts between project dependencies.

### Setting up a Virtual Environment

To create a virtual environment in your project directory, run:

```bash
python3 -m venv venv
```
Activate the virtual environment with:

On Windows:

```cmd
venv\Scripts\activate
On macOS and Linux:
```
```bash
source venv/bin/activate
```
After activation, install the required dependencies with:

```bash
Copy code
pip install -r requirements.txt
```
Deactivate the virtual environment when done with:

```bash
deactivate
```

##Getting Started
After setting up your virtual environment and installing dependencies, run the script with your .eml files.

##Contributing
Contributions are welcome! Fork the repo, make your improvements, and submit a pull request.






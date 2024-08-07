# Anthropic CLI Assistant

## Description

a simple command line interface for claude3.5 AI, This tool supports both streaming and non-streaming modes for real-time and batch responses.

## Features

- **Streaming Mode:** Get real-time responses from the AI model as text arrives.
- **Batch Mode:** Obtain complete responses after processing is finished.
- **Token Usage Reporting:** Track the number of input and output tokens used.

## Installation

To set up the Anthropic CLI Assistant, follow these instructions:

### Prerequisites


- Python 3.8
- required libraries (e.g., `anthropic`, `python-dotenv`)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/CrocSpider/anthropic-cmd
    ```
2. Navigate to the project directory:
    ```bash
    cd anthropic-cmd
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. edit the example.env and add your API key:
    ```bash
    ANTHROPIC_API_KEY=your_api_key_here
    ```

## Usage

### Streaming Mode

Run the CLI assistant in streaming mode to receive responses in real-time:
```bash
python assist_stream.py
```
### Normal Mode

```bash
python assistant.py
```

## License

None.
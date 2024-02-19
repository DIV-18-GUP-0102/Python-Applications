# Mini Chat Bot

This is a simple chat bot built using Streamlit and OpenAI's GPT-3.5 model. The bot allows users to engage in conversation by typing messages, and the bot responds accordingly.

## Prerequisites

1. Python 3.8
2. Streamlit 1.31.1 


## Usage

To use the chat bot, follow these steps:

1. Run the Python script containing the code provided.
2. The chat bot interface will be displayed in your web browser.
3. You can start the conversation by typing a message in the input field labeled "What is 
   up?".
4. Press Enter to send your message to the bot.
5. The bot will respond to your message based on the conversation history and its AI capabilities.

## Functionality

1. The chat bot interface displays messages from both the user and the assistant (bot).
2. Users can type messages in the input field and send them to the bot.
3. The bot processes user messages using the GPT-3.5 model from OpenAI and generates responses.
4. The conversation history is displayed in the chat interface, showing both user and bot messages.

## Configuration
Before running the chat bot, I set up my OpenAI API key in the .streamlit/secrets.toml file within my Streamlit application directory.

1. Create a .streamlit folder in your Streamlit application directory if it doesn't exist.
2. Inside the .streamlit folder, create a secrets.toml file.
3. Add the following content to the secrets.toml file:
```bash
OPENAI_API_KEY = "your_api_key"
```

## Dependencies

1. Streamlit: Streamlit is used to create the web-based user interface.
2. OpenAI: The OpenAI API for accessing AI models, such as GPT-3.5.

## Usage Limits
The usage of the GPT-3.5 model is subject to the following limits:

1. TPM (Tokens per Minute): 40,000 TPM (Tokens per Minute)
2. RPM (Requests per Minute): 3 RPM (Requests per Minute)
3. RPD (Requests per Day): 200 RPD (Requests per Day)

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License
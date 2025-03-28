# Mental Health Chatbot 🤖

A simple terminal-based mental health chatbot using `llama-cpp-python` and LLaMA 2 model.

## Installation

### 1. Install Dependencies
```sh
pip install llama-cpp-python==0.1.78
```

### Create and Activate a Virtual Environment:**
   ```sh
   python3 -m venv chatbot-env
   source chatbot-env/bin/activate  
   # On Windows use `chatbot-env\Scripts\activate`
   ```
### 3. Run the Chatbot
```sh
python mental_health_chatbot.py
```

## Features
- Provides mental health support and advice.
- Uses LLaMA 2 for generating responses.
- Filters out irrelevant topics to stay focused on well-being.
- Optimized for low-end PCs (8GB RAM, Intel i5, no GPU).

## Model Requirements
- Download a suitable LLaMA 2 model (`ggmlv3.q2_K` recommended for low-end PCs).
- Place the model in the appropriate directory and update `model_path` in `mental_health_chatbot.py`.

## Usage
- Start the chatbot and type messages related to mental health.
- Type `exit` or `quit` to end the session.

## Example Interaction
```sh
You: I feel stressed
Bot: I'm here to help! What's been making you feel this way?
```

## License
This project is open-source and for educational purposes only.

## Contributing
Feel free to submit issues or contribute improvements via pull requests!
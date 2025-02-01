# Local chatbot with DeepSeek and Chainlit 🚀

A **100% local chatbot app** powered by **DeepSeek-R1** (via Ollama) and built with **Chainlit** for an intuitive chat interface.  The assistant uses the DeepSeek-R1 model to generate concise and clear responses to user queries. This app runs entirely on your local machine, ensuring privacy and security.

---

## Features ✨
- **Local Execution**: No cloud dependencies—everything runs on your machine.
- **Privacy-First**: All data stays local, perfect for sensitive use cases.
- **User-Friendly UI**: Built with **Chainlit** for a seamless chat experience.
- **Customizable Prompts**: The system prompt can be customized to guide the model's behavior.
- **Adjustable Parameters**: Temperature and max tokens can be adjusted to control the creativity and length of the responses.

---

## How It Works 🛠️
1. **User Input**: The user types a message in the Chainlit chat interface.
2. **Model Inference**: The message is sent to **DeepSeek-R1** (via Ollama) for processing.
3. **Response Generation**: DeepSeek generates a response based on the input.
4. **Output**: The response is displayed in the chat interface.

## Prerequisites

- Python 3.7 or higher
- Chainlit
- Ollama Client

## Install Ollama

1. macOS
Open a terminal and run:
   ```sh
   curl -fsSL https://ollama.com/install.sh | sh
   ```
   
2. Windows
Go to this link:
`https://ollama.com/download/windows`

### Verifying Installation
After installation, verify that Ollama is installed by running:
```sh
ollama --version
```

### Pulling a Model
To download a model, use the following command:
```sh
ollama pull <model-name>
```
For example, to pull the **Deepseek** model:
```sh
ollama pull deepseek-r1:7b
```

### Running a Model
Once the model is pulled, you can run it locally using:
```sh
ollama run mistral
```

## Local usage with UI

1. **Start the Chainlit server**:
    ```bash
    chainlit run app.py
    ```

2. **Access the UI**:
    Open your web browser and navigate to `http://localhost:8000`.

3. **Interact with the Assistant**:
    Enter your queries in the UI, and the assistant will provide real-time responses.

## Configuration

- **System Prompt**: Modify the `system_prompt` variable in `app.py` to customize the assistant's behavior.
- **Model Parameters**: Adjust the `temperature` and `max_tokens` in the `client.generate` method to control the response characteristics.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.




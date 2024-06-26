# Conversation LLM Agents

# Introduction

ConversationAI is a Python-based application that simulates conversations between a salesman and a customer. It leverages the power of the Crew AI framework, which utilizes AI agents to generate realistic and engaging dialogues. This application is designed to assist businesses in understanding customer needs, addressing objections, and showcasing product features and benefits effectively.


# Features

- **Configurable Product Details:** The application allows you to specify the product or service you want to simulate conversations for, enabling customized dialogues tailored to your offerings.
- **Multiple Conversation Rounds:**  You can generate multiple rounds of conversations, providing a comprehensive set of potential customer interactions and responses.
- **CSV Output:** The simulated conversations are saved in a CSV file for easy analysis and review.
- **Agent Roles:** The application utilizes two distinct agent roles: the Salesman and the User. The Salesman agent is trained to present products persuasively, highlight features and benefits, and address customer concerns. The User agent is designed to ask relevant questions and engage with the Salesman's responses.
- **Sequential Processing:** The application follows a sequential process, where the User agent generates a question based on the Salesman's previous response, and the Salesman agent then provides a detailed and persuasive answer to the User's question.

# Installation

1. Clone the repository:
```sh
git clone https://github.com/saivarshithh/LLM Agents using CrewAI.git
```

2. Navigate to the project directory:

```sh
cd LLM Agents
```

3. Install the required dependencies:

```sh
pip install -r requirements.txt
```

4. Set up the necessary environment variables by creating a `.env` file in the project root directory. You'll need to provide your `GOOGLE_API_KEY` and `SERPER_API_KEY`:

```bash
GOOGLE_API_KEY=your_google_api_key
SERPER_API_KEY=your_seper_api_key
```

# Usage

1. Run the `crew.py` script:
 
```python
python crew.py
```

2. When prompted, enter the name of the product or service you want to simulate conversations for.
3. Enter the number of conversation rounds you want to generate.
4. The application will generate the specified number of conversations and save them in a CSV file with the format `{product}_conversations.csv`.


# Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

# License
This project is licensed under the MIT License.

# Acknowledgments

This project was built using the following libraries:

- Crew AI
- LangChain Google Generative AI
- Python-dotenv

Special thanks to the Crew AI and LangChain communities for their excellent tools and resources.

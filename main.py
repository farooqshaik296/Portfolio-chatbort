from flask import Flask, request, jsonify, render_template_string
from llamaapi import LlamaAPI

# Initialize Flask app
app = Flask(__name__)

# Initialize the LlamaAPI SDK
llama = LlamaAPI("LA-ae1c878f9f364c11be3bd2bf1a5ec0c07c3ce86456bc46e284987fe1cccb4af0")

# API endpoint to handle questions
@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question', '')

    if not question:
        return jsonify({'error': 'No question provided'}), 400

    # Build the API request
    api_request_json = {
        "messages": [
            {"role": "system", "content": "You are an AI assistant that answers questions based on a resume"},
            {"role": "user", "content": "Here is the resume: SHAIK FAROOQ\nB.Tech CSE from DSU Trichy | Seeking Data Analyst role\n[farooq20903@gmail.com](mailto:farooq20903@gmail.com)\n+91 6300288724\nTrichy, India\nLinkedIn | GitHub\n\nEDUCATION\nB.Tech in Computer Science and Engineering\nDhanalakshmi Srinivasan University, Trichy\nMay 2025\nTrichy, India\nCGPA: 7.5/10\n\nIntermediate\nNarayana Junior College\nApril 2021\nOngole, India\nCGPA: 8.6/10\n\nEXPERIENCE\nData Analyst Intern\nYoshops\nNov 2023 – Jan 2024\nRemote\n Conducted data analysis on online shopping sales data to identify key trends and patterns.\n Utilized Python and Pandas for data preprocessing, cleaning, and feature engineering.\n Created data visualizations and interactive dashboards to communicate insights effectively.\n Collaborated with cross-functional teams to extract actionable insights and optimize sales strategies.\n\nTECHNICAL SKILLS\nProgramming Languages\nPython SQL\n\nData Analysis\nData Cleaning Data Visualization Statistical Analysis\nPandas NumPy Matplotlib Seaborn Excel\nExploratory Data Analysis (EDA) Power BI\n\nMachine Learning\nSupervised Learning Unsupervised Learning Scikit-Learn\nXGBoost Random Forest SVM Clustering\nDimensionality Reduction\n\nTools & Technologies\nGit Jupyter VS Code MongoDB SQL Server\n\nPROJECTS\nGoogle Playstore EDA\n Processed and cleaned data to handle missing values, duplicates, and inconsistencies.\n Analyzed key metrics such as app ratings, review counts, and installation numbers to understand their distribution and relationships.\n Created comprehensive visualizations using Matplotlib and Seaborn to illustrate trends, correlations, and outliers.\n Performed sentiment analysis on user reviews to gauge user satisfaction and identify common issues.\n Skills: Python SQL PowerBI\n\nCOVID-19 Exploratory Data Analysis\n Processed and cleaned COVID-19 datasets to ensure data quality and accuracy.\n Analyzed global COVID-19 data to understand the spread and impact of the virus across different countries.\n Created sophisticated visualizations to highlight key findings and patterns in the data.\n Examined the socioeconomic impact of COVID-19, identifying correlations between virus spread and socioeconomic factors.\n Skills: Python Pandas NumPy Matplotlib Seaborn Jupyter Notebook\n\nTrading Results Display\n Developed a web application to display trading results using historical and real-time data.\n Designed an intuitive user interface with Bootstrap for displaying trading metrics and visualizations.\n Implemented efficient data handling and storage using SQLite.\n Created sophisticated visualizations to highlight key findings and patterns in the trading data.\n Skills: Python Flask SQLite Bootstrap Data Analysis Data Visualization\n\nLEADERSHIP\nVice President, AI Club\nDhanalakshmi Srinivasan University, Trichy\nSep 2023 – Present\nTrichy, India\n Spearheaded AI workshops and seminars, and coordinated with industry professionals for guest lectures and hands-on sessions.\n Led AI-based projects, managed club activities, and organized competitions and hackathons.\n\nLinks\n[LinkedIn](https://www.linkedin.com/in/shaik-farooq-ab2b20228/)\n[GitHub](https://github.com/farooqshaik296)\n[COVID-19 Data Analysis Project](https://github.com/farooqshaik296/covid19_data_analysis)\n[Trading Results Project](https://github.com/farooqshaik296/trading_results)\n\n---\nLet me know if you need any further adjustments or help!,my name is shaik farooq"},
            {"role": "user", "content": question},
        ],
        "stream": False,
    }

    # Execute the Request
    response = llama.run(api_request_json)

    # Extract and return the answer
    answer = response.json()['choices'][0]['message']['content']
    return jsonify({'answer': answer})

# Frontend HTML template
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resume Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .chat-container {
            width: 375px;
            max-width: 100%;
            background-color: white;
            border-radius: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }
        .chat-header {
            background-color: #007bff;
            color: white;
            padding: 15px;
            text-align: center;
            font-size: 1.2rem;
            font-weight: bold;
        }
        .chat-messages {
            padding: 20px;
            height: 400px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
        }
        .message {
            margin-bottom: 15px;
            display: flex;
            align-items: flex-end;
        }
        .message.user {
            justify-content: flex-end;
        }
        .message.bot {
            justify-content: flex-start;
        }
        .message p {
            max-width: 70%;
            padding: 10px 15px;
            border-radius: 20px;
            background-color: #e4e6eb;
            margin: 0;
            font-size: 0.9rem;
        }
        .message.user p {
            background-color: #007bff;
            color: white;
        }
        .message.bot p {
            background-color: #f1f0f0;
            color: black;
        }
        .input-container {
            display: flex;
            padding: 10px;
            border-top: 1px solid #ddd;
        }
        input[type="text"] {
            flex: 1;
            padding: 10px;
            border-radius: 20px;
            border: 1px solid #ddd;
            outline: none;
        }
        button {
            background-color: #007bff;
            border: none;
            color: white;
            padding: 10px 20px;
            margin-left: 10px;
            border-radius: 20px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">Resume Chatbot</div>
        <div class="chat-messages" id="chat-messages">
            <!-- Messages will appear here -->
        </div>
        <div class="input-container">
            <input type="text" id="question" placeholder="Ask a question about the resume...">
            <button onclick="askQuestion()">Send</button>
        </div>
    </div>

    <script>
        function createMessageElement(content, sender) {
            const messageDiv = document.createElement('div');
            messageDiv.classList.add('message', sender);
            const messageText = document.createElement('p');
            messageText.textContent = content;
            messageDiv.appendChild(messageText);
            return messageDiv;
        }

        function askQuestion() {
            const question = document.getElementById('question').value;
            if (!question) return;

            const chatMessages = document.getElementById('chat-messages');

            // Add user message at the end
            const userMessage = createMessageElement(question, 'user');
            chatMessages.appendChild(userMessage);

            // Clear input
            document.getElementById('question').value = '';

            fetch('/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ question: question }),
            })
            .then(response => response.json())
            .then(data => {
                // Add bot response at the end
                const botMessage = createMessageElement(data.answer, 'bot');
                chatMessages.appendChild(botMessage);

                // Scroll to the bottom of the chat
                chatMessages.scrollTop = chatMessages.scrollHeight;
            })
            .catch(error => {
                // Handle errors
                console.error('Error:', error);
                const errorMessage = createMessageElement('An error occurred. Please try again.', 'bot');
                chatMessages.appendChild(errorMessage);
                chatMessages.scrollTop = chatMessages.scrollHeight;
            });
        }
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True)

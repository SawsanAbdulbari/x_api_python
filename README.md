# 🎉 X Bot Project

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

This project is a X bot that automates various X operations such as posting tweets, liking tweets, and managing followers. It is built using the Tweepy library and is designed to interact with the X API.

## 📚 Table of Contents

- [📥 Installation](#installation)
  - [🔧 Prerequisites](#prerequisites)
  - [⚙️ Setup](#setup)
- [🔑 Configuration](#configuration)
- [🚀 Usage](#usage)
  - [🛠️ Available Commands](#available-commands)
- [✨ Features](#features)
- [📝 Logging](#logging)
- [⚠️ Error Handling](#error-handling)
- [🤝 Contributing](#contributing)
- [📜 License](#license)
- [📞 Contact](#contact)

## 📥 Installation

### 🔧 Prerequisites

- Python 3.7 or higher
- X Developer Account for API keys

### ⚙️ Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername X-bot.git
   cd X-bot
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## 🔑 Configuration

1. Create a `.env` file in the root directory and add your X API credentials:
   ```plaintext
   API_KEY=your_api_key
   API_SECRET_KEY=your_api_secret_key
   ACCESS_TOKEN=your_access_token
   ACCESS_TOKEN_SECRET=your_access_token_secret
   BEARER_TOKEN=your_bearer_token
   ```

2. Update the `config/config.py` file with the correct data path:
   ```python
   data_path = "path/to/your/data/directory"
   ```

## 🚀 Usage

To run the bot, use the following command with the desired options:

```bash
python main.py --post-text
```

### 🛠️ Available Commands

- `--post-text`: Post a text-only tweet.
- `--post-image`: Post a tweet with an image.
- `--like-tweet`: Like a tweet.
- `--get-followers`: Get the list of followers.
- `--get-following`: Get the list of users you are following.
- `--delete-tweet`: Delete the last tweet.

## ✨ Features

- Post text-only tweets and tweets with images.
- Like and delete tweets.
- Retrieve followers and following lists.
- Rate limit handling with automatic retries.
- Pin and unpin lists.
- Get user lists.
- Test mode to simulate operations without making API calls.
- Read data from files.
- Check if directory exists.
- Write tweet ID to file.
- Read tweet ID from file.
- Read file content.
- Get user ID.
- Get user details.
- Get user lists.
- Get user tweets.
- Get user tweets count.
- Get user followers count.
- Get user following count.
- Get user tweets count.

## 📝 Logging

The project uses a custom logging configuration to output logs to the console. Logs are color-coded based on the log level for better readability.

## ⚠️ Error Handling

Errors are logged with detailed messages to help diagnose issues. The bot handles rate limits by pausing and retrying operations.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## 📜 License

This project is licensed under the MIT License.

## 📞 Contact

For questions or support, please contact [Sawsan Abdulbari](https://www.linkedin.com/in/sawsanabdulbari/).

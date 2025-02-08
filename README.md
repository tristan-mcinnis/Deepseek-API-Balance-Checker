# DeepSeek Balance Checker

A simple Python script to check your DeepSeek API account balance.

## Description

This script makes an HTTP GET request to the DeepSeek API to retrieve your account balance information. It uses environment variables to securely store your API key.

## Prerequisites

- Python 3.x
- `requests` library
- `python-dotenv` library
- A DeepSeek API key

## Installation

1. Install the required packages:
```bash
pip install requests python-dotenv
```

2. Create a `.env` file in the root directory of your project and add your DeepSeek API key:
```
DEEPSEEK_API_KEY=your_api_key_here
```

## Usage

Simply run the script:
```bash
python balance_checker.py
```

The script will output your current DeepSeek API account balance information in JSON format.

## Environment Variables

- `DEEPSEEK_API_KEY`: Your DeepSeek API authentication token

## Security Note

Never commit your `.env` file to version control. Make sure to add `.env` to your `.gitignore` file.

## License

This project is open source and available under the MIT License.

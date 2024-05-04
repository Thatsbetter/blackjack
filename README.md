# Telegram Blackjack Bot

This is a Telegram bot designed to play the simple card game of Blackjack with users. Built with Python and using the `pyTelegramBotAPI` library, this bot allows users to engage in an interactive Blackjack game experience directly within the Telegram platform.

## Features

- Start a new game of Blackjack
- Hit to take a new card
- Stay to stop taking cards
- Automatic scoring and dealer behavior
- Simple and responsive user interface with custom Telegram keyboards

## Prerequisites

Before you begin, make sure you have the following installed:
- Python 3.6 or later
- pip (Python package installer)

## Installation

To set up the Blackjack Bot on your local machine:

1. Clone this repository:  
   `git clone https://github.com/yourusername/telegram-blackjack-bot.git`
2. Navigate to the project directory:  
   `cd telegram-blackjack-bot`
3. Install required packages:  
   `pip install -r requirements.txt`
4. Create a `credential.json` file in the root directory where `credential.py` is located, with the following structure:

   

json
   {
     "telegram_api_token": "your_bot_token"
   }
   



   Replace `your_bot_token` with the actual token that you receive from the BotFather after creating your bot.

## Usage

To run the bot:

bash
python main.py



The bot will start polling for messages. Interact with the bot via the Telegram app by starting a conversation. Use the `/start` or `/help` command to see introductory information.

## Commands

- `/start` - Welcomes the user and provides information on how to play.
- `/play` - Starts a new game.
- `/hit` - Deals another card to the player.
- `/stay` - Ends the player's turn and lets the dealer play.
- `/stop` - Ends the current game.

## Development

Want to contribute? Great! You can follow these steps to make changes and test them:

1. Fork the repo on GitHub.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License.
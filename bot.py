from telebot import TeleBot, types

from deck import Deck, Player
from credential import Credential

TOKEN = Credential().get_telegram_token()
bot = TeleBot(TOKEN)

user_game_state = {}

def create_game(user_id):
    deck = Deck()
    player = Player()
    dealer = Player()
    player.add_cards(deck.draw_cards(2))
    dealer.add_cards(deck.draw_cards(2))

    user_game_state[user_id] = {
        'deck': deck,
        'player': player,
        'dealer': dealer,
        'game_active': True
    }

    return user_game_state[user_id]


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Blackjack Bot! Type /play to start a game.")


@bot.message_handler(commands=['play'])
def new_game(message):
    user_id = message.chat.id
    if user_id in user_game_state and user_game_state[user_id]['game_active']:
        bot.send_message(user_id, "You already have an ongoing game! Type /stop to end it if you wish to restart.")
        return

    game_state = create_game(user_id)
    bot.send_message(user_id, render_game_state(game_state, reveal_dealer=False), reply_markup=get_keyboard())

@bot.message_handler(commands=['stop'])
def stop_game(message):
    user_id = message.chat.id
    if user_id in user_game_state and user_game_state[user_id]['game_active']:
        # Mark the current game as inactive
        user_game_state[user_id]['game_active'] = False
        bot.send_message(user_id, "Your game has been stopped. Thank you for playing!")
    else:
        bot.send_message(user_id, "You don't have an active game currently.")
@bot.callback_query_handler(func=lambda call: call.data in ['hit', 'stay'])
def handle_query(call):
    user_id = call.message.chat.id
    response = process_game_action(call.data, user_game_state[user_id])

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=response)
    bot.answer_callback_query(call.id)

    if user_game_state[user_id]['game_active']:
        bot.send_message(user_id, render_game_state(user_game_state[user_id], reveal_dealer=False), reply_markup=get_keyboard())
    else:
        bot.send_message(user_id, render_game_state(user_game_state[user_id], reveal_dealer=True))


def process_game_action(action, game_state):
    player = game_state['player']
    dealer = game_state['dealer']
    deck = game_state['deck']
    response = ""

    if action == "hit":
        player.add_card(deck.draw_card())
        if player.calculate_score() > 21:
            game_state['game_active'] = False
            response = "❌ You bust! ❌"
        else:
            response = f"You hit. Your score is now {player.calculate_score()}."
    elif action == "stay":
        response = end_game(game_state)

    return response


def end_game(game_state):
    dealer = game_state['dealer']
    deck = game_state['deck']

    while dealer.calculate_score() < 17:
        dealer.add_card(deck.draw_card())

    return compare_scores(game_state)

def compare_scores(game_state):
    player_score = game_state['player'].calculate_score()
    dealer_score = game_state['dealer'].calculate_score()

    if player_score > 21:
        result = "❌ Busted! ❌"
    elif dealer_score > 21 or player_score > dealer_score:
        result = "🏆You Won! 🏆"
    elif player_score < dealer_score:
        result = "❌ Dealer wins.❌"
    else:
        result = "🟰 It's a draw. 🟰"

    game_state['game_active'] = False
    return result


def render_game_state(game_state, reveal_dealer):
    player_score = game_state['player'].calculate_score()
    player_hand = game_state['player'].show_hand(True)
    dealer_hand = game_state['dealer'].show_hand(reveal_dealer)

    return f"Your hand: {player_hand}\n Your Score = {player_score} \n \n Dealer's hand: {dealer_hand}"


def get_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Hit 🃏", callback_data="hit"),
               types.InlineKeyboardButton("Stay ✋", callback_data="stay"))
    return markup


if __name__ == '__main__':
    bot.polling()

import streamlit as st
import random

# New Color Theme
PLAYER1_COLOR = "#FF6B6B"  # Coral red
PLAYER2_COLOR = "#4ECDC4"  # Tiffany blue
BG_COLOR = "#292F36"      # Dark slate
TEXT_COLOR = "#F7FFF7"    # Almost white
WIN_COLOR = "#FFE66D"     # Yellow for winning cells
ACCENT_COLOR = "#6B5B95"  # Purple for accents

# Player configuration
PLAYERS = {
    'X': {'color': PLAYER1_COLOR, 'name': "Player 1 (Red)", 'symbol': 'X'},
    'O': {'color': PLAYER2_COLOR, 'name': "Player 2 (Blue)", 'symbol': 'O'},
    ' ': {'color': BG_COLOR, 'name': " ", 'symbol': ' '}
}

class TicTacToe:
    def __init__(self):
        self.reset_state()
        self.current_player = 'X'  # Player X starts first

    def reset_state(self):
        """Reset the game state"""
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        self.win_combo = []
        self.current_player = random.choice(['X', 'O'])  # Random starting player

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            self.win_combo = []  # Reset before checking for winner
            if self.check_winner(square, letter):
                self.current_winner = letter
            else:
                # Switch player if no winner yet
                self.current_player = 'O' if letter == 'X' else 'X'
            return True
        return False

    def check_winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            self.win_combo = [row_ind*3, row_ind*3+1, row_ind*3+2]
            return True

        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            self.win_combo = [col_ind, col_ind+3, col_ind+6]
            return True

        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                self.win_combo = [0, 4, 8]
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                self.win_combo = [2, 4, 6]
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

def main():
    # Custom CSS for styling
    st.markdown(f"""
    <style>
        .stApp {{
            background-color: {BG_COLOR};
            color: {TEXT_COLOR};
        }}
        .stButton>button {{
            width: 100%;
            height: 100px;
            font-size: 48px;
            font-weight: bold;
            margin: 2px;
            background-color: {BG_COLOR};
            color: {TEXT_COLOR};
            border: 2px solid {ACCENT_COLOR};
            transition: all 0.3s ease;
        }}
        .stButton>button:hover {{
            transform: scale(1.02);
            box-shadow: 0 0 15px {ACCENT_COLOR};
        }}
        .header {{
            color: {TEXT_COLOR};
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        .status {{
            font-size: 1.5em;
            text-align: center;
            margin: 20px 0;
            padding: 15px;
            border-radius: 10px;
            background-color: rgba(0,0,0,0.2);
        }}
        .reset-btn {{
            width: 100% !important;
            height: auto !important;
            background-color: {ACCENT_COLOR} !important;
            color: white !important;
            padding: 15px !important;
            font-size: 1.2em !important;
            border: none !important;
            border-radius: 10px !important;
            transition: all 0.3s ease !important;
            margin-top: 20px !important;
        }}
        .reset-btn:hover {{
            background-color: {PLAYER1_COLOR} !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3) !important;
        }}
        .player-display {{
            font-size: 1.5em;
            text-align: center;
            margin-bottom: 20px;
            padding: 10px;
            border-radius: 8px;
            background-color: rgba(0,0,0,0.1);
        }}
        .current-player {{
            box-shadow: 0 0 20px {ACCENT_COLOR};
            border: 2px solid {TEXT_COLOR} !important;
        }}
        .winning-cell {{
            animation: winner-glow 1s ease-in-out infinite alternate;
            background-color: rgba(255, 230, 109, 0.3) !important;
        }}
        @keyframes winner-glow {{
            from {{
                box-shadow: 0 0 5px {WIN_COLOR};
                transform: scale(1);
            }}
            to {{
                box-shadow: 0 0 20px {WIN_COLOR}, 0 0 30px {WIN_COLOR};
                transform: scale(1.05);
            }}
        }}
        .turn-indicator {{
            font-size: 1.2em;
            text-align: center;
            margin: 15px 0;
            padding: 10px;
            border-radius: 5px;
            background-color: rgba(107, 91, 149, 0.2);
        }}
    </style>
    """, unsafe_allow_html=True)

    st.title("🎮 Tic-Tac-Toe: Two Player Mode")
    st.markdown(f'<div class="header">Classic Tic-Tac-Toe Game</div>', unsafe_allow_html=True)

    # Initialize game state
    if 'game' not in st.session_state:
        game = TicTacToe()
        st.session_state.game = game

    game = st.session_state.game

    # Player indicators with current player highlight
    col1, col2 = st.columns(2)
    with col1:
        player1_class = "current-player" if game.current_player == 'X' else ""
        st.markdown(
            f"""<div class='player-display {player1_class}' style='color:{PLAYERS['X']['color']}'>
            {PLAYERS['X']['name']}</div>""", 
            unsafe_allow_html=True
        )
    with col2:
        player2_class = "current-player" if game.current_player == 'O' else ""
        st.markdown(
            f"""<div class='player-display {player2_class}' style='color:{PLAYERS['O']['color']}'>
            {PLAYERS['O']['name']}</div>""", 
            unsafe_allow_html=True
        )

    # Turn indicator
    current_player_name = PLAYERS[game.current_player]['name']
    st.markdown(
        f"""<div class='turn-indicator'>
        Current Turn: <span style='color:{PLAYERS[game.current_player]['color']}; font-weight:bold'>
        {current_player_name}</span></div>""", 
        unsafe_allow_html=True
    )

    # Display board
    st.markdown("<div class='header'>Game Board</div>", unsafe_allow_html=True)
    cols = st.columns(3)
    
    for i in range(9):
        with cols[i % 3]:
            if game.board[i] == ' ' and game.current_winner is None:
                if st.button(' ', key=f'btn_{i}'):
                    # Make move for current player
                    game.make_move(i, game.current_player)
                    st.rerun()
            else:
                player = game.board[i]
                winner_class = "winning-cell" if game.current_winner and game.current_winner == player and i in game.win_combo else ""
                st.markdown(
                    f"""<button disabled style='
                        background-color: {BG_COLOR}; 
                        color: {PLAYERS[player]['color']}; 
                        font-size: 48px; 
                        font-weight: bold; 
                        width: 100%;
                        height: 100px;
                        border: 2px solid {PLAYERS[player]['color']};
                        border-radius: 5px;
                        ' class='{winner_class}'>{player}</button>""", 
                    unsafe_allow_html=True
                )

    # Game status
    if game.current_winner == 'X':
        st.markdown(
            f"""<div class='status' style='color:{PLAYERS['X']['color']}'>
            🎉 {PLAYERS['X']['name']} wins!</div>""", 
            unsafe_allow_html=True
        )
    elif game.current_winner == 'O':
        st.markdown(
            f"""<div class='status' style='color:{PLAYERS['O']['color']}'>
            🎉 {PLAYERS['O']['name']} wins!</div>""", 
            unsafe_allow_html=True
        )
    elif not game.empty_squares():
        st.markdown(
            """<div class='status'>🤝 It's a tie! Good game!</div>""", 
            unsafe_allow_html=True
        )
    
    # Reset button with confirmation
    if st.button("🔄 New Game", key="reset", help="Click to start a new game"):
        game.reset_state()
        st.rerun()

    # Game instructions
    with st.expander("ℹ️ How to Play"):
        st.markdown("""
        ## Tic-Tac-Toe Rules:
        
        1. **Player 1** is Red (X) and **Player 2** is Blue (O)
        2. Players take turns marking a space on the 3×3 grid
        3. The first player to get 3 of their marks in a row (up, down, across, or diagonally) wins
        4. When all 9 squares are full, the game is over (tie)
        
        The current player's turn is highlighted with a glowing border.
        """)

if __name__ == "__main__":
    main()
from roulette_model import RouletteGame

# these are necessary when checking where the bet where placed. Bets on all options are not mandatory, so the code
# checks whether or not these variable are None or they have value
number_bet_input = None
place_number_bet_amount = None
color_bet_input = None
place_color_bet_amount = None
odds_evens_bet_input = None
place_odds_evens_bet_amount = None
dozens_bet_input = None
place_dozens_bet_amount = None
low_high_nums_bet_input = None
place_low_high_nums_bet_amount = None
columns_bet_input = None
place_columns_bet_amount = None
dict_of_bets = {}

while True:

    print("==========================================================")
    try:
        game_input = int(input(f"ENTER NUMBER TO SELECT GAME"
                               f"\n 1 -- Guess roulette number"
                               f"\n 2 -- Guess color of the number"
                               f"\n 3 -- Guess odds or evens"
                               f"\n 4 -- Guess dozens"
                               f"\n 5 -- Guess low or high numbers"
                               f"\n 6 -- Guess columns"
                               f"\n 7 -- Finish bet and play "))
        if 0 < game_input < 8:
            pass
        else:
            print("==========================================================")
            print("Enter only number from 1 to 7.")
            continue
    except ValueError:
        print("==========================================================")
        print("Ilegal character entered, please enter numbers only.")
        continue

    if game_input == 1:
        try:
            number_of_num_bets = int(input("Enter how many numbers you want to place bet on: "))
        except ValueError:
            print("Ilegal character entered, please enter numbers only.")
            continue
        num = 1
        while num <= number_of_num_bets:  # allows to place bets on more than one number
            try:
                number_bet_input = int(input("Enter the number from 0 to 36 "))
            except ValueError:
                print("Ilegal character entered, please enter numbers only.")
                continue
            if 0 <= number_bet_input < 37:
                try:
                    place_number_bet_amount = int(input("Enter your bet for this game, the winning will be 2 to 1: "))
                    if place_number_bet_amount > 0:
                        dict_of_bets[number_bet_input] = place_number_bet_amount
                    else:
                        print("Amount placed is 0 or below")
                        continue
                except ValueError:
                    print("Ilegal character entered, please enter numbers only.")
                    continue
            else:
                print("numbers should be be between 0 and 36")
                continue
            num += 1

    if game_input == 2:
        while True:
            try:
                color_bet_input = int(input("Enter color: 1 -- red | 2 -- black: "))
                if color_bet_input == 1 or color_bet_input == 2:
                    break
                else:
                    print("Please enter only number 1 or 2: 1 -- red | 2 -- black")
                    continue
            except ValueError:
                print("Ilegal character entered, please enter numbers only.")
                continue
        while True:
            try:
                place_color_bet_amount = int(input("Enter your bet for this game, the winning will be 2 to 1: "))
                if place_color_bet_amount > 0:
                    break
                else:
                    print("Amount placed is 0 or below")
                    continue
            except ValueError:
                print("Ilegal character entered, please enter numbers only.")
                continue
        if color_bet_input == 1:
            color_bet_input = 'red'
        else:
            color_bet_input = 'black'

    if game_input == 3:
        while True:
            try:
                odds_evens_bet_input = int(input("Enter odd or even: 1 -- odd | 2 -- even "))
                if odds_evens_bet_input == 1 or odds_evens_bet_input == 2:
                    break
                else:
                    print("Please enter only number 1 or 2: 1 -- odd | 2 -- even")
                    continue
            except ValueError:
                print("Ilegal character entered, please enter numbers only.")
                continue
        while True:
            try:
                place_odds_evens_bet_amount = int(input("Enter your bet for this game, the winning will be 2 to 1: "))
                if place_odds_evens_bet_amount > 0:
                    break
                else:
                    print("Amount placed is 0 or below")
                    continue
            except ValueError:
                print("Ilegal character entered, please enter numbers only.")
                continue
        if odds_evens_bet_input == 1:
            odds_evens_bet_input = 'odd'
        else:
            odds_evens_bet_input = 'even'

    if game_input == 4:
        while True:
            try:
                dozens_bet_input = int(input("Enter dozens: 1 -- 1st 12 | 2 -- 2nd 12 | 3 -- 3rd 12 "))
                if dozens_bet_input == 1 or dozens_bet_input == 2 or dozens_bet_input == 3:
                    break
                else:
                    print("Please enter only number 1, 2 or 3: 1 -- 1st 12 | 2 -- 2nd 12 | 3 -- 3rd 12")
                    continue
            except ValueError:
                print("Ilegal character entered, please enter numbers only.")
                continue
        while True:
            try:
                place_dozens_bet_amount = int(input("Enter your bet for this game, the winning will be 2 to 1: "))
                if place_dozens_bet_amount > 0:
                    break
                else:
                    print("Amount placed is 0 or below")
                    continue
            except ValueError:
                print("Ilegal character entered, please enter numbers only.")
                continue
        if dozens_bet_input == 1:
            dozens_bet_input = '1st 12'
        elif dozens_bet_input == 2:
            dozens_bet_input = '2nd 12'
        else:
            dozens_bet_input = '3rd 12'

    if game_input == 5:
        while True:
            try:
                low_high_nums_bet_input = int(input("Choose low or high numbers: "
                                                    "1 -- Low numbers (1-18) "
                                                    "| 2 -- High numbers (19-36) "))
                if low_high_nums_bet_input == 1 or low_high_nums_bet_input == 2:
                    break
                else:
                    print("Please enter only number 1 or 2: 1 -- Low numbers (1-18) | 2 -- High numbers (19-36)")
                    continue
            except ValueError:
                print("Ilegal character entered, please enter numbers only.")
                continue
        while True:
            try:
                place_low_high_nums_bet_amount = int(input("Enter your bet for this game, "
                                                           "the winning will be 2 to 1: "))
                if place_low_high_nums_bet_amount > 0:
                    break
                else:
                    print("Amount placed is 0 or below")
                    continue
            except ValueError:
                print("Ilegal character entered, please enter numbers only.")
                continue
        if low_high_nums_bet_input == 1:
            low_high_nums_bet_input = 'low'
        else:
            low_high_nums_bet_input = 'high'

    if game_input == 6:
        while True:
            try:
                columns_bet_input = int(input("Enter: 1 -- 1st column | 2 -- 2nd column | 3 -- 3rd column "))
                if columns_bet_input == 1 or columns_bet_input == 2 or columns_bet_input == 3:
                    break
                else:
                    print("Please enter only number 1, 2 or 3: 1 -- 1st column | 2 -- 2nd column | 3 -- 3rd column")
                    continue
            except ValueError:
                print("Ilegal character entered, please enter numbers only.")
                continue
        while True:
            try:
                place_columns_bet_amount = int(input("Enter your bet for this game, the winning will be 2 to 1: "))
                if place_columns_bet_amount > 0:
                    break
                else:
                    print("Amount placed is 0 or below")
                    continue
            except ValueError:
                print("Ilegal character entered, please enter numbers only.")
                continue
        if columns_bet_input == 1:
            columns_bet_input = "1st column"
        elif columns_bet_input == 2:
            columns_bet_input = "2nd column"
        else:
            columns_bet_input = "3rd column"

    if game_input == 7:
        print('==========================================================')
        roulette_game_obj = RouletteGame()
        if number_bet_input is not None:
            for k, v in dict_of_bets.items():
                roulette_game_obj.number_game(k, v)

        if color_bet_input is not None:
            roulette_game_obj.color_game(color_bet_input, place_color_bet_amount)

        if odds_evens_bet_input is not None:
            roulette_game_obj.even_odd_game(odds_evens_bet_input, place_odds_evens_bet_amount)

        if dozens_bet_input is not None:
            roulette_game_obj.dozen_game(dozens_bet_input, place_dozens_bet_amount)

        if low_high_nums_bet_input is not None:
            roulette_game_obj.low_high_game(low_high_nums_bet_input, place_low_high_nums_bet_amount)

        if columns_bet_input is not None:
            roulette_game_obj.columns_game(columns_bet_input, place_columns_bet_amount)

        print(f"Your winnings: {roulette_game_obj.winnings} EUR")
        break

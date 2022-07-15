import random
import logging

logging.basicConfig(filename='games.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class RouletteGame:  # EUROPEAN ROULETTE
    red_color_roulette_list = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black_color_roulette_list = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    green_color_roulette_list = [0]
    first_dozen_roulette_list = list(range(1, 13))
    second_dozen_roulette_list = list(range(13, 25))
    third_dozen_roulette_list = list(range(25, 36))
    low_roulette_num_list = list(range(1, 19))  # first half from 1 to 18
    high_roulette_num_list = list(range(19, 37))  # second half from 19 to 36
    first_column_num_list = list(range(1, 37, 3))
    second_column_num_list = list(range(2, 37, 3))
    third_column_num_list = list(range(3, 37, 3))
    random_roulette_selection = random.randint(0, 36)  # this is a random roulette number selection
    winnings = 0

    def number_game(self, bet_number, bet_number_amount):
        if bet_number == self.random_roulette_selection:
            print(f"Roulette number - {self.random_roulette_selection}, your number: {bet_number} YOU WON "
                  f"{bet_number_amount * 35} EUR")
            self.winnings += bet_number_amount * 35
            logging.info(f"Bet: {bet_number}, bet amount: {bet_number_amount}, roulette number: "
                         f"{self.random_roulette_selection}, winnings: {bet_number_amount * 35} ")
        else:
            print(f"Roulette number - {self.random_roulette_selection}, your number: {bet_number} YOU LOST "
                  f"{bet_number_amount} EUR")
            self.winnings -= bet_number_amount
            logging.info(f"Bet: {bet_number}, bet amount: {bet_number_amount}, roulette number: "
                         f"{self.random_roulette_selection}, losses: {bet_number_amount} ")

    def check_number_color(self):
        if self.random_roulette_selection in self.red_color_roulette_list:
            return "RED"
        elif self.random_roulette_selection in self.black_color_roulette_list:
            return "BLACK"
        else:
            return "GREEN"

    def color_game(self, bet_color, bet_color_amount):
        if self.check_number_color() == bet_color.upper():
            print(f"You bet {bet_color}, roulette number: {self.random_roulette_selection}, which is "
                  f"{self.check_number_color()}  - YOU WON {bet_color_amount * 2} EUR")
            self.winnings += bet_color_amount * 2
            logging.info(f"Bet: {bet_color}, bet amount: {bet_color_amount}, roulette number: "
                         f"{self.random_roulette_selection} - {self.check_number_color()}, "
                         f"winning: {bet_color_amount * 2} EUR")
        else:
            print(f"You bet {bet_color}, roulette number: {self.random_roulette_selection}, which is "
                  f"{self.check_number_color()}  - YOU LOST {bet_color_amount} EUR")
            self.winnings -= bet_color_amount
            logging.info(f"Bet: {bet_color}, bet amount: {bet_color_amount}, "
                         f"roulette number: {self.random_roulette_selection} - {self.check_number_color()}, "
                         f"losses: {bet_color_amount} EUR")

    def check_if_num_even_or_odd(self):
        if self.random_roulette_selection % 2 == 0:
            return "EVEN"
        else:
            return "ODD"

    def even_odd_game(self, bet_odd_or_even, bet_odd_or_even_amount):
        if self.check_if_num_even_or_odd() == bet_odd_or_even.upper():
            print(f"You bet {bet_odd_or_even}, roulette number: {self.random_roulette_selection}, which is "
                  f"{self.check_if_num_even_or_odd()}  - YOU WON {bet_odd_or_even_amount * 2} EUR")
            self.winnings += bet_odd_or_even_amount * 2
            logging.info(f"Bet: {bet_odd_or_even}, bet amount: {bet_odd_or_even_amount}, "
                         f"{self.random_roulette_selection} - {self.check_if_num_even_or_odd()}, "
                         f"winnings: {bet_odd_or_even_amount * 2} EUR")
        else:
            print(f"You bet {bet_odd_or_even}, roulette number: {self.random_roulette_selection}, which is "
                  f"{self.check_if_num_even_or_odd()}  - YOU LOST {bet_odd_or_even_amount} EUR")
            self.winnings -= bet_odd_or_even_amount
            logging.info(f"Bet: {bet_odd_or_even}, bet amount: {bet_odd_or_even_amount}, "
                         f"{self.random_roulette_selection} - {self.check_if_num_even_or_odd()}, "
                         f"losses: {bet_odd_or_even_amount} EUR")

    def check_number_dozen(self):
        if self.random_roulette_selection in self.first_dozen_roulette_list:
            return "1st 12"
        elif self.random_roulette_selection in self.second_dozen_roulette_list:
            return "2nd 12"
        elif self.random_roulette_selection in self.third_dozen_roulette_list:
            return "3rd 12"
        else:
            return "not a part of of any dozens"

    def dozen_game(self, bet_dozen, bet_dozen_amount):
        if self.check_number_dozen() == bet_dozen:
            print(f"You bet {bet_dozen}, roulette number: {self.random_roulette_selection}, which is "
                  f"{self.check_number_dozen()}  - YOU WON {bet_dozen_amount * 3} EUR")
            self.winnings += bet_dozen_amount * 3
            logging.info(f"Bet {bet_dozen}, bet amount: {bet_dozen_amount}, "
                         f"roulette number: {self.random_roulette_selection} - {self.check_number_dozen()}, "
                         f"winnings: {bet_dozen_amount * 3} EUR")
        else:
            print(f"You bet {bet_dozen}, roulette number: {self.random_roulette_selection}, which is "
                  f"{self.check_number_dozen()}  - YOU LOST {bet_dozen_amount} EUR")
            self.winnings -= bet_dozen_amount
            logging.info(f"Bet {bet_dozen}, bet amount: {bet_dozen_amount}, "
                         f"roulette number: {self.random_roulette_selection} - {self.check_number_dozen()}, "
                         f"losses: {bet_dozen_amount} EUR")

    def check_if_num_low_high(self):
        if self.random_roulette_selection in self.low_roulette_num_list:
            return "LOW"
        elif self.random_roulette_selection in self.high_roulette_num_list:
            return "HIGH"
        else:
            return "is not a part of low or high number"

    def low_high_game(self, bet_low_high, bet_low_high_amount):
        if self.check_if_num_low_high() == bet_low_high.upper():
            print(f"You bet {bet_low_high}, roulette number: {self.random_roulette_selection}, which is "
                  f"{self.check_if_num_low_high()}  - YOU WON {bet_low_high_amount * 2} EUR")
            self.winnings += bet_low_high_amount * 2
            logging.info(f"Bet {bet_low_high}, bet amount: {bet_low_high_amount}, "
                         f"roulette number: {self.random_roulette_selection} - {self.check_if_num_low_high()}, "
                         f"winnings: {bet_low_high_amount * 2} EUR")
        else:
            print(f"You bet {bet_low_high}, roulette number: {self.random_roulette_selection}, which is "
                  f"{self.check_if_num_low_high()}  - YOU LOST {bet_low_high_amount} EUR")
            self.winnings -= bet_low_high_amount
            logging.info(f"Bet {bet_low_high}, bet amount: {bet_low_high_amount}, "
                         f"roulette number: {self.random_roulette_selection} - {self.check_if_num_low_high()}, "
                         f"losses: {bet_low_high_amount} EUR")

    def check_if_num_columns(self):
        if self.random_roulette_selection in self.first_column_num_list:
            return "1st column"
        elif self.random_roulette_selection in self.second_column_num_list:
            return "2nd column"
        elif self.random_roulette_selection in self.second_column_num_list:
            return "3rd column"
        else:
            return "is not a part of any columns"

    def columns_game(self, bet_column, bet_column_amount):
        if self.check_if_num_columns() == bet_column:
            print(f"You bet {bet_column}, roulette number: {self.random_roulette_selection}, which is "
                  f"{self.check_if_num_columns()}  - YOU WON {bet_column_amount * 3} EUR")
            self.winnings += bet_column_amount * 3
            logging.info(f"Bet {bet_column}, bet amount: {bet_column_amount}, "
                         f"roulette number: {self.random_roulette_selection} - {self.check_if_num_columns()}, "
                         f"winnings: {bet_column_amount * 3} EUR")
        else:
            print(f"You bet {bet_column}, roulette number: {self.random_roulette_selection}, which is "
                  f"{self.check_if_num_columns()}  - YOU LOST {bet_column_amount} EUR")
            self.winnings -= bet_column_amount
            logging.info(f"Bet {bet_column}, bet amount: {bet_column_amount}, "
                         f"roulette number: {self.random_roulette_selection} - {self.check_if_num_columns()}, "
                         f"losses: {bet_column_amount} EUR")

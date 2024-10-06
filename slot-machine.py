import random

def deposit():
    print("How much would you like to deposit?")
    deposit_input = input()
    if deposit_input.isdigit():
        deposit_amount = int(deposit_input)
        #6-7.satir da inputun tamamen rakamlardan olusup olusmadigi kontrol ettik
        if deposit_amount > 0:
            return deposit_amount
        else:
            print("Invalid deposit amount. Must be greater than 0.")
            return 0
    else:
        print("Invalid input. Please enter a number.")
        return 0
    
def get_number_of_lines():
    print("How many lines would you like to play? ")
    ui_lines=input()
    if ui_lines.isdigit():
        lines=int(ui_lines)
    if lines>0:
        return lines
    else:
        print("Invalid number of lines. Must be greater than 0.")
        
    return lines
    
def spin_slot_machine(lines):
    symbols = ["🍒", "🍋", "🍊", "🍉", "⭐"]
    for _ in range(lines):
        print(random.choice(symbols))
        
def get_bet_amount():
    print("How much would you like to bet?")
    bet_input=input()
    if bet_input.isdigit():
        bet_amount=int(bet_input)
        if bet_amount>0:
            return bet_amount
        else:
            print("Invalid bet amount. Must be greater than 0.")
            return 0
    else:
        print("Invalid input. Please enter a number.")
        return 0

def main():
    deposit_amount = deposit()
    bet=get_bet_amount()
    if deposit_amount>0:
        lines=get_number_of_lines()
        if lines>0:
            spin_slot_machine(lines)
        else:
            print("Invalid number of lines. Must be greater than 0.")

if __name__ == "__main__":
    main()
    
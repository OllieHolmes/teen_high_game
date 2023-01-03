import gafu
from gafu import simple_divider, new_day_divider, new_line, read_delay
import time

def welcome_to_teen_high(player_name):
    print(f"""
    Welcome to Teen High. You are a transfer student, and today is your first day.
    How exciting!!
    
    There are so many possibilities for you. 
    Go to class and study, make friends, join clubs, and become the most popular teen in school.
    Or fail and remain unknown. The choice is up to you. 
    
    Good luck on your new adventure, {player_name}!""")
    read_delay(30)
    new_day_divider()
    new_line()

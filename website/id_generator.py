from . import DateToolKit as dtk
from datetime import datetime
import datetime as dt
import random


letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = []
for x in range(10):
	numbers.append(x)

def generateTID():

    current_date = dt.date.today()
    current_time = datetime.now().strftime("%H:%M:%S")

    # Date Format: "YYYY-MM-DD"
    formatted_date = current_date.strftime("%Y-%m-%d")
    date = formatted_date
    time = current_time

    _ = f'{date}{random.choice(numbers)}{random.choice(numbers)}{random.choice(letters)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(letters)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{time}{random.choice(letters)}{random.choice(letters)}{random.choice(numbers)}{random.choice(letters)}{random.choice(numbers)}{random.choice(letters)}{random.choice(numbers)}{random.choice(letters)}'

    return _.replace("-", "").replace(":", "")
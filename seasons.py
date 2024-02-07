import datetime
from datetime import date
import sys
import inflect


def main():
    birthday = get_birthday()
    display_minutes(birthday)


def get_birthday():
    entry = input("Please enter your birthday in YYYY-MM-DD format: ")
    return create_date_object(entry)


def create_date_object(birthday):
    try:
        return date.fromisoformat(birthday)
    except ValueError:
        sys.exit("Incorrect value entered")


def display_minutes(birthday):
    p = inflect.engine()
    print(
        p.number_to_words(calculate_minutes(birthday)).replace(" and", "").capitalize() + " minutes"
    )


def calculate_minutes(birthday):
    change_in_time = datetime.date.today() - birthday
    return change_in_time.days * 1440  # 1440 minutes in a day


if __name__ == "__main__":
    main()

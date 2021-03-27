import pandas as pd

def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    a = [1, 7, 2]
    calories = {"day1": 420, "day2": 380, "day3": 390}
    data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
    }

    df = pd.DataFrame(data)
    print(df.loc[[0,1]])




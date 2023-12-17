import pandas as pd
import matplotlib.pyplot as plt
from enum import Enum


labels = [
    "Период промышленной революции и колониального господства",
    "Период Первой мировой войны и послевоенного восстановления",
    "Период между двумя мировыми войнами",
    "Вторая мировая война",
    "Холодная война",
    "Период после холодной войны и развитие глобализации",
    "Эпоха современных вызовов и изменений"
]


class Epochs(Enum):
    TILL_1899 = 0
    TILL_1919 = 1
    TILL_1939 = 2
    TILL_1945 = 3
    TILL_1989 = 4
    TILL_2001 = 5
    TILL_2022 = 6


def get_historical_period(time_slot: int) -> int:
    if 1783 <= time_slot <= 1899:
        return Epochs.TILL_1899.value
    elif 1900 <= time_slot <= 1919:
        return Epochs.TILL_1919.value
    elif 1920 <= time_slot <= 1939:
        return Epochs.TILL_1939.value
    elif 1940 <= time_slot <= 1945:
        return Epochs.TILL_1945.value
    elif 1946 <= time_slot <= 1989:
        return Epochs.TILL_1989.value
    elif 1990 <= time_slot <= 2001:
        return Epochs.TILL_2001.value
    elif 2002 <= time_slot <= 2022:
        return Epochs.TILL_2022.value
    raise Exception(f"Time '{time_slot}' not in 1783-2022")


def get_percents(time_slots: list[int]) -> list[int]:
    dict_of_perc = {}
    one_percent = len(time_slots) / 100
    result = [0] * len(Epochs)

    for time_slot in time_slots:
        time_flag = get_historical_period(time_slot)

        if time_flag in dict_of_perc:
            dict_of_perc[time_flag] += 1
        else:
            dict_of_perc[time_flag] = 1

    for i, value in enumerate(dict_of_perc.values()):
        result[i] = value / one_percent

    return result


file_path = "/Users/matvey/Downloads/Пишу тебе. Корпус для хакатона (2023).xlsx"
load = pd.read_excel(file_path, sheet_name="2023.08.03 Пишу тебе. Корпус (б")
load = load.loc[:, ["Дата открытки (нормализованная)"]]

years = []

for date in load.values:
    year = int()
    try:
        if str(date[0]) == "nan" or str(date[0]) == "00:00:00":
            continue
        year = int(date[0].date().year)
    except AttributeError:
        year = int(str(date[0]).split(".")[-1])

    years.append(year)

for y in sorted(set(years)):
    print(y, labels[get_historical_period(y)])

sizes = get_percents(years)

fig1, ax1 = plt.subplots()
wedges, texts, autotexts = ax1.pie(sizes, autopct='%1.1f%%', textprops=dict(color="w"), startangle=90)
ax1.legend(wedges, labels, title="Epochs", loc="center left", bbox_to_anchor=(0.6, 0, 0.5, 1))
ax1.axis('equal')

plt.show()


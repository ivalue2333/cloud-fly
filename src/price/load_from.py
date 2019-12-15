from copy import deepcopy

import matplotlib.pyplot as plt

from src.price.model import PriceModel

FieldPrefix = "#"

KeyValueSplit = "="


def load_from_file():
    data_list = []
    dict_copy = {}
    with open("price.txt", "r", encoding="utf-8") as fp:
        for line in fp.readlines():
            data_dict = deepcopy(dict_copy)
            line = str(line).strip()
            if line.startswith(FieldPrefix):
                line = line.strip(FieldPrefix)
                line_split = line.split(KeyValueSplit)
                dict_copy[line_split[0]] = line_split[1]
            else:
                line_split = line.split(KeyValueSplit)
                data_dict["name"] = line_split[0]
                data_dict["price"] = float(line_split[1])
                data_list.append(data_dict)
    return data_list


def save():
    data_list = load_from_file()
    PriceModel().create(data_list)


def load_from_database(spec):
    return list(PriceModel().find(spec))


def show_history():
    spec = {
        "name": "黄瓜口口脆"
    }
    data_list = load_from_database(spec)
    x_list = [v["date"] for v in data_list]
    y_list = [v["price"] for v in data_list]

    plt.plot(x_list, y_list, color="green")

    plt.show()


def show_price():
    spec = {
        "date": "2019-12-01",
    }
    data_list = load_from_database(spec)

    data_list = sorted(data_list, key=lambda item: item["price"], reverse=True)

    x_list = [v["name"] for v in data_list]
    y_list = [v["price"] for v in data_list]

    for name, price in zip(x_list, y_list):
        print(name, price)

    # plt.bar(range(1, len(y_list) + 1), y_list, facecolor='#9999ff', edgecolor='white')
    #     #
    #     # plt.show()


if __name__ == "__main__":
    # save()
    # show_history()
    show_price()

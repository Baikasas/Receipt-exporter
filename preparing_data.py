import requests
import json
import os
from tkinter import Label, Button, Toplevel
import sys


def read_receipt(json_name, image):

    receipt_ocr_endpoint = 'https://ocr.asprise.com/api/v1/receipt'

    try:
        r = requests.post(receipt_ocr_endpoint, data={
          'client_id': 'TEST',
          'recognizer': 'auto',
          'ref_no': 'ocr_python_123',
          },
          files={"file": open(f"{image}", "rb")})

        with open(f'{json_name}.json', 'w') as f:
            json.dump(json.loads(r.text), f, ensure_ascii=False, indent=2)
    except Exception as e:
        inform(f"Problem occurred analysing image: {e}", turn_off=True)


def data_extracting(file, image, photo_action):

    with open(f'{file}.json', 'r') as f:
        info = json.load(f)

    try:
        items = info['receipts'][0]['items']
        if photo_action:
            os.remove(image)

    except KeyError:
        inform(f"Daily limit has been reached{', photo was not deleted.' if photo_action else '.'} 6 receipts done last time, around 50 items", turn_off=True)

    endings = ["pritaikyt", 'Suteiktos', 'Atsiskaityta', "A = 21,00", "A 21,00", "Tarpin"]

    products = []
    for item in items:
        if any(ending in item['description'] for ending in endings):
            break
        else:
            products.append([item['description'], item['amount']])

    for count, pair in enumerate(products):
        if "Nuolaida" in pair[0]:
            products[count - 1][1] += pair[1]
            del products[count]

    return products


def inform(text, window=None, turn_off=False):
    info_window = Toplevel(window)
    label = Label(info_window, text=text)
    label.grid(row=0, column=0)
    ok = Button(info_window, text="Ok", command=lambda: _exiting(info_window, window, turn_off))
    ok.grid(row=1, column=0)


def _exiting(one, two, turn_off):
    one.destroy()
    if two:
        two.destroy()
    if turn_off:
        sys.exit()


def define_subcategories(products, options):
    defined_subcategories = []

    for product in products:
        subcategory = next((subcat for subcat, names in options.items()
                            if product[0].lower() in names or any(name in product[0].lower() for name in names)), None)

        defined_subcategories.append([product[0], subcategory if subcategory else "N/A", product[1]])

    return defined_subcategories


def add_categories(categories, defined_subcategories):
    for sub in defined_subcategories:

        for category, subs in categories.items():
            if sub[1] in subs:
                sub.insert(1, category)
                break
        else:
            sub.insert(1, "N/A")

    return defined_subcategories


def extract_options(categories):
    options = []

    for category in categories.values():
        options.extend(category)

    return options


def data_work_1(json_name, photo, photo_action):

    #read_receipt(json_name, photo) #comment if using data from json file
    products = data_extracting(json_name, photo, photo_action)

    return products


def data_work_2(products, categories, options):
    defined = define_subcategories(products, options)

    data = add_categories(categories, defined)
    drop_down_list = extract_options(categories)

    return data, drop_down_list

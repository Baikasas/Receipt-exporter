import json
from tkinter import Tk, Entry, Button, Toplevel, Checkbutton, IntVar, Frame, Label, Radiobutton
import os
from preparing_data import inform
import sys
from choosing_file import choosing_file


def updating(api, key, window):

    try:
        with open("api_key.json", 'r') as f:
            info = json.load(f)

        if api == info[0] and key == info[1]:
            inform("Api and a key are not new.", window)
        elif api == "Api file path":
            api = info[0]
        elif key == "Doc key":
            key = info[1]

    except FileNotFoundError:
        inform("File 'api_key.json' is not found, it has been created.", window)

    else:
        with open("api_key.json", 'w') as g:
            json.dump([api, key], g, indent=2, ensure_ascii=False)
        inform("Data updated", window)


def updating_api():
    update_window = Toplevel(root)

    api = Entry(update_window, width=8)
    api.insert(0, "Api file path")
    api.grid(row=0, column=0)

    path = Button(update_window, text="Select", command=lambda: choosing_file(api, "json"))
    path.grid(row=0, column=1)

    key = Entry(update_window, width=18)
    key.insert(0, "Doc key")
    key.grid(row=1, column=0, columnspan=2)

    update = Button(update_window, text="Update", command=lambda: updating(api.get(), key.get(), update_window))
    update.grid(row=0, column=2)


def transition(var, photo_action, photo):

    for file in ["categories", "options"]:
        try:
            with open(f'{file}.json', 'r') as f:
                if os.path.getsize(f'{file}.json') == 0:
                    inform(f"{file}.json is empty, add at least 1 category-subcategory pair.")
                    return
                else:
                    if file == "categories":
                        categories = json.load(f)
                    else:
                        options = json.load(f)

        except FileNotFoundError:
            inform(f"{file}.json file does not exist, add at least 1 category-subcategory pair.")
            return

        except json.JSONDecodeError:
            inform(f"{file}.json file syntax is not correct.")
            return

    if photo == "Photo location" or photo == "":
        inform("Photo location is missing")
        return #comment if using data from json only
    elif not os.path.exists(photo):
        inform("Photo location does not exist")
        return

    if var == 1:
        google_sheet = True

        from google_sheets_export import validate_api_key

        message = validate_api_key()
        inform(message)

        if message != "Api and key info valid":
            return

    elif var == 2:
        google_sheet = False

    else:
        inform("No export mode selected")
        return

    from preparing_data import data_work_1
    from datetime import datetime

    json_name = datetime.now().strftime("%Y-%m-%d_%H:%M")
    #json_name = "2023-03-16_15:54" #for data from json only
    products = data_work_1(json_name, photo, photo_action)

    from preparing_data import data_work_2
    data, drop_down_list = data_work_2(products, categories, options)

    for widget in top_frame.grid_slaves():
        widget.destroy()
    for widget in center.grid_slaves():
        widget.destroy()

    from main_window import main_table
    main_table(data, drop_down_list, center, top_frame, google_sheet, json_name, categories)


def add_cat_sub():
    update_window = Toplevel(root)

    label_1 = Label(update_window, text="Category:")
    label_1.grid(row=0, column=0)

    label_2 = Label(update_window, text="Subcategory:")
    label_2.grid(row=1, column=0)

    category = Entry(update_window, width=8)
    category.grid(row=0, column=1)

    subcategory = Entry(update_window, width=8)
    subcategory.grid(row=1, column=1)

    cancel = Button(update_window, text="Cancel", command=lambda: update_window.destroy())
    cancel.grid(row=2, column=0)

    update = Button(update_window, text="Add", command=lambda: add(category.get(), subcategory.get(), update_window))
    update.grid(row=2, column=1)


def add(category, subcategory, window):

    if "" in [category, subcategory]:
        inform("Data is missing")
    else:
        for file in ["categories", "options"]:
            try:
                with open(f'{file}.json', 'r') as f:
                    if os.path.getsize(f'{file}.json') == 0:
                        inform(f"{file}.json was empty.")
                        data = dict()
                    else:
                        data = json.load(f)

            except FileNotFoundError:
                inform(f"{file}.json has been created.")
                data = dict()

            except json.JSONDecodeError:
                inform(f"{file}.json file syntax is not correct.", window)
                return

            except Exception as e:
                inform(e, window)
                return

            if file == "categories":
                if any(subcategory in cat for cat in data.values()):
                    inform("Subcategory already found. Only unique subcategories accepted!")
                elif category in data:
                    data[category].append(subcategory)
                else:
                    data[category] = [subcategory]

            elif file == "options":
                if subcategory in data:
                    inform("Subcategory already found")
                    return
                else:
                    data[subcategory] = ["N/A"]

            with open(f'{file}.json', 'w') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                inform(f"{file}.json data updated", window)


def starting_view():
    jpg_entry = Entry(top_frame, width=10)
    jpg_entry.insert(0, "Photo location")
    jpg_entry.grid(row=0, column=0, sticky="nsew")

    location = Button(top_frame, text="Choose", command=lambda: choosing_file(jpg_entry, "jpg"))
    location.grid(row=0, column=1)

    photo_action = IntVar()
    delete_photo = Checkbutton(top_frame, text="Delete a photo", variable=photo_action)
    delete_photo.grid(row=1, column=0, sticky="nsew")

    next_step = Button(top_frame, text="Next step", command=lambda: transition(var.get(), photo_action.get(), jpg_entry.get()))
    next_step.grid(row=0, column=3)

    var = IntVar()
    google = Radiobutton(center, text="Google Sheets", variable=var, value=1)
    google.grid(row=0, column=0, sticky="nsew")

    excel = Radiobutton(center, text="Excel", variable=var, value=2)
    excel.grid(row=1, column=0, sticky="nsew")

    update_api = Button(center, text="Update Api & Key", command=updating_api)
    update_api.grid(row=0, column=1)

    cat_sub_pair = Button(center, text="Add category & subcategory", command=add_cat_sub)
    cat_sub_pair.grid(row=1, column=1)


def off():

    ask_window = Toplevel()
    label = Label(ask_window, text="Are you sure to exit?")
    label.grid(row=0, column=0, columnspan=2)
    close = Button(ask_window, text="Exit", command=lambda: sys.exit(), width=5)
    cancel = Button(ask_window, text="Cancel", command=lambda: ask_window.destroy(), width=5)
    close.grid(row=1, column=0)
    cancel.grid(row=1, column=1)


root = Tk()
root.title("Receipt exporter")

root.protocol("WM_DELETE_WINDOW", off)

top_frame = Frame(root, width=900)
center = Frame(root)

top_frame.grid(row=0, sticky="n")
center.grid(row=1, sticky="s")

starting_view()

root.mainloop()

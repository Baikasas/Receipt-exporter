from tkinter import Label, Button, OptionMenu, StringVar, DISABLED
from functools import partial
from decimal import Decimal
from categorize import categories


class Table:

    def __init__(self, root, data, drop_down_list):
        self.widgets = []
        self.root = root

        self.drop_down_list = drop_down_list
        self.names_to_remember = []

        for i in range(len(data)):

            self.name = Label(root, text=data[i][0])
            self.name.grid(row=i, column=0)

            self.cat = Label(root, text=data[i][1])
            self.cat.grid(row=i, column=1)

            self.menu = StringVar()
            self.menu.set(data[i][2])
            self.drop = OptionMenu(root, self.menu, *drop_down_list, command=partial(self.update_cat, i))
            self.drop.grid(row=i, column=2)

            if data[i][2] == "N/A":
                self.names_to_remember.append((self.name, self.menu))

            self.cost = Label(root, text=data[i][3])
            self.cost.grid(row=i, column=3)
            self.split_cost = Label(root, text="         ")
            self.split_cost.grid(row=i, column=4)

            self.button_0 = Button(root, text="0", command=partial(self.update_cost, i, 1))
            self.button_0.grid(row=i, column=5)
            self.button_1_4 = Button(root, text="1/4", command=partial(self.update_cost, i, 3/4))
            self.button_1_4.grid(row=i, column=6)
            self.button_1_3 = Button(root, text="1/3", command=partial(self.update_cost, i, 2/3))
            self.button_1_3.grid(row=i, column=7)
            self.button_1_2 = Button(root, text="1/2", command=partial(self.update_cost, i, 1/2))
            self.button_1_2.grid(row=i, column=8)
            self.button_2_3 = Button(root, text="2/3", command=partial(self.update_cost, i, 1/3))
            self.button_2_3.grid(row=i, column=9)
            self.button_3_4 = Button(root, text="3/4", command=partial(self.update_cost, i, 1/4))
            self.button_3_4.grid(row=i, column=10)
            self.button_1 = Button(root, text="1/1", command=partial(self.update_cost, i, 0/1))
            self.button_1.grid(row=i, column=11)

            self.widgets.append([self.name, self.cat, self.menu, self.cost, self.split_cost,
                                 self.button_0, self.button_1_4, self.button_1_3, self.button_1_2, self.button_2_3,
                                 self.button_3_4, self.button_1, self.drop])

    def update_cat(self, row, value):

        for category, subs in categories.items():
            if value in subs:
                new_cat = category
                break

        self.widgets[row][1].configure(text=new_cat)

    def update_cost(self, row, value):

        if self.widgets[row][4].cget("text") == "         ":
            cost = self.widgets[row][3].cget("text")
            split_cost = round((cost * value), 2)
            remaining_cost = float((Decimal(cost) - Decimal(split_cost)).quantize(Decimal('0.00')))

            self.widgets[row][4].configure(text=split_cost)
            self.widgets[row][3].configure(text=remaining_cost)
        else:
            self.widgets[row][3].configure(text=self.widgets[row][3].cget("text")+self.widgets[row][4].cget("text"))
            self.widgets[row][4].configure(text="         ")

    def summary_view(self):
        sub_categories = {"Destroy": []}

        for count, tupl in enumerate(self.names_to_remember):
            self.names_to_remember[count] = (tupl[0].cget("text"), tupl[1].get())

        for count, row in enumerate(self.widgets):

            row[12].configure(state=DISABLED)

            if row[2].get() in sub_categories:
                row_index = sub_categories[row[2].get()] #if subcategory already in the dict, we will make it into one - sum numbers and delete one occurence

                self.widgets[row_index][3].configure(
                    text=float(Decimal(self.widgets[row_index][3].cget("text")).quantize(Decimal('0.00')) +
                               Decimal(row[3].cget("text")).quantize(Decimal('0.00'))))

                original = Decimal(self.widgets[row_index][4].cget("text")).quantize(Decimal('0.00')) \
                                        if self.widgets[row_index][4].cget("text") != "         " else 0

                new = Decimal(row[4].cget("text")).quantize(Decimal('0.00')) \
                    if row[4].cget("text") != "         " else 0

                total = float(original+new)
                if total == 0:
                    total = "         "

                self.widgets[row_index][4].configure(text=total)

                for widget in row:
                    try:
                        widget.destroy()
                    except AttributeError:
                        continue

                sub_categories["Destroy"].append(count)

            else:
                sub_categories[row[2].get()] = count
                row[0].destroy()

        for index in reversed(sub_categories["Destroy"]):
            del self.widgets[index]

        return self.names_to_remember

    def destroy_buttons(self):
        for row in self.widgets:
            for i in range(5, 12):
                row[i].destroy()

    def destroy_info(self):
        for row in self.widgets:
            row[1].destroy()
            row[3].destroy()
            row[4].destroy()
            row[12].destroy()

from tkinter import filedialog, END


def choosing_file(entry, kind):

    name = filedialog.askopenfilename(title="Select a file", filetypes=[(f"{kind} files", f"*.{kind}")])

    entry.delete(0, END)
    entry.insert(0, name)

# Receipt exporter
## Introduction

This project had a dual objective - to improve my python skills and to provide a practical tool for myself to save time by automating receipt data insertion to my budget spreadsheet. For the last reason, some functions might seem missing or too pre-determined (e.g. always exporting data in one structure or always presenting buttons for splitting receipts, etc.), but the goal of the program was not for it to be universal for every user. I might customize an app if it will look beneficial for my improvement or if anyone else would actually like to use it.

## About an app

Receipt exporter uses Asprise Python OCR to read data from receipt image and users inputs in Tkinter GUI to prepare and export data to google sheet or excel.

## Usage example

This is the starting window of the program.

<img width="383" alt="Screenshot 2023-03-21 at 15 32 04" src="https://user-images.githubusercontent.com/96027197/227045384-ecef76ec-1b3d-4440-9fb2-f129b780ba65.png">

In case of first-time use or data changes, a user should provide category-subcategory pairs of the possible products in the receipt and Api with spreadsheet key if exporting to google spreadsheet. In both cases, as in many more that I will not specify, various data validity checks will happen, and in case of an error, the user will be notified.
Photo location might be typed in the box or the user might choose the file with the help of the 'Choose' button. The user also needs to choose the exporting method and if the photo should be deleted after exporting.

After clicking 'Next step' many checks will happen e.g. if Api and key are valid, if the photo exists, etc. After that Asprise Python OCR will read the data, in case of an error, the photo will not be deleted, if chosen so.

<img width="1028" alt="Screenshot 2023-03-21 at 15 33 22" src="https://user-images.githubusercontent.com/96027197/227045464-3ba5ab1e-e1a4-4396-bc4b-57802066947a.png">

In the next window, we see data from receipt - names of the products and prices. Categories and 
subcategories will be set automatically if a product has already been bought before. In any case, the user can change it manually. In the image we see that the first item is recognized and the second item was not saved in an app before, so no category is given.

<img width="1082" alt="Screenshot 2023-03-21 at 15 34 01" src="https://user-images.githubusercontent.com/96027197/227045541-4a89b949-0a94-4c38-8c5f-39ba1ecdefce.png">

Buttons on the right side of the window are used in case of splitting certain prices with someone else e.g. selecting 3/4 would register 75% of the price for the user and 25% for another person. The splitting sum might be exported to a different sheet and won't have any categories attached.
We choose a subcategory for the second item from the options menu, category shows up automatically. Also we choose to not have any part of the product’s price for ourselves. After reviewing data and making necessary changes the user proceeds with "Summary view".

<img width="702" alt="Screenshot 2023-03-21 at 15 38 03" src="https://user-images.githubusercontent.com/96027197/227045938-0f1da624-fc25-4b9e-bcbf-90873c00fdaf.png">

In the summary view we see prices added up by similar subcategories, also the user has to provide a date, cash/card spending option, and place to put data in on a spreadsheet. He also may choose to remember data of the sheets and columns for the next time. Now he can use ‘Export’.

<img width="598" alt="Screenshot 2023-03-21 at 15 39 27" src="https://user-images.githubusercontent.com/96027197/227046058-f4e22d87-be8d-447a-a723-4aae5b611003.png">

In the last window, there’s an option of deleting the JSON data file that has been created from the image, and the user might want to attach category-subcategory pair to some names for them to be set automatically next time. If it's already on the list, an option to save will not show up.

Data will be exported in an 8 column structure that is used in my spreadsheet for budget management.

<img width="974" alt="Screenshot 2023-03-21 at 15 58 05" src="https://user-images.githubusercontent.com/96027197/227046103-64edfc89-e8e8-4b16-b890-3688a7a6e718.png">

Note: no files need to be created for the program to work, the user will be notified and in most cases, the file will be created.

## Contributing

Any kind of contribution to this project is highly welcome! I would be eager to know any other approaches to this project or just improvements from which I could learn.

If you would like to contribute to this project, please follow these steps:

1. Fork this repository.
2. Create a new branch with a descriptive name.
3. Make your changes and commit them with a descriptive message.
4. Push your changes to your forked repository.
5. Open a pull request against the main branch of this repository.
6. Describe your changes in the pull request and wait for feedback from the maintainers.

By contributing to this project, you agree to license your contribution under the Apache License 2.0.

## License

This project is licensed under the Apache License 2.0.

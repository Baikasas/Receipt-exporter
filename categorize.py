import json

categories = {
    'Food':["Food",
            "Vištiena",
            "Žuvis",
            "Mėsa",
            "Pieno produktai",
            "Daržovės",
            "Vaisiai",
            "Duona",
            "Skanučiai",
            "Čipsai",
            "Paruoštukai",
            "Sultys",
            "Vanduo",
            "Alko",
            "Snakas",
            "Arbata",
            "Eating out",
            "Prieskoniai, etc",
            "Ant sumuštinio"
            ],
    'Household':["Furniture",
                "Kitchen",
                "Toiletries",
                "Fix",
                "Extra"],


    'Self-development':["Books"],

    'Entertainment':["Board-games",
                     "Going out",
                     "Trips",
                     "Extra"],

    'Education':["Kanceliarija"],
}

options = [["Food", "Empty"],
           ["Vištiena","šlaunelės"," krūtinėlė, blauzdelės, peteliai"],
           ["Žuvis"],
           ["Mėsa"],
           ["Pieno produktai"],
           ["Daržovės"],
           ["Vaisiai"],
            ["Duona"],
            ["Skanučiai"],
            ["Sultys"],
            ["Vanduo"],
            ["Alko"],
            ["Snakas"],
            ["Arbata"],
            ["Eating out"],
            ["Prieskoniai, etc"],
           ["Čipsai", "natcho taffel", "lay's"],
           ["Ant sumuštinio", "paštetas"],
           ["Paruoštukai", "blyneliai"],
           ["Furniture"],
           ["Kitchen"],
           ["Toiletries"],
           ["Fix"],
           ["Books"],
           ["Board-games"],
                     ["Going out"],
                     ["Trips"],
            ["Kanceliarija"]
           ]

#with open("options.json", 'w') as g:
   # json.dump(options, g, indent=2, ensure_ascii=False)

#with open("test.json", 'w') as f:
   # save = {"Bread": ['x', 'y'], "Butter":["w"] }
   # json.dump(save, f, indent=2)

options={
  "Food": [
    "kiaušiniai",
    "grikių kruopos",
    "makaronai",
    "miltai",
    "avinžirniai",
    "auksiniai plikyti ryžiai"
  ],
  "Vištiena": [
    "vištiena",
    "šlaunelės",
    "krūtinėlė",
    "lauzdelės",
    "peteliai",
    "broilerių file"
  ],
  "Žuvis": [
    "žuvis"
  ],
  "Mėsa": [
    "mėsa",
    "kiaul.ment.šašlyk"
  ],
  "Pieno produktai": [
    "pienas",
    "fermentinis rokiškio süris",
    "saris germanto gouda",
    "grietine",
    "fetos sūris",
    "sviestas",
    "halloumi sūris",
    "dvaro sviestas",
    "rokiškio naminė grietinė"
  ],
  "Daržovės": [
    "špinatai",
    "keptos raudonos paprikos mega di catò",
    "salotų mišinys fit & easy gurmas",
    "agurkai ilgavaisiai",
    "lietuviški svogūnai"
  ],
  "Vaisiai": [
    "obuoliai golden (75-85 mm)",
    "obuoliai royal gala (75-80 mm)",
    "mangas",
    "bananai"
  ],
  "Duona": [
    "duona",
    "ruginė sumuštinių duona toste",
    "duona skrudinimui toste protein"
  ],
  "Skanučiai": [
    "keksiukas su razinomis",
    "medaus pyragas",
    "dzūkijos sausainiai rududu",
    "marcipaninis sukutis",
    "cinamoninė pynė",
    "pergales saldainių rinkinys",
    "saldainiai unique marc de champagne",
    "avietiniai kviečių trapučiai",
    "šokoladas"

  ],
  "Sultys": [
    "sultys"
  ],
  "Vanduo": [
    "vanduo"
  ],
  "Alko": [
    "alus"
  ],
  "Snakas": [
    "traškios riekelės jore"
  ],
  "Arbata": [
    "arbata"
  ],
  "Eating out": [
    "N/A"
  ],
  "Prieskoniai, etc": [
    "prieskoniai",
    "krapai (20",
    "bazilikai well done (indelyje, 20 g)"
  ],
  "Čipsai": [
    "natcho taffel",
    "lay's",
    "kukurūzų rutuliukai nacho taffel, sūrio skonio,",
    "traškučiai"
  ],
  "Ant sumuštinio": [
    "paštetas"
  ],
  "Paruoštukai": [
    "blyneliai",
    "oykata",
    "cezario salotos su vištiena ir kepta sonine",
    "žemaičių blynai su mėsos įdaru"
  ],
  "Furniture": [
    "stalas"
  ],
  "Kitchen": [
    "peilis"
  ],
  "Toiletries": [
    "tualetinis popierius"
  ],
  "Fix": [
    "N/A"
  ],
  "Books": [
    "knyga"
  ],
  "Board-games": [
    "stalo žaidimas"
  ],
  "Going out": [
    "Going out"
  ],
  "Trips": [
    "N/A"
  ],
  "Kanceliarija": [
    "tušinukas"
  ]
}

categories={
  "Food": [
    "Food",
    "Vištiena",
    "Žuvis",
    "Mėsa",
    "Pieno produktai",
    "Daržovės",
    "Vaisiai",
    "Duona",
    "Skanučiai",
    "Čipsai",
    "Paruoštukai",
    "Sultys",
    "Vanduo",
    "Alko",
    "Snakas",
    "Arbata",
    "Eating out",
    "Prieskoniai, etc",
    "Ant sumuštinio"
  ],
  "Household": [
    "Furniture",
    "Kitchen",
    "Toiletries",
    "Fix",
    "Extra"
  ],
  "Self-development": [
    "Books"
  ],
  "Entertainment": [
    "Board-games",
    "Going out",
    "Trips",
    "Extra"
  ],
  "Education": [
    "Kanceliarija"
  ]
}
# import
import requests
from tkinter import *
from tkinter import ttk

# API basic info
api = "fded7dc65f899c5a67a9f049"

# StringVar of list of currencies
li_currencies = list()

codes = f"https://v6.exchangerate-api.com/v6/{api}/codes"
codes_res = requests.get(codes)

for pair in codes_res.json()["supported_codes"]:
    li_currencies.append(f"{pair[0]} - {pair[1]}")

# Create a GUI
root = Tk()
root.title("Currency Converter")

root.geometry("500x250")
root.resizable(0, 0)
root.configure(bg = "RoyalBlue4")

# heading
Label(root, text = "David's Currency Converter", font = ("Times New Roman", 18), bg = "RoyalBlue4").place(x = 70)

# "convert from"
Label(root, text = "Convert from:", font = ("Georgia", 13, "italic"), bg = "RoyalBlue4").place(x = 60, y = 60)

amnt_from = Entry(root, width = 25)
amnt_from.place(x = 45, y = 100)

FROM__currency_names = ttk.Combobox(root, state = "readonly", values = li_currencies, width = 30)
FROM__currency_names.place(x = 20, y = 140)
FROM__currency_names.current((li_currencies.index("USD - United States Dollar")))

# "convert to"
Label(root, text='Convert to:', font=('Georgia', 13, 'italic'), bg='RoyalBlue').place(x=330, y=60)

converted_currency = StringVar(root)
amnt_to = Entry(root, width=25, textvariable=converted_currency)
amnt_to.place(x=300, y=100)

TO__currency_names = ttk.Combobox(root, state='readonly', values=li_currencies, width=30)
TO__currency_names.place(x=275, y=140)
TO__currency_names.current((li_currencies.index("ZAR - South African Rand")))

# Conversion
def convert_currency(fded7dc65f899c5a67a9f049, converted_rate, from_, to, amount):
    data = requests.get(f"https://v6.exchangerate-api.com/v6/{fded7dc65f899c5a67a9f049}/pair/{from_[:3]}/{to[:3]}/{amount}")

    res = data.json()

    converted_rate.set(str(res["conversion_result"]))

# Submit
submit_btn = Button(root, text = "Submit", bg = "SpringGreen2", command = lambda: convert_currency(api, converted_currency, FROM__currency_names.get(), TO__currency_names.get(), amnt_from.get()))

submit_btn.place(x = 225, y = 190)

# Finalize GUI
root.update()
root.mainloop()
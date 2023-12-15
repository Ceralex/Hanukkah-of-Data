from db import create_cursor

diz = {
    "A": "2",
    "B": "2",
    "C": "2",
    "D": "3",
    "E": "3",
    "F": "3",
    "G": "4",
    "H": "4",
    "I": "4",
    "J": "5",
    "K": "5",
    "L": "5",
    "M": "6",
    "N": "6",
    "O": "6",
    "P": "7",
    "Q": "7",
    "R": "7",
    "S": "7",
    "T": "8",
    "U": "8",
    "V": "8",
    "W": "9",
    "X": "9",
    "Y": "9",
    "Z": "9"
}

def main():
    c = create_cursor("noahs.sqlite")
    customers = c.execute("""
                            SELECT 
                            UPPER(name) AS full_name,
                            REPLACE(phone, '-', '') AS cleaned_phone
                            FROM customers
                          """).fetchall()

    for (full_name, phone) in customers:
        full_name = str(full_name)
        phone = str(phone)
        name = full_name.split(" ")[0]
        surname = full_name.split(" ")[1]

        if len(surname) != 10:
            continue

        number = ""
        for c in surname:
            number += diz[c]
        
        if number == phone:
            print("Match:", full_name, phone)
 
if __name__ == "__main__":
    main()
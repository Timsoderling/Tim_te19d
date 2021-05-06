from functions import *
from config import *

check_file_exists()

read_file()

transactions.append(1000)


while True:                                 
    meny = ("\n###########"                 
            "\n# Lilla banken" 
            "\n# Meny"
            "\n###########"
            "\n1. Visa saldo"
            "\n2. Gör en insättning"
            "\n3. Gör ett uttag"
            "\n0. Avsluta programmet"
            "\nGör ditt val: ".format(balance()))        

    val = validate_int(meny, "Felaktig inmatning")             
 
    if val == 0:
        break
    elif val == 1:
        print(print_transactions())

    elif val == 2:
        insättning = validate_int("Hur mycket vill du sätta in ", "fel inmatning")
        if insättning < 0:
            print("En insättning måste vara större än 0.")
        else:
            add_transactions(insättning)
        


    elif val == 3:
        uttag = validate_int("Hur mycket vill du ta ut","fel inmatning")
        if uttag <= balance() and uttag >=0:
            add_transactions(-uttag, True)

        else:
            print("Du har inte tillräckligt med pengar i kontot. Uttag medjes ej")





print("Tack för besöket")
import datetime

hora = 19
match hora:
    case 7|8|9:print("Ve y desayuna")
    case 11|12|13:print("Ve a tu almuerzo")
    case 17|18| 19:print("Ve a cenar")
    case _: print("No toca comer")
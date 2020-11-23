"""
Bobby Chapa
11/20/2020
format kaspersky export text file into a text file import into  keepass
"""


from textIO_Objects import textIO as t
from formatForKeepass_Objects import formatForKeepass as k


def main():
    # kaspersky export text file directory
    kaspersky_Example = r"\Example_Kaspersky_Export.txt"
    kaspersky_Real = r"\KasperskyExport_19-11-2020.txt"

    tim = r"C:\Users\Bobby\PycharmProjects\Keepass_Kasp_Import\textFiles" + kaspersky_Example #kaspersky_Real

    # keepass import text file directory
    keepass_Example = r"\Example_Keepass_Import.txt"
    keepass_Real = r"\keepass_import.txt"

    tep = r"C:\Users\Bobby\PycharmProjects\Keepass_Kasp_Import\textFiles" + keepass_Example #keepass_Real

    # ----- set and get objects ----- #

    kaspersky_text = t(tim, 'r', '')             # set import text file directory
    read_import = kaspersky_text.io_Text_line()  # get 'read' import text file

    keepass_format = k(read_import)              # set 'format' values
    cleanText = keepass_format.parse_timport()   # get formatted and cleaned text

    # ----- write formated text ----- #

    # write clean formated text to keepass_import.txt
    keepass_text = t(tep, 'w', cleanText)  # set export to keepass_import.txt
    keepass_text.io_Text()                 # write cleaned and formatted text to export text file for keepass

    # write clean formated text to console
    print()
    print(cleanText)  # print to console

    print("Done!")

    return


if __name__ == "__main__":
    main()

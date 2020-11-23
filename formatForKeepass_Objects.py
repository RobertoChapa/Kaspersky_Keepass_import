"""
Bobby Chapa 11-5-2020
Format for keepass
"""


# format output for keepass. returns text file read for import by keepass
class formatForKeepass:
    def __init__(self, read_timport):
        self.read_timport = read_timport

    # input output file stream. writes, reads, or appends to text file
    # arguments: name of text file, w/r/a, text
    def parse_timport(self):
        output = '"Account"' + ',' + '"Login Name"' + ',' + '"Password"' + ',' + '"Web Site"' + ',' + '"Comments"' + "\n"
        for key, value in self.read_timport.items():  # skip the first row
            if key != '':
                output += self.format_write(key, True)
                # print('Account', k.strip())

                ln = self.read_timport[key][0]  # Login Name
                output += self.format_write(ln, True)

                pw = self.read_timport[key][1]  # Password
                output += self.format_write(pw, True)

                ws = self.read_timport[key][2]  # Web Site
                output += self.format_write(ws, True)

                com = self.read_timport[key][3]  # Comment
                output += self.format_write(com, False)  # last value in row

        return output

    # adds a comma at the end of each value except for the last value in each row
    @staticmethod
    def format_write(kas_text, test):
        s = '"' + kas_text + '"'
        if test:
            s += ','
        else:
            s += "\n"
        return s

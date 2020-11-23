"""
Bobby Chapa 11-5-2020
IO read, write, append to text file class
"""


class textIO:
    def __init__(self, Text_File, operation, text):
        self.Text_File = Text_File
        self.operation = operation  # w,r,a
        self.text = text

    # input output file stream. writes, reads, or appends to text file
    # arguments: name of text file, w/r/a, text
    def io_Text(self):
        TextFile = open(self.Text_File, self.operation)  # operation = w,r,a

        try:
            if self.operation == 'w':
                TextFile.write(self.text)
                message = "write completed"
            elif self.operation == 'r':
                message = TextFile.read()
            elif self.operation == 'a':
                TextFile.write(self.text)
                message = "append completed"
            else:
                message = "Enter valid operation"
        except Exception as e:
            message = "Error: " + str(e)
        finally:
            TextFile.close()

        return message

    # Kaspersky export formatting
    # retrieve data and insert into a dictionary
    def io_Text_line(self):
        TextFile = open(self.Text_File, self.operation)  # operation = w,r,a

        passwordDictionary = {}
        new_key = ''
        new_website_url = ''
        new_login_name = ''
        new_login = ''
        new_password = ''
        new_comment = ''

        try:
            i = 0
            lines = TextFile.readlines()
            for line in lines:
                if 'Website name:' in line:  # new_key
                    new_key = line.strip()
                    new_key = new_key[13:]
                    new_key = new_key.replace('name:', '')
                    new_key = new_key.replace('Text:', '')
                    new_key = new_key.strip()

                    # if key is a duplicate rename key by appending '_num' to key
                    # this is because the Dictionary will not allow duplicate keys
                    if passwordDictionary.get(new_key) is not None:
                        i += 1
                        new_key = new_key + '_' + str(i)
                    else:
                        i = 0
                elif 'Website URL:' in line:
                    new_website_url = line.replace('Website URL:', '').strip()
                elif 'Login:' in line:
                    new_login = line.replace('Login:', '').strip()
                    new_login = new_login.replace('Text:', '').strip()
                elif 'Password:' in line:
                    new_password = line.replace('Password:', '').strip()
                elif 'Comment:' in line:
                    new_comment = line.replace('Comment:', '').strip()

                passwordDictionary[new_key] = [new_login, new_password, new_website_url, new_comment]

        except Exception as e:
            message = "Error: " + str(e)
            print(message)
        finally:
            TextFile.close()

        return passwordDictionary

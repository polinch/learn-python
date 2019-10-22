
class FileReader(object):
    def __init__(self, file_path):
        self.path = file_path

    def read(self):
        try:
            file = open(self.path, "r")
            file_content = file.read()
        except IOError:
            file_content = ""
        return file_content


reader = FileReader('example.txt')
print(reader.read())

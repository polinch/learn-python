import os
import tempfile


class File(object):

    def __init__(self, file_path):
        self.path = file_path

    def write(self, added_string):
        f = open(self.path, 'a')
        f.write(added_string)
        f.close()

    def __add__(self, other):
        f = open(self.path, 'r')
        g = open(other.path, 'r')
        k = tempfile.NamedTemporaryFile(delete=False)
        new_file = File(os.path.join(tempfile.gettempdir(), k.name))
        new = open(new_file.path, 'r+')
        line = f.readline()
        while line:
            new.write(line)
            line = f.readline()
        f.close()
        line_2 = g.readline()
        while line_2:
            new.write(line_2)
            line_2 = g.readline()
        g.close()
        new.close()
        return new_file

    def __str__(self):
        return self.path

    def __getitem__(self, item):
        f = open(self.path, 'r')
        return f.readlines()[item]


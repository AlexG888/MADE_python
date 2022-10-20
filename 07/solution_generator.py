class Generator:
    def __init__(self, fname, search_list):
        self.file = open(fname, "r")
        self.search_list = search_list

    def __next__(self):
        line = self.file.readline()
        out = ""
        while line:
            for word in self.search_list:
                if word.upper() in line.upper().split():
                    out = line
            if out == "":
                line = self._next_line()
            else:
                return out
        raise StopIteration()

    def _next_line(self):
        return self.file.readline()

    def __del__(self):
        self.file.close()

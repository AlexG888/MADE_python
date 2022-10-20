import json
import csv


class BaseReader:
    pass


class BaseWriter:
    pass


class JsonWriter(BaseWriter):
    def dump_data(self, data, fileobj):
        with open(fileobj, "w") as outfile:
            json.dump(data, outfile)


class JsonReader(BaseReader):
    def read(self, fileobj):
        with open(fileobj) as jsonfile:
            self.data = json.load(jsonfile)
            return self.data


class CsvWriter(BaseWriter):
    def dump_data(self, data, fileobj):
        with open(fileobj, "w") as csvfile:
            writer = csv.writer(csvfile, delimiter='\n')
            writer.writerow(data)


class CsvReader(BaseReader):
    def read(self, fileobj):
        with open(fileobj) as csvfile:
            self.data = csv.reader(csvfile)
            return self.data


class TxtWriter(BaseWriter):
    def dump_data(self, data, fileobj):
        with open(fileobj, "w") as file:
            for line in data:
                file.write(line + "\n")


class TxtReader(BaseReader):
    def read(self, fileobj):
        with open(fileobj) as file:
            self.data = file.read()
            return self.data


def dump_data(data, fileobj, writer: BaseWriter):
    return writer.dump_data(data, fileobj)


def read_data(fileobj, reader: BaseReader):
    return reader.read(fileobj)





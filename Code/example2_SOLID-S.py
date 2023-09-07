"""S - single responsibility"""
from pathlib import Path
from zipfile import ZipFile


class FileManager:
    def __init__(self, filepath):
        self.path = Path(filepath)

    def read(self):
        return self.path.read_bytes()

    def write(self, encoding="utf-8"):
        with open(self.path, mode='w', encoding=encoding) as file:
            file.write('Hello')


class ZipManager:
    def __init__(self, filepath):
        self.path = Path(filepath)

    def zipfile(self):
        with ZipFile(self.path, mode="w", compression=2) as archive:
            archive.write('text')

    def unzip(self):
        pass

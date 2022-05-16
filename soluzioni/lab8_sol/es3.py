from es2 import File, BitMap, TextFile


class Directory:
    def __init__(self, name):
        self._files = []
        self._name = name

    def get_name(self):
        return self._name

    def add_file(self, file):
        self._files.append(file)

    def open_files(self):
        for f in self._files:
            print("----------------")
            print(f.get_name())
            print(f)

    def __repr__(self):
        content = "\n".join(["\t{}".format(f.get_info()) for f in self._files])
        return "{}: \n{}".format(self.get_name(), content)


def main():
    # creo file semplice
    empty = File("empty.info")
    img = BitMap("myimage.bmp", [[1, 2, 3], [4, 255, 6]])
    txt = TextFile("mytext.txt")
    txt.add_line("ciao")
    txt.add_line("come")
    txt.add_line("va")

    # creo cartella
    folder = Directory("my_folder")

    # aggiungo file
    folder.add_file(empty)
    folder.add_file(img)
    folder.add_file(txt)

    # stampo contenuto cartella
    print(folder)

    # stampo contenuto file in cartella
    folder.open_files()


if __name__ == "__main__":
    main()
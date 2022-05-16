from es2 import File, BitMap, TextFile


class Directory(File):
    def __init__(self, name):
        super().__init__(name)
        self._files = []

    # override
    def get_dim(self):
        return len(self._files)

    def add_file(self, file):
        self._files.append(file)

    def open_files(self):
        for f in self._files:
            print("----------------")
            print(f.get_name())
            print(f)

    # override
    def get_info(self):
        # per ogni file contenuto ottengo informazioni (proteggo se cartella è se stessa)
        content = [f.get_info() for f in self._files if f is not self]
        # per ogni stringa di info sul file, aggiunto tab davanti a ogni linea che contiene
        content = ["\t" + "\n\t".join(i.split("\n")) for i in content]
        # unisco tutte le info file in una stringa separando gli a-capo
        content = "\n".join(content)
        # credo descrizione cartella (nome, dimensione)
        ret = "{}: {}".format(self.get_name(), self.dim())
        # se il contenuto non è vuoto lo aggiungo
        return ret if not content else "{}\n{}".format(ret, content)

    # override
    def __repr__(self):
        return self.get_info()


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

    # creo altra cartella e aggiungo file
    sub_folder = Directory("my_sub_folder")
    sub_folder.add_file(txt)
    sub_folder.add_file(img)
    folder.add_file(sub_folder)
    print(folder)

    # aggiungo se stessa e controllo che non venga stampata
    folder.add_file(folder)


if __name__ == "__main__":
    main()
class File:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def dim(self):
        return 0

    def get_info(self):
        return "{}: {}".format(self.get_name(), self.dim())

    # questo è un override dalla classe object
    def __repr__(self):
        return ""


class TextFile(File):
    def __init__(self, name):
        # chiamo costruttore padre passando parametri
        super().__init__(name)
        self.content = []

    def add_line(self, line):
        self.content.append(line)

    # questo è un override
    def dim(self):
        return len(self.content)

    # questo è un override
    def __repr__(self):
        return "\n".join(self.content)


class BitMap(File):
    def __init__(self, name, bitmap):
        # chiamo costruttore padre passando parametri
        super().__init__(name)
        self._bitmap = bitmap

    # questo è un override
    def dim(self):
        return len(self._bitmap[0]), len(self._bitmap)

    # questo è un override
    def __repr__(self):
        hex_bitmap = []
        for line in self._bitmap:
            hex_row = ["{:4}".format(hex(pixel)) for pixel in line]
            hex_bitmap.append(" ".join(hex_row))
        return "\n".join(hex_bitmap)


def main():
    print("-----------------")
    # creo file semplice
    empty = File("empty.info")
    # testo metodi
    print(empty.get_name())
    print(empty.dim())
    print(empty.get_info())
    print(empty)

    print("-----------------")
    # creo file di testo
    txt = TextFile("mytext")
    # popolo file
    txt.add_line("ciao")
    txt.add_line("come")
    txt.add_line("va")
    # metodi ereditati
    print(txt.get_name())
    # metodi overridden
    print(txt.dim())
    print(txt)
    # metodo ereditato che usa metodo overridden (dim)
    print(txt.get_info())

    print("----------------")
    # creo file immagine
    table = [
        [201, 198, 56],
        [102, 32, 28]
    ]
    img = BitMap("myimage", table)
    # metodi ereditati
    print(img.get_name())
    # metodi overridden
    print(img.dim())
    print(img)
    # metodo ereditato che usa metodo overridden (dim)
    print(img.get_info())


if __name__ == "__main__":
    main()












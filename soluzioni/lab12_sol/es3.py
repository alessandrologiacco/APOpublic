# stampo matrice colori
def print_img(img_table):
    for line in img_table:
        for pixel in line:
            print(pixel, end = " ")
        print()


def recursive_paint(x, y, new_color, old_color, img):
    # se posizione (x, y) non valida non faccio nulla
    if x < 0 or x >= len(img) or y < 0 or y >= len(img[0]):
        return
    # se colore in (x, y) non è quello da sostituire non faccio nulla
    if img[x][y] != old_color:
        return
    # sostituisco colore
    img[x][y] = new_color
    # sostituisco colore in tutte le celle attorno ad (x, y)
    for i in range(-1, 2):
        for j in range(-1, 2):
            recursive_paint(x+i, y+j, new_color, old_color, img)


def paint_bucket(x, y, new_color, img):
    # ottengo colore da sostituire
    old_color = img[x][y]
    # sostituisco colore in x, y
    recursive_paint(x, y, new_color, old_color, img)


def main():
    my_img = [
        [5, 2, 3, 2, 1, 4],
        [1, 4, 2, 5, 2, 4],
        [2, 3, 2, 2, 2, 5],
        [2, 4, 1, 2, 3, 1]
    ]
    print("Starting image:")
    print_img(my_img)
    paint_bucket(x=2, y=4, new_color=1, img=my_img)
    print("Ending image:")
    print_img(my_img)


if __name__ == "__main__":
    main()

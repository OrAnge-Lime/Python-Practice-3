from PIL import Image, ImageDraw


def board(num, size):
    col = (255, 255, 255)
    picture = Image.new("RGB", (num * size, num * size), col)
    x = size * num
    y = x
    draw = ImageDraw.Draw(picture)
    for i in range(0, x, size):
        if i % (size * 2) == 0:
            for j in range(0, y, size):
                if j % (size * 2) == 0:
                    draw.rectangle(
                        [i, j, i + size - 1, j + size - 1], fill='black')
        else:
            for j in range(size, y, size):
                if j % (size * 2) != 0:
                    draw.rectangle(
                        [i, j, i + size - 1, j + size - 1], fill='black')
    picture.save('res.png', "PNG")
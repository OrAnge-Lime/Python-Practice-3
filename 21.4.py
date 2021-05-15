def defractalize(fractal):
    while fractal in fractal:
        fractal.remove(fractal)


fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
fractal.append(fractal)
fractal.append(9)
defractalize(fractal)
print(fractal)

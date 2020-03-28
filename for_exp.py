from GameTheoruLib import GameTheory

gt = GameTheory()

arr = [
    [ [-5, 5], [0, -2], [0, -4]],
    [ [0,  0], [-5, 3], [0, -4]],
    [ [0,  0], [0, -2], [-5, 1]]
]

p1 = [0.4, 0.3, 0.3]
p2 = [0.3, 0.6, 0.1]

print(gt.expectedValue(arr, p1, p2))
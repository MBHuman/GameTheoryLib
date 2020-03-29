class GameTheory:



    def expectedValue(self, a: list, p1: list, p2: list) -> list:
        """
            Возвращает выйгрыши для обеих сторон
            для вероятности p1 и p2 игроков
            где p1 - первый игрок
            и где p2 - второй игрок

            Example for use:
                from GameTheoryLib import GameTheory

                gt = GameTheory()

                arr = [
                    [ [-5, 5], [0, -2], [0, -4]],
                    [ [0,  0], [-5, 3], [0, -4]],
                    [ [0,  0], [0, -2], [-5, 1]]
                ]

                p1 = [0.4, 0.3, 0.3]
                p2 = [0.3, 0.6, 0.1]

                print(gt.expectedValue(arr, p1, p2))
        """
        ans1 = 0
        ans2 = 0
        l = []
        for i in range(len(a)):
                for j in range(len(a[i])):
                        ans1 += a[i][j][0] * p1[i] * p2[j]
        l.append(ans1)
        for i in range(len(a)):
                for j in range(len(a[i])):
                        ans2 += a[i][j][1] * p1[i] * p2[j]
        l.append(ans2)

        return l

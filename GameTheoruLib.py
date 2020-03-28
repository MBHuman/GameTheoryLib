class GameTheory:

    def solve(self, a: list, p1: list, p2: list):
        """
            Возвращает выйгрыши для обеих сторон
            для вероятности p1 и p2 игроков
            где p1 - первый игрок
            и где p2 - второй игрок
        """
        ans1 = 0
        ans2 = 0
        l = []
        for i in range(len(a)):
                for j in range(len(a)):
                        ans1 += a[i][j][0] * p1[i] * p2[j]
        l.append(ans1)
        for i in range(len(a)):
                for j in range(len(a)):
                        ans2 += a[i][j][1] * p1[i] * p2[j]
        l.append(ans2)

        return l

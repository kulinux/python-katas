from enum import Enum

class TennisScore(Enum):
    NORMAL = 1
    DEUCE = 2
    P1_ADV = 3
    P2_ADV = 4
    P1_WIN = 5
    P2_WIN = 6



class Tennis:
    state = TennisScore.NORMAL
    p1Score = 0
    p2Score = 0

    def result(self):
        if self.state == TennisScore.NORMAL: return "{} - {}".format(self._translate(self.p1Score), self._translate(self.p2Score))
        elif self.state == TennisScore.DEUCE: return "Deuce"
        elif self.state == TennisScore.P1_ADV: return "Player 1 adventage"
        elif self.state == TennisScore.P2_ADV: return "Player 2 adventage"
        elif self.state == TennisScore.P1_WIN: return "Player 1 win"
        elif self.state == TennisScore.P2_WIN: return "Player 2 win"

    def scoreP1(self):
        if self.state == TennisScore.NORMAL and self.p1Score == 40:
            self.state = TennisScore.P1_WIN
            return

        if self.state == TennisScore.NORMAL and self.p1Score in [0, 15, 30]:
            self.p1Score = self._score(self.p1Score)


        if self.state == TennisScore.NORMAL and \
            self.p1Score == 40 and \
            self.p2Score == 40:
                self.state = TennisScore.DEUCE
                return
        if self.state == TennisScore.P1_ADV:
            self.state = TennisScore.P1_WIN
            return

        if self.state == TennisScore.P2_ADV:
            self.state = TennisScore.DEUCE
            return

    def scoreP2(self):
        if self.state == TennisScore.NORMAL and self.p2Score == 40:
            self.state = TennisScore.P2_WIN
            return

        if self.state == TennisScore.NORMAL and self.p2Score in [0, 15, 30]:
            self.p2Score = self._score(self.p2Score)

        if self.state == TennisScore.NORMAL and \
                self.p1Score == 40 and \
                self.p2Score == 40:
            self.state = TennisScore.DEUCE
            return
        if self.state == TennisScore.P2_ADV:
            self.state = TennisScore.P2_WIN
            return

        if self.state == TennisScore.P1_ADV:
            self.state = TennisScore.DEUCE
            return


    def _translate(self, score):
        assert score in [0, 15, 30, 40]
        if score == 0: return "love"
        elif score == 15: return "fifteen"
        elif score == 30: return "thirty"
        elif score == 40: return "forty"

    def _score(self, score):
        assert score in [0, 15, 30]
        if score == 0 : return 15
        elif score == 15: return 30
        elif score == 30: return 40

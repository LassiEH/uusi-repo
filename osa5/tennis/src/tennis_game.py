class TennisGame:

    SCORE_NAMES =["Love", "Fifteen", "Thirty", "Forty"]
    ADVANTAGE_POINT = 4
    DEUCE_POINT = 3

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self._get_tie_score()
        elif self.player1_score >= self.ADVANTAGE_POINT or self.player2_score >= self.ADVANTAGE_POINT:
            return self._get_advantage_or_win_score()
        else:
            return self._get_regular_score()

    def _get_tie_score(self):
        if self.player1_score < self.DEUCE_POINT:
            score = f"{self.SCORE_NAMES[self.player1_score]}-All"
        else:
            score = "Deuce"
        return score

    def _get_advantage_or_win_score(self):
        score_difference = self.player1_score - self.player2_score
        if abs(score_difference) == 1:
            leading_player = self.player1_name if score_difference > 0 else self.player2_name
            return f"Advantage {leading_player}"
        else:
            winning_player = self.player1_name if score_difference > 0 else self.player2_name
            return f"Win for {winning_player}"

    def _get_regular_score(self):
        score = f"{self.SCORE_NAMES[self.player1_score]}-{self.SCORE_NAMES[self.player2_score]}"
        return score
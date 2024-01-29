class Game:

    all = []

    def __init__(self, title):
        self.title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, 'title') == False:
            if isinstance(title, str) and len(title)>0:
                self._title = title 

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        list_of_players = [result.player for result in Result.all if result.game == self]
        set_of_players = set(list_of_players)
        list_of_unique_players = list(set_of_players)
        return list_of_unique_players

    def average_score(self, player):
        total_score = 0
        times_player_scored = 0
        for result in Result.all:
            if result.player == player:
                total_score += result.score
                times_player_scored += 1

        return total_score/times_player_scored

class Player:

    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self,username):
        if isinstance(username,str) and (len(username)>=2 and len(username)<=16):
            self._username = username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        list_of_games_played = [result.game for result in Result.all if result.player == self]
        set_of_games_played = set(list_of_games_played)
        list_of_unqiue_games_played = list(set_of_games_played)

        return list_of_unqiue_games_played

    def played_game(self, game):
        list_of_games_for_player = [result.game for result in Result.all if result.player == self]
        for game_played in list_of_games_for_player:
            if game_played == game:
                return True
        
        return False

    def num_times_played(self, game):
        list_of_games_for_player = [result.game for result in Result.all if result.player == self]
        counter = 0

        for game_played in list_of_games_for_player:
            if game_played == game:
                counter += 1

        return counter

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if hasattr(self, 'score') == False:
            if isinstance(score,int) and (score>=1 and score<=5000):
                self._score = score

    
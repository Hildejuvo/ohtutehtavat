import unittest

from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_existing_player(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_returns_none_for_unknown_player(self):
        player = self.stats.search("Selanne")
        self.assertIsNone(player)

    def test_search_finds_player_by_partial_name(self):
        player = self.stats.search("Gret")
        self.assertEqual(player.name, "Gretzky")

    def test_team_returns_players_of_given_team(self):
        players = self.stats.team("EDM")
        names = [player.name for player in players]

        self.assertEqual(
            names,
            ["Semenko", "Kurri", "Gretzky"]
        )

    def test_team_returns_empty_list_for_unknown_team(self):
        players = self.stats.team("BOS")
        self.assertEqual(players, [])

    def test_top_returns_players_in_points_order(self):
        players = self.stats.top(2)
        names = [player.name for player in players]

        # Nykyinen top(2) palauttaa 3 pelaajaa
        self.assertEqual(
            names,
            ["Gretzky", "Lemieux", "Yzerman"]
        )

    def test_top_returns_highest_scoring_player_first(self):
        players = self.stats.top(0)
        self.assertEqual(len(players), 1)
        self.assertEqual(players[0].name, "Gretzky")

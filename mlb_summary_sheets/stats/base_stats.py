import matplotlib.pyplot as plt
from mlb_summary_sheets.config import StatsConfig
from mlb_summary_sheets.apis.fangraphs_client import FangraphsClient
from mlb_summary_sheets.components.stats_table import StatsTable
from mlb_summary_sheets.player import Player
from mlb_summary_sheets.apis.pybaseball_client import PybaseballClient


class BaseStats:
    def __init__(self, player: Player, season: int, stat_type: str):
        self.player = player
        self.season = season
        self.stat_type = stat_type
        self.standard_stats = StatsConfig().stat_lists[stat_type]['standard']
        self.advanced_stats = StatsConfig().stat_lists[stat_type]['advanced']
        self.splits_stats_list = StatsConfig().stat_lists[stat_type]['splits']
        self.stats = FangraphsClient.fetch_leaderboards(season=self.season, stat_type=self.stat_type)
        print(list(self.stats.columns))
        if self.stat_type == 'batting':
             self.splits_stats = PybaseballClient.fetch_batting_splits_leaderboards(player_bbref=self.player.bbref_id, season=self.season)


    def display_standard_stats(self, ax: plt.Axes):
        df_player = self.stats[self.stats['xMLBAMID'] == self.player.mlbam_id][self.standard_stats].reset_index(drop=True)
        stats_table = StatsTable(df_player, self.standard_stats, self.stat_type)
        stats_table.create_table(ax, "Standard {}".format(self.stat_type.capitalize()))

    def display_advanced_stats(self, ax: plt.Axes):
        df_player = self.stats[self.stats['xMLBAMID'] == self.player.mlbam_id][self.advanced_stats].reset_index(drop=True)
        stats_table = StatsTable(df_player, self.advanced_stats, self.stat_type)
        stats_table.create_table(ax, "Advanced {}".format(self.stat_type.capitalize()))

    def display_splits_stats(self, ax: plt.Axes):
        stats_table = StatsTable(self.splits_stats, self.splits_stats_list, self.stat_type)
        stats_table.create_table(ax, "Splits {}".format(self.stat_type.capitalize()), True)


class PitchingStats(BaseStats):
    def __init__(self, player: Player, season: int):
        super().__init__(player, season, 'pitching')

class BattingStats(BaseStats):
    def __init__(self, player: Player, season: int):
        super().__init__(player, season, 'batting')
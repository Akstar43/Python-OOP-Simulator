import argparse
class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Game")
        self.parse = argparse.ArgumentParser
        self.player_name = self.parse.add_argument('player_name', metavar='playername', help="Add player name")
        self.parser.parse_args(self.player_name)
        self.block_name = self.parse.add_argument('block_name', metavar='blockname', help='Add Block name')
        self.parser.parse_args(self.block_name)
        self.blockmax = self.parse.add_argument('max', metavar='max', help='Size of the block')
        self.parser.parse_args(self.blockmax)
        self.durability_taken = self.parse.add_argument('durability', metavar='dur', help='durability taken to break')
        self.parser.parse_args(self.durability_taken)
        
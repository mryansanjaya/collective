from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS
# PAGES
class No1Welcome(Page):
    pass

class No2Introduction(Page):
    pass

class No3Instruction(Page):
    pass

class No4Instruction(Page):
    pass

class No5VideoInstruction(Page):
    pass
class No6Instruction(Page):
    pass

page_sequence = [No1Welcome, No2Introduction, No3Instruction, No4Instruction, No6Instruction]

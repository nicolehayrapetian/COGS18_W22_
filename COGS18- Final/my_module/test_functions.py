from my_module.classes import Player 
from my_module.classes import Question
from my_module.classes import Situations

def test_player_class ():
    player = Player('name')
    assert type (player) == Player 
    assert type (player.lives) == int
    assert type (player.rank) == int
    assert type (player.dragonslayer) == bool
    assert player.lives == 3
    assert player.rank == 0
    assert player.dragonslayer == False 
    assert callable (player.lose_life)
    player.lose_life ()
    assert player.lives == 2
    assert callable (player.upper_rank)
    player.upper_rank ()
    assert player.rank == 1
    assert callable (player.rank_title)
    assert player.rank_title () == 'PEASANT'
    player.rank = 4 
    assert player.rank_title () == 'FARMER'
    player.rank = 7
    assert player.rank_title () == 'KNIGHT'
    player.rank = 10
    assert player.rank_title () == 'BLACK KNIGHT'
    player.rank = 14 
    assert player.rank_title () == 'DRAGON SLAYER'
    assert callable (player.info)

def test_question_class ():
    question = Question ('What color is the sky?', ['a) blue', 'b) green', 'c) purple', 'd) yellow'], ['a'])
    assert type (question) == Question 
    assert type (question.question) == str
    assert type (question.choices) == list
    assert type (question.answers) == list
    assert callable (question.print_choices)
    assert callable (question.check_answer)
    assert question.check_answer ('c') == False
    assert question.check_answer ('e') == False 
    assert question.check_answer ('a') == True
    assert question.validate ('e') == False 
    assert question.validate ('d') == True 

def test_situation_class ():
    situation = Situations ()
    assert type (situation) == Situations 
    assert type (situation.nonfatal) == dict 
    assert type (situation.fatal) == dict
    assert type (situation.dragon) == dict
    for v in situation.nonfatal.values ():
        assert type (v) == list 
        assert len (v) == 3
        for i in v:
            assert type (i) == str 
    for v in situation.fatal.values ():
        assert type (v) == list 
        assert len (v) == 3
        for i in v:
            assert type (i) == str 
    for v in situation.dragon.values ():
        assert type (v) == list 
        assert len (v) == 1
        for i in v:
            assert type (i) == str 

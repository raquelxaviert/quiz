import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct


def test_add_multiple_choices():
    question = Question(title='q2')
    question.add_choice('a', False)
    question.add_choice('b', True)
    assert len(question.choices) == 2
    assert question.choices[1].is_correct

def test_remove_choice_by_id():
    question = Question(title='q3')
    c1 = question.add_choice('a', False)
    c2 = question.add_choice('b', True)
    question.remove_choice_by_id(c1.id)
    assert len(question.choices) == 1
    assert question.choices[0].id == c2.id

def test_remove_all_choices():
    question = Question(title='q4')
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.remove_all_choices()
    assert len(question.choices) == 0

def test_set_correct_choices():
    question = Question(title='q5')
    c1 = question.add_choice('a', False)
    c2 = question.add_choice('b', False)
    question.set_correct_choices([c2.id])
    assert not c1.is_correct
    assert c2.is_correct

def test_correct_selected_choices_returns_correct():
    question = Question(title='q6', max_selections=2)
    c1 = question.add_choice('a', True)
    c2 = question.add_choice('b', False)
    correct = question.correct_selected_choices([c1.id, c2.id])
    assert c1.id in correct
    assert c2.id not in correct

def test_correct_selected_choices_max_selections():
    question = Question(title='q7', max_selections=1)
    c1 = question.add_choice('a', True)
    c2 = question.add_choice('b', False)
    with pytest.raises(Exception):
        question.correct_selected_choices([c1.id, c2.id])

def test_choice_text_length_limits():
    question = Question(title='q8')
    with pytest.raises(Exception):
        question.add_choice('', False)
    with pytest.raises(Exception):
        question.add_choice('a'*101, False)

def test_question_points_limits():
    with pytest.raises(Exception):
        Question(title='q9', points=0)
    with pytest.raises(Exception):
        Question(title='q9', points=101)

def test_choice_id_increment():
    question = Question(title='q10')
    c1 = question.add_choice('a', False)
    c2 = question.add_choice('b', False)
    assert c2.id == c1.id + 1

def test_remove_choice_by_invalid_id():
    question = Question(title='q11')
    question.add_choice('a', False)
    with pytest.raises(Exception):
        question.remove_choice_by_id(999)
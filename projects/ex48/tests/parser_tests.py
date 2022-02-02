from nose.tools import *
from ex48 import lexicon, parser

def test_peek():
    assert_equal(parser.peek([('verb', 'run'), ('direction', 'north')]), 'verb')
    assert_equal(parser.peek([('direction', 'north')]), 'direction')


    word_list = ([('direction', 'north')])
    assert_raises(Exception, parser.peek(word_list))



def test_match():
    word_list = ([('verb', 'run'), ('direction', 'north')])
    assert_equal(parser.match(word_list, 'verb'), ('verb', 'run'))
    assert_equal(parser.match(word_list, 'direction'), ('direction','north'))

def test_Sentence():
    assert_equal(parser.Sentence(('noun', 'player'), ('verb', 'run'), ('direction', 'north')).subject, 'player')

def test_Parse_init():
    assert_equal(parser.Parse(([('verb', 'run'), ('direction', 'north')])).word_list,
                ([('verb', 'run'), ('direction', 'north')]))

def test_Parse_parse_verb():
    word_list = ([('verb', 'run'), ('direction', 'north')])
    assert_equal(parser.Parse(word_list).parse_verb(), ('verb', 'run'))

def test_Parse_parse_object():
    word_list = ([('direction', 'north')])
    assert_equal(parser.Parse(word_list).parse_object(), ('direction', 'north'))

def test_Parse_parse_subject():
    word_list = ([('verb', 'run'), ('direction', 'north')])
    assert_equal(parser.Parse(word_list).parse_subject(), ('noun', 'player'))
    word_list = ([('noun', 'bear'), ('verb', 'run'), ('direction', 'north')])
    assert_equal(parser.Parse(word_list).parse_subject(), ('noun', 'bear'))

def test_Parse_parse_sentence():
    word_list = ([('verb', 'run'), ('direction', 'north')])
    assert_equal(parser.Parse(word_list).parse_sentence().subject, 'player')
    word_list = ([('verb', 'run'), ('direction', 'north')])
    assert_equal(parser.Parse(word_list).parse_sentence().verb, 'run')
    word_list = ([('verb', 'run'), ('direction', 'north')])
    assert_equal(parser.Parse(word_list).parse_sentence().object, 'north')
    word_list = ([('verb', 'run'), ('direction', 'north')])
    assert_not_equal(parser.Parse(word_list).parse_sentence().object, 'direction')

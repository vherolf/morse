from mautrix.types import EventType, GenericEvent
from maubot import Plugin, MessageEvent
from maubot.handlers import event
from typing import Type, Tuple
from maubot.handlers import command

import re

## the bot class
class morse(Plugin):

    @command.new("morse", help="Morse a message")
    @command.argument("message" , pass_raw=True)
    async def morse_handler(self, evt: MessageEvent, message: str) -> None:
        await evt.respond(decodeMorseText(message))

    @command.passive(regex=r"^...---...$")
    async def ice_berg(self, evt: GenericEvent, _: str(Tuple[str]) ) -> None:
        await evt.respond( "WATCH THE ICEBERG!" )

# from dataclasses import dataclass

# @dataclass
# class Morse(object):
#     letter : str
#     sequence : str

from typing import NamedTuple

class Morse(NamedTuple):
    letter: str
    sequence: str

morsecode = (
        Morse("A",".-"),
        Morse("B","-..."),
        Morse("C","-.-."),
        Morse("D","-.."),
        Morse("E","."),
        Morse("F","..-."),
        Morse("G","--."),
        Morse("H","...."),
        Morse("I",".."),
        Morse("J",".---"),
        Morse("K","-.-"),
        Morse("L",".-.."),
        Morse("M","--"),
        Morse("N","-."),
        Morse("O","---"),
        Morse("P",".--."),
        Morse("Q","--.-"),
        Morse("R",".-."),
        Morse("S","..."),
        Morse("T","-"),
        Morse("U","..-"),
        Morse("V","...-"),
        Morse("W",".--"),
        Morse("X","-..-"),
        Morse("Y","-.--"),
        Morse("Z","--.."),
        Morse("1",".----"),
        Morse("2","..---"),
        Morse("3","...--"),
        Morse("4","....-"),
        Morse("5","....."),
        Morse("6","-...."),
        Morse("7","--..."),
        Morse("8","---.."),
        Morse("9","----."),
        Morse("0","-----"),
        Morse("À",".--.-"),
        Morse("Ä",".-.-"),
        Morse("È",".-..-"),
        Morse("É","..-.."),
        Morse("Ö","---."),
        Morse("Ü","..--"),
        Morse("ß","...--.."),
        Morse("CH","----"),
        Morse("Ñ","--.--"),
        Morse(".",".-.-.-"),
        Morse(",","--..--"),
        Morse(":","---..."),
        Morse(";","-.-.-."),
        Morse("?","..--.."),
        Morse("-","-....-"),
        Morse("_","..--.-"),
        Morse("(","-.--."),
        Morse(")","-.--.-"),
        Morse("'",".----."),
        Morse("=","-...-"),
        Morse("+",".-.-."),
        Morse("/","-..-."),
        Morse("@",".--.-."),
        Morse("KA","-.-.-"),
        Morse("BT","-...-"),
        Morse("AR",".-.-."),
        Morse("VE","...-."),
        Morse("SK","...-.-"),
        Morse("SOS","...---..."),
        Morse("HH","........"),
        Morse("!","----------------------------------------------------------"),
        )


## decode helper functions

def sentencesFromMorseText(text='... --- \t .  \n ... --- .  \r  ... --- .'):
    ## splits text into sentences
    sentences = re.split(r'(\\{1,}|\r{1,}|\n{1,})', text)
    print('sentences', sentences)
    return sentences

def wordsFromMorseSentences(sentence='... --- .  ... --- .   ... --- .'):
    ## splits a sentence into words when two or more spaces 
    words = re.split("\s{2,}", sentence)
    print('words', words)
    return words

def charsFromMorseWords(word='... --- .  ... --- .   ... --- .'):
    ## splits a sentence into words when two or more spaces 
    chars = re.split("\s{1,}", word)
    print('chars', chars)
    return chars

def normalize(text='_'):
    # replace unusual minus and and not needed white spaces
    return text.replace(' ','').replace('_','-')

def decodeMorseChar(char='.'):
    for glyph in morsecode:
        if glyph.sequence == char:
            return glyph.letter
    return None


## morse text decoder function

def decodeMorseText(text):
    result = ' '
    sentences = sentencesFromMorseText(text)
    for sentence in sentences:
        words = wordsFromMorseSentences(sentence)
        for word in words:
            chars = charsFromMorseWords(word)
            result = result + ' '
            for char in chars:
                g = decodeMorseChar(normalize(char))
                if g is not None:
                  result = result + str( g )
                  print( decodeMorseChar(normalize(char)) )
    return str(result)

if __name__ == '__main__':
    while True:
        entered = input("Enter your morse code: ")
        if entered == 'q':
            break
        print('translated to: ', decodeMorseText(entered) ) 

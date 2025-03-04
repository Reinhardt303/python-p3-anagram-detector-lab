class Anagram:
    def __init__(self, word):
        self.word = word

    @property
    def word(self):
        return self._word
    
    @word.setter
    def word(self, word):
        self._word = word

    def match(self, possible_anagrams):
        matches = []
        word_list = [letter for letter in self.word]
        for werd in possible_anagrams:
            possible_anagram = [letter for letter in werd]
            if sorted(possible_anagram) == sorted(word_list):
                matches.append(werd)
        return matches







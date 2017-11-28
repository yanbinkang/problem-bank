class WordCloudData:

    def __init__(self, input_string):
        self.input_string = input_string
        self.words_to_counts = {}
        self.populate_hash()

    def populate_hash(self):
        # iterates over each character in the input string, splitting
        # words and passing them to add_word_to_hash()

        current_word = ''
        for i in range(0, len(self.input_string)):

            character = self.input_string[i]

            # if we reached the end of the string we check if the last
            # character is a letter and add the last word to our hash
            if i == len(self.input_string)-1:
                if self.is_letter(character): current_word += character
                if current_word: self.add_word_to_hash(current_word)

            # if we reach a space or emdash we know we're at the end of a word
            # so we add it to our hash and reset our current word
            elif character == ' ' or character == u'\u2014':
                if current_word: self.add_word_to_hash(current_word)
                current_word = ''

            # we want to make sure we split on elipses so if we get two periods in
            # a row we add the current word to our hash and reset our current word
            elif character == '.':
                if i < len(self.input_string)-1 and self.input_string[i+1] == '.':
                    if current_word: self.add_word_to_hash(current_word)
                    current_word = ''

            # if the character is a letter or an apostrophe, we add it to our current word
            elif self.is_letter(character) or character == '\'':
                current_word += character

            # if the character is a hyphen, we want to check if it's surrounded by letters
            # if it is, we add it to our current word
            elif character == '-':
                if i > 0  and self.is_letter(self.input_string[i-1]) and \
                    self.is_letter(self.input_string[i+1]):
                    current_word += character

    def add_word_to_hash(self, word):

        # if the word is already in the hash we increment its count
        if self.words_to_counts.has_key(word):
            self.words_to_counts[word] += 1

        # if a lowercase version is in the hash, we know our input word must be uppercase
        # but we only include uppercase words if they're always uppercase
        # so we just increment the lowercase version's count
        elif self.words_to_counts.has_key(word.lower()):
            self.words_to_counts[word.lower()] += 1

        # if an uppercase version is in the hash, we know our input word must be lowercase.
        # since we only include uppercase words if they're always uppercase, we add the
        # lowercase version and give it the uppercase version's count
        elif self.words_to_counts.has_key(word.capitalize()):
            self.words_to_counts[word] = 1
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()]

        # otherwise, the word is not in the hash at all, lowercase or uppercase
        # so we add it to the hash
        else:
            self.words_to_counts[word] = 1

    def is_letter(self, character):
        return character in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

import string
from myPythonHelperModule import *


class Message:
    def __init__(self, txt):
        self.msg_text = txt
        self.accepted_words = extract_words("words.txt")

    def get_message_text(self):
        return self.msg_text

    def get_accepted_words(self):
        return self.accepted_words.copy()

    def make_shift_dict(self, shift):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        letter_dict = {}

        shift = shift % 26

        for i in range(0, len(lower)):
            shifted_letter = ""
            if i + shift >= len(lower):
                shifted_letter = lower[shift - (len(lower) - i - 1) - 1]

            else:
                shifted_letter = lower[i + shift]
            letter_dict[lower[i]] = shifted_letter

        for i in range(0, len(upper)):
            shifted_letter = ""
            if i + shift >= len(upper):
                shifted_letter = upper[shift - (len(upper) - i - 1) - 1]

            else:
                shifted_letter = upper[i + shift]
            letter_dict[upper[i]] = shifted_letter

        return letter_dict

    def apply_shift(self, shift):
        shifted_message = ""
        for i in self.get_message_text():
            if i in self.make_shift_dict(shift).keys():
                shifted_message += self.make_shift_dict(shift)[i]
            else:
                shifted_message += i
        return shifted_message


class AnytextMessage(Message):
    def __init__(self, txt, shft):
        super().__init__(txt)
        self.shift = shft
        self.encr_shift_dict = self.make_shift_dict(self.shift)
        self.encr_msg_txt = self.apply_shift(self.shift)

    def get_shift(self):
        return self.shift

    def get_encr_dict(self):
        return self.encr_shift_dict.copy()

    def get_encr_msg(self):
        return self.encr_msg_txt

    def change_shift(self, new_shift):
        self.shift = new_shift
        self.encr_shift_dict = self.make_shift_dict(self.shift)
        self.encr_msg_txt = self.apply_shift(self.shift)


class CeasarsDecoder(Message):
    def __init__(self, text):
        super().__init__(text)

    def decrypt_message(self):
        sentence = ""
        best_sentence = ""
        num_of_real_words = 0
        best_n_real_words = 0
        best_shift = 0

        for shift in range(25):

            sentence = self.apply_shift(shift)

            for word in sentence.split(" "):
                if is_word(self.get_accepted_words(), word):
                    num_of_real_words += 1

            if best_n_real_words < num_of_real_words:
                best_sentence = sentence
                best_n_real_words = num_of_real_words
                best_shift = shift

        return (best_sentence, best_shift)


encripted_message = CeasarsDecoder(get_story_text())

print(encripted_message.decrypt_message())

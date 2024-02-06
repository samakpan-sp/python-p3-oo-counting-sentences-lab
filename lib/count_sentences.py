import re

class MyString:
    def __init__(self, value=""):
        self.value = str(value)

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        sentences = re.split(r'[.!?]', self.value)
        xs = [sentence.strip() for sentence in sentences if sentence.strip()]
        return len(xs)

# Example usage:
xs = MyString(
    """You are doing a great job. Keep it up Sam.
      You will soon be happy with the result of your efforts.
      Money will never be your problem. You'll be invited for tech talks a lot.
      The youth, particularly will gain much from you in your entire life.
      """
)

print(xs.count_sentences())  # Output: 4

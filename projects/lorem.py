import random

def generate_word():
    words = ["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit", "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua", "ut", "enim", "ad", "minim", "veniam", "quis", "nostrud", "exercitation", "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "ea", "commodo", "consequat", "duis", "aute", "irure", "dolor", "in", "reprehenderit", "in", "voluptate", "velit", "esse", "cillum", "dolore", "eu", "fugiat", "nulla", "facilisis", "at", "vinculcum", "voluptate", "quis", "nostrud", "exercitation", "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "ea", "commodo", "consequat"]
    return random.choice(words)

def generate_sentence(length=10):
    return " ".join(generate_word() for _ in range(length)) + "."

def generate_paragraph(num_sentences=5):
    return " ".join(generate_sentence() for _ in range(num_sentences))

if __name__ == "__main__":
    print(generate_paragraph())

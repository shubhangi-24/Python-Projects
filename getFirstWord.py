
text = """

"""


lines = text.strip().split("\n")
first_words = [line.split(":")[0].split()[0] for line in lines if ":" in line]


for word in first_words:
    print(word)

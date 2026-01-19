paragraph = """Python is a powerful programming language.
It is widely used for web development, data analysis,
machine learning, and automation. This Python course
is designed for beginners and professionals alike."""

print("Length:", len(paragraph))

print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

print("Preview:", paragraph[:50])

updated_paragraph = paragraph.replace("Python", "PYTHON")
print("Replaced text:\n", updated_paragraph)

lowercase_paragraph = paragraph.lower()
print("Lowercase:\n", lowercase_paragraph)

trimmed_paragraph = paragraph.strip()

words = trimmed_paragraph.split()
print("Words list:", words)

if "course" in trimmed_paragraph.lower():
    print("The word 'course' was found in the paragraph.")

print(
    "The course description is {} characters long and has {} words."
    .format(len(trimmed_paragraph), len(words))
)

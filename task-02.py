dummy_text = """
The rapid advancement of technology in the 21st century has fundamentally transformed 
the way we live, work, and communicate. From smartphones that connect us instantly 
to people across the globe, to artificial intelligence systems that can process vast 
amounts of data in seconds, our world has become increasingly interconnected and 
automated. This digital revolution has brought countless benefits, including improved 
healthcare, enhanced education opportunities, and unprecedented access to information. 
However, it has also raised important questions about privacy, security, and the 
future of employment in an age where machines can perform many tasks previously 
done by humans.
In the realm of education, technology has opened new doors for learning and 
collaboration. Students can now access online courses from prestigious universities, 
participate in virtual classrooms, and collaborate with peers from different 
continents. Digital libraries and research databases have made information more 
accessible than ever before, democratizing knowledge in ways that were unimaginable 
just a few decades ago. Teachers can use interactive tools and multimedia resources 
to create engaging lessons that cater to different learning styles and paces.
The business world has also undergone significant changes due to technological 
innovation. E-commerce has revolutionized retail, allowing companies to reach global 
markets without the need for physical storefronts. Cloud computing has enabled 
businesses of all sizes to access powerful computing resources and storage solutions 
without massive upfront investments in infrastructure. Remote work has become 
increasingly common, with video conferencing and collaboration tools making it 
possible for teams to work together effectively from anywhere in the world.
"""

word_lst = dummy_text.lower().strip().replace("\n", "").split(" ")
total_characters = len(dummy_text)
total_words = len(word_lst)

word_frequency = {}

for word in word_lst:
    if word in word_frequency.keys():
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

unique_words = [k for k, v in word_frequency.items() if v == 1]
max_repeat = max([v for k, v in word_frequency.items()])
min_repeat = min([v for k, v in word_frequency.items()])
most_common = [k for k, v in word_frequency.items() if v >= 5]

print("=================")
print("Text Statistics:")
print("=================")
print(f"Total Character Is: {total_characters}")
print(f"Total Words Is: {total_words}")
print(f"Uniqu Words : {unique_words}")
print(f"Min reapeated Words Is: {max_repeat}, Min reapeted words Is {min_repeat}")
print(f"Most Common Words : {most_common}")

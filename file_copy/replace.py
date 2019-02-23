def find_and_replace(source, find_word, replace_word):
    text = ''
    with open(source, encoding='utf8') as f:
        text = f.read()
    text = text.replace(find_word, replace_word)

    with open(source, mode='w', encoding='utf8') as f:
        f.write(text)


find_and_replace('file_copy/story.txt', 'Sambaran', 'Alice')

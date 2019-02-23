def statistics(file):
    with open(file, encoding='utf8') as f:
        text = f.read()
        lines = text.count('\n') + 1
        words = len(text.split())
        characters = len(text)
        return {'lines': lines, 'words': words, 'characters': characters}


print(statistics('file_copy/story.txt'))

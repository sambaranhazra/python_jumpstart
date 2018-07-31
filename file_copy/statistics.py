def statistics(file):
    with open(file, encoding='utf8') as f:
        print("Lines: ".format(len(f.readlines())))


statistics('story.txt')

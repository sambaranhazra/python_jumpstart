def copy_file(src, dest):
    text = ''
    with open(src, encoding="utf8") as fs:
        text = fs.read()

    with open(dest, 'w', encoding="utf8") as fd:
        fd.write(text)


def copy_and_reverse(src, dest):
    text = ''
    with open(src, encoding="utf8") as fs:
        text = fs.read()

    with open(dest, 'w', encoding="utf8") as fd:
        fd.write(text[::-1])


if __name__ == '__main__':
    copy_file('file_copy/story.txt', 'file_copy/story_copy.txt')
    copy_and_reverse('file_copy/story.txt', 'file_copy/story_reversed.txt')

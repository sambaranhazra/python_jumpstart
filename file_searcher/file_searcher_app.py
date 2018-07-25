import os
import collections

SearchResult = collections.namedtuple("SearchResult", "file_name,line_number,line")


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("We can't search that location.")
        return
    text = get_search_text_from_user()
    if not text:
        print("We can't search for that text.")
        return

    search_matches = search_folders(folder, text)
    for match in search_matches:
        print("file name: {}, line number: {}, text: {}".format(match.file_name, match.line_number, match.line))


def print_header():
    print("------------------------")
    print("    FILE SEARCH APP     ")
    print("------------------------")


def get_folder_from_user():
    folder = input("What folder do you want to search")
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None
    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input("What are you searching for [single phrases only]?")
    if not text:
        print("We can't search for nothing!")
        return
    return text.lower()


def search_folders(folder, text):
    # all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folders(full_item, text)
            # all_matches.extend(search_folders(full_item, text))
        else:
            matches = search_file(full_item, text)
            # all_matches.extend(matches)
            yield from matches
    # return all_matches


def search_file(file_name, search_text):
    # matches = []
    with open(file_name, "r", encoding="utf-8", errors='ignore') as fin:
        number = 0
        for line in fin:
            number += 1
            if line.lower().find(search_text) >= 0:
                result = SearchResult(file_name=file_name, line=line, line_number=number)
                yield result
                # matches.append(result)
    # return matches


if __name__ == '__main__':
    main()

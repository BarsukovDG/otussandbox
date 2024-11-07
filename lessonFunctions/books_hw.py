from csv import DictReader
import json


def filter_lists(list_to_filter, keys_to_filter, add_books=False):
    """
    Used only to filter two of dict lists for this practice module.
    Returns list of new dicts

    :param list_to_filter: list of dictionaries to filter
    :param keys_to_filter: tuple of keys, that should to be in filtered objects
    :param add_books: True value add books key in dict
    """
    new_list = []
    new_dict = {}
    for item in list_to_filter:
        for k, v in item.items():
            if k in keys_to_filter:
                new_dict[k] = v
        if add_books:
            new_dict['books'] = []
        new_list.append(new_dict)
        new_dict = {}
    return new_list


def add_book_to_user_loop(books_list, user_list):
    """
    Adding books from book_list to user one-by-one

    :param books_list: list of books needed to be shared between users
    :param user_list: list of users to share books between
    """
    books_left = len(books_list)
    while books_left != 0:
        for user_data in user_list:
            user_data["books"].append(books_list[0])
            del books_list[0]
            books_left -= 1
            if not books_left:
                break
    return user_list


def get_result_json():
    books_list = []
    book_keys = ("Title", "Author", "Genre", "Pages")
    user_keys = ("name", "gender", "address", "age")

    with open('../hwFiles/books.csv', newline='') as books:
        reader = DictReader(books)
        for row in reader:
            books_list.append(row)

    with open('../hwFiles/users.json', 'r') as users:
        """
        To print readable json structure use indent in json.dumps method
        print(json.dumps(parsed, indent=4))
        """
        parsed = json.load(users)

    user_filtered = filter_lists(parsed, user_keys, add_books=True)
    books_filtered = filter_lists(books_list, book_keys, add_books=False)

    data = add_book_to_user_loop(books_filtered, user_filtered)

    with open('../hwFiles/results.json', 'w') as results:
        results.write(json.dumps(data, indent=4))

    """
    Task result example:
    
    [
        {
            "name": "Lolita Lynn",
            "gender": "female",
            "address": "389 Neptune Avenue, Belfair, Iowa, 6116",
            "age": 34,
            "books": [
                {
                    "title": "Fundamentals of Wavelets",
                    "author": "Goswami, Jaideva",
                    "pages": 228,
                    "genre": "signal_processing"
                }
            ]
        },
    ]
"""


get_result_json()

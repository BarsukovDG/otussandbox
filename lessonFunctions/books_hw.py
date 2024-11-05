from csv import DictReader
import json


def get_result_json():
    books_list = []
    books_filtered = []
    books_dict = {}
    result_dict = {}
    result_list = []
    book_keys = ("Title", "Author", "Genre", "Pages")
    user_keys = ("name", "gender", "address", "age", "books")

    with open('../hwFiles/books.csv', newline='') as books:
        reader = DictReader(books)
        for row in reader:
            books_list.append(row)
        print(len(books_list))
        for i in books_list:
            print(i)
            for k, v in i.items():
                print(f'the key is : {k}, and the value is {v}')
                if k in book_keys:
                    books_dict[k] = v
                    books_filtered.append(books_dict)
        print(len(books_filtered))
        # print(books_filtered[0])
        # print(books_filtered)

    with open('../hwFiles/users.json', 'r') as users:
        parsed = json.load(users)
        print(len(parsed))
        print(parsed)
        # print(json.dumps(parsed, indent=4))

    for _ in parsed:
        for k, v in _.items():
            if k in user_keys:
                result_dict[k] = v
                result_dict['books'] = []
                result_list.append(result_dict)
    # print(result_list)

    # for _ in books_list:
    #     print(_)

    # # with open('../hwFiles/results.json', 'w') as results:
    # #     results.write(json.dumps(data, indent=4))
    #
    """
    Result Example
    example = [
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

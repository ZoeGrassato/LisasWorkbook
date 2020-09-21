def workbook(n, k, arr):
    index = 1
    dictionary_of_chapters = {}
    for item in arr:
        if item >= k:
            number_of_pages = item / k
            if number_of_pages.is_integer():
                dictionary_of_chapters[index] = int(number_of_pages)
            else:
                dictionary_of_chapters[index] = int(number_of_pages) + 1
        else:
            dictionary_of_chapters[index] = 1
        index += 1

def determine_if_contains_special_problems(k, number_of_problems, current_chapter):



listOfItems = [4, 2, 6, 1, 10]
workbook(5, 3, listOfItems)







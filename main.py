def workbook(n, k, arr):
#here we determine how many pages will be needed per chapter
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

    special_problems = determine_special_problems(k, sum(arr), dictionary_of_chapters, arr)
    return special_problems



#here we determine if the pages for the current_chapter contain any special problems
def determine_special_problems(k, number_of_problems, chapters, arr):
    total_special_problems = 0
    index = 1
    page = 1

    for i in range (0, len(chapters)):
        num_of_problems_cur_chapter = arr[index - 1]
        problems_left = num_of_problems_cur_chapter
        num_of_pages_cur_chapter = chapters[index]

        for j in range(0, num_of_pages_cur_chapter):
            start_at = num_of_problems_cur_chapter - problems_left
            select_load = 0
            if j == num_of_pages_cur_chapter - 1:
                select_load = start_at + 1 + problems_left
            else:
                select_load = start_at + (k + 1)

            sublist = [i for i in range(start_at + 1, select_load)]
            if page in sublist:
                total_special_problems += 1
            problems_left = problems_left - 3
            page = page + 1
        index = index + 1

    return total_special_problems


listOfItems = [4, 2, 6, 1, 10]
workbook(5, 3, listOfItems)







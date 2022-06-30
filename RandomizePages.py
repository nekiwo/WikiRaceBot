import random


def randomize_pages(pages):
    new_pages = []

    i = 0
    done = False
    while not done:
        if pages[i] is not None:
            r = random.random()
            if r > 0.2:
                new_pages.append(pages[i])
                done = True
            else:
                i = i + 1
        else:
            new_pages.append(pages[i - 1])
            done = True

    return pages

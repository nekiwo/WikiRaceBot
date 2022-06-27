from ParsePageTitles import parse_page_titles
from api.FetchPage import fetch_page
from RandomizePages import randomize_pages
from RankPages import rank_pages


def main():
    start_article = input("Type starting article: ")
    end_article = input("Type starting article: ")

    print("Start Article: " + start_article)
    print("End Article: " + end_article)
    print("Start")

    ended = False
    current_article = start_article

    i = 0
    while not ended:
        pages = fetch_page(current_article)

        if end_article in pages:
            ended = True
            print("Finished in " + str(i) + " iterations")

        pages = parse_page_titles(pages)
        pages = rank_pages(pages)
        pages = randomize_pages(pages)

        current_article = pages[0]

        i = i + 1
        if i == 100:
            ended = True
            print("Finished due to limited iterations")


if __name__ == "__main__":
    main()

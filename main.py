from ParsePageTitles import parse_page_titles
from api.FetchPage import fetch_page
from RandomizePages import randomize_pages
from RankPages import rank_pages
import sys


def main():
    start_article = input("Type starting article: ")
    end_article = input("Type ending article: ")

    print("Start Article: " + start_article)
    print("End Article: " + end_article)
    print("Start")

    current_article = start_article

    i = 0
    while True:
        pages = fetch_page(current_article)
        print(current_article)

        if pages != 0:
            if end_article.lower() in [p.lower() for p in pages]:
                print("Finished in " + str(i) + " iterations")
                sys.exit()

            pages = parse_page_titles(pages)
            pages = rank_pages(pages, end_article)
            pages = randomize_pages(pages)

            current_article = pages[0]

            i = i + 1
            if i == 100:
                print("Limited iterations reached. Stop.")
                sys.exit()
        else:
            print("Can't fetch page. Stop.")
            sys.exit()


if __name__ == "__main__":
    main()

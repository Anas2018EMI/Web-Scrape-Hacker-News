from bs4 import BeautifulSoup
import requests

articles_titles = []
articles_links = []
articles_upvotes = []

response = requests.get("https://news.ycombinator.com/news")
hacker_news_webpage = response.text

soup = BeautifulSoup(hacker_news_webpage, "html.parser")
arcticles = soup.select(".titleline > a")
# print(len(arcticles))
for title in arcticles:
    article_title = title.string
    article_link = title.get("href")
    articles_titles += [article_title]
    articles_links += [article_link]
    # print(f"article_title: {article_title}")
    # print(f"article_link: {article_link}")
    # print()
# print()
# print()
# print()

subtexts = soup.find_all(class_="subtext")
for subtext in subtexts:
    upvote = subtext.find(class_="score")
    # print(upvote)
    if upvote == None:
        article_upvote = 0
    else:
        article_upvote = int(upvote.get_text().strip(" points"))

    # print(f"article_upvote: {article_upvote}")
    articles_upvotes += [article_upvote]
    # print()

# print(len(articles_titles))
# print(articles_titles)
# print()
# print(len(articles_links))
# print(articles_links)
# print()
# print(len(articles_upvotes))
# print(articles_upvotes)
highest_upvote_index = articles_upvotes.index(max(articles_upvotes))

print(
    f"The highest upvote points article:\n {articles_titles[highest_upvote_index]} \n{articles_links[highest_upvote_index]}")

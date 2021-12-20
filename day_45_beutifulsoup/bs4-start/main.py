from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
content = response.text

soup = BeautifulSoup(content, 'html.parser')
article_text = []
article_link = []
articles = soup.find_all('a', class_='titlelink')
for article in articles:
    text = article.text
    article_text.append(text)
    link = article.get("href")
    article_link.append(link)

article_upvote = [int(score.text.split()[0]) for score in soup.find_all(
    'span', class_='score')]


# print(article_text)
# print(article_link)
print(article_upvote)
max_upvote = max(article_upvote)
max_upvote_index = article_upvote.index(max_upvote)+1

print(f'The article with the most upvotes is {article_text[max_upvote_index]}')

# with open('./website.html', 'r', encoding='utf-8') as html:
#     website = html.read()

# soup = BeautifulSoup(website, 'html.parser')

# anchor_tags = soup.find_all()
# # print(anchor_tags)

# class_heading = soup.find_all('h3', class_='heading')
# # print(class_heading)

# name = soup.select_one('#name')
# # print(name.getText())

# heading = soup.select('heading')
# print(heading)

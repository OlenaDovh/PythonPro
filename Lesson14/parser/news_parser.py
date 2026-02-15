import requests as req
from bs4 import BeautifulSoup
import pandas as pd
import dateparser


def get_page(url: str) -> BeautifulSoup | None:
    """Returns html code of input link page"""
    try:
        response = req.get(url, timeout=30)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'lxml')
    except Exception as e:
        print(e)
        return None


def parse_news(soup: BeautifulSoup) -> list[dict]:
    """Returns list of the news with its title, url, date, description"""
    if not soup:
        return []

    news = soup.find_all("div", class_="article_title")
    news_list = []

    for item in news:
        try:
            a = item.find("a")
            if not a:
                continue

            link = a.get("href")
            title = a.get_text(strip=True)

            elem = item.parent
            div = elem.find("div", class_="article_date")
            if div:
                date = div.get_text(strip=True).replace("Переклад iPress– ", "").strip()
                formated_date = dateparser.parse(date, languages=['uk'])
            else:
                formated_date = None

            news_list.append({
                "title": title,
                "link": link,
                "date": formated_date
            })

        except Exception as e:
            print(e)
            continue

    return news_list


def save_to_csv(news_file_name, data: list[dict], period: int = 100) -> None:
    """Creates csv file with the main news data in it"""
    if not data:
        return

    df = pd.DataFrame(data)

    if 'date' in df.columns:
        df = df[df['date'] > (pd.Timestamp.now().normalize() - pd.Timedelta(days=period))]
        df = df.sort_values(by='date', ascending=False)

    df.to_csv(news_file_name, index=False, encoding="utf-8")


def parse(url: str, news_file_name: str, period: int = 100) -> None:
    """Unified function for use in external space"""
    news_data = get_page(url)
    news_list = parse_news(news_data)
    save_to_csv(news_file_name, news_list, period)

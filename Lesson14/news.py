from parser import parse, get_count_by_date_report

parse("https://ipress.ua", "news.csv", 7)

get_count_by_date_report("news.csv", "report_news.csv")

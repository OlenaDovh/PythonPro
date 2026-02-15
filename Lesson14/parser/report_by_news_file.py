import pandas as pd


def get_count_by_date_report(file: str, report_file_name: str) -> None | str:
    """Creates report (csv) with the count of news per day"""
    try:
        df = pd.read_csv(file, parse_dates=['date'], encoding="utf-8")
        report_df = df.groupby(df['date'].dt.date)['title'].count().sort_index(ascending=False)
        report = report_df.reset_index()
        report.columns = ['Дата', 'Кількість новин']
        report.to_csv(report_file_name, index=False, encoding="utf-8")
    except Exception as e:
        print(e)

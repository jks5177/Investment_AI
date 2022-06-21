import requests
import pandas as pd

# 크롤링을 위한 함수화
def hankyung_data(fromDate, toDate, reportType='ALL', gradeCode='ALL',changePrices='ALL',searchType='ALL') :
    url = f'https://markets.hankyung.com/api/v1/consensus/search/report?page=1&reportType={reportType}&fromDate={fromDate}&toDate={toDate}&gradeCode={gradeCode}&changePrices={changePrices}&searchType={searchType}'
    response = requests.get(url)
    last_page = response.json()['last_page']
    datas = []
    for page in range(1, last_page+1) :
        url = f'https://markets.hankyung.com/api/v1/consensus/search/report?page={page}&reportType={reportType}&fromDate={fromDate}&toDate={toDate}&gradeCode={gradeCode}&changePrices={changePrices}&searchType={searchType}'
        response = requests.get(url)
        data = response.json()['data']
        if type(data) == dict :
            data = data.values()
        datas.append(pd.DataFrame(data))
    df = pd.concat(datas)
    df.reset_index(inplace=True)
    df.dropna(axis=1, inplace=True)
    result_df = df[['REPORT_IDX', 'PUBLISH_CODE', 'OFFICE_NAME', 'INDUSTRY_CODE', 'INDUSTRY_NAME', 'REPORT_TITLE', 'REPORT_WRITER', 'REPORT_FILEPATH', 'REPORT_DATE']]
    
    return result_df
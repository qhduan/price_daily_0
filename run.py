import os
import akshare as ak

stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
codes = list(stock_zh_a_spot_em_df['代码'])
os.makedirs('stocks', exist_ok=True)
codes = [
    code
    for code in codes
    if int(code) % 10 == 0
]
for i, code in enumerate(codes):
    print(f'{i + 1}/{len(codes)} {code}')
    try:
        stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=code, period="daily", adjust="qfq")
        with open(f'stocks/{code}.csv', 'w') as fp:
            fp.write(stock_zh_a_hist_df.to_csv(index=False))
    except:
        print(f'{code} failed')

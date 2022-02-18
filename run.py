import os
import akshare as ak

stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
codes = list(stock_zh_a_spot_em_df['代码'])
os.makedirs('stocks', exist_ok=True)
for code in codes:
    print(code)
    stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=code, period="daily", adjust="qfq")
    with open(f'stocks/{code}.csv', 'w') as fp:
        fp.write(stock_zh_a_hist_df.to_csv(index=False))


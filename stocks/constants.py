import os

current_dir = os.path.dirname(os.path.realpath(__file__))
db_file_path = os.path.join(current_dir, "../data/stocks.db")
csv_file_paty = os.path.join(current_dir, "../data/stocks.csv")
chromedriver_path = "C:\\Users\\ralph\\Downloads\\chromedriver.exe"

SYMBOLS = ['CMA', 'DLTR', 'ICE', 'BA', 'FIS', 'AMP', 'XLNX', 'LEG', 'C', 'RHI', 'GPC', 'LEN', 'MSI', 'MRK', 'STZ',
           'TMK', 'SHW', 'ADI', 'XYL', 'HRS', 'NFX', 'ES', 'HUM', 'PCLN', 'CF', 'ETN', 'LB', 'GOOG', 'AET', 'DAL',
           'CVS', 'DHR', 'MUR', 'PX', 'SPY', 'GWW', 'AVGO', 'FTR', 'SQ', 'JPM', 'MKC', 'BBBY', 'YHOO', 'SIG', 'TEL',
           'CTSH', 'TXT', 'KO', 'YUM', 'TMO', 'QCOM', 'AIG', 'VLO', 'NKE', 'URI', 'PGR', 'XRX', 'EXPE', 'AAPL', 'D',
           'FISV', 'LLTC', 'TSCO', 'K', 'ORCL', 'TWTR', 'AYI', 'IVZ', 'DHI', 'BDX', 'PBCT', 'CXO', 'CPB', 'FSLR', 'CL',
           'PDCO', 'RSG', 'MAR', 'TRIP', 'WFC', 'ULTA', 'MCK', 'WHR', 'NDAQ', 'SRCL', 'BIIB', 'BEN', 'CMG', 'ISRG',
           'SNA', 'CMCSA', 'FMC', 'AON', 'FTI', 'EQR', 'HP', 'CTAS', 'PSA', 'CME', 'ADP', 'BLL', 'DOW', 'AJG', 'ITW',
           'KSU', 'APH', 'JBHT', 'AES', 'SLG', 'WM', 'ILMN', 'LLL', 'HIG', 'EA', 'PSX', 'MAC', 'STX', 'SRE', 'CSX',
           'KMX', 'MDLZ', 'CB', 'CI', 'TIF', 'OKE', 'PYPL', 'MTD', 'VRSK', 'BBT', 'AVY', 'ABC', 'JNPR', 'GOOGL', 'TGT',
           'DVA', 'FAST', 'BCR', 'PPL', 'DUK', 'UNM', 'CNP', 'CTXS', 'TRV', 'IDXX', 'SLB', 'CBG', 'BBY', 'VFC', 'XOM',
           'GT', 'MSFT', 'FLIR', 'CFG', 'M', 'CAG', 'IP', 'LOW', 'DE', 'VRSN', 'GD', 'MMC', 'IBM', 'CVX', 'EL', 'WBA',
           'MCHP', 'AXP', 'EQT', 'DTE', 'MS', 'ADSK', 'PWR', 'MCO', 'LRCX', 'NFLX', 'COH', 'EVHC', 'WY', 'XRAY', 'JNJ',
           'EBAY', 'AMG', 'GM', 'NVDA', 'AZO', 'MHK', 'BAX', 'UNP', 'KHC', 'PHM', 'LH', 'MCD', 'PBI', 'CBS', 'ENDP',
           'BRK-B', 'UHS', 'TROW', 'SWKS', 'MO', 'DRI', 'KORS', 'RCL', 'KMB', 'KMI', 'INTU', 'FFIV', 'VAR', 'BMY',
           'MMM', 'ALB', 'VNO', 'WMT', 'COO', 'EQIX', 'NTRS', 'SPLS', 'HAR', 'EFX', 'FB', 'URBN', 'A', 'BAC', 'MOS',
           'BABA', 'CHD', 'ABT', 'ARNC', 'AIZ', 'NRG', 'VIAB', 'DLPH', 'HAWK', 'EXPD', 'KLAC', 'DNB', 'AEP', 'PCG',
           'KEY', 'IFF', 'APA', 'REGN', 'HPQ', 'WLTW', 'WEC', 'FITB', 'UNH', 'TJX', 'GPN', 'PH', 'TDC', 'SWN', 'EOG',
           'FOXA', 'UA', 'CSCO', 'PPG', 'R', 'CSRA', 'IRM', 'HRB', 'MU', 'DLR', 'ADM', 'LNC', 'COST', 'CELG', 'RHT',
           'NI', 'RL', 'IPG', 'SCG', 'DISCA', 'ADBE', 'PG', 'GGP', 'LLY', 'INTC', 'VTR', 'ABBV', 'DOV', 'KR', 'PEG',
           'DISCK', 'SWK', 'WMB', 'LNT', 'AIV', 'APD', 'AAP', 'NWSA', 'FRT', 'SCHW', 'QRVO', 'RIG', 'UVXY', 'WRK',
           'ALXN', 'AME', 'MYL', 'NUE', 'AKAM', 'LVLT', 'ALL', 'FL', 'ORLY', 'CCI', 'UAL', 'LUK', 'BSX', 'UDR', 'TSN',
           'NBL', 'APC', 'AMT', 'SO', 'OMC', 'CHK', 'UAA', 'NWS', 'ROST', 'COF', 'BXP', 'MA', 'CINF', 'PFE', 'PNR',
           'FE', 'MET', 'HSIC', 'CA', 'UTX', 'CMI', 'FOX', 'SJM', 'L', 'HAS', 'LMT', 'AMZN', 'FCX', 'MAT', 'HBAN',
           'LKQ', 'NAVI', 'HES', 'CAH', 'AEE', 'KIM', 'FTV', 'PEP', 'HAL', 'MJN', 'HBI', 'V', 'TSO', 'DG', 'PNC', 'ACN',
           'MTB', 'TAP', 'DGX', 'COP', 'HD', 'EXC', 'AAL', 'HST', 'CAT', 'ALLE', 'GILD', 'HOG', 'MRO', 'ETR', 'CLX',
           'HCA', 'T', 'TSLA', 'DVN', 'MNK', 'SYMC', 'EMN', 'CNC', 'ECL', 'MAA', 'WYNN', 'NEM', 'ATVI', 'RRC', 'ROK',
           'HCP', 'EXR', 'TGNA', 'FLR', 'SYK', 'AMGN', 'PXD', 'CTL', 'GRMN', 'PAYX', 'SEE', 'BWA', 'WDC', 'AFL', 'DD',
           'STI', 'WFM', 'RF', 'ETFC', 'ZTS', 'LYB', 'GLD', 'JEC', 'F', 'XEL', 'MLM', 'TXN', 'LUV', 'PCAR', 'HCN',
           'NOC', 'DFS', 'GPS', 'IR', 'SYF', 'FDX', 'EIX', 'GIS', 'SPGI', 'STT', 'AWK', 'JCI', 'ESRX', 'TDG', 'O',
           'MAS', 'OXY', 'CHRW', 'ADS', 'NTAP', 'FLS', 'AVB', 'HRL', 'NOV', 'COG', 'QQQ', 'MNST', 'VRTX', 'NLSN', 'ALK',
           'ZION', 'GLW', 'DIS', 'CHTR', 'EDIT', 'WAT', 'NWL', 'TSS', 'WU', 'AMAT', 'VMC', 'PKI', 'VZ', 'UPS', 'XEC',
           'HPE', 'MON', 'CCL', 'HON', 'ROP', 'PVH', 'PLD', 'AGN', 'ANTM', 'JWN', 'XL', 'USB', 'RAI', 'BLK', 'CERN',
           'COL', 'ESS', 'SLV', 'RTN', 'HOLX', 'GS', 'MPC', 'CRM', 'TWX', 'BF-B', 'CMS', 'SYY', 'PFG', 'SNI', 'MDT',
           'SBUX', 'EMR', 'BHI', 'COTY', 'KSS', 'PNW', 'BK', 'PRU', 'SPG', 'WYN', 'SE', 'NEE', 'EW', 'ZBH', 'FBHS',
           'HSY', 'DPS', 'ED', 'NSC', 'PRGO', 'PM', 'AN', 'GE']

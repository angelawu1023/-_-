# %%
import pandas as pd
import numpy as np
from pathlib import Path

INPUT_CSV = "spotify_user.csv"
OUTPUT_CSV = "spotify_country_subscription_ratios.csv"

# 可能的欄位名稱候選，程式會自動找出存在的欄位
COUNTRY_CANDIDATES = ['country', 'Country', 'COUNTRY', 'user_country', 'country_name']
SUB_CANDIDATES = ['plan', 'subscription_type', 'account_type', 'product', 'level', 'membership', 'status', 'account_type_name']

def find_column(df, candidates):
    for c in candidates:
        if c in df.columns:
            return c
    return None

def normalize_subscription(s):
    """把各種文字形式映射為 Family/Premium/Student/Free/Other"""
    if pd.isna(s):
        return 'Other'
    t = str(s).lower().strip()
    # 先處理 family（例如 "Premium Family", "family plan"）
    if 'family' in t:
        return 'Family'
    if 'student' in t:
        return 'Student'
    if 'premium' in t:
        # 注意：若 'premium family' 已在上面被 family 捕捉
        return 'Premium'
    # free 或 trial 視為 Free
    if 'free' in t or 'trial' in t:
        return 'Free'
    # 其他常見字串可擴充
    return 'Other'

def main():
    path = Path(INPUT_CSV)
    if not path.exists():
        raise FileNotFoundError(f"找不到 {INPUT_CSV}，請確認檔案放在同一目錄下。")

    df = pd.read_csv(path, dtype=str)  # 先以字串讀取，避免類型問題

    country_col = find_column(df, COUNTRY_CANDIDATES)
    sub_col = find_column(df, SUB_CANDIDATES)

    if country_col is None:
        raise ValueError(f"找不到 country 欄位。候選名稱：{COUNTRY_CANDIDATES}。目前 csv 欄位：{list(df.columns)}")
    if sub_col is None:
        raise ValueError(f"找不到 subscription/account 欄位。候選名稱：{SUB_CANDIDATES}。目前 csv 欄位：{list(df.columns)}")

    # 若 country 有缺值，標成 Unknown（或可改為 dropna）
    df[country_col] = df[country_col].fillna('Unknown')

    # 建立標準化欄位
    df['sub_category'] = df[sub_col].apply(normalize_subscription)

    # 計算每個 country 的各類使用者數量
    counts = df.groupby(country_col)['sub_category'].value_counts().unstack(fill_value=0)

    # 確保有這些欄位（若某些類別不存在則補 0）
    for col in ['Family', 'Premium', 'Student', 'Free', 'Other']:
        if col not in counts.columns:
            counts[col] = 0

    # 重新排序欄位
    counts = counts[['Family', 'Premium', 'Student', 'Free', 'Other']]

    # 加上 total 與比率
    counts['Total_users'] = counts.sum(axis=1)
    # 避免除以零
    ratios = counts[['Family','Premium','Student','Free']].div(counts['Total_users'], axis=0).fillna(0)
    ratios = ratios.rename(columns={
        'Family': 'Family_ratio',
        'Premium': 'Premium_ratio',
        'Student': 'Student_ratio',
        'Free': 'Free_ratio'
    })

    # 若你也要 Other_ratio 可以啟用下面一行
    counts['Other_ratio'] = (counts['Other'] / counts['Total_users']).fillna(0)

    # 合併輸出表格
    result = counts.reset_index().merge(ratios.reset_index(), on=country_col)

    # 建議欄位順序
    cols_order = [country_col, 'Total_users',
                  'Family', 'Premium', 'Student', 'Free', 'Other',
                  'Family_ratio', 'Premium_ratio', 'Student_ratio', 'Free_ratio', 'Other_ratio']
    # 若某些欄位不存在則過濾
    cols_order = [c for c in cols_order if c in result.columns]
    result = result[cols_order]

    # 儲存 CSV
    result.to_csv(OUTPUT_CSV, index=False, encoding='utf-8-sig')
    print(f"已輸出：{OUTPUT_CSV}（行數：{len(result)}）")

if __name__ == "__main__":
    main()

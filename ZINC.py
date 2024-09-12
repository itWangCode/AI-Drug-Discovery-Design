import requests
import pandas as pd
from tqdm import tqdm
from rdkit import Chem
from rdkit.Chem import Descriptors

# 辅助函数：将IC50转换为pIC50
def convert_ic50_to_pic50(IC50_value):
    try:
        return 9 - math.log10(IC50_value)
    except (ValueError, ZeroDivisionError):
        return None

# 辅助函数：从ZINC数据库获取化合物信息
def fetch_zinc_compounds(mwt_min, mwt_max, logp_min, logp_max):
    url = f"http://zinc15.docking.org/substances/subsets/purchasable/filters/?mwt-between={mwt_min},{mwt_max}&logp-between={logp_min},{logp_max}&output=csv"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        compounds_df = pd.read_csv(response.content.decode('utf-8'))
        return compounds_df
    else:
        print("Failed to fetch data")
        return None

# 设置分子量和logP过滤条件
mwt_min, mwt_max = 200, 250  # 分子量范围
logp_min, logp_max = 4, 4.5  # logP范围

# 获取符合条件的化合物
compounds_df = fetch_zinc_compounds(mwt_min, mwt_max, logp_min, logp_max)

# 如果有数据，继续处理
if compounds_df is not None:
    # 筛选需要的列
    compounds_df = compounds_df[['smiles', 'zinc_id', 'inchikey', 'mwt', 'logp', 'reactive', 'purchasable', 'tranche_name', 'features']]


    # 打印并保存为CSV文件
    print(compounds_df.head())
    compounds_df.to_csv('zinc_compounds_filtered.csv', index=False)

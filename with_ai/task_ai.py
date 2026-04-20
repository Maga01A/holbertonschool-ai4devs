import pandas as pd

def ai_processor(filename, category, page, page_size):
    # AI suggested using pandas for better efficiency
    df = pd.read_csv(filename)
    filtered_df = df[df['category'] == category]
    
    return filtered_df.iloc[(page-1)*page_size : page*page_size].to_dict('records')

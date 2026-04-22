import pandas as pd

def process_data_with_ai(file_path):
    # Prompt: "Write a python function to read a CSV, remove nulls, and group by category"
    df = pd.read_csv(file_path)
    df_cleaned = df.dropna()
    summary = df_cleaned.groupby('category').sum()
    return summary

if __name__ == "__main__":
    print("AI-optimized data processor ready.")

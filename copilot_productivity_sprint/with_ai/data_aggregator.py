import pandas as pd

def aggregate_user_data(csv_file):
    # Prompt: "Using pandas, write a function to group data by 'user_id' and sum 'session_time'"
    try:
        df = pd.read_csv(csv_file)
        result = df.groupby('user_id')['session_time'].sum().reset_index()
        return result
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    print("AI-Generated Aggregator Ready.")

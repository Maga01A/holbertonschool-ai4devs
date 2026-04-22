def calculate_efficiency_gain(manual_time, ai_time):
    # Prompt: "Write a python function to calculate percentage decrease between two numbers"
    if manual_time <= 0:
        return 0
    gain = ((manual_time - ai_time) / manual_time) * 100
    return round(gain, 2)

if __name__ == "__main__":
    print(f"Efficiency Gain: {calculate_efficiency_gain(120, 30)}%")

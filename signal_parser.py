import json, re

def parse_signal(json_path='signal.json'):
    with open(json_path, 'r') as f:
        data = json.load(f)

    caption = data["message"].get("caption", "")
    symbol = re.search(r'(XAUUSD|EURUSD|GBPUSD)', caption).group(1)
    action = "BUY" if "BUY" in caption.upper() else "SELL"

    nums = [float(x) for x in re.findall(r'\d{3,5}', caption)]
    return {
        "symbol": symbol,
        "action": action,
        "entry_zone": nums[:2],
        "stoploss": nums[2],
        "take_profit": nums[-1]
    }

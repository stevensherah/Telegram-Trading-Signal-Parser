import MetaTrader5 as mt5

def connect_mt5():
    if not mt5.initialize():
        raise RuntimeError("MT5 failed")

def place_trade(signal):
    mt5.symbol_select(signal["symbol"], True)
    return mt5.order_send({
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": signal["symbol"],
        "volume": 0.1,
        "type": mt5.ORDER_TYPE_BUY,
        "price": mt5.symbol_info_tick(signal["symbol"]).ask,
        "sl": signal["stoploss"],
        "tp": signal["take_profit"],
        "magic": 10001,
        "comment": "Signal Bot"
    })

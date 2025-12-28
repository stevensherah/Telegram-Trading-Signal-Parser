from sqlalchemy import *
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()
engine = create_engine("sqlite:///trades.db")
Session = sessionmaker(bind=engine)

class Trade(Base):
    __tablename__ = "trades"
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    action = Column(String)
    entry = Column(String)
    sl = Column(Float)
    tp = Column(Float)
    time = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)

def log_trade(s):
    session = Session()
    t = Trade(symbol=s["symbol"], action=s["action"],
              entry=str(s["entry_zone"]), sl=s["stoploss"], tp=s["take_profit"])
    session.add(t)
    session.commit()

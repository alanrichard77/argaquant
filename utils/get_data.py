import yfinance as yf
import pandas as pd

def get_company_data(query):
    try:
        ticker = yf.Ticker(query + ".SA")
        hist = ticker.history(period="6mo")
        name = ticker.info.get("shortName", "Empresa")

        price_plot = {
            "data": [{
                "x": hist.index.strftime('%Y-%m-%d').tolist(),
                "y": hist['Close'].tolist(),
                "type": "scatter",
                "name": "Preço"
            }],
            "layout": {"title": "Histórico de Preço"}
        }

        return {
            "ticker": query.upper(),
            "name": name,
            "price_plot": price_plot,
            "pl": round(ticker.info.get("trailingPE", 0), 2),
            "dy": round(ticker.info.get("dividendYield", 0) * 100, 2) if ticker.info.get("dividendYield") else 0,
        }
    except:
        return None
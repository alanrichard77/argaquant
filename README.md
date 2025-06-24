# ARGA QUANT - O Futuro dos Investimentos

ARGA QUANT é um projeto de análise de ações brasileiras, inspirado na proposta do Simply Wall St, porém com foco total no mercado nacional e adaptado às fontes de dados disponíveis no Brasil.

### 🔍 Funcionalidades:

- Coleta de dados automatizada de múltiplas fontes:
  - StatusInvest (API)
  - Fundamentus (scraping)
  - Yahoo Finance (preço e volume)
- Indicadores fundamentais:
  - P/L, P/VP, EV/EBITDA, ROE, ROIC, Margens
  - Endividamento e liquidez
  - Dividendos e payout
- Indicadores técnicos:
  - RSI, Médias móveis, Candlestick de reversão
- Comparativos com setor e histórico de lucros
- Visual moderno com Plotly
- Rodapé com direitos reservados
- Hospedável no Replit, com `gunicorn`

### 🧰 Instalação

1. Suba os arquivos no [Replit](https://replit.com/)
2. Verifique se o `requirements.txt` inclui:
    - flask
    - plotly
    - pandas
    - yfinance
    - numpy
    - gunicorn
    - requests
    - beautifulsoup4
3. O comando de execução correto no Replit deve ser:

```bash
gunicorn app:app --bind=0.0.0.0:8000
```

### 👨‍💻 Em breve:
- Comparação entre empresas
- Módulo de geração de relatórios em PDF
- Login para salvar carteiras

---

© ARGA - Todos os direitos reservados - 2025
# Product Analytics Dashboard

Camada de métricas para um dashboard de produto: funil de ativação, usuários
ativos por dia e retenção por coorte semanal.

## O que demonstra

- definição de métricas com usuários únicos;
- normalização de eventos e timestamps;
- análise de funil e coortes para apoiar decisões de produto;
- testes automatizados para evitar contagens duplicadas.

## Executar

```powershell
pip install -r requirements.txt
python -m unittest discover -s tests -v
```

Os eventos do exemplo são sintéticos. Uma camada visual pode consumir as
funções em `src/metrics.py` usando Streamlit, Metabase ou outra ferramenta.

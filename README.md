<p align="center">
  <img src="https://github.com/RafaelGallo/Case-Tecnico-Data-Science-Labs/blob/main/img/log/designer-usando-uma-tecnologia-futurista-de-tela-de-tablet-digital-transparente.jpg?raw=true" alt="Capa do Projeto - Data Science Labs" width="850"/>
</p>

<h1 align="center">Case Técnico — Data Science Labs</h1>
<h3 align="center">Predição de Preços de Imóveis em Tóquio (Tokyo Housing Price Prediction)</h3>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python"></a>
  <a href="https://pandas.pydata.org/"><img src="https://img.shields.io/badge/Pandas-Data_Analysis-150458?logo=pandas&logoColor=white" alt="Pandas"></a>
  <a href="https://numpy.org/"><img src="https://img.shields.io/badge/Numpy-Numerical_Computing-013243?logo=numpy&logoColor=white" alt="Numpy"></a>
  <a href="https://scikit-learn.org/"><img src="https://img.shields.io/badge/Scikit--Learn-Machine_Learning-F7931E?logo=scikit-learn&logoColor=white" alt="Scikit-learn"></a>
  <a href="https://lightgbm.readthedocs.io/"><img src="https://img.shields.io/badge/LightGBM-Boosting_Model-00C48D?logo=lightgbm&logoColor=white" alt="LightGBM"></a>
  <a href="https://xgboost.readthedocs.io/"><img src="https://img.shields.io/badge/XGBoost-Gradient_Boosting-EB8C00?logo=xgboost&logoColor=white" alt="XGBoost"></a>
  <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit"></a>
  <a href="https://sqlite.org/"><img src="https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white" alt="SQLite"></a>
  <a href="https://github.com/RafaelGallo/Case-Tecnico-Data-Science-Labs"><img src="https://img.shields.io/badge/Status-Completed-success?logo=github" alt="Status"></a>
</p>


## Introdução

O projeto **Case Técnico – Data Science Labs** tem como objetivo **analisar e prever os preços de imóveis na região de Tóquio** com base em atributos estruturais, geográficos e urbanísticos.A solução foi desenvolvida como parte de um **desafio técnico de Data Science**, aplicando um fluxo completo de ciência de dados — desde o **ETL e tratamento de dados** até a **modelagem de Machine Learning** e análise dos resultados. A base de dados, inicialmente composta por **arquivos CSV**, foi consolidada em um **banco SQLite (`tokyo.sqlite`)**, permitindo consultas otimizadas e integração fluida com o pipeline analítico. A partir disso, foram realizadas etapas de **limpeza, engenharia de atributos e análises exploratórias** para compreender os principais fatores que influenciam o preço de venda de imóveis.

Entre os principais objetivos do projeto estão:

* **Identificar padrões espaciais e temporais** no mercado imobiliário de Tóquio;
* **Analisar correlações** entre área, preço por m², zoneamento e localização;
* **Desenvolver e comparar modelos de Machine Learning** para previsão de preços;
* **Interpretar as variáveis mais relevantes** que impactam o valor dos imóveis;
* **Gerar insights acionáveis** para suporte a decisões de investimento e planejamento urbano.

O projeto demonstra a aplicação prática de **boas práticas em ciência de dados**, unindo **engenharia de dados, estatística e aprendizado de máquina** em um pipeline integrado e replicável.
*Em suma, este projeto representa um case completo de Data Science aplicado ao setor imobiliário, com foco em previsibilidade, explicabilidade e valor analítico real.*

## **Tecnologias Utilizadas**

* **Python 3.10+**
* **Bibliotecas:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `xgboost`, `lightgbm`, `sqlite3`, `tqdm`
* **Ambiente:** Jupyter / VSCode
* **Controle de versão:** Git + GitHub (Git LFS para `tokyo.sqlite`)

### **Estrutura do Repositório**

```
Case-Tecnico-Data-Science-Labs
 ┣ app/              → Aplicação (API, Streamlit, dashboards)
 ┣ data/             → Dados brutos e tratados (CSVs)
 ┣ db/               → Banco SQLite (tokyo.sqlite)
 ┣ doc/              → Documentação e relatórios técnicos
 ┣ img/              → Imagens usadas nos notebooks e slides
 ┣ models/           → Modelos treinados (.pkl, .joblib)
 ┣ notebook/         → Notebooks exploratórios e finais
 ┣ output/           → Resultados de previsões e métricas
 ┣ py/               → Scripts auxiliares
 ┣ sql/              → Consultas SQL e criação de tabelas
 ┣ src/              → Código-fonte principal (pipelines, EDA, ML)
 ┣ .gitattributes    → Configuração Git LFS (para arquivos grandes)
 ┣ .gitignore        → Exclusões de cache e dados sensíveis
 ┣ LICENSE           → Licença aberta do projeto
 ┗ README.md         → Documentação principal
```

### **Base de Dados**

* **Origem:** Arquivos CSV integrados em um banco SQLite (`db/tokyo.sqlite`)
* **Tamanho:** ~91 MB (armazenado via Git LFS)
* **Principais Variáveis:**

  * `Area`, `TotalFloorArea`, `Frontage`, `Breadth`, `CoverageRatio`,
    `FloorAreaRatio`, `MinTimeToNearestStation`, `MaxTimeToNearestStation`,
    `UnitPrice`, `PricePerTsubo`, `Type_le`, `Region_le`, `Prefecture_le`, `CityPlanning_le`
* **Alvo (target):** `TradePrice`

### *Pipeline do Projeto**

<img width="754" height="601" alt="image" src="https://github.com/user-attachments/assets/bd43a18a-7212-45dd-92b5-d04a6c34b163" />

**Etapas:**

1. **ETL:** Extração e carga dos CSVs para o banco SQLite
2. **Pré-processamento:** `fillna`, `dropna`, `astype`, `LabelEncoder`, `merge`
3. **Análise exploratória (EDA):** Outliers, correlação e distribuição de variáveis
4. **Feature Engineering:** Criação e normalização de atributos
5. **Modelagem:** Avaliação de algoritmos (Linear, Ridge, Lasso, XGBoost, GradientBoosting, etc.)
6. **Validação:** RMSLE, MAPE e R²
7. **Deploy:** Batch/API Prediction e integração via cloud

### **Principais Resultados**

| Modelo               | RMSLE    | MAPE      | R²       |
| :------------------- | :------- | :-------- | :------- |
| **GradientBoosting** | **0.88** | **1.079** | **0.72** |

*GradientBoosting* apresentou melhor performance geral, com boa aderência entre valores reais e previstos.

### **Análises Complementares**

* **Correlação:** forte relação entre `Area`, `TotalFloorArea` e `TradePrice`.
* **Outliers:** tratados via Z-Score para `Area` e `TradePrice`.
* **Feature Importance:** `TotalFloorArea` e `Area` se destacam como as mais relevantes.

### **Tecnologias Utilizadas**

* **Linguagem:** Python 3.10+
* **Principais bibliotecas:**

  * `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`
  * `xgboost`, `lightgbm`, `sqlite3`, `tqdm`
* **Ambiente:** Jupyter / VSCode
* **Controle de versão:** Git + GitHub (com LFS)

### **Como Reproduzir o Projeto**

```bash
# Clonar o repositório
git clone https://github.com/seuusuario/Case-Tecnico-Data-Science-Labs.git
cd Case-Tecnico-Data-Science-Labs

# Criar ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instalar dependências
pip install -r requirements.txt

# Executar notebook
jupyter notebook notebook/Case_DataScienceLabs.ipynb
```

## **Análise de Dados**

Estudo exploratório para identificar padrões e tendências de preço por região, área e ano de construção.

### Correlação das Variáveis

<img src="https://github.com/RafaelGallo/Case-Tecnico-Data-Science-Labs/blob/main/img/0.png" width="700"/>

### Top 10 Regiões com Maior Preço de Venda

<img src="https://github.com/RafaelGallo/Case-Tecnico-Data-Science-Labs/blob/main/img/3.png" width="700"/>

**Insight: Regiões com os Imóveis mais Caros em Tokyo**

1. **Áreas Comerciais** têm os imóveis mais caros da cidade, com uma **mediana de ¥82 milhões**. Isso destaca o alto valor de terrenos com potencial para empreendimentos ou uso corporativo.
2. Em segundo lugar, aparecem as **Áreas Industriais** com ¥55 milhões, sugerindo uma valorização crescente — talvez por reurbanização ou reconversão para empreendimentos mistos.
3. As **Áreas Residenciais Tradicionais** ocupam o terceiro lugar com ¥42 milhões, reforçando sua atratividade para moradia, mas ainda abaixo do apelo comercial e industrial.
4. A categoria **Unknown** (¥25M) e **Potential Residential Area** (¥10M) representam terrenos com menor atratividade — possivelmente pela falta de infraestrutura, documentação ou localização.

**Implicações Estratégicas**

* **Investidores** podem mirar áreas industriais e comerciais para empreendimentos de alto padrão ou geração de renda com aluguel.
* **Construtoras e urbanistas** podem enxergar oportunidades de crescimento em áreas potenciais com preços ainda acessíveis.
* A diferença de valor entre “Commercial” e “Potential Residential” é de mais de **700%**, mostrando forte disparidade e margem para valorização futura.


### Preço Médio por m² (faixas de área)

<img src="https://github.com/RafaelGallo/Case-Tecnico-Data-Science-Labs/blob/main/img/4.png" width="700"/>

**Top 10 Regiões por Mediana de Preço de Venda (TradePrice)**

O gráfico apresenta as regiões com maior mediana de preço de venda (em milhões de ienes). Dentre as regiões, destacam-se:

| Região                     | Mediana de Preço de Venda (¥) |
| -------------------------- | ----------------------------- |
| Commercial Area            | ¥ 82 milhões                  |
| Industrial Area            | ¥ 55 milhões                  |
| Residential Area           | ¥ 42 milhões                  |
| Unknown                    | ¥ 25 milhões                  |
| Potential Residential Area | ¥ 10 milhões                  |

* **Commercial Area** lidera com ampla margem, sendo a região com maior mediana de preço — ¥82M. Isso reflete o valor agregado de áreas com infraestrutura voltada para atividades comerciais.
* **Industrial Area** aparece em segundo lugar, indicando valorização de áreas industriais, possivelmente por localização estratégica ou demanda.
* **Residential Area** tem mediana mais baixa que a industrial, o que pode refletir maior oferta de imóveis ou localização periférica.
* **Unknown** e **Potential Residential Area** possuem os menores valores, o que pode indicar baixa urbanização, pouca liquidez ou regiões em desenvolvimento.

| Faixa de Área (m²) | Preço Médio por m² (¥) |
| ------------------ | ---------------------- |
| (0–50]             | ¥ 739.478              |
| (50–100]           | ¥ 594.052              |
| (100–200]          | ¥ 458.591              |
| (200–500]          | ¥ 469.342              |
| (500–10000]        | ¥ 365.397              |
| **Média Geral**    | ¥ 525.372              |

**Tendência Observada:**

* Existe uma **clara tendência decrescente** do preço por m² conforme o tamanho da área construída aumenta.
* **Unidades pequenas (0–50m²)** apresentam o maior valor por m², refletindo o padrão de **concentração urbana**, onde unidades compactas são mais caras por m².
* **Unidades maiores (acima de 500m²)** têm o menor valor por m², sinalizando **descontos proporcionais** conforme aumenta a área — algo típico em empreendimentos comerciais, galpões ou mansões.
* A **linha de tendência** reforça a queda do preço unitário por m² com o aumento da metragem.
* A **linha vermelha pontilhada** representa a média geral e ajuda a visualizar quais faixas estão acima ou abaixo da média.

**Interpretação Estratégica:**

* O gráfico evidencia **economia de escala**: quanto maior a área construída, menor o custo unitário por m².
* Pode indicar oportunidades de **investimento em unidades maiores**, que têm menor custo por área construída.
* Para o mercado residencial urbano, **unidades compactas seguem valorizadas**, sendo ideais para revenda ou aluguel.

### Preço Médio de Venda por Ano

<img src="https://github.com/RafaelGallo/Case-Tecnico-Data-Science-Labs/blob/main/img/8.png" width="700"/>

Nesse gráfico é superior apresenta a evolução do preço médio de venda dos imóveis entre 2005 e 2019, com a linha azul indicando a média anual e a linha tracejada laranja representando a média móvel de 3 anos. Observa-se uma tendência de queda entre 2007 e 2011, com o preço médio reduzindo de aproximadamente ¥60 milhões para ¥44 milhões, seguida de recuperação gradual a partir de 2013, atingindo cerca de ¥54 milhões em 2018. O gráfico inferior mostra a contagem anual de imóveis vendidos, indicando um crescimento contínuo nas transações até 2013, com pico de aproximadamente 26 mil imóveis, seguido de leve estabilização e posterior queda em 2019. Esses padrões sugerem uma correlação inversa parcial entre volume e preço períodos de maior oferta e volume tendem a coincidir com preços médios mais baixos. Essa variável temporal (Year) deve ser considerada no modelo preditivo, seja como feature contínua ou via dummies por período, para capturar efeitos de ciclo econômico e variações de mercado ao longo do tempo.

### Evolução Temporal de Vendas

<img src="https://github.com/RafaelGallo/Case-Tecnico-Data-Science-Labs/blob/main/img/9.png" width="700"/>

Nesse gráfico série temporal mostra a variação do preço médio de venda de imóveis em Tóquio entre 2005 e 2019, com a linha azul representando a média anual e a linha tracejada laranja indicando a média móvel de 3 anos, acompanhada pelo intervalo de confiança (faixa sombreada). Observa-se uma queda acentuada nos preços entre 2007 e 2011, quando o valor médio caiu de aproximadamente ¥60,6 milhões para ¥44 milhões, seguida de uma recuperação gradual entre 2013 e 2018, chegando a ¥54,5 milhões. Essa dinâmica evidencia um ciclo de mercado imobiliário influenciado por fatores macroeconômicos, com estabilização após 2015. Essa variável temporal (Year) é relevante para o modelo preditivo, pois reflete flutuações de preço ao longo do tempo. Recomenda-se sua inclusão como variável contínua ou categórica, além da criação de uma feature derivada de tendência (por exemplo, taxa de variação anual), útil para capturar o comportamento cíclico observado.

### Volume de Imóveis Vendidos por Zoneamento Urbano

<img src="https://github.com/RafaelGallo/Case-Tecnico-Data-Science-Labs/blob/main/img/15.png" width="700"/>

**Análise**

**Objetivo**

Avaliar como o volume de transações imobiliárias em Tóquio evoluiu entre 2005 e 2019, considerando o tipo de zoneamento urbano (*City Planning*). O objetivo é identificar quais áreas apresentam maior dinâmica de mercado e se há padrões temporais relevantes.

**Principais Observações**

1. **Predominância de zonas residenciais de baixa densidade**
   As zonas Category I Exclusively Low-story Residential Zone concentram consistentemente o maior volume de vendas ao longo de todo o período, ultrapassando 6.000 imóveis vendidos por ano nos picos de 2012–2014.
   Isso reflete o alto dinamismo de compra e venda em áreas predominantemente residenciais e de baixa altura, típicas de bairros familiares de Tóquio.

2. **Zonas residenciais de média e alta densidade (Category I e II)**
   Apresentam volumes médios (entre 2.000 e 4.000 imóveis/ano), porém com tendência estável ou levemente crescente até 2016, antes de uma queda discreta nos anos finais.
   Essa estabilidade indica mercado maduro, com oferta e demanda equilibradas.

3. **Zonas comerciais e industriais**

   * Commercial Zone e Neighborhood Commercial Zone apresentam comportamento intermediário, com volumes regulares (entre 2.000 e 3.000 unidades anuais).
   * Industrial Zone e Exclusively Industrial Zone registram baixo volume de transações, o que é esperado devido à menor frequência de compra e venda em propriedades industriais.

4. **Áreas de planejamento especial e controle de urbanização**
   Categorias como Urbanization Control Area e Outside City Planning Area exibem volumes quase residuais (inferiores a 500 imóveis/ano), indicando restrições urbanísticas severas e baixo dinamismo imobiliário nessas regiões.

5. **Pico e desaceleração (2010–2013 → 2018–2019)**
   A maior parte das categorias apresenta pico de vendas entre 2010 e 2013, seguido de leve desaceleração a partir de 2016.
   Essa tendência possivelmente reflete:

   * Esforços de reurbanização pós-crise global de 2008 e reconstruções após o terremoto de 2011;
   * Posterior estabilização do mercado com redução de novas construções.

**Interpretação Geral**

* O gráfico revela uma forte centralização das transações em zonas residenciais, sobretudo nas áreas de baixa densidade, que sustentam a maior parte do mercado imobiliário de Tóquio.
* O comportamento cíclico — com crescimento até 2013 e leve retração posterior — sugere maturação do mercado urbano, com menor especulação e maior estabilidade no estoque de imóveis.
* Zonas industriais e de controle urbanístico têm participação marginal, o que reforça o caráter altamente residencial e regulado do território metropolitano.

**Conclusão**

O zoneamento urbano é um fator determinante para o volume de vendas imobiliárias.
As zonas residenciais de baixa densidade representam o núcleo mais ativo do mercado, enquanto áreas comerciais e industriais exercem papel complementar.
Essas informações são cruciais para modelos de previsão de preço e demanda, permitindo ponderar a variável CityPlanning como um atributo relevante e não linear no comportamento do mercado.

### Mudança no Perfil Urbanístico ao Longo do Tempo

<img src="https://github.com/RafaelGallo/Case-Tecnico-Data-Science-Labs/blob/main/img/16.png" width="700"/>

O gráfico apresenta a evolução do número de imóveis vendidos entre 2005 e 2019 nas cinco principais categorias de zoneamento urbano. Observa-se que a Commercial Zone possui o maior volume de vendas durante todo o período, variando entre aproximadamente 3.000 e 4.800 imóveis por ano. Essa categoria mostra crescimento constante até 2016, com leve redução nos anos seguintes. A Neighborhood Commercial Zone apresenta comportamento semelhante, embora com valores ligeiramente menores. Ambas indicam forte concentração de transações em áreas com uso predominantemente comercial. A Quasi-industrial Zone mantém trajetória de crescimento moderado e contínuo ao longo dos anos, saindo de valores próximos a 1.000 imóveis para cerca de 2.500 ao final do período. Isso sugere aumento gradual na utilização dessas áreas para fins mistos, acompanhando a readequação de espaços urbanos. A Quasi-residential Zone e a categoria identificada como 0 (sem classificação) registram volumes muito inferiores, com pequenas variações anuais e comportamento estável. O baixo número de transações nessas zonas indica menor dinamismo imobiliário ou áreas de ocupação consolidada com pouca oferta disponível.De forma geral, o gráfico evidencia que o mercado imobiliário se concentra majoritariamente nas zonas comerciais e industriais leves, com tendência de estabilidade após um período de expansão até meados da década de 2010. Essa distribuição reflete o processo de urbanização densa e a priorização de usos comerciais em regiões com maior infraestrutura urbana.

## **Análise de Outliers**

Remoção e padronização dos dados por **Z-Score**, destacando valores atípicos nas variáveis `Area` e `TradePrice`.

<img src="https://github.com/RafaelGallo/Case-Tecnico-Data-Science-Labs/blob/main/img/24.png" width="700"/>

Os boxplots apresentados mostram a distribuição das variáveis Area e TradePrice após o tratamento de outliers. Observa-se que, em comparação aos gráficos originais, houve uma redução significativa na amplitude dos valores extremos. As distribuições agora estão mais compactas, com menos pontos fora dos limites das caixas, indicando que os valores atípicos foram atenuados, removidos ou ajustados por meio de técnicas como limitação pelo IQR (Interquartile Range), winsorização ou remoção direta de observações discrepantes.
No caso da variável Area, a maior parte das propriedades se concentra entre aproximadamente 50 e 150 m², o que representa um intervalo típico para imóveis residenciais urbanos. Embora ainda haja alguns valores mais altos, eles estão dentro de uma faixa plausível, sem influências extremas. Já o TradePrice apresenta uma distribuição igualmente mais equilibrada. A concentração dos preços em torno do intervalo inferior sugere um mercado com predominância de imóveis de valor médio, mas agora sem a distorção causada pelos preços excessivamente altos observados anteriormente. Em resumo, o tratamento de outliers reduziu a variabilidade artificial dos dados, tornando o conjunto mais consistente para análises estatísticas e modelagem preditiva. Isso contribui para a melhoria da robustez e precisão dos modelos, evitando que valores anômalos influenciem indevidamente os resultados.

## **Feature Engineering**

Aplicação de técnicas de transformação e codificação de variáveis categóricas (`LabelEncoder`, `astype`, `merge`) e normalização de atributos contínuos.

<img src="https://github.com/RafaelGallo/Case-Tecnico-Data-Science-Labs/blob/main/img/25.png" width="700"/>

### Importância das Features (GradientBoosting)

<img src="https://github.com/RafaelGallo/Case-Tecnico-Data-Science-Labs/blob/main/img/18.png" width="700"/>

**Análise**

Nesse gráfico mostra plot importancia features mostram a influência de cada variável independente (feature) sobre o valor previsto dos imóveis, comparando diferentes algoritmos de regressão linear e baseada em árvores. Essa análise é essencial para entender quais fatores mais impactam o preço e como cada modelo os interpreta.

Nos três modelos LinearRegression, Lasso (L1) e Ridge (L2) observa-se consistência na direção e magnitude dos coeficientes, indicando estabilidade dos resultados. As variáveis Type_le e Region_le possuem os maiores coeficientes negativos, sugerindo forte influência do tipo de imóvel e da região sobre o preço final. Variáveis como MinTimeToNearestStation e Frontage (frente do terreno) também aparecem entre os principais preditores, o que reforça a importância da localização e do tamanho físico. A regularização L1 (Lasso) tende a reduzir a importância de variáveis menos relevantes, enquanto a L2 (Ridge) suaviza os pesos extremos, sem anulá-los completamente mantendo o equilíbrio entre simplicidade e estabilidade. Esses modelos são interpretáveis e ajudam a identificar relações lineares diretas, embora possam não capturar interações complexas entre variáveis.

Nos modelos não lineares (Decision Tree, Random Forest, XGBoost, Gradient Boosting e LightGBM), a interpretação muda: em vez de coeficientes, observam-se importâncias de atributos baseadas em ganho de informação na decision tree as variáveis TotalFloorArea (área total construída) e Area são as mais relevantes, indicando que o tamanho do imóvel é o principal fator explicativo. PricePerTsubo (preço por unidade de área) e Frontage aparecem como complementares, reforçando a lógica de valorização espacial. No Random Forest o padrão se mantém: área total e área do terreno concentram grande parte da explicação. A presença de variáveis como UnitPrice e PricePerTsubo reforça a correlação direta entre preço unitário e valor total. No modelo XGBoost há destaque para PricePerTsubo como o fator mais relevante, seguido de TotalFloorArea e UnitPrice, o que indica que o modelo aprendeu bem a relação entre valor por área e preço total, XGBoost também reconhece a importância de variáveis locacionais, como Region_le e MinTimeToNearestStation. No modelo Gradient Boosting
Assim como nas árvores anteriores, a área construída e a área do terreno dominam o impacto. As demais variáveis têm peso relativamente menor, mostrando que o modelo concentra sua explicação em poucas dimensões principais. No LightGBM Apresenta uma distribuição mais equilibrada das importâncias, indicando que, além da área e total de pavimentos, características construtivas e locacionais também são relevantes. Breadth, Frontage e CityPlanning_le aparecem com contribuições moderadas, evidenciando sensibilidade à forma e uso do terreno. Apesar das diferenças metodológicas, os modelos mostram convergência nas variáveis mais determinantes para o valor imobiliário, Tipo de Variável, Exemplos, Impacto, Dimensão física, TotalFloorArea, Area, Frontage, maior impacto positivo Localização	Region_le, CityPlanning_le, MinTimeToNearestStation, Influência relevante (negativa ou positiva), Indicadores de valor,	UnitPrice, PricePerTsubo, Que são relacionados diretamente ao preço total.

**Conclusão Geral**

A análise conjunta dos coeficientes e importâncias mostra que os fatores estruturais (área, frente, largura) e locacionais (região, proximidade de estação) são determinantes no valor dos imóveis. Enquanto os modelos lineares destacam relações proporcionais e diretas, os modelos baseados em árvores evidenciam interações não lineares e reforçam a dominância das variáveis de dimensão física. Essa etapa fornece insumos fundamentais para interpretação de modelos e apoio à tomada de decisão, seja para políticas urbanas, planejamento imobiliário ou recomendações de preço.

## **Modelagem de Machine Learning**

Foram testados diversos algoritmos supervisionados para prever o preço (`TradePrice`), com validação cruzada e métricas de erro.

| Modelo               | RMSLE    | MAPE      | R²       |
| :------------------- | :------- | :-------- | :------- |
| **GradientBoosting** | **0.88** | **1.079** | **0.72** |
| RandomForest         | 0.93     | 1.19      | 0.68     |
| LightGBM             | 0.95     | 1.21      | 0.66     |

## **Resultados Finais**

Visualizações do desempenho dos modelos preditivos e relação entre valores reais e previstos.

### Comparativo de Modelos

<img src="https://github.com/RafaelGallo/Case-Tecnico-Data-Science-Labs/blob/main/img/22.png" width="700"/>

**Análise Comparativa dos Modelos**

A tabela apresenta o desempenho de diferentes algoritmos de regressão aplicados à previsão do preço de venda de imóveis (TradePrice). As métricas analisadas foram RMSLE (Root Mean Squared Logarithmic Error) penaliza grandes diferenças entre valores reais e previstos em escala logarítmica; ideal para problemas com grande variação de magnitude de preços. MAPE (Mean Absolute Percentage Error) indica o erro percentual médio entre previsões e valores reais. R² (Coeficiente de Determinação) mede o quanto o modelo explica da variabilidade dos dados.

**Interpretação dos Resultados**

| Modelo                              | Destaque                   | Análise Técnica                                                                                                                                                                                       |
| :---------------------------------- | :------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LightGBM                        | Melhor desempenho geral | Obteve R² = 0.756, RMSLE = 0.606 e MAPE = 0.905, demonstrando excelente capacidade de generalização e bom equilíbrio entre viés e variância. É o modelo mais consistente para o problema. |
| RandomForest                    | Forte desempenho        | Apresentou R² = 0.748 e o menor RMSLE (0.439), indicando previsões bem ajustadas em escala logarítmica. Porém, tende a superajustar (overfitting) em amostras menores.                        |
| XGBoost                         | Desempenho competitivo  | Entregou R² = 0.747 e MAPE 1.011, mostrando robustez, mas um leve aumento de erro em comparação ao LightGBM.                                                                                  |
| GradientBoosting                | Modelo interpretável    | Teve R² = 0.729, com métricas próximas às do XGBoost. Apresenta melhor interpretabilidade, sendo útil para análise de Feature Importance.                                                       |
| DecisionTree                    | Simples e rápido        | Resultados medianos *R² = 0.546. Apesar da baixa generalização, é útil como baseline interpretável.                                                                                              |
| Lasso, Ridge e LinearRegression | Baixa performance       | Obtiveram R² = 0.588 e MAPE = 1.782, mostrando limitação em capturar relações não lineares entre as variáveis.                                                                                |

**Insight Final**

Os algoritmos baseados em árvores de decisão com boosting (LightGBM, XGBoost, GradientBoosting) dominaram o desempenho, pois capturam melhor a não linearidade e interações entre variáveis. Modelos lineares, por outro lado, tiveram desempenho inferior por não representarem adequadamente a complexidade do mercado imobiliário.

**Conclusão**

O modelo LightGBM foi escolhido como melhor modelo preditivo, apresentando:

* Boa capacidade explicativa R² = 0.756,
* Baixo erro logarítmico RMSLE = 0.606,
* E excelente estabilidade em previsão de preços reais.

*Para fins de interpretabilidade e apresentação, o modelo GradientBoosting foi também explorado em análises gráficas e explicabilidade das features.*


### Previsões (Relação Real × Previsto)

<img src="https://github.com/RafaelGallo/Case-Tecnico-Data-Science-Labs/blob/main/img/21.png" width="700"/>

Os gráficos mostram a comparação entre os valores reais e os valores previstos pelos diferentes modelos utilizados. A linha vermelha indica o ponto ideal onde as previsões seriam exatamente iguais aos valores reais. Quanto mais próximos os pontos estiverem dessa linha, mais precisas são as previsões do modelo. Nos modelos lineares, como regressão linear, Lasso e Ridge, observa-se uma dispersão maior dos pontos em relação à linha de referência. Eles conseguem acompanhar as tendências gerais dos dados, mas apresentam dificuldade para representar bem os imóveis de valores mais altos. Isso indica que esses modelos não captam adequadamente as relações mais complexas entre as variáveis do conjunto de dados. O modelo de árvore de decisão mostra comportamento irregular. Há muitos pontos afastados da linha de referência, o que sugere que o modelo se ajustou demais aos dados de treinamento e não generaliza bem. O modelo Random Forest mostra um avanço perceptível. As previsões estão mais próximas da linha ideal e há menor dispersão dos pontos. Isso indica que ele consegue representar melhor as relações não lineares e manter maior estabilidade entre as previsões. O modelo XGBoost também mostra boa aderência à linha, com desempenho consistente, embora apresente certa variação nos extremos dos valores, principalmente para imóveis com preços muito altos. O modelo Gradient Boosting apresenta padrão semelhante, mas com um pouco mais de dispersão. Ele tende a subestimar os valores mais elevados, o que reduz um pouco a precisão em faixas de preço altas. O modelo LightGBM apresenta o melhor resultado geral. As previsões acompanham bem a linha de referência e há pouca dispersão, mostrando que o modelo conseguiu equilibrar bem a relação entre viés e variância. Ele se mostra eficaz tanto para imóveis de valor mais baixo quanto para os de valor mais alto, mantendo boa coerência nas estimativas. De forma geral, nota-se que os modelos mais simples capturam apenas parte das relações presentes nos dados, enquanto os modelos baseados em árvores e especialmente os modelos de boosting alcançam previsões mais próximas dos valores reais. O LightGBM se destaca como o mais equilibrado e consistente entre todos, apresentando o melhor desempenho nas previsões.

## **Métricas do Modelo**

* **RMSLE:** 0.88
* **MAPE:** 1.079
* **R²:** 0.72

*O modelo GradientBoosting apresentou o melhor equilíbrio entre erro e explicabilidade.*

### **Visualizações**

| Tipo                           | Descrição                               |
| ------------------------------ | --------------------------------------- |
| **Correlação**              | Relação entre variáveis numéricas       |
| **Feature Importance**      | Atributos mais relevantes para previsão |
| **Resíduos**                | Distribuição de erros por modelo        |
| **Relação Real x Previsto** | Avaliação do desempenho do modelo       |

## **Licença**

Distribuído sob a **MIT License** — uso livre com atribuição de autoria.

## **Autor**

**Rafael Henrique Gallo**

Data Scientist
[LinkedIn](https://www.linkedin.com/in/rafael-henrique-gallo)
[GitHub](https://github.com/RafaelGallo)

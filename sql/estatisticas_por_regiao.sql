SELECT Region, COUNT(*) AS n, AVG(TradePrice) AS avg_price, MAX(TradePrice) AS max_price
FROM vw_train
GROUP BY Region
ORDER BY avg_price DESC;

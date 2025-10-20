SELECT No, Area, TradePrice, Type, Municipality
FROM vw_train
WHERE Area > 100 AND TradePrice > 10000000 AND Type LIKE '%Residential%'
ORDER BY TradePrice DESC
LIMIT 10;

SELECT Region, COUNT(*) AS n, AVG(TradePrice) AS avg_price, MAX(TradePrice) AS max_price
FROM vw_train
GROUP BY Region
ORDER BY avg_price DESC;

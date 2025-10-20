SELECT Area, TradePrice, Type, Municipality
FROM vw_train
WHERE Area > 100 AND TradePrice > 10000000 AND Type LIKE '%Residential%'
ORDER BY TradePrice DESC
LIMIT 10;

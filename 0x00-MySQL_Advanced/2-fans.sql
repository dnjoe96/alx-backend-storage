-- return fan ranking by fans of countries

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin

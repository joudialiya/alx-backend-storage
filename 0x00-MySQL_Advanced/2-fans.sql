# Select group
SELECT origin, SUM(id) AS nb_fans
FROM metal_bands GROUP BY origin;

-- Select group
SELECT origin, COUNT(*) AS nb_fans
FROM metal_bands
GROUP BY origin;

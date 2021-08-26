SELECT * FROM

(SELECT LAG(first_strain) OVER (ORDER BY 1) AS d0, LAG(last_strain) OVER (ORDER BY balancelle) AS f0,
first_strain AS d1, last_strain AS f1,
LEAD(first_strain) OVER (ORDER BY 1) AS d2, LEAD(last_strain) OVER (ORDER BY balancelle) AS f2
FROM stockeur_2) AS a

WHERE d0 IS NOT NULL AND f0 IS NOT NULL 
AND d2 IS NOT NULL AND f2 IS NOT NULL 
AND NOT (
	custom_sort(d0) < custom_sort(f0)
	AND custom_sort(f0) < custom_sort(d1)
	AND custom_sort(d1) < custom_sort(f1)
	AND custom_sort(d2) < custom_sort(f2)
	AND custom_sort(f1) < custom_sort(d2)
)
ORDER BY custom_sort(d0);
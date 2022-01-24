SELECT * 
FROM clients_de_brclims
JOIN excel_de_clients
ON trim(LOWER(code_postal)) = trim(LOWER(ville)) 


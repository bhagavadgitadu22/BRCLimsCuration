INSERT INTO good_documents_grouped(journal, annee, volume, first_page, xxx_ids, n_lignes)
SELECT journal, annee, volume, first_page, array_agg(xxx_id), array_agg(n_ligne)
FROM good_documents
GROUP BY journal, annee, volume, first_page;
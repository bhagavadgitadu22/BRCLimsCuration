-- on enlève éléments inutiles de array
UPDATE all_documents
SET doc = array_remove(doc, '')
WHERE doc != array_remove(doc, '');

UPDATE all_documents
SET doc = array_remove(doc, ' ')
WHERE doc != array_remove(doc, ' ');

UPDATE all_documents
SET doc = array_remove(doc, ' .')
WHERE doc != array_remove(doc, ' .');

UPDATE all_documents
SET doc = array_unique_stable(doc)
WHERE doc != array_unique_stable(doc);

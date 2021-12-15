UPDATE all_documents
SET string_doc = btrim(string_doc, ';. :-');

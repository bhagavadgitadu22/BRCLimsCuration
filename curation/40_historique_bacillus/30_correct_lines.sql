-- et on corrige les mentions de l'institut pasteur par un raccourci
UPDATE lines_bacillus
SET texte = regexp_replace(texte, ' ?IP', ', Inst. Pasteur, Paris, France', 'g');

UPDATE lines_bacillus
SET texte = 'Collection of Inst. Pasteur, Paris, France'
WHERE texte SIMILAR TO '(Coll. I.P|Coll. Institut Pasteur|Coll I.P)';

UPDATE lines_bacillus
SET texte = regexp_replace(texte, ' ?\(I.P.\)', ', Inst. Pasteur, Paris, France', 'g')
WHERE texte != regexp_replace(texte, ' ?\(I.P.\)', ', Inst. Pasteur, Paris, France', 'g');

UPDATE lines_bacillus
SET texte = 'C H St-Brieuc'
WHERE texte = 'C H St-Brieux';

UPDATE lines_bacillus
SET texte = regexp_replace(texte, ' ?<- ?', ' <- ')
WHERE texte SIMILAR TO '%[^ ]<-%';

UPDATE lines_bacillus
SET texte = replace(texte, 'Inst. D''Oenologie Bordeaux', 'Inst. d''Oenologie Bordeaux')
WHERE texte != replace(texte, 'Inst. D''Oenologie Bordeaux', 'Inst. d''Oenologie Bordeaux');

UPDATE lines_bacillus
SET texte = replace(texte, 'Coll. Allemande', 'DSMZ')
WHERE texte != replace(texte, 'Coll. Allemande', 'DSMZ');

-- et on corrige les mentions de l'institut pasteur par un raccourci
UPDATE lines_bacillus
SET texte = regexp_replace(texte, ' ?IP', ', Inst. Pasteur, Paris, France', 'g');

UPDATE lines_bacillus
SET texte = 'CIP'
WHERE texte SIMILAR TO '(Coll. I.P|Coll. Institut Pasteur|Coll I.P)';

UPDATE lines_bacillus
SET texte = regexp_replace(texte, ' ?(I.P.)', ', Inst. Pasteur, Paris, France', 'g');

UPDATE lines_bacillus
SET texte = 'C H St-Brieuc'
WHERE texte = 'C H St-Brieux';

DELETE FROM t_alerte_souche
WHERE als_sch_id IN (SELECT xxx_id FROM souches_de_champis);

DELETE FROM t_sequence
WHERE seq_sch_id IN (SELECT xxx_id FROM souches_de_champis);

DELETE FROM t_galerieresultat
WHERE gar_gal_id IN (SELECT xxx_id FROM t_galerie
WHERE gal_sch_id IN (SELECT xxx_id FROM souches_de_champis));

DELETE FROM t_galerie
WHERE gal_sch_id IN (SELECT xxx_id FROM souches_de_champis);

DELETE FROM t_souche
WHERE xxx_id IN (SELECT xxx_id FROM souches_de_champis);
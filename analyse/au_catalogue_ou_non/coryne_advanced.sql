DROP TABLE IF EXISTS coryne_strains;

CREATE TABLE coryne_strains (
	identifiant varchar(32)
);

INSERT INTO coryne_strains
VALUES ('CIP 203527'),('CIP 203527'),('CIP 100044'),('CIP 100133'),('CIP 100351'),('CIP 101067'),('CIP 101487'),('CIP 101518'),('CIP 101589'),('CIP 101649'),
('CIP 101899'),('CIP 102190'),('CIP 102212'),('CIP 102217'),('CIP 102491'),('CIP 102704'),('CIP 102841'),('CIP 106766'),('CIP 107409'),('CIP 107411'),
('CIP 107412'),('CIP 107413'),('CIP 107414'),('CIP 107415'),('CIP 107416'),('CIP 110893T'),('CIP 200298'),('CIP 200377'),('CIP 200394'),('CIP 201040'),
('CIP 201041'),('CIP 201042'),('CIP 201043'),('CIP 201044'),('CIP 201045'),('CIP 201046'),('CIP 201047'),('CIP 201048'),('CIP 201049'),('CIP 201050'),
('CIP 201051'),('CIP 201052'),('CIP 201053'),('CIP 201054'),('CIP 201058'),('CIP 201062'),('CIP 201064'),('CIP 201065'),('CIP 201066'),('CIP 201067'),
('CIP 201068'),('CIP 201069'),('CIP 201071'),('CIP 201072'),('CIP 201073'),('CIP 201074'),('CIP 201075'),('CIP 201077'),('CIP 203106'),('CIP 203125'),
('CIP 203148'),('CIP 203149'),('CIP 203152'),('CIP 203177'),('CIP 203183'),('CIP 203219'),('CIP 203248'),('CIP 203271'),('CIP 203277'),('CIP 203280'),
('CIP 203287'),('CIP 203493'),('CIP 203507'),('CIP 203508'),('CIP 203510'),('CIP 203525'),('CIP 203526'),('CIP 203552'),('CIP 203560'),('CIP 203577'),
('CIP 203620'),('CIP 203644'),('CIP 203670'),('CIP 203709'),('CIP 203717'),('CIP 203719'),('CIP 203720'),('CIP 203726'),('CIP 203727'),('CIP 203739'),
('CIP 203748'),('CIP 203762'),('CIP 203768'),('CIP A24'),('CRBIP25.100'),('CRBIP25.101'),('CRBIP25.102'),('CRBIP25.103'),('CRBIP25.104'),('CRBIP25.105');

SELECT identifiant, sch_catalogue
FROM coryne_strains
JOIN last_version_souches_cip
ON identifiant = sch_identifiant;

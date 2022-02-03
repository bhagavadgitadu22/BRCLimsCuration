UPDATE deposants_utilises
SET nom = trim(nom)
WHERE nom != trim(nom);
				  
UPDATE deposants_utilises
SET entreprise = trim(entreprise)
WHERE entreprise != trim(entreprise);

UPDATE deposants_utilises
SET entreprise = 'Technical University of Berlin'
WHERE entreprise IN ('Technological Berlin University', 'Berlin University');

UPDATE deposants_utilises
SET entreprise = 'Bundeswehr Medical Academy'
WHERE entreprise IN (CONCAT('BSW Sanit', CHR(228), 'tsakademie des Bundeswehr'));

UPDATE deposants_utilises
SET entreprise = 'Institute for Geosciences and Natural Resources (BGR)'
WHERE entreprise IN ('Bundesanstalt Geowissenschfaften Roshstoffe');

UPDATE deposants_utilises
SET entreprise = 'Center for Diseases Control (CDC)'
WHERE entreprise IN ('CDC', 'Center for Diseases Control', 'Laboratory Centre for Disease Control');

UPDATE deposants_utilises
SET entreprise = 'Chinese Academy of Science'
WHERE entreprise IN ('Chinese Academy of Sciences', 'Chinese Academy Sciences');

UPDATE deposants_utilises
SET entreprise = CONCAT('Compi', CHR(232), 'gne Technological University')
WHERE entreprise IN (CONCAT('Compi', CHR(232), 'gne University'));

UPDATE deposants_utilises
SET entreprise = 'Bari Aldo Moro University'
WHERE entreprise IN ('Degli studi di Bari University');

UPDATE deposants_utilises
SET entreprise = 'German Research Centre for Biotechnology (GBF)'
WHERE entreprise IN ('GBF', 'GBF National Research Center Biotechnology');

UPDATE deposants_utilises
SET entreprise = CONCAT('Hans Kn', CHR(246), 'll Institute')
WHERE entreprise IN (CONCAT('Hans Kn', CHR(246), 'll Institut', 'Hans Kn', CHR(246), 'll Institute'));

UPDATE deposants_utilises
SET entreprise = 'Hawaii University'
WHERE entreprise IN ('Hawai University');

UPDATE deposants_utilises
SET entreprise = 'Helmholtz Center'
WHERE entreprise IN ('Helmholz Center');

UPDATE deposants_utilises
SET entreprise = 'INRAE'
WHERE entreprise IN ('INRA', 'IRSTEA');

UPDATE deposants_utilises
SET entreprise = 'Pasteur Institute'
WHERE entreprise IN ('Inst. Pasteur', 'Institut Pasteur');

UPDATE deposants_utilises
SET entreprise = 'Labiris'
WHERE entreprise IN ('Institut de Recherches Microbiologiques Wiame');

UPDATE deposants_utilises
SET entreprise = 'IFP Energies nouvelles (IFPEN)'
WHERE entreprise IN (CONCAT('Institut Français du P', CHR(233), 'trole'));

UPDATE deposants_utilises
SET entreprise = 'Pasteur Institute of Lille'
WHERE entreprise IN ('Institut Pasteur Lille', 'Institut Pasteur de Lille');

UPDATE deposants_utilises
SET entreprise = 'Pasteur Institute of Lyon'
WHERE entreprise IN ('Institut Pasteur Lyon');

UPDATE deposants_utilises
SET entreprise = 'Pasteur Institute of New Caledonia'
WHERE entreprise IN ('Institut Pasteur New Caledonia');

UPDATE deposants_utilises
SET entreprise = 'Pasteur Institute of Senegal'
WHERE entreprise IN ('Institut Pasteur Senegal');

UPDATE deposants_utilises
SET entreprise = 'KU Leuven'
WHERE entreprise IN ('KU Leuven University');

UPDATE deposants_utilises
SET entreprise = 'Aix-Marseille University'
WHERE entreprise IN ('Mediterranean University', 'Mediterranean Provence University');

UPDATE deposants_utilises
SET entreprise = 'Milan University'
WHERE entreprise IN ('Milano University');

UPDATE deposants_utilises
SET entreprise = 'Munich University'
WHERE entreprise IN (CONCAT('M', CHR(252), 'nchen University'));

UPDATE deposants_utilises
SET entreprise = 'Pennsylvania State University'
WHERE entreprise IN ('Pennsylvania University');

UPDATE deposants_utilises
SET entreprise = 'Technical University of Munich'
WHERE entreprise IN ('Technological Munich University', 'Munich Technical University');

UPDATE deposants_utilises
SET entreprise = 'Wurzburg University'
WHERE entreprise IN (CONCAT('W', CHR(252), 'rzburg University'));

UPDATE deposants_utilises
SET entreprise = 'Lyon National Veterinary School'
WHERE entreprise IN ('Lyon National Veterinay School');

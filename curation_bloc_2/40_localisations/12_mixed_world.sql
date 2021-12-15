-- on mixe les tables des pays en anglais et français
DROP TABLE IF EXISTS world;

CREATE TABLE world (
  id SERIAL,
  name_en varchar(75) NOT NULL DEFAULT '',
  name_fr varchar(75) NOT NULL DEFAULT '',
  PRIMARY KEY (id)
);

INSERT INTO public.world (name_en, name_fr) VALUES ('Afghanistan', 'Afghanistan');
INSERT INTO public.world (name_en, name_fr) VALUES ('Åland Islands', 'Îles Åland');
INSERT INTO public.world (name_en, name_fr) VALUES ('Albania', 'Albanie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Algeria', 'Algérie');
INSERT INTO public.world (name_en, name_fr) VALUES ('American Samoa', 'Samoa américaines');
INSERT INTO public.world (name_en, name_fr) VALUES ('Andorra', 'Andorre');
INSERT INTO public.world (name_en, name_fr) VALUES ('Angola', 'Angola');
INSERT INTO public.world (name_en, name_fr) VALUES ('Anguilla', 'Anguilla');
INSERT INTO public.world (name_en, name_fr) VALUES ('Antarctica', 'Antarctique');
INSERT INTO public.world (name_en, name_fr) VALUES ('Antigua and Barbuda', 'Antigua-et-Barbuda');
INSERT INTO public.world (name_en, name_fr) VALUES ('Argentina', 'Argentine');
INSERT INTO public.world (name_en, name_fr) VALUES ('Armenia', 'Arménie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Aruba', 'Aruba');
INSERT INTO public.world (name_en, name_fr) VALUES ('Australia', 'Australie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Austria', 'Autriche');
INSERT INTO public.world (name_en, name_fr) VALUES ('Azerbaijan', 'Azerbaïdjan');
INSERT INTO public.world (name_en, name_fr) VALUES ('Bahamas', 'Bahamas');
INSERT INTO public.world (name_en, name_fr) VALUES ('Bahrain', 'Bahreïn');
INSERT INTO public.world (name_en, name_fr) VALUES ('Bangladesh', 'Bangladesh');
INSERT INTO public.world (name_en, name_fr) VALUES ('Barbados', 'Barbade');
INSERT INTO public.world (name_en, name_fr) VALUES ('Belarus', 'Biélorussie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Belgium', 'Belgique');
INSERT INTO public.world (name_en, name_fr) VALUES ('Belize', 'Belize');
INSERT INTO public.world (name_en, name_fr) VALUES ('Benin', 'Bénin');
INSERT INTO public.world (name_en, name_fr) VALUES ('Bermuda', 'Bermudes');
INSERT INTO public.world (name_en, name_fr) VALUES ('Bhutan', 'Bhoutan');
INSERT INTO public.world (name_en, name_fr) VALUES ('Bolivia (Plurinational State of)', 'Bolivie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Bonaire, Sint Eustatius and Saba', 'Pays-Bas caribéens');
INSERT INTO public.world (name_en, name_fr) VALUES ('Bosnia and Herzegovina', 'Bosnie-Herzégovine');
INSERT INTO public.world (name_en, name_fr) VALUES ('Botswana', 'Botswana');
INSERT INTO public.world (name_en, name_fr) VALUES ('Bouvet Island', 'Île Bouvet');
INSERT INTO public.world (name_en, name_fr) VALUES ('Brazil', 'Brésil');
INSERT INTO public.world (name_en, name_fr) VALUES ('British Indian Ocean Territory', 'Territoire britannique de l''océan Indien');
INSERT INTO public.world (name_en, name_fr) VALUES ('Brunei Darussalam', 'Brunei');
INSERT INTO public.world (name_en, name_fr) VALUES ('Bulgaria', 'Bulgarie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Burkina Faso', 'Burkina Faso');
INSERT INTO public.world (name_en, name_fr) VALUES ('Burundi', 'Burundi');
INSERT INTO public.world (name_en, name_fr) VALUES ('Cabo Verde', 'Cap-Vert');
INSERT INTO public.world (name_en, name_fr) VALUES ('Cambodia', 'Cambodge');
INSERT INTO public.world (name_en, name_fr) VALUES ('Cameroon', 'Cameroun');
INSERT INTO public.world (name_en, name_fr) VALUES ('Canada', 'Canada');
INSERT INTO public.world (name_en, name_fr) VALUES ('Cayman Islands', 'Îles Caïmans');
INSERT INTO public.world (name_en, name_fr) VALUES ('Central African Republic', 'République centrafricaine');
INSERT INTO public.world (name_en, name_fr) VALUES ('Chad', 'Tchad');
INSERT INTO public.world (name_en, name_fr) VALUES ('Chile', 'Chili');
INSERT INTO public.world (name_en, name_fr) VALUES ('China', 'Chine');
INSERT INTO public.world (name_en, name_fr) VALUES ('Christmas Island', 'Île Christmas');
INSERT INTO public.world (name_en, name_fr) VALUES ('Cocos (Keeling) Islands', 'Îles Cocos');
INSERT INTO public.world (name_en, name_fr) VALUES ('Colombia', 'Colombie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Comoros', 'Comores (pays)');
INSERT INTO public.world (name_en, name_fr) VALUES ('Congo', 'République du Congo');
INSERT INTO public.world (name_en, name_fr) VALUES ('Congo (Democratic Republic of the)', 'République démocratique du Congo');
INSERT INTO public.world (name_en, name_fr) VALUES ('Cook Islands', 'Îles Cook');
INSERT INTO public.world (name_en, name_fr) VALUES ('Costa Rica', 'Costa Rica');
INSERT INTO public.world (name_en, name_fr) VALUES ('Côte d''Ivoire', 'Côte d''Ivoire');
INSERT INTO public.world (name_en, name_fr) VALUES ('Croatia', 'Croatie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Cuba', 'Cuba');
INSERT INTO public.world (name_en, name_fr) VALUES ('Curaçao', 'Curaçao');
INSERT INTO public.world (name_en, name_fr) VALUES ('Cyprus', 'Chypre (pays)');
INSERT INTO public.world (name_en, name_fr) VALUES ('Czechia', 'Tchéquie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Denmark', 'Danemark');
INSERT INTO public.world (name_en, name_fr) VALUES ('Djibouti', 'Djibouti');
INSERT INTO public.world (name_en, name_fr) VALUES ('Dominica', 'Dominique');
INSERT INTO public.world (name_en, name_fr) VALUES ('Dominican Republic', 'République dominicaine');
INSERT INTO public.world (name_en, name_fr) VALUES ('Ecuador', 'Équateur (pays)');
INSERT INTO public.world (name_en, name_fr) VALUES ('Egypt', 'Égypte');
INSERT INTO public.world (name_en, name_fr) VALUES ('El Salvador', 'Salvador');
INSERT INTO public.world (name_en, name_fr) VALUES ('Equatorial Guinea', 'Guinée équatoriale');
INSERT INTO public.world (name_en, name_fr) VALUES ('Eritrea', 'Érythrée');
INSERT INTO public.world (name_en, name_fr) VALUES ('Estonia', 'Estonie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Eswatini', 'Eswatini');
INSERT INTO public.world (name_en, name_fr) VALUES ('Ethiopia', 'Éthiopie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Falkland Islands (Malvinas)', 'Malouines');
INSERT INTO public.world (name_en, name_fr) VALUES ('Faroe Islands', 'Îles Féroé');
INSERT INTO public.world (name_en, name_fr) VALUES ('Fiji', 'Fidji');
INSERT INTO public.world (name_en, name_fr) VALUES ('Finland', 'Finlande');
INSERT INTO public.world (name_en, name_fr) VALUES ('France', 'France');
INSERT INTO public.world (name_en, name_fr) VALUES ('French Guiana', 'Guyane');
INSERT INTO public.world (name_en, name_fr) VALUES ('French Polynesia', 'Polynésie française');
INSERT INTO public.world (name_en, name_fr) VALUES ('French Southern Territories', 'Terres australes et antarctiques françaises');
INSERT INTO public.world (name_en, name_fr) VALUES ('Gabon', 'Gabon');
INSERT INTO public.world (name_en, name_fr) VALUES ('Gambia', 'Gambie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Georgia', 'Géorgie (pays)');
INSERT INTO public.world (name_en, name_fr) VALUES ('Germany', 'Allemagne');
INSERT INTO public.world (name_en, name_fr) VALUES ('Ghana', 'Ghana');
INSERT INTO public.world (name_en, name_fr) VALUES ('Gibraltar', 'Gibraltar');
INSERT INTO public.world (name_en, name_fr) VALUES ('Greece', 'Grèce');
INSERT INTO public.world (name_en, name_fr) VALUES ('Greenland', 'Groenland');
INSERT INTO public.world (name_en, name_fr) VALUES ('Grenada', 'Grenade (pays)');
INSERT INTO public.world (name_en, name_fr) VALUES ('Guadeloupe', 'Guadeloupe');
INSERT INTO public.world (name_en, name_fr) VALUES ('Guam', 'Guam');
INSERT INTO public.world (name_en, name_fr) VALUES ('Guatemala', 'Guatemala');
INSERT INTO public.world (name_en, name_fr) VALUES ('Guernsey', 'Guernesey');
INSERT INTO public.world (name_en, name_fr) VALUES ('Guinea', 'Guinée');
INSERT INTO public.world (name_en, name_fr) VALUES ('Guinea-Bissau', 'Guinée-Bissau');
INSERT INTO public.world (name_en, name_fr) VALUES ('Guyana', 'Guyana');
INSERT INTO public.world (name_en, name_fr) VALUES ('Haiti', 'Haïti');
INSERT INTO public.world (name_en, name_fr) VALUES ('Heard Island and McDonald Islands', 'Îles Heard-et-MacDonald');
INSERT INTO public.world (name_en, name_fr) VALUES ('Holy See', 'Saint-Siège (État de la Cité du Vatican)');
INSERT INTO public.world (name_en, name_fr) VALUES ('Honduras', 'Honduras');
INSERT INTO public.world (name_en, name_fr) VALUES ('Hong Kong', 'Hong Kong');
INSERT INTO public.world (name_en, name_fr) VALUES ('Hungary', 'Hongrie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Iceland', 'Islande');
INSERT INTO public.world (name_en, name_fr) VALUES ('India', 'Inde');
INSERT INTO public.world (name_en, name_fr) VALUES ('Indonesia', 'Indonésie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Iran (Islamic Republic of)', 'Iran');
INSERT INTO public.world (name_en, name_fr) VALUES ('Iraq', 'Irak');
INSERT INTO public.world (name_en, name_fr) VALUES ('Ireland', 'Irlande (pays)');
INSERT INTO public.world (name_en, name_fr) VALUES ('Isle of Man', 'Île de Man');
INSERT INTO public.world (name_en, name_fr) VALUES ('Israel', 'Israël');
INSERT INTO public.world (name_en, name_fr) VALUES ('Italy', 'Italie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Jamaica', 'Jamaïque');
INSERT INTO public.world (name_en, name_fr) VALUES ('Japan', 'Japon');
INSERT INTO public.world (name_en, name_fr) VALUES ('Jersey', 'Jersey');
INSERT INTO public.world (name_en, name_fr) VALUES ('Jordan', 'Jordanie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Kazakhstan', 'Kazakhstan');
INSERT INTO public.world (name_en, name_fr) VALUES ('Kenya', 'Kenya');
INSERT INTO public.world (name_en, name_fr) VALUES ('Kiribati', 'Kiribati');
INSERT INTO public.world (name_en, name_fr) VALUES ('Korea (Democratic People''s Republic of)', 'Corée du Nord');
INSERT INTO public.world (name_en, name_fr) VALUES ('Korea (Republic of)', 'Corée du Sud');
INSERT INTO public.world (name_en, name_fr) VALUES ('Kuwait', 'Koweït');
INSERT INTO public.world (name_en, name_fr) VALUES ('Kyrgyzstan', 'Kirghizistan');
INSERT INTO public.world (name_en, name_fr) VALUES ('Lao People''s Democratic Republic', 'Laos');
INSERT INTO public.world (name_en, name_fr) VALUES ('Latvia', 'Lettonie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Lebanon', 'Liban');
INSERT INTO public.world (name_en, name_fr) VALUES ('Lesotho', 'Lesotho');
INSERT INTO public.world (name_en, name_fr) VALUES ('Liberia', 'Liberia');
INSERT INTO public.world (name_en, name_fr) VALUES ('Libya', 'Libye');
INSERT INTO public.world (name_en, name_fr) VALUES ('Liechtenstein', 'Liechtenstein');
INSERT INTO public.world (name_en, name_fr) VALUES ('Lithuania', 'Lituanie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Luxembourg', 'Luxembourg (pays)');
INSERT INTO public.world (name_en, name_fr) VALUES ('Macao', 'Macao');
INSERT INTO public.world (name_en, name_fr) VALUES ('Madagascar', 'Madagascar');
INSERT INTO public.world (name_en, name_fr) VALUES ('Malawi', 'Malawi');
INSERT INTO public.world (name_en, name_fr) VALUES ('Malaysia', 'Malaisie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Maldives', 'Maldives');
INSERT INTO public.world (name_en, name_fr) VALUES ('Mali', 'Mali');
INSERT INTO public.world (name_en, name_fr) VALUES ('Malta', 'Malte');
INSERT INTO public.world (name_en, name_fr) VALUES ('Marshall Islands', 'Îles Marshall (pays)');
INSERT INTO public.world (name_en, name_fr) VALUES ('Martinique', 'Martinique');
INSERT INTO public.world (name_en, name_fr) VALUES ('Mauritania', 'Mauritanie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Mauritius', 'Maurice (pays)');
INSERT INTO public.world (name_en, name_fr) VALUES ('Mayotte', 'Mayotte');
INSERT INTO public.world (name_en, name_fr) VALUES ('Mexico', 'Mexique');
INSERT INTO public.world (name_en, name_fr) VALUES ('Micronesia (Federated States of)', 'États fédérés de Micronésie (pays)');
INSERT INTO public.world (name_en, name_fr) VALUES ('Moldova (Republic of)', 'Moldavie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Monaco', 'Monaco');
INSERT INTO public.world (name_en, name_fr) VALUES ('Mongolia', 'Mongolie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Montenegro', 'Monténégro');
INSERT INTO public.world (name_en, name_fr) VALUES ('Montserrat', 'Montserrat');
INSERT INTO public.world (name_en, name_fr) VALUES ('Morocco', 'Maroc');
INSERT INTO public.world (name_en, name_fr) VALUES ('Mozambique', 'Mozambique');
INSERT INTO public.world (name_en, name_fr) VALUES ('Myanmar', 'Birmanie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Namibia', 'Namibie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Nauru', 'Nauru');
INSERT INTO public.world (name_en, name_fr) VALUES ('Nepal', 'Népal');
INSERT INTO public.world (name_en, name_fr) VALUES ('Netherlands', 'Pays-Bas');
INSERT INTO public.world (name_en, name_fr) VALUES ('New Caledonia', 'Nouvelle-Calédonie');
INSERT INTO public.world (name_en, name_fr) VALUES ('New Zealand', 'Nouvelle-Zélande');
INSERT INTO public.world (name_en, name_fr) VALUES ('Nicaragua', 'Nicaragua');
INSERT INTO public.world (name_en, name_fr) VALUES ('Niger', 'Niger');
INSERT INTO public.world (name_en, name_fr) VALUES ('Nigeria', 'Nigeria');
INSERT INTO public.world (name_en, name_fr) VALUES ('Niue', 'Niue');
INSERT INTO public.world (name_en, name_fr) VALUES ('Norfolk Island', 'Île Norfolk');
INSERT INTO public.world (name_en, name_fr) VALUES ('North Macedonia', 'Macédoine du Nord');
INSERT INTO public.world (name_en, name_fr) VALUES ('Northern Mariana Islands', 'Îles Mariannes du Nord');
INSERT INTO public.world (name_en, name_fr) VALUES ('Norway', 'Norvège');
INSERT INTO public.world (name_en, name_fr) VALUES ('Oman', 'Oman');
INSERT INTO public.world (name_en, name_fr) VALUES ('Pakistan', 'Pakistan');
INSERT INTO public.world (name_en, name_fr) VALUES ('Palau', 'Palaos');
INSERT INTO public.world (name_en, name_fr) VALUES ('Palestine (State of)', 'Palestine');
INSERT INTO public.world (name_en, name_fr) VALUES ('Panama', 'Panama');
INSERT INTO public.world (name_en, name_fr) VALUES ('Papua New Guinea', 'Papouasie-Nouvelle-Guinée');
INSERT INTO public.world (name_en, name_fr) VALUES ('Paraguay', 'Paraguay');
INSERT INTO public.world (name_en, name_fr) VALUES ('Peru', 'Pérou');
INSERT INTO public.world (name_en, name_fr) VALUES ('Philippines', 'Philippines');
INSERT INTO public.world (name_en, name_fr) VALUES ('Pitcairn', 'Îles Pitcairn');
INSERT INTO public.world (name_en, name_fr) VALUES ('Poland', 'Pologne');
INSERT INTO public.world (name_en, name_fr) VALUES ('Portugal', 'Portugal');
INSERT INTO public.world (name_en, name_fr) VALUES ('Puerto Rico', 'Porto Rico');
INSERT INTO public.world (name_en, name_fr) VALUES ('Qatar', 'Qatar');
INSERT INTO public.world (name_en, name_fr) VALUES ('Réunion', 'La Réunion');
INSERT INTO public.world (name_en, name_fr) VALUES ('Romania', 'Roumanie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Russian Federation', 'Russie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Rwanda', 'Rwanda');
INSERT INTO public.world (name_en, name_fr) VALUES ('Saint Barthélemy', 'Saint-Barthélemy');
INSERT INTO public.world (name_en, name_fr) VALUES ('Saint Helena, Ascension and Tristan da Cunha', 'Sainte-Hélène, Ascension et Tristan da Cunha');
INSERT INTO public.world (name_en, name_fr) VALUES ('Saint Kitts and Nevis', 'Saint-Christophe-et-Niévès');
INSERT INTO public.world (name_en, name_fr) VALUES ('Saint Lucia', 'Sainte-Lucie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Saint Martin (French part)', 'Saint-Martin');
INSERT INTO public.world (name_en, name_fr) VALUES ('Saint Pierre and Miquelon', 'Saint-Pierre-et-Miquelon');
INSERT INTO public.world (name_en, name_fr) VALUES ('Saint Vincent and the Grenadines', 'Saint-Vincent-et-les-Grenadines');
INSERT INTO public.world (name_en, name_fr) VALUES ('Samoa', 'Samoa');
INSERT INTO public.world (name_en, name_fr) VALUES ('San Marino', 'Saint-Marin');
INSERT INTO public.world (name_en, name_fr) VALUES ('Sao Tome and Principe', 'Sao Tomé-et-Principe');
INSERT INTO public.world (name_en, name_fr) VALUES ('Saudi Arabia', 'Arabie saoudite');
INSERT INTO public.world (name_en, name_fr) VALUES ('Senegal', 'Sénégal');
INSERT INTO public.world (name_en, name_fr) VALUES ('Serbia', 'Serbie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Seychelles', 'Seychelles');
INSERT INTO public.world (name_en, name_fr) VALUES ('Sierra Leone', 'Sierra Leone');
INSERT INTO public.world (name_en, name_fr) VALUES ('Singapore', 'Singapour');
INSERT INTO public.world (name_en, name_fr) VALUES ('Sint Maarten (Dutch part)', 'Saint-Martin');
INSERT INTO public.world (name_en, name_fr) VALUES ('Slovakia', 'Slovaquie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Slovenia', 'Slovénie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Solomon Islands', 'Îles Salomon');
INSERT INTO public.world (name_en, name_fr) VALUES ('Somalia', 'Somalie');
INSERT INTO public.world (name_en, name_fr) VALUES ('South Africa', 'Afrique du Sud');
INSERT INTO public.world (name_en, name_fr) VALUES ('South Georgia and the South Sandwich Islands', 'Géorgie du Sud-et-les îles Sandwich du Sud');
INSERT INTO public.world (name_en, name_fr) VALUES ('South Sudan', 'Soudan du Sud');
INSERT INTO public.world (name_en, name_fr) VALUES ('Spain', 'Espagne');
INSERT INTO public.world (name_en, name_fr) VALUES ('Sri Lanka', 'Sri Lanka');
INSERT INTO public.world (name_en, name_fr) VALUES ('Sudan', 'Soudan');
INSERT INTO public.world (name_en, name_fr) VALUES ('Suriname', 'Suriname');
INSERT INTO public.world (name_en, name_fr) VALUES ('Svalbard and Jan Mayen', 'Svalbard et ile Jan Mayen');
INSERT INTO public.world (name_en, name_fr) VALUES ('Sweden', 'Suède');
INSERT INTO public.world (name_en, name_fr) VALUES ('Switzerland', 'Suisse');
INSERT INTO public.world (name_en, name_fr) VALUES ('Syrian Arab Republic', 'Syrie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Taiwan (Province of China)', 'Taïwan / (République de Chine (Taïwan))');
INSERT INTO public.world (name_en, name_fr) VALUES ('Tajikistan', 'Tadjikistan');
INSERT INTO public.world (name_en, name_fr) VALUES ('Tanzania (United Republic of)', 'Tanzanie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Thailand', 'Thaïlande');
INSERT INTO public.world (name_en, name_fr) VALUES ('Timor-Leste', 'Timor oriental');
INSERT INTO public.world (name_en, name_fr) VALUES ('Togo', 'Togo');
INSERT INTO public.world (name_en, name_fr) VALUES ('Tokelau', 'Tokelau');
INSERT INTO public.world (name_en, name_fr) VALUES ('Tonga', 'Tonga');
INSERT INTO public.world (name_en, name_fr) VALUES ('Trinidad and Tobago', 'Trinité-et-Tobago');
INSERT INTO public.world (name_en, name_fr) VALUES ('Tunisia', 'Tunisie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Turkey', 'Turquie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Turkmenistan', 'Turkménistan');
INSERT INTO public.world (name_en, name_fr) VALUES ('Turks and Caicos Islands', 'Îles Turques-et-Caïques');
INSERT INTO public.world (name_en, name_fr) VALUES ('Tuvalu', 'Tuvalu');
INSERT INTO public.world (name_en, name_fr) VALUES ('Uganda', 'Ouganda');
INSERT INTO public.world (name_en, name_fr) VALUES ('Ukraine', 'Ukraine');
INSERT INTO public.world (name_en, name_fr) VALUES ('United Arab Emirates', 'Émirats arabes unis');
INSERT INTO public.world (name_en, name_fr) VALUES ('United Kingdom of Great Britain and Northern Ireland', 'Royaume-Uni');
INSERT INTO public.world (name_en, name_fr) VALUES ('United States of America', 'États-Unis');
INSERT INTO public.world (name_en, name_fr) VALUES ('United States Minor Outlying Islands', 'Îles mineures éloignées des États-Unis');
INSERT INTO public.world (name_en, name_fr) VALUES ('Uruguay', 'Uruguay');
INSERT INTO public.world (name_en, name_fr) VALUES ('Uzbekistan', 'Ouzbékistan');
INSERT INTO public.world (name_en, name_fr) VALUES ('Vanuatu', 'Vanuatu');
INSERT INTO public.world (name_en, name_fr) VALUES ('Venezuela (Bolivarian Republic of)', 'Venezuela');
INSERT INTO public.world (name_en, name_fr) VALUES ('Viet Nam', 'Viêt Nam');
INSERT INTO public.world (name_en, name_fr) VALUES ('Virgin Islands (British)', 'Îles Vierges britanniques');
INSERT INTO public.world (name_en, name_fr) VALUES ('Virgin Islands (U.S.)', 'Îles Vierges des États-Unis');
INSERT INTO public.world (name_en, name_fr) VALUES ('Wallis and Futuna', 'Wallis-et-Futuna');
INSERT INTO public.world (name_en, name_fr) VALUES ('Western Sahara', 'République arabe sahraouie démocratique');
INSERT INTO public.world (name_en, name_fr) VALUES ('Yemen', 'Yémen');
INSERT INTO public.world (name_en, name_fr) VALUES ('Zambia', 'Zambie');
INSERT INTO public.world (name_en, name_fr) VALUES ('Zimbabwe', 'Zimbabwe');
INSERT INTO public.world (name_en, name_fr) VALUES ('Pacific Ocean', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Bering Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Gulf of Alaska', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Gulf of California', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Sea of Okhotsk', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Sea of Japan', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Seto Inland Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('East China Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('South China Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Beibu Gulf', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Sulu Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Celebes Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Bohol Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Philippine Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Flores Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Banda Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Arafura Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Tasman Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Yellow Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Bohai Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Coral Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Gulf of Carpentaria', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Atlantic Ocean', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Hudson Bay', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('James Bay', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Baffin Bay init fam', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Gulf of St. Lawrence', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Caribbean Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Gulf of Mexico', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Sargasso Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('North Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Baltic Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Gulf of Bothnia', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Irish Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Celtic Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('English Channel', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Mediterranean Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Adriatic Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Aegean Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Black Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Sea of Azov', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Ionian Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Ligurian Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Mirtoon Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Tyrrhenian Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Gulf of Sidra', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Sea of Marmara', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Sea of Crete', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Indian Ocean', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Red Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Gulf of Aden', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Persian Gulf', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Gulf of Oman', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Arabian Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Bay of Bengal', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Gulf of Thailand', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Java Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Timor Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Gulf of Kutch', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Gulf of Khambhat', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Arctic Ocean', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Barents Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Kara Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Beaufort Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Amundsen Gulf', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Greenland Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Chukchi Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Laptev Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('East Siberian Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Antarctic Ocean', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Amundsen Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Weddell Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Ross Sea', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Great Australian Bight', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Gulf St. Vincent', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Spencer Gulf', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Africa', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Asia', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('North America', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('South America', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Europe', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Space', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Unknown', '');
INSERT INTO public.world (name_en, name_fr) VALUES ('Arctic', '');

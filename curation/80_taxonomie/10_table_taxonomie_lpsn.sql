DROP TABLE IF EXISTS taxonomy;

CREATE TABLE taxonomy (
  genus_name varchar(75),
  sp_epithet varchar(75),
  subsp_epithet varchar(75),
  record_no varchar(75),
  record_lnk varchar(75)
);

CREATE TEMPORARY TABLE t (
  genus_name varchar(75),
  sp_epithet varchar(75),
  subsp_epithet varchar(75),
  reference text,
  status text,
  authors text,
  address text,
  risk_grp text,
  nomenclatural_type text,
  record_no varchar(75),
  record_lnk varchar(75)
);

COPY t (genus_name,sp_epithet,subsp_epithet,reference,status,authors,address,risk_grp,nomenclatural_type,record_no,record_lnk)
FROM '/var/lib/pgsql/brclimscuration/csv_utiles/lpsn_gss_2021-07-27.csv'
CSV HEADER;

INSERT INTO taxonomy (genus_name,sp_epithet,subsp_epithet,record_no,record_lnk)
SELECT genus_name,sp_epithet,subsp_epithet,record_no,record_lnk
FROM t;

DROP TABLE t;

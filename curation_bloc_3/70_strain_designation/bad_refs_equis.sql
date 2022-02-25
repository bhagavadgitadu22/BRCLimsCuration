DROP TABLE IF EXISTS bilan_collections;
DROP TABLE IF EXISTS good_refs;

SELECT t_deposant.don_lib AS collection
INTO bilan_collections
FROM t_souche
JOIN t_donneedico AS t_deposant
ON sch_depositaire = t_deposant.xxx_id
JOIN t_donneedico AS t_categorie
ON t_deposant.don_parent = t_categorie.don_code
AND t_deposant.don_dic_id = t_categorie.don_dic_id
WHERE t_categorie.don_lib = 'Collections'
GROUP BY t_deposant.don_lib
ORDER BY t_deposant.don_lib;

SELECT ref_equi 
INTO good_refs
FROM (SELECT unnest(string_to_array(sch_references_equi, ';')) AS ref_equi
FROM t_souche) AS a
WHERE ref_equi LIKE ANY(SELECT CONCAT(collection, '%') FROM bilan_collections)
OR LOWER(ref_equi) SIMILAR TO '(abb|abrc|abriicc|aca-dc|acam|acc|accc|acm|acoi|afrc|agal|ahlda|ahn|ahrl|ahu|aist|aj|aku|aliru|amc|amif|amp|amrc|amrc-c|anmr|api|ars|as|atcc|athum|atu|aucm|aucnm|ayu|bac|bacc|bc|bcc|bccm|bccmlmg|bccn|bccusp|bcrc|bdbpi|bdun|bduz|bei|beiresources|bg|bgsc|bim|biocc|biorepositories|bkmw|bmbc|bmcc|bmtu|bnm|bpic|br|brcc|brl|bsd|btcc|bucsav|cabi|cabi-grc|cabri|caim|cair|caircc|cairo|calu|capm|cau|caup|cb|cbas|cbcc|cbfs|cbmai|cbri|cbrvs|cbs|cc|ccala|ccam|ccap|ccarm|ccbau|ccb-mbl|ccccm|cccieb|cccm|ccdm|ccdmbi|cceb|ccf|ccfc|ccfcdaom|ccgb|cchrgm|ccibso|ccim|ccm|ccma|ccm-a|ccmcu|ccmee|ccmi|ccmm|ccmp|ccoc|ccos|ccrc|ccri|ccsiia|ccsm|ccstamb|cct|cctcc|cctm|ccub|ccug|ccy|cda|cdbb|cdc|ceb|cect|celms|cenacumi|cepim|cepm|cetesb|cfbp|cfcc|cfml|cfn|cgmcc|cgsc|ch-ag|ciam|ciat|cicc|cicim|cicv|cimsc|cip|cipt|cirm-bia|cirmbp|cirm-bp|clep|clip|cmaa|cmcc|cm-cnrg|cmdm-puj|cmi|cmmc|cmppb|cmpuj|cmrvs|cn|cnblm|cncm|cncru|cnctc|cnpbs|cnpso|cnrz|cns|cnu|cny|cpac|cpcc|cphs|cppipp|cpz|crab|crbip|cripp|crirc|crl|crs|cscc|csir|csma|csur|cub|cuetm|cvcc|cvcm|cy|dact|daom|dapp-pg|dar|dbm|dbs|dbua|dbum|dbvpg|dcc|de-csiro|dmbuk|dmccum|dmccus|dmkku1|dmku|dmmz|dmpmc|dmsrde|dmst|dmuij|dmur|dmvb|doa|doab|dpc|dpdu|dpiwe-fhu|dpua|drl|dsir|dsm|dsmz|ecacc|ecco|ecor|egi|emcc|encb-ipn|esap|eth|ethz|ex|fat|fbabc|fbgmu|fccm|fda|fdc|ferm|fgsc|firdi|fjat|flrm|fmj|fmr|fncc|fpc|fri|frr|ftcc|ftk|gab|gam|gbs|gcc|gcl|gcmcc|gcmr|gdmcc|giem|gifu|gimcc|gsf|gsoil|gtc|gtc-gifu|hac|hacc|ham|hambi|hau|hcc|hdp|hki|hkucc|hmgb|hncmb|hpktcc|hscc|hull|hut|iacr|iaf|iafb|ial|iam|iamcc|iaur|iaw|iba|ibac|ibl|ibphm|ibppm|ibprm|ibrc|ibs|ibsbf|ibso|ibt|icbb|iccf|ici|icmp|icpb|iebc|iegm|iekc|iem|ifam|ifbm|ifm|ifo|igc|igesalq|ihem|iibm-unam|iid|ijfm|imac|imas|imcc|imd|imet|img|imi|immib|imru|imsnu|imur|imv|imvs|imyza|ina|inacc|incqs|indre|inifat|inmi|inpa|inra|ioc|ioeb|iomcc|ip|ipdh|ipf|ipod|ippas|ipr|ipt|ipv|isc|isp|ispb|isri|iss|ita|italsl|italsm|itbcc|itcc|itd|itdi|item|itg|ith|itm|iung|iw|iz|jbri|jcm|jct|jfcc|jhh|jscc|jsm|kacc|kbs|kcc|kccm|kcom|kctc|kemb|kemc|kemh|kfcc|kit|klmb|kmm|kordi|kos|kpb|kuen|kukens|ky|lakto-flora|lancefield|lbg|lcc|lcdc|lcp|lddc|le|lege|lhmc|lia|lipimc|lipp|lmau|lmch|lmd|lmg|lms|lock|lrtl|lsh|lshb|lsu|lth|lti|luh|ly|maff|mao|mar|marbec|marseille|mbic|mbicc|mcc|mccc|mccm|mcc-nies|mcc-uplb|mcitm|mcm|mcml|mda|mdc|mdh|mfc|mim|mit|mmca|mml|mola|mrc|mscl|mscmu|msdj|mtcc|mthu|mu|mucl|mucob|mul|muscl|nadc|nau|nbbcru|nbimcc|nbrc|nbrl|nca|ncaim|ncam|ncb|ncc|nccb|nccp|ncdc|ncdo|ncfb|nch|ncib|ncim|ncimb|ncma|ncmb|ncmh|ncpf|ncppb|ncpv|ncsc|nctc|ncyc|neau|nem|neu|ngr|nhl|ni|niaes|niah|niaid|nibh|nies|nih|nihj|niph|nisl|niva-cya|nizo|nlep|nmh|nml|nml-hccc|nrc|nrcc|nrcm|nric|nrl|nrrl|nrzec|nscnfb|ntcci|ntccm|nthc|nua|num|nusdm|nzdri|nzfs|nzp|nzrcc|nzrd|nzrm|nzrp|oac|ocm|oeu|ogc|ogi|oki|omz|oob|ors|out|pah|pamc|pbc|pbf|pcc|pci|pcm|pcu|pd|pddcc|pgsc|phls|phlswho|picc|pir|pncm|pncm-biotech|ppcc|ppppb|prl|psa|ptcc|ptcci|pycc|pzh|qm|qualicontm|rb|rbcar|rbf|rcam|rcc|rcdm|rcs|rdcm|rgm|rh|rhmu|ria|rib|rifis|rify|rimd|ritfc|rkm|rlcc|rm|rmf|rmit|rml|rrlb|rscs|rskk|rtci|rv|rvau|sabammrccc|sag|saitp|sarc|sarcc|sbt|sc|sccm|scsio|sebr|semia|sfri|sg|sgsc|sicgh|siia|skf|skuk|slcc|smcc|smcc-w|smg|smtwa|smum|sn|spmcc|sraicc|src-ccm|sri|srrc|ssi|ssic|st-ivel|stm|swc|sysu|tama|tau-mac|tbrc|tc|tcb|tcc|tcfb|thg|ti|timm|tistr|tkbc|tmc|tmi|tmw|tncc|tph|trm|tua|uamh|uasm|uba|ubc|ubocc|uc|uccm|ucd|ucl|uclaf|ucm|ufpeda|ufrjim|uicc|ujb|ukkp|ukncc|ulc|umass|umfftd|umh|umip|uniqem|uniquem|unsw|unswcc|upcc|upl|upm|upmr|uprm|upsc|uqb|uqm|usba|uscc|usda|usfcc|utcc|utex|utmb|utmc|uuc|uwo|vcp|vcrc|viam|vizr|vkm|vkpm|vniiscm|vpb|vpi|vpri|vruc|vsb|vtcc|vtt|vttcc|vut|wa|wac|wacc|waite|wal|warc|wb|wcum|wdcm|wdds|wfcc|wfpl|who|windsor|wpbs|wr|wri|wrl|wrrl|ws|wsbc|wsf|wslc|wsro|wvb|wvdh|wvu|yblf|yfi|yim|yit|ym|zeneca|zim|zimet)%'
OR LOWER(ref_equi) SIMILAR TO 'care%';

SELECT ref_equi, COUNT(*)
FROM (SELECT unnest(string_to_array(sch_references_equi, ';')) AS ref_equi
FROM t_souche
WHERE xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)) AS a
WHERE ref_equi NOT IN (SELECT * FROM good_refs)
GROUP BY ref_equi 
ORDER BY ref_equi;

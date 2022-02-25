import re

texte = '''<button id="abb" class="accordion">ABB <a href="/text/collections#abb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Asian Bacterial Bank, Samsung Biomedical Research Institute, Sungkyunkwan University, Seoul, Republic of Korea. <b>Country code:</b> KR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="abrc" class="accordion">ABRC <a href="/text/collections#abrc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Anaerobic Bacterial Resource Centre, University of Hyderabad, Department of Plant sciences, University of Hyderabad, Hyderabad, Andhra Pradesh, 500 046, India. <b>Country code:</b> IN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/912" class="">912</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="abriicc" class="accordion">ABRIICC <a href="/text/collections#abriicc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Agricultural Biotechnology Research Institute of Iran Culture Collection, Seed and Plant Improvement Institute Campus, Agricultural Biotechnology Research Institute of Iran, Mahdasht road, Karaj, 31535-1897 Tehran, Iran. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/843" class="">843</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="aca-dc" class="accordion">ACA-DC <a href="/text/collections#aca-dc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Greek Coordinated Collections of Microorganisms, Dairy Laboratory, Department of Food Science and Technology, Agricultural University of Athens, Agricultural University of Athens, Iera Odos 75, Botanikos, GR-11855 Athens, Greece. <b>Country code:</b> GR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/609" class="">609</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="acam" class="accordion">ACAM <a href="/text/collections#acam" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://data.aad.gov.au/aadc/biodiversity/display_collection.cfm?collection_id=90" class="">Australian Collection of Antarctic Microorganisms, Cooperative Research Centre for Antarctic And Southern Ocean Environment, University of Tasmania, GPO Box 252C, Hobart. Tas. 7001, Australia.</a> <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/571" class="">571</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 54.</p>
</div>
<button id="acc" class="accordion">ACC <a href="/text/collections#acc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Akers Culture Collection, ICI Ltd., Alderley Park, Macclesfield, Cheshire, U.K. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1112" class="">1112</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="accc" class="accordion">ACCC <a href="/text/collections#accc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.accc.org.cn/" class="">Agricultural Culture Collection of China, Institute of Soil and Fertilization, Chinese Academy of Agricultural Sciences, 30 Baishiqiao Road, Beijing 100081, People's Republic of China.</a> <b>Country code:</b> CN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/572" class="">572</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 142.</p>
</div>
<button id="acm" class="accordion">ACM <a href="/text/collections#acm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.uq.edu.au/departments/unit.html?unit=405" class="">Australian Collection of Microorganisms, Department of Microbiology and Parasitology, The University of Queensland, Brisbane. Qld. 4072, Australia.</a> <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/13" class="">13</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 54.</p>
</div>
<button id="acoi" class="accordion">ACOI <a href="/text/collections#acoi" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Coimbra Collection of Algae, Department of Botany, University of Coimbra, 3000 Coimbra, Portugal. <b>Country code:</b> PT. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/906" class="">906</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="afrc" class="accordion">AFRC <a href="/text/collections#afrc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institute of Food Research, National Collection of Food Bacteria, Shinfield, Reading, Berkshire, United Kingdom. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="agal" class="accordion">AGAL <a href="/text/collections#agal" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Patent Culture Collection, Australian Government Analytical Laboratory, 1 Suakin St, Pymble. NSW. 2073, Australia. <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ahlda" class="accordion">AHLDA <a href="/text/collections#ahlda" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Animal Health Division Culture Collection, Department of Agriculture, Baron-Hay Crt., South Perth. WA. 6151, Australia. <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/334" class="">334</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ahn" class="accordion">AHN <a href="/text/collections#ahn" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Anaerobe Reference Laboratory, Helsinki Collection, National Public Health Institute, Helsinki, Finland. <b>Country code:</b> FI. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="ahrl" class="accordion">AHRL <a href="/text/collections#ahrl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Animal Health Research Laboratory, CSIRO Division of Animal Health, Private Bag No. 1, Parkville. Vic. 3052, Australia. <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ahu" class="accordion">AHU <a href="/text/collections#ahu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://lab.agr.hokudai.ac.jp/oukin/preserve.html" class="">Laboratory of Culture Collection of Microorganisms, Graduate School of Agriculture, Hokkaido University, Sapporo, Japan.</a> <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/635" class="">635</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 5.</p>
</div>
<button id="aist" class="accordion">AIST <a href="/text/collections#aist" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Institute of Advanced Industrial Science and Technology, Ibaraki, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="aj" class="accordion">AJ <a href="/text/collections#aj" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Central Research Laboratories, Ajinomoto Co, Inc., Kawasaki, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 21.</p>
</div>
<button id="aku" class="accordion">AKU <a href="/text/collections#aku" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Faculty of Agriculture, Kyoto University, Kyoto, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="aliru" class="accordion">ALIRU <a href="/text/collections#aliru" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Australian Legume Inoculants Research Unit, NSW Agriculture Horticultural Research and Advisory Station, Locked Bag 26, Gosford, New South Wales, 2250, Australia. <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/622" class="">622</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="amc" class="accordion">AMC <a href="/text/collections#amc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Biologics Research, Walter Reed Army Institute of Research, Washignton, D.C., USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="amif" class="accordion">AMIF <a href="/text/collections#amif" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>American Meat Institute Foundation, Chicago, Ill., USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="amp" class="accordion">AMP <a href="/text/collections#amp" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Australian Mycological Panel. <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="amrc" class="accordion">AMRC <a href="/text/collections#amrc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>FAO-WHO International Reference Centre for Animal Mycoplasmas, Institute for Medical Microbiology, University of Aarhus, Aarhus, Denmark. <b>Country code:</b> DK. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="amrc-c" class="accordion">AMRC-C <a href="/text/collections#amrc-c" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collaborating Center for Animal Mycoplasmas, Institute for Medical Microbiology, University of Aarhus, Aarhus, Denmark. <b>Country code:</b> DK. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="anmr" class="accordion">ANMR <a href="/text/collections#anmr" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Asian Network on Microbial Research. Database available in JCM. See: <a href="/text/collections#jcm" class="">JCM.</a> <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="api" class="accordion">API <a href="/text/collections#api" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>bioMérieux sa, 69280 Marcy l'Etoile, France. <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 8.</p>
</div>
<button id="ars" class="accordion">ARS <a href="/text/collections#ars" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Agricultural Research Service culture collection. See: <a href="/text/collections#nrrl" class="">NRRL.</a> <b>Country code:</b> US. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="as" class="accordion">AS <a href="/text/collections#as" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Acronym used by the China General Microbiological Culture Collection Center for their accession numbers. See: <a href="/text/collections#cgmcc" class="">CGMCC.</a> <b>Country code:</b> CN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="atcc" class="accordion">ATCC <a href="/text/collections#atcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.lgcstandards-atcc.org/Advanced%20Search" class="">American Type Culture Collection. Corporate: ATCC, 10801 University Boulevard, Manassas, VA 20110-2209, USA Products and Services Orders: ATCC, P.O. Box 1549, Manassas, VA 20108-1549, USA.</a> <b>Country code:</b> US. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1" class="">1</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 4815.</p>
</div>
<button id="athum" class="accordion">ATHUM <a href="/text/collections#athum" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Athens Collection of Fungi, University of Athens, Athens, Greece. <b>Country code:</b> GR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/650" class="">650</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="atu" class="accordion">ATU <a href="/text/collections#atu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Biotechnology, Division of Agriculture and Life Sciences, The University of Tokyo, Tokyo, Japan. <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/636" class="">636</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="aucm" class="accordion">AUCM <a href="/text/collections#aucm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#vkm" class="">VKM.</a> <b>Country code:</b> RU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="aucnm" class="accordion">AUCNM <a href="/text/collections#aucnm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>All-Union Collection of Nonpathogenic Microrganisms, Department of Type Cultures of Microorganisms, Institute of Biochemistry and Physiology of Microorganisms, URSS Academy of Sciences, Puschino, Moscow Region 142292, Russia. <b>Country code:</b> RU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="ayu" class="accordion">AYU <a href="/text/collections#ayu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Laboratory of Applied Microbiology, Yamaguchi University, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="bac" class="accordion">BAC <a href="/text/collections#bac" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.ibvr.org/Catalog.aspx" class="">Acronym used for bacteria by the Biobank of Veterinary Resources of the Istituto Zooprofilattico Sperimentale della Lombardia e dell'Emilia Romagna (IZSLER-BVR), Via Bianchi 9, 25124 Brescia.</a> <b>Country code:</b> IT. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="bacc" class="accordion">BACC <a href="/text/collections#bacc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Brucella AFSSA Culture Collection, AFSSA Alfort, O.I.E./FAO Brucellosis Reference Laboratory, Maisons-Alfort BP67 F-94703, France. <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/789" class="">789</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="bc" class="accordion">BC <a href="/text/collections#bc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Bacterial Collection of the Institute of Microbiology, Faculty of Science, University of Messina, Salita Sperone 31, I-98166 Villagio S. Agata Messina, Italy. <b>Country code:</b> IT. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 11.</p>
</div>
<button id="bcc" class="accordion">BCC <a href="/text/collections#bcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.biotec.or.th/BCC/" class="">BIOTEC Culture Collection, National Center for Genetic Engineering and Biotechnology (BIOTEC), 73/1 Rama VI Road, Patumwan, Bangkok, 10400, Thailand.</a> <b>Country code:</b> TH. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/783" class="">783</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 137.</p>
</div>
<button id="bccm" class="accordion">BCCM <a href="/text/collections#bccm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#lmg" class="">LMG.</a> <b>Country code:</b> BE. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1039" class="">1039</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="bccmlmg" class="accordion">BCCM/LMG <a href="/text/collections#bccmlmg" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#lmg" class="">LMG.</a> <b>Country code:</b> BE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="bccn" class="accordion">BCCN <a href="/text/collections#bccn" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Brucella Culture Collection, INRA, Nouzilly, F-37380, France. <b>Country code:</b> FR. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 5.</p>
</div>
<button id="bccusp" class="accordion">BCCUSP <a href="/text/collections#bccusp" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Brazilian Cyanobacteria Collection - University of Sao Paulo, University of Sao Paulo, Av. Padua Dias, 11, Piracicaba, Sao Paulo, 13418-900, Brazil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/844" class="">844</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="bcrc" class="accordion">BCRC <a href="/text/collections#bcrc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.bcrc.firdi.org.tw/en/home/" class="">Bioresource Collection and Research Center, Food Industry Research and Development Institute, P.O.Box 246, Hsinchu, Taiwan, 30099.</a> <b>Country code:</b> TW. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/59" class="">59</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 788.</p>
</div>
<button id="bdbpi" class="accordion">BDBPI <a href="/text/collections#bdbpi" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Bacteriology Department, Benaki Phytopathological Institute, 8 Delta Street, G-14561, Kiphissia, Athens, Greece. <b>Country code:</b> GR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="bdun" class="accordion">BDUN <a href="/text/collections#bdun" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Botany, University of Nottingham, Nottingham, UK. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="bduz" class="accordion">BDUZ <a href="/text/collections#bduz" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Biological Sciences University of Zimbabwe, University of Zimbabwe, Mount Pleasant, Harare MP167, Zimbabwe. <b>Country code:</b> ZW. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/17" class="">17</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="bei" class="accordion">BEI <a href="/text/collections#bei" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.beiresources.org" class="">BEI Resources, 10801 University Boulevard, Manassas, VA 20110-2209, USA.</a> <b>Country code:</b> US. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 6.</p>
</div>
<button id="beiresources" class="accordion">beiResources <a href="/text/collections#beiresources" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.beiresources.org/" class="">Biodefense and Emerging Infections Research Resources Repository, BEI Resources, 10801 University Boulevard, Manassas, VA 20110-2209, USA.</a> <b>Country code:</b> US. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="bg" class="accordion">BG <a href="/text/collections#bg" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://wwz.ifremer.fr/umr6197/Souchotheque" class="">Souchothèque de Bretagne, Laboratoire de Microbiologie des Environnements Extrêmes, IFREMER Centre Bretagne CS 10070 29280 PLOUZANE.</a> <b>Country code:</b> FR. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 4.</p>
</div>
<button id="bgsc" class="accordion">BGSC <a href="/text/collections#bgsc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.bgsc.org/" class="">Bacillus Genetic Stock Center, Department of Biochemistry, College of Biological Sciences, Ohio State University, USA.</a> <b>Country code:</b> US. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/573" class="">573</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 10.</p>
</div>
<button id="bim" class="accordion">BIM <a href="/text/collections#bim" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://mbio.bas-net.by" class="">Belarusian Collection of non-pathogenic microorganisms, Institute of microbiology, Belarus National Academy of Sciences, 2 Kuprevich str., Minsk 220141, Belarus.</a> <b>Country code:</b> BY. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/909" class="">909</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="biocc" class="accordion">BioCC <a href="/text/collections#biocc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>BioCC BioCen Culture Collection, BioCen, 1 1/2 Beltran, Bejucal, Havana, 6048, Cuba. <b>Country code:</b> CU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/841" class="">841</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="biorepositories" class="accordion">Biorepositories <a href="/text/collections#biorepositories" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.biorepositories.org/" class="">Registry of Biological Repositories (Institutional Acronyms and Collections Codes).</a> <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="bkmw" class="accordion">BKMW <a href="/text/collections#bkmw" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection, Institute of Microbiology, USSR Academy of Sciences, Moscow, Russia. <b>Country code:</b> RU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="bmbc" class="accordion">BMBC <a href="/text/collections#bmbc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Brazilian Marine Bacteria Collection, Universidade Federal de Santa Catarina, Beco dos Coroas, (fundos), Florianopolis, Santa Catarina, 88062-601, Brazil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/910" class="">910</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="bmcc" class="accordion">BMCC <a href="/text/collections#bmcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.ehu.eus/es/web/bmcc" class="">Basque Microalgae Culture Collection, University of the Basque Country.</a> <b>Country code:</b> ES. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1232" class="">1232</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="bmtu" class="accordion">BMTU <a href="/text/collections#bmtu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Boehringer Mannheim GmbH Forschungszentrum Tutzing, Tutzing, Germany. <b>Country code:</b> DE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="bnm" class="accordion">BNM <a href="/text/collections#bnm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://inba.agro.uba.ar/e_index.html" class="">Banco Nacional de Microorganismos (National Bank of Microorganisms), Instituto de Investigaciones en Biociencias Agricolas y Ambientales (INBA), Facultad de Agronomía, Universidad de Buenos Aires, Av. San Martin 4453, Ciudad Autonoma de Buenos Aires, Buenos Aires, C1417DSE.</a> <b>Country code:</b> AR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/938" class="">938</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="bpic" class="accordion">BPIC <a href="/text/collections#bpic" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collections of Phytopathogenic Fungi and Bacteria, Benaki Phylopathological Institute, 8 St. Delta Street, Kiphissia, GR-14561 Athens, Greece. <b>Country code:</b> GR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/610" class="">610</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="br" class="accordion">BR <a href="/text/collections#br" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.embrapa.br/en/agrobiologia/crb-jd" class="">Coleção de Culturas Embrapa Agrobiologia, Embrapa Agrobiologia km 7 Rodovia BR 465, Laboratório de cultura de bactérias, Cx Postal 74505, 23890-000-Seropédica RJ Brazil.</a> <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/364" class="">364</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 37.</p>
</div>
<button id="brcc" class="accordion">BRCC <a href="/text/collections#brcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>USDA-ARS Rhizobium Germplasm Resource Collection, U.S. Department of Agriculture, Agricultural Research Service, Soybean and Alfalfa Research Laboratory, BARC-West, 10300 Baltimore Boulevard, Building 011, Room 19-9, Beltsville, MD 20705, USA. <b>Country code:</b> US. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/540" class="">540</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="brl" class="accordion">BRL <a href="/text/collections#brl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Butterwick Research Laboratories, Welwyn, Hertfordshire, UK. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="bsd" class="accordion">BSD <a href="/text/collections#bsd" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Biodegradative Strain Database, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="btcc" class="accordion">BTCC <a href="/text/collections#btcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Bulgarian Type Culture Collection, Institute for State Control of Drugs, Bd. Vladimir Zaimov 26, Sofia, Bulgaria. <b>Country code:</b> BG. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/632" class="">632</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 8.</p>
</div>
<button id="bucsav" class="accordion">BUCSAV <a href="/text/collections#bucsav" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institute of Biology, Czechoslovak Academy of Sciences, Prague, Czech Republic. <b>Country code:</b> CZ. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="cabi" class="accordion">CABI <a href="/text/collections#cabi" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.cabi.org/" class="">CABI Bioscience, UK.</a> <b>Country code:</b> GB. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cabi-grc" class="accordion">CABI-GRC <a href="/text/collections#cabi-grc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.cabi.org/" class="">The Genetic Resource Collection, CABI Bioscience UK Centre (Egham) formerly IMI, Bakeham Lane, Egham, Surrey, TW20 9TY, UK (Strain numbers: IMI).</a> <b>Country code:</b> GB. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/214" class="">214</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cabri" class="accordion">CABRI <a href="/text/collections#cabri" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.cabri.org/" class="">Common Access to Biotechnological Resources and Information.</a> <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="caim" class="accordion">CAIM <a href="/text/collections#caim" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.ciad.mx/caim/CAIM.html" class="">Collection of Aquacultural Important Microorganisms, CIAD/Mazatlán Unit for Aquaculture and Environmental Management, AP 711, Mazatlán, Sinaloa, 82000, Mexico.</a> <b>Country code:</b> MX. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/813" class="">813</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 96.</p>
</div>
<button id="cair" class="accordion">CAIR <a href="/text/collections#cair" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Center for the Application of Isotopes and Radiation, P.O.Box 2 KBYL, Jakarta Selatan 12240, Indonesia. <b>Country code:</b> ID. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="caircc" class="accordion">CAIRCC <a href="/text/collections#caircc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Center for the Application of Isotopes and Radiation, P.O.Box 2 KBYL, Jakarta Selatan 12240, Indonesia. <b>Country code:</b> ID. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/623" class="">623</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cairo" class="accordion">CAIRO <a href="/text/collections#cairo" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Cairo Microbiological Resource Centre - Cairo Mircen, Faculty of Agriculture, Cairo, Egypt. <b>Country code:</b> EG. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="calu" class="accordion">CALU <a href="/text/collections#calu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Algae St. Petersburg (Leningrad) State University, Centre for Culture Collection of Microorganisms, Laboratory of Microbiology, Faculty of Biology, St.Petersburg State University. <b>Country code:</b> RU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/461" class="">461</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 4.</p>
</div>
<button id="capm" class="accordion">CAPM <a href="/text/collections#capm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://capm.vri.cz/en" class="">Collection of Animal Pathogenic Microorganisms, Veterinary Research Institute, Hudcova 70, 621 32 Brno, Czech Republic.</a> <b>Country code:</b> CZ. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/181" class="">181</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="cau" class="accordion">CAU <a href="/text/collections#cau" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Microbiology, Chung-Ang University College of Medicine, Seoul, Republic of Korea, 84 HeukSeok-Ro, Dongjak-Gu, Seoul, Korea. <b>Country code:</b> KR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 55.</p>
</div>
<button id="caup" class="accordion">CAUP <a href="/text/collections#caup" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Algae, Charles University, Department of Botany, Faculty of Science, Benátská 2, 128 01 Praha 2, Czech Republic. <b>Country code:</b> CZ. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/486" class="">486</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cb" class="accordion">CB <a href="/text/collections#cb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>The CB Rhizobium Collection, The CB Rhizobium Collection, CSIRO Tropical Agriculture, 306 Carmody Road, St. Lucia. Brisbane. Qld. 4067, Australia. <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/57" class="">57</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 18.</p>
</div>
<button id="cbas" class="accordion">CBAS <a href="/text/collections#cbas" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://cbas.fiocruz.br/index?catalogue" class="">Bacteria Collection of Environment and Health, Laboratory of Molecular Genetics of Microorganisms (LGMM) of the Oswaldo Cruz Institute, FIOCRUZ, Rio de Janeiro, Brazil.</a> <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/958" class="">958</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 13.</p>
</div>
<button id="cbcc" class="accordion">CBCC <a href="/text/collections#cbcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Colworth Bacterial Culture Collection, Unilever Research Laboratory, Colworth House, Sharnbrook, U.K. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cbfs" class="accordion">CBFS <a href="/text/collections#cbfs" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Herbarium for Nonvascular Cryptogams at the Department of Botany, Faculty of Science, University of South Bohemia, Czech Republic. <b>Country code:</b> CZ. <b>Index Herbariorum:</b> <a href="http://sweetgum.nybg.org/science/ih/herbarium-details/?irn=62191" class="">62191</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 22.</p>
</div>
<button id="cbmai" class="accordion">CBMAI <a href="/text/collections#cbmai" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://webdrm.cpqba.unicamp.br/index.php?eLinguagemStr=en" class="">Brazilian Collection of Microorganisms from the Environment and Industry (Colecao Brasileira de Microrganismos de Ambiente e Industria), Campinas State University (UNICAMP), CPQBA-UNICAMP / Av. Alexandre Cazelatto, 999 / Vila Betel, Paulinia, SP, CEP 13140-000, Brazil.</a> <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/823" class="">823</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 18.</p>
</div>
<button id="cbri" class="accordion">CBRI <a href="/text/collections#cbri" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Cell Biology Research Institute, Department of Agriculture, Ottawa, Canada. <b>Country code:</b> CA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cbrvs" class="accordion">CBRVS <a href="/text/collections#cbrvs" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://cbrvs.fiocruz.br/index?services" class="">Coleção de Bactérias de Referência em Vigilância Sanitária, Instituto Nacional de Controle de Qualidade em Saúde (INCQS), Av. Brasil, 4365 - Manguinhos, Rio de Janeiro - RJ - Brasil - CEP: 21.040-900.</a> <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1153" class="">1153</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="cbs" class="accordion">CBS <a href="/text/collections#cbs" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.cbs.knaw.nl/" class="">Centraalbureau voor Schimmelcultures, Uppsalalaan 8, 3584 CT Utrecht, The Netherlands- P.O.Box 85167, 3508 AD Utrecht, The Netherlands.</a> <b>Country code:</b> NL. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/133" class="">133</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 476.</p>
</div>
<button id="cc" class="accordion">CC <a href="/text/collections#cc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>CSIRO Canberra Rhizobium Collection, Division of Plant Industry CSIRO, G.P.O. Box 1600, Canberra, ACT, 2601, Australia. <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/61" class="">61</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 14.</p>
</div>
<button id="ccala" class="accordion">CCALA <a href="/text/collections#ccala" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of Algae at the Laboratory of Algology (Culture Collection of Autotrophic Organisms, Czechoslovak Database of Algae and Cyanobacteria), Czechoslovak Academy of Sciences, Institute of Botany, Department Hydrobotany, Dukelská 145, CZ-37 982 Třeboň, Czech Republic. <b>Country code:</b> CZ. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/905" class="">905</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 25.</p>
</div>
<button id="ccam" class="accordion">CCAM <a href="/text/collections#ccam" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>China Collection of Anaerobic Microorganisms, Biogas Institute of Ministry of Agriculture and Rural Affairs, Section 4-13, Renmin Nan Road, Chengdu, Sichuan, 610041. <b>Country code:</b> CN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1189" class="">1189</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 6.</p>
</div>
<button id="ccap" class="accordion">CCAP <a href="/text/collections#ccap" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.ccap.ac.uk/" class="">Culture Collection of Algae and Protozoa, Centre for Ecology and Hydrology, CEH Windermere, The Ferry House, Far Sawrey, Ambleside, Cumbria LA22 0LP, United Kingdom.</a> <b>Country code:</b> GB. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/522" class="">522</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 14.</p>
</div>
<button id="ccarm" class="accordion">CCARM <a href="/text/collections#ccarm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of Antibiotic Resistant Microbes, 126 Kongnung 2dong, Nowon-gu, Seoul 139-774, Republic of Korea. <b>Country code:</b> KR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/847" class="">847</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="ccbau" class="accordion">CCBAU <a href="/text/collections#ccbau" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of Beijing Agricultural University, Beijing, People's Republic of China. <b>Country code:</b> CN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/116" class="">116</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 68.</p>
</div>
<button id="ccb-mbl" class="accordion">CCB-MBL <a href="/text/collections#ccb-mbl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.ccb.usm.my/index.php/ccb-mbl" class="">Centre For Chemical Biology, Universiti Sains Malaysia, Sains@USM, Blok B No. 10, Persiaran Bukit Jambul 11900 Bayan Lepas Pulau Pinang Malaysia.</a> <b>Country code:</b> MY. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="ccccm" class="accordion">CCCCM <a href="/text/collections#ccccm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://micronet.im.ac.cn/database/aboutccccm.html" class="">China Committee for Culture Collection of Microorganisms, Institute of Microbiology, Academia Sinica, Beijiing, People's Republic of China.</a> <b>Country code:</b> CN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cccieb" class="accordion">CCCIEB <a href="/text/collections#cccieb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collections of Microorganisms of Center of Genetic Engineering and Biotechnology, Center of genetic Engineering and Biotechnology, 31 Ave / 158 and 190, C. Habana P.O. Box 6162, Cuba. <b>Country code:</b> CU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/771" class="">771</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cccm" class="accordion">CCCM <a href="/text/collections#cccm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Canadian Center for the Culture of Microorganisms, Department of Botany, 6270 University Boulevard, Vancouver, B.C. Canada V6T 1Z4. <b>Country code:</b> CA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ccdm" class="accordion">CCDM <a href="/text/collections#ccdm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of Department of Microbiology, Huazhong Agricultural University, Shizishan, Wuhan, Hubei, 430070, China. <b>Country code:</b> CN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/878" class="">878</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ccdmbi" class="accordion">CCDMBI <a href="/text/collections#ccdmbi" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection, Department of Microbiology, Bose Institute, 93/1 Acharya Prafulla Chandra, Calcutta, West Bengal, 700009, India. <b>Country code:</b> IN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/119" class="">119</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cceb" class="accordion">CCEB <a href="/text/collections#cceb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of Entomophagous Bacteria, Institute of Entomology, Czechoslovak Academy of Sciences, Flemingovo 2, Prague 6, Czechoslovakia. <b>Country code:</b> CZ. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 4.</p>
</div>
<button id="ccf" class="accordion">CCF <a href="/text/collections#ccf" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Colleccion de Cuttivos Finlay, Instituto Finlay, 27# 19805, Civdad de la Habara 11600, Cuba. <b>Country code:</b> CU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/182" class="">182</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ccfc" class="accordion">CCFC <a href="/text/collections#ccfc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Canadian Collection of Fungal Cultures, Agriculture and Agri-Food Canada, Rm. 1015, K.W. Neatby Bldg., K1A OC6 Ottawa, Ontario, Canada. <b>Country code:</b> CA. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/150" class="">150</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ccfcdaom" class="accordion">CCFC/DAOM <a href="/text/collections#ccfcdaom" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Canadian Collection of Fungal Cultures, Agriculture and Agri-Food Canada, Rm. 1015, K.W. Neatby Bldg., K1A OC6 Ottawa, Ontario, Canada. <b>Country code:</b> CA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ccgb" class="accordion">CCGB <a href="/text/collections#ccgb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Cole(e7)o de Culturas do G(ea)ero Bacillus e G(ea)eros Correlatos, Fundacao Oswaldo Cruz - Instituto Oswaldo Cruz- Departamento de Bacteriologia - Laborat(f3)io de Fisiologia Bacteriana, Av. Brasil, 4365 - Manguinhos, Cx. Postal 926, Rio de Janeiro, Rio de Janeiro, 21045-900, Brazil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/574" class="">574</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="cchrgm" class="accordion">CChRGM <a href="/text/collections#cchrgm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.cchrgm.cl/" class="">Chilean Collection of Microbial Genetic Resources, Instituto de Investigaciones Agropecuarias (INIA), Av. Vicente Méndez 515, Chillán, Bio-Bío, 3800021.</a> <b>Country code:</b> CL. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1067" class="">1067</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ccibso" class="accordion">CCIBSO <a href="/text/collections#ccibso" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.ibp.ru/collection/default.php" class="">Culture Collection IBSO, Institute of Biophysics (Siberian Bransh of Russian Academy of Sciences), Akademgorodok, Krasnoyarsk 660036, Russia.</a> <b>Country code:</b> RU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/836" class="">836</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ccim" class="accordion">CCIM <a href="/text/collections#ccim" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of the Institute of Microbiology, Academia Sinica, Beijing, People's Republic of China. <b>Country code:</b> CN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/860" class="">860</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="ccm" class="accordion">CCM <a href="/text/collections#ccm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.sci.muni.cz/ccm/index.html" class="">Czech Collection of Microorganisms, Masaryk University, Faculty of Science, Tvrdého 14, 602 00 Brno, Czech Republic.</a> <b>Country code:</b> CZ. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/65" class="">65</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 620.</p>
</div>
<button id="ccma" class="accordion">CCMA <a href="/text/collections#ccma" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Coleção de Culturas de Microbiologia Agrícola, Culture Collection of Agricultural Microbiology, Universidade Federal de Lavras, Brazil. <b>Country code:</b> BR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="ccm-a" class="accordion">CCM-A <a href="/text/collections#ccm-a" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Coleccion de Cultivos Microbianos, Facultad de Farmacia y Bioquimica, Universidad de Buenos Aires, Junin 956, Piso 8, Buenos Aires 1113, Argentina. <b>Country code:</b> AR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/29" class="">29</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="ccmcu" class="accordion">CCMCU <a href="/text/collections#ccmcu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of Microorganisms, Department of Microbiology (Escuela Tecnica Superior de Ingenieros Agronomos), Ciudad Universitaria, 28040 Madrid, Spain. <b>Country code:</b> ES. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/559" class="">559</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ccmee" class="accordion">CCMEE <a href="/text/collections#ccmee" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of Microorganisms from Extreme Environments, University of Oregon, Center for Ecology and Evolutionary Biology, 5289 University of Oregon, Eugene, OR 97403-5289, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="ccmi" class="accordion">CCMI <a href="/text/collections#ccmi" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of Industrial Microorganisms, National Institute of Industrial Technology, Azinhaga dos Lameiros, Lisboa 1699-038, Portugal. <b>Country code:</b> PT. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/761" class="">761</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ccmm" class="accordion">CCMM <a href="/text/collections#ccmm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.ccmm.ma/" class="">Moroccan Coordinated Collections of Microorganisms, Centre National pour la Recherche Scientifique et Technique (CNRST), 52, Avenue Omar Ibn Khattab - B.P 8027 - Agdal, Rabat 10.102, Morocco.</a> <b>Country code:</b> MA. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/883" class="">883</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 13.</p>
</div>
<button id="ccmp" class="accordion">CCMP <a href="/text/collections#ccmp" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://ncma.bigelow.org/" class="">Provasoli-Guillard National Center for Culture of Marine Phytoplankton, Bigelow Laboratory, McKown Point, West Boothbay Harbor, ME 04575, USA.</a> <b>Country code:</b> US. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/2" class="">2</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="ccoc" class="accordion">CCOC <a href="/text/collections#ccoc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Fundacao Oswaldo Cruz-FIOCRUZ, Instituto Nacional de Controle de Qualidade em Saude-INCQS, Av. Brasil, 4365-Manguinhos, Rio de Janeiro, RJ, 21045-900, Brazil. <b>Country code:</b> BR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ccos" class="accordion">CCOS <a href="/text/collections#ccos" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.ccos.ch/" class="">Culture Collection of Switzerland, Einsiedlerstr. 34, CH 8820 Waedenswil, Switzerland.</a> <b>Country code:</b> CH. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/944" class="">944</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 40.</p>
</div>
<button id="ccrc" class="accordion">CCRC <a href="/text/collections#ccrc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.bcrc.firdi.org.tw/index.do" class="">The Culture Collection and Research Center, Food Industry Research and Development Institute, P.O. Box 246, Hsinchu, 30099, Taiwan, R.O.C.</a> <b>Country code:</b> TW. <b>Index Herbariorum:</b> <a href="http://sweetgum.nybg.org/science/ih/herbarium-details/?irn=59" class="">59</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 399.</p>
</div>
<button id="ccri" class="accordion">CCRI <a href="/text/collections#ccri" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection du Centre de Recherche en Infectiologie, Universite Laval, 2705 Boulevard Laurier, RC709, Quebec, Quebec, G1V 4G2, Canada. <b>Country code:</b> CA. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/861" class="">861</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 7.</p>
</div>
<button id="ccsiia" class="accordion">CCSIIA <a href="/text/collections#ccsiia" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of Sichuan Industrial Institute Antibiotics, Sichuan Industrial Institute of Antibiotics, Shanbangiao P.O.Box 610051, Chengdu, Sichuan, China. <b>Country code:</b> CN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/576" class="">576</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ccsm" class="accordion">CCSM <a href="/text/collections#ccsm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection for Soil Microorganisms, Soil and Water Reserarch Instutute(SWRI), North Kargar Ave., Jalal Al Ahmad, Tehran, Tehran, 14155-6185, Iran. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/891" class="">891</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ccstamb" class="accordion">CCStamb <a href="/text/collections#ccstamb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.stamboulian.com.ar" class="">Reference Microorganism Stamboulian Laboratory, Av. Scalabrini Ortiz 676 (C1414DNT), Buenos Aires, Argentina, 4858-7000.</a> <b>Country code:</b> AR. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="cct" class="accordion">CCT <a href="/text/collections#cct" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Coleção de Culturas Tropical, Rua Latino Coelho, 1301 Parque Taquaral, CEP 13087-010 - Campinas - SP - Brasil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/885" class="">885</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 12.</p>
</div>
<button id="cctcc" class="accordion">CCTCC <a href="/text/collections#cctcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.cctcc.org/sci/microbe_common/searchc.php" class="">Chinese Centre for Type Cultures Collections, Wuhan University, Wuhan, Hubei, 430072, China.</a> <b>Country code:</b> CN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/611" class="">611</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1076.</p>
</div>
<button id="cctm" class="accordion">CCTM <a href="/text/collections#cctm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centre de Collection de Types Microbiens, Institut Universitaire de Microbiologie, 44 Rue du Bugnon, CH-1011, Lausanne, Switzerland. <b>Country code:</b> CH. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/475" class="">475</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ccub" class="accordion">CCUB <a href="/text/collections#ccub" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Actinomycete Culture Collection, University of Bradford, Richmon Rd., Bradford, Yorkshire BD7 1DP, U.K. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ccug" class="accordion">CCUG <a href="/text/collections#ccug" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.ccug.se/" class="">Culture Collection, University of Göteborg, Department of Clinical Bacteriology, Institute of Clinical Bacteriology, Immunology, and Virology, Guldhedsgatn 10A s-413, 46 Göteborg, Sweden.</a> <b>Country code:</b> SE. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/32" class="">32</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 3110.</p>
</div>
<button id="ccy" class="accordion">CCY <a href="/text/collections#ccy" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of Yeasts, Institute of Chemistry, Slovak Academy of Sciences, Bratislava, Slovakia. <b>Country code:</b> SK. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/333" class="">333</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cda" class="accordion">CDA <a href="/text/collections#cda" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Canadian Department of Agriculture, Ottawa, Canada. <b>Country code:</b> CA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="cdbb" class="accordion">CDBB <a href="/text/collections#cdbb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://cinvestav.mx/cgse/uscncmcc/" class="">Unidad de Servicios de la Coleccion Nacional de Cepas Microbianas y Cultivos Celulares, Centro de Investigacion y de Estudios Avanzados del IPN, Av. Instituto Politecnico Nacional 2508, Mexico, D.F., Del. G.A. Madero, 07360, Mexico.</a> <b>Country code:</b> MX. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/500" class="">500</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cdc" class="accordion">CDC <a href="/text/collections#cdc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centers for Disease Control, United States Public Health Service, 1600 Clifton Rd., Atlanta, Georgia 30333, USA. <b>Country code:</b> GE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 105.</p>
</div>
<button id="ceb" class="accordion">CEB <a href="/text/collections#ceb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centre d'Etudes du Bouchet, Le Bouchet, France. <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cect" class="accordion">CECT <a href="/text/collections#cect" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.uv.es/uvweb/spanish-type-culture-collection/en/strains/culture-media-catalogue-/strains-search-engine-1285892802374.html" class="">Colección Espagnola de Cultivos Tipo, Universitat de Valencia, Edeficio de Investigación, Campus de Burjasot, 46100 Burjasot (Valencia), Spain.</a> <b>Country code:</b> ES. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/412" class="">412</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 1094.</p>
</div>
<button id="celms" class="accordion">CELMS <a href="/text/collections#celms" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.tymri.ut.ee/en/institute/microbial-collection" class="">Collection of Environmental and Laboratory Microbial Strains, University of Tartu, 23 Riia Str, Tartu 51010, Estonia.</a> <b>Country code:</b> EE. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/926" class="">926</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="cenacumi" class="accordion">CENACUMI <a href="/text/collections#cenacumi" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centro Nacional de Cultivos Microbianos, P.O.Box 60-600, Mexico City, D.F., 03800, Mexico. <b>Country code:</b> MX. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/757" class="">757</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cepim" class="accordion">CEPIM <a href="/text/collections#cepim" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centro per gli Enterobatteri Patogeni per l'Italia Meridionale, Instituto di Igiene dell'Universita, Via del Vespro, 133, Palermo 90127, Italy. <b>Country code:</b> IT. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/213" class="">213</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cepm" class="accordion">CEPM <a href="/text/collections#cepm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centre d'Etudes sur le Polymorphisme des Micro-organismes, Institut de Recherche pour le Developpement, 911 avenue Agropolis-B.P.5045, 34032 Montpellier Cedex 01, France. <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/787" class="">787</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cetesb" class="accordion">CETESB <a href="/text/collections#cetesb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Setor de Pesquisa Tecnologica de Sistemas de Tratamento de Efluentes Domesticos, Cia. de Tecnologia de Saneamento Ambiental, Av. Prof. Frederico Herman Jr, 345, Alto de Pinheiros, 05489 Sao Paulo, SP, Brazil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/714" class="">714</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cfbp" class="accordion">CFBP <a href="/text/collections#cfbp" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://catalogue-cfbp.inra.fr/recherche_e.php" class="">Collection Francaise des Bacteries Phytopathogenes, INRA Station de Pathologie Végétale et Phytobactériologie, 42 rue G. Morel, B.P. 57, F-49071 Beaucouzé Cedex, France.</a> <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/639" class="">639</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 243.</p>
</div>
<button id="cfcc" class="accordion">CFCC <a href="/text/collections#cfcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.cfcc-caf.org.cn/servlet/JunZhongServlet_en?find=A" class="">China Forestry Culture Collection Center, Research Institute of Forest Ecology, Environment and Protection, Chinese Academy of Forestry, Beijing 100091, PR China.</a> <b>Country code:</b> CN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/995" class="">995</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 41.</p>
</div>
<button id="cfml" class="accordion">CFML <a href="/text/collections#cfml" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection de la Faculté de Médecine de Lille, 1 place de Verdun, 59045 Lille Cedex, France. <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 12.</p>
</div>
<button id="cfn" class="accordion">CFN <a href="/text/collections#cfn" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centro de Investigación sobre Fijación de Nitrógeno, Universidad Nacional Autónoma de México, Apdo Postal 565-A, Cuernavaca, Morelos, Mexico. <b>Country code:</b> MX. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 5.</p>
</div>
<button id="cgmcc" class="accordion">CGMCC <a href="/text/collections#cgmcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.cgmcc.net/english/catalogue.html" class="">China General Microbiological Culture Collection Centre, Institute of Microbiology, Chinese Academy of Sciences, Beijing 100080, PR China.</a> <b>Country code:</b> CN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/550" class="">550</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 2115.</p>
</div>
<button id="cgsc" class="accordion">CGSC <a href="/text/collections#cgsc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://cgsc.biology.yale.edu/" class="">Escherichia coli Genetic Stock Center, 830 Kline Biology Tower, MCD Biology Department, 266 Whitney Ave., PO box 208103, Yale University, New Haven, CT 06520-8193, USA.</a> <b>Country code:</b> US. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/827" class="">827</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ch-ag" class="accordion">CH-AG <a href="/text/collections#ch-ag" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection de Recherche, Centre Hospitalier General Avranches-Granville Laboratoire de Microbiologie, 59 rue de la Liberte, 50300 Avranches, France. <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/790" class="">790</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ciam" class="accordion">CIAM <a href="/text/collections#ciam" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Nonpathogenic Microorganisms for Agriculture, All-Russia Research Institute for Agricultural Microbiology (ARRIAM), Shosse Podbelskogo, 3, Saint-Petersburg - Pushkin 196608, Russian Federation. <b>Country code:</b> RU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/890" class="">890</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ciat" class="accordion">CIAT <a href="/text/collections#ciat" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Rhizobium Collection, Centro International de Agricultura Tropical, AA 6713, Cali, Colombia. <b>Country code:</b> CO. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/536" class="">536</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="cicc" class="accordion">CICC <a href="/text/collections#cicc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.china-cicc.org/English/english.html" class="">Chinese Center for industrial Culture Collection, Xiao Yun Road Chao Yan District Beijing, China.</a> <b>Country code:</b> CN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/582" class="">582</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 102.</p>
</div>
<button id="cicim" class="accordion">CICIM <a href="/text/collections#cicim" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>The Culture and Information Centre of Industrial Microoganisms of China Universities, Southern Yangtze University, 170 Huihe Rd., Wuxi, Jiangsu, 214036, China. <b>Country code:</b> CN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/897" class="">897</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cicv" class="accordion">CICV <a href="/text/collections#cicv" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centro de Investigaciones en Ciencias Veterinarias, Las Cabanas Y Los Reseros, Villa Udaondo, Buenos Aires, 1708-C.C.No 77, Argentina. <b>Country code:</b> AR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/33" class="">33</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cimsc" class="accordion">CIMSC <a href="/text/collections#cimsc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collezione Instituto di Microbiologia, Spedali Civili, P. le Spedali Civili 1, Brescia 25100, Italy. <b>Country code:</b> IT. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/424" class="">424</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cip" class="accordion">CIP <a href="/text/collections#cip" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://catalogue-crbip.pasteur.fr/recherche_catalogue.xhtml" class="">Collection de l'Institut Pasteur, Institut Pasteur, 28 Rue du Docteur Roux, 75724 Paris Cedex 15, France.</a> <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/759" class="">759</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2978.</p>
</div>
<button id="cipt" class="accordion">CIPT <a href="/text/collections#cipt" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection Institut Pasteur Tuberculose, Institut Pasteur, 25 rue du Dr Roux, Paris 75724 Cedex 15, France. <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/346" class="">346</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cirm-bia" class="accordion">CIRM-BIA <a href="/text/collections#cirm-bia" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://collection-cirmbia.fr/page/Souches_table" class="">Centre International de Ressources Microbiennes Bacteries d'Interet Alimentaire, Institut National de la Recherche Agronomique, INRA UMR STLO - 65, rue de Saint brieuc, Rennes Cedex 35042, France.</a> <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/918" class="">918</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="cirmbp" class="accordion">CIRMBP <a href="/text/collections#cirmbp" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#cirm-bp" class="">CIRM-BP.</a> <b>Country code:</b> FR. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="cirm-bp" class="accordion">CIRM-BP <a href="/text/collections#cirm-bp" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www6.inrae.fr/cirm_eng/" class="">Centre International de Ressources Microbiennes - Bacteries Pathogenes, Institut National de la Recherche Agronomique, IASP 311- INRA, centre de Tours, Nouzilly 37380, France.</a> <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/917" class="">917</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="clep" class="accordion">CLEP <a href="/text/collections#clep" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://clep.fiocruz.br/" class="">Coleção de Leptospira, Fundação Oswaldo Cruz (Fiocruz), Rio de Janeiro, Brazil.</a> <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1012" class="">1012</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="clip" class="accordion">CLIP <a href="/text/collections#clip" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Listeria Collection of the Pasteur Institute, Institut Pasteur, 28 Rue du Docteur Roux, 75724 Paris Cedex 15, France. <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 5.</p>
</div>
<button id="cmaa" class="accordion">CMAA <a href="/text/collections#cmaa" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://alelomicro.cenargen.embrapa.br/InterMicro/Intercambio/acessos.xjs?ids=13" class="">Collection of Microorganisms of Agricultural and Environmental Importance, Rodovia SP 340, Km 127, 5 - Bairro Tanquinho Velho, Jaguariuna, Sao Paulo, 13820-000.</a> <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1149" class="">1149</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 8.</p>
</div>
<button id="cmcc" class="accordion">CMCC <a href="/text/collections#cmcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>China Medical Culture Collection Center, National Institute for the Control of Pharmaceutical and Biological Products (NICPBP), Ministry of Public Health, Beijing, China. <b>Country code:</b> CN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/123" class="">123</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="cm-cnrg" class="accordion">CM-CNRG <a href="/text/collections#cm-cnrg" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://cmcnrg.inifap.gob.mx/" class="">Coleccion de Microorganismos del Centro Nacional de Recursos Geneticos, Boulevard de la Biodiversidad no. 400, Tepatitlan de Morelos, Jalisco, 47600.</a> <b>Country code:</b> MX. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1006" class="">1006</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="cmdm-puj" class="accordion">CMDM-PUJ <a href="/text/collections#cmdm-puj" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Coleccion Microorganismos Departamento Microbiologia, Pontificia Universidad Javeriana, 7 CARRERA #43-82, Bogota, Cundinamarca, Colombia. <b>Country code:</b> CO. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cmi" class="accordion">CMI <a href="/text/collections#cmi" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#imi" class="">IMI.</a> <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 10.</p>
</div>
<button id="cmmc" class="accordion">CMMC <a href="/text/collections#cmmc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>China Marine Microbe Collection, Yellow Sea Fisheries Research Institute of Chinese Academy of Fishery Sciences, nanjing Road 106, qingdao, shandong, 266071, China. <b>Country code:</b> CN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/865" class="">865</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cmppb" class="accordion">CMPPB <a href="/text/collections#cmppb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Microbiological Cultures - Potential Producers of Biopesticides, Research-Industrial Company Rosagroservice, Gamaleya street, 18, Moscow, 123098, Russia. <b>Country code:</b> RU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cmpuj" class="accordion">CMPUJ <a href="/text/collections#cmpuj" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://ciencias.javeriana.edu.co/investigacion/colecciones-biologicas/microorganismos" class="">Colección de Microorganismos Pontificia Universidad Javeriana, Bogotá D.C., Colombia, Carrera 7 No. 40 - 62.</a> <b>Country code:</b> CO. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 5.</p>
</div>
<button id="cmrvs" class="accordion">CMRVS <a href="/text/collections#cmrvs" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.incqs.fiocruz.br/index.php?option=com_content&amp;view=article&amp;id=183" class="">Coleção de Micro-organismos de Referência em Vigilância Sanitária, Instituto Nacional de Controle de Qualidade em Saúde (INCQS), Av. Brasil, 4365 - Manguinhos, Rio de Janeiro - RJ - Brasil - CEP: 21.040-900. Online catalogue is currently under construction.</a> <b>Country code:</b> BR. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="cn" class="accordion">CN <a href="/text/collections#cn" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Wellcome Collection of Bacteria, Burroughs Wellcome Research Laboratories, Beckenham, Kent, UK. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 13.</p>
</div>
<button id="cnblm" class="accordion">CNBLM <a href="/text/collections#cnblm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collectione Nationale de Bacteria, Lab. Microbiologia, Centro per l'Ecologia Teorica e Applicata CETA, Via Vittorio Veneto 19, I-34170, Gorizia, Ital. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cncm" class="accordion">CNCM <a href="/text/collections#cncm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.pasteur.fr/recherche/unites/Cncm/" class="">Collection Nationale de Cultures de Microorganismes, Institut Pasteur, 25 Rue du Docteur Roux, 75015 Paris, France. "Microorganisms in the CNCM (National Collection of Cultures of Microorganisms) are deposited under the Budapest Treaty for the purposes of patent procedure. Information and samples are not accessible according to the good will of the CNCM, but according to the Regulations under this treaty. Pursuant to Rule 9.2 of these regulations no information can be given by the CNCM about microorganisms we have, and therefore, no catalogue is publicly available." (Hurtado-Ortiz, R., pers. comm., February 2020).</a> <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/174" class="">174</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 23.</p>
</div>
<button id="cncru" class="accordion">CNCRU <a href="/text/collections#cncru" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Colección Nacional de Cepas de Rhizobium, Ruta 48, Km 10, Rincón del Colorado, Canelones, 11100, Uruguay. <b>Country code:</b> UY. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1082" class="">1082</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cnctc" class="accordion">CNCTC <a href="/text/collections#cnctc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.szu.cz/cnctc/a/uvod.php" class="">Czech National Collection of Type Cultures, National Institute of Public Health, Srobarova 48, 110 42 Praha 10, Czech Republic.</a> <b>Country code:</b> CZ. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/130" class="">130</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 19.</p>
</div>
<button id="cnpbs" class="accordion">CNPBS <a href="/text/collections#cnpbs" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centro Nacional de Pesquisa em Biologia do Solo, Rio de Janeiro, Brazil. <b>Country code:</b> BR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cnpso" class="accordion">CNPSo <a href="/text/collections#cnpso" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.embrapa.br/en/international" class="">Culture Collection of Diazotrophic and Plant Growth Promoting Bacteria of Embrapa Soja, C.P. 231, Rodovia João Carlos Strass, s/n, Cx. Postal 231, Londrina, Paraná, 86001-970, Brazil.</a> <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1054" class="">1054</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 22.</p>
</div>
<button id="cnrz" class="accordion">CNRZ <a href="/text/collections#cnrz" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centre National de Recherches Zootechniques, Jouy-en-Josas, France. <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 4.</p>
</div>
<button id="cns" class="accordion">CNS <a href="/text/collections#cns" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centre National des Salmonella, Paris, France. <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="cnu" class="accordion">CNU <a href="/text/collections#cnu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Newcastle University, Department of Microbiology, The Medical School, University of Newcastle, Newcastle upon Tyne NE1 7RU, United Kingdom. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 4.</p>
</div>
<button id="cny" class="accordion">CNY <a href="/text/collections#cny" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centre National des Yersinia, Institut Pasteur, Paris, France. <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="cpac" class="accordion">CPAC <a href="/text/collections#cpac" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Cpac-Embrapa, Embrapa-Cerrados, CX.Postal 08223, Planaltina, DF, 73301-970, Brazil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/776" class="">776</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cpcc" class="accordion">CPCC <a href="/text/collections#cpcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.phycol.ca/" class="">Canadian Phycological Culture Centre (formerly known as the University of Toronto Culture Collection of Algae and Cyanobacteria, UTCC), Department of Biology, University of Waterloo, 200 University Ave W., Waterloo, ON, CANADA N2L3G1.</a> <b>Country code:</b> CA. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/955" class="">955</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 48.</p>
</div>
<button id="cphs" class="accordion">CPHS <a href="/text/collections#cphs" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.health.qld.gov.au/healthsupport/businesses/forensic-and-scientific-services/testing-analysis/diseases/leptospirosis" class="">WHO/FAO/OIE Collaborating Centre for Reference and Research on Leptospirosis, Western Pacific Region, Laboratory of Microbiology and Pathology, Centre for Public Health Sciences, Queensland Department of Health, 39 Kessels Road, Coopers Plains. Qld. 4108, Australia.</a> <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/14" class="">14</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cppipp" class="accordion">CPPIPP <a href="/text/collections#cppipp" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Plant Pathogens, Plant Protection Institute, Miczurina 20, 60-318 Poland. <b>Country code:</b> PL. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/785" class="">785</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cpz" class="accordion">CPZ <a href="/text/collections#cpz" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centro Panamericano de Zoonosis, Casilla 3092 Correo Central, Martinez, Buenos Aires, D-3300, Argentina. <b>Country code:</b> AR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/275" class="">275</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="crab" class="accordion">CRAB <a href="/text/collections#crab" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centre National de Référence des Antibiotiques, Bacterial strains available from the CRAB, Institut Pasteur, 25 rue du Dr Roux - 75724 Paris Cedex 15, France. <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="crbip" class="accordion">CRBIP <a href="/text/collections#crbip" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.pasteur.fr/en/research/crbip-biological-resource-center-institut-pasteur" class="">Biological Resource Center of Institut Pasteur, France.</a> <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/925" class="">925</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 4.</p>
</div>
<button id="cripp" class="accordion">CRIPP <a href="/text/collections#cripp" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of Rhizobia, Research Institute of Crop Production, Drnovská 507, 161 06 Praha 6 - Ruzyně, Czech Republic. <b>Country code:</b> CZ. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="crirc" class="accordion">CRIRC <a href="/text/collections#crirc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>CDC Rickettsial Isolate Reference Collection, Rickettsial Zoonoses Branch, Division of Vector-Borne Diseases, National Center for Emerging and Zoonotic Infectious Diseases, Centers for Disease Control and Prevention, Mail Stop H17-3, 1600 Clifton Rd. NE; MS G13, Atlanta, GA, 30333. <b>Country code:</b> US. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1093" class="">1093</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 8.</p>
</div>
<button id="crl" class="accordion">CRL <a href="/text/collections#crl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centro de Referencia Para Lactobacilos, Consejo Nacional de Investigaciones Cientificas y Tecnicas, Chacabuco 145, San Miguel de Tucuman, Tucuman, 4000, Argentina. <b>Country code:</b> AR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/614" class="">614</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="crs" class="accordion">CRS <a href="/text/collections#crs" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Rhizobium Strains, Institute of Soil Sciences (IUNG), Department of Microbiology, ul. Gorskiego 7 (Osada Palacowa), 24-100 Pulawy, Poland. <b>Country code:</b> PL. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="cscc" class="accordion">CSCC <a href="/text/collections#cscc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>CSIRO Starter Culture Collection, CSIRO Division of Foodscience, Graham Road, Highett. Vic. 3190, Australia. <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="csir" class="accordion">CSIR <a href="/text/collections#csir" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Council for Scientific and Industrial Research, Pretoria, South Africa. <b>Country code:</b> ZA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="csma" class="accordion">CSMA <a href="/text/collections#csma" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centro di Studio dei Microorganismi Autotrofi - CNR, Instituto di Microbiologia Agraria e Tecnica Universita degli Studi - P.zale Cascine, 27, Firenze 50144, Italy. <b>Country code:</b> IT. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/147" class="">147</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="csur" class="accordion">CSUR <a href="/text/collections#csur" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.mediterranee-infection.com/diagnostic/les-centres-nationaux-de-reference-cnr/cnr-rickettsioses/collection-de-souches/" class="">Collection de Souches de l'Unité des Rickettsies, Unité des Rickettsies, CNRS UMR6020, 27 Bd Jean Moulin, 13385 Marseille, France.</a> <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/875" class="">875</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 404.</p>
</div>
<button id="cub" class="accordion">CUB <a href="/text/collections#cub" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Actinomycete Culture Collection, University of Bradford, Richmon Rd., Bradford, Yorkshire BD7 1DP, U.K. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="cuetm" class="accordion">CUETM <a href="/text/collections#cuetm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection de l'Unité d'Écotoxicologie Microbienne, Institut National de la Recherche Agronomique (INRA), 369 rue Jules Guesde, B.P. 39, 59651 Villeneuve d'Ascq cedex, France. <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 7.</p>
</div>
<button id="cvcc" class="accordion">CVCC <a href="/text/collections#cvcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>China Veterinary Culture Collection Center, National Control Institute of Veterinary Bio-products and Pharmaceutical (NCIVBP), Ministry of Agriculture, Beijing, China. <b>Country code:</b> CN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/876" class="">876</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cvcm" class="accordion">CVCM <a href="/text/collections#cvcm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centro Venezolano de Colecciones de Microorganismos, Instituto de Biologia Experimental, Universidad Central de Venezuela, Calle Suapure, Colinas de Bello Monte, Caracas, DC, 1041-A, Venezuela. <b>Country code:</b> VE. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/815" class="">815</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="cy" class="accordion">CY <a href="/text/collections#cy" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centre des Yersinia, Institut Pasteur, 25 Rue du Docteur Roux, Paris, 75724 Cedex 15, France. <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/7" class="">7</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 9.</p>
</div>
<button id="dact" class="accordion">DACT <a href="/text/collections#dact" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Dept. Agricult. Chem. Technol., Technical University of Budapest, Gellert ter 4, 1111 Budapest XI., Hungary. <b>Country code:</b> HU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/496" class="">496</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="daom" class="accordion">DAOM <a href="/text/collections#daom" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Mycological Herbarium, Plant Research Institute, Department of Agriculture Ottawa, Canada. See: <a href="/text/collections#ccfcdaom" class="">CCFC/DAOM.</a> <b>Country code:</b> CA. <b>Index Herbariorum:</b> <a href="http://sweetgum.nybg.org/science/ih/herbarium-details/?irn=123915" class="">123915</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="dapp-pg" class="accordion">DAPP-PG <a href="/text/collections#dapp-pg" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Dipartimento di Arboricoltura e Protezione delle Piante, Università di Perugia, Borgo XX Giugno, 74, 06121 Perugia, Italy. <b>Country code:</b> IT. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="dar" class="accordion">DAR <a href="/text/collections#dar" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Plant Pathology Herbarium, Orange Agricultural Institute, Forest Road, Orange. NSW 2800, Australia. <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/365" class="">365</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="dbm" class="accordion">DBM <a href="/text/collections#dbm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Yeasts and Industrial Microorganisms, Institute of Chemical Technology, Department of Biochemistry and Microbiology, Technická 5, 166 28 Praha 6, Czech Republic. <b>Country code:</b> CZ. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/654" class="">654</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="dbs" class="accordion">DBS <a href="/text/collections#dbs" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://dictybase.org/StockCenter/StockCenter.html" class="">Department of Biological Culture Collection, National University of Singapore, Kent Ridge Road 119260, Singapore.</a> <b>Country code:</b> SG. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/510" class="">510</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="dbua" class="accordion">DBUA <a href="/text/collections#dbua" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Biology, Section of Ecology and Systematics, University of Athens, Panepistimiopolis, G-15784, Athens, Greece. <b>Country code:</b> GR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="dbum" class="accordion">DBUM <a href="/text/collections#dbum" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Biochemistry, Faculty of Medicine, University of Malaya, U50603 Kuala Lumpur, Malaysia. <b>Country code:</b> MY. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/765" class="">765</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="dbvpg" class="accordion">DBVPG <a href="/text/collections#dbvpg" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collezione del Lieviti Industriali, Dipartimento di Biologia Vegetale, Universita degli Studi di Perugia, Borgno XX Giugno, 74, I-06121, Perugia. <b>Country code:</b> PE. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/180" class="">180</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="dcc" class="accordion">DCC <a href="/text/collections#dcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Dairy Culture Collection, Faculty of Biotechnology, Agricultural College of Athens, Iera Odos 75, G- 11855, Otanikos Athens, Greece. <b>Country code:</b> GR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="de-csiro" class="accordion">DE-CSIRO <a href="/text/collections#de-csiro" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>CSIRO Insect Pathogen Collection, CSIRO Division of Entomology, PO Box 1700, Canberra. ACT 2601, Australia. <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/70" class="">70</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="dmbuk" class="accordion">DMBUK <a href="/text/collections#dmbuk" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Microbiology, University of Kelaniya, Dalugama, Kelaniya, Sri Lanka. <b>Country code:</b> LK. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/564" class="">564</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="dmccum" class="accordion">DMCCUM <a href="/text/collections#dmccum" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Microbiology Department Culture Collection, Department of Microbiology, University of Melbourne, Royal Parade, Parkville. Vic. 3052, Australia. <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="dmccus" class="accordion">DMCCUS <a href="/text/collections#dmccus" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>School of Biological Sciences Culture Collection, University of Surrey, Stag Hill, Guildford, Surrey, GU2 5XH, United Kingdom. <b>Country code:</b> GB. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/478" class="">478</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="dmkku1" class="accordion">DMKKU1 <a href="/text/collections#dmkku1" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Microbiology, Faculty of Medicine, Khon Kaen University, 123 Mitraparp, Muang, Khon Kaen, 40002, Thailand. <b>Country code:</b> TH. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/680" class="">680</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="dmku" class="accordion">DMKU <a href="/text/collections#dmku" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Microbiology, Faculty of Science. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/669" class="">669</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="dmmz" class="accordion">DMMZ <a href="/text/collections#dmmz" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Medical Microbiology, University of Zurich, CH-8028, Zurich, Switzerland. <b>Country code:</b> CH. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 9.</p>
</div>
<button id="dmpmc" class="accordion">DMPMC <a href="/text/collections#dmpmc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Microbiology, Department of Microbiology, Queen Elizabeth II Medical Centre, University of Western Australia, Nedlands. WA. 6009, Australia. <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/454" class="">454</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="dmsrde" class="accordion">DMSRDE <a href="/text/collections#dmsrde" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>DMSRDE Culture Collection, DRDO New Delhi, G.T. Road Post Box No. 320, Kanpur, Uttar Pradesh, 208 013, India. <b>Country code:</b> IN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/166" class="">166</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="dmst" class="accordion">DMST <a href="/text/collections#dmst" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://narst.dmsc.moph.go.th/Culture_Collection_HTML/Dmst_cc/index.html" class="">Department of Medical Sciences Culture Collection, National Institute of Health, Department of Medical Sciences, Tiwanond Road, Nonthaburi, 11000, Thailand.</a> <b>Country code:</b> TH. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/707" class="">707</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="dmuij" class="accordion">DMUIJ <a href="/text/collections#dmuij" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Microbiology, University of Indonesia, J1. Pegangsaan Timur 16, Jakarta Pusat, Indonesia. <b>Country code:</b> ID. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/472" class="">472</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="dmur" class="accordion">DMUR <a href="/text/collections#dmur" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Mycology, University of Recife, Brazil. <b>Country code:</b> BR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="dmvb" class="accordion">DMVB <a href="/text/collections#dmvb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Veterinary Branch of National Strain Collection, Veterinary Institute, Department of Microbiology, Al. Partyzantow 57, 24-100 Pulawy, Poland. <b>Country code:</b> PL. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/194" class="">194</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="doa" class="accordion">DOA <a href="/text/collections#doa" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.biotec.or.th/tncc/doa_dete.html" class="">Department Of Agriculture, Thailand.</a> <b>Country code:</b> TH. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="doab" class="accordion">DOAB <a href="/text/collections#doab" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department Of Agriculture Bacteria collection. Canada. As of 2021-03-04, collection website and registration with WFCC are still pending (Tambong, J., pers. comm.). <b>Country code:</b> CA. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 5.</p>
</div>
<button id="dpc" class="accordion">DPC <a href="/text/collections#dpc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Dairy Products Research Center, Teagasc, Moorepark, Fermoy, County Cork, Ireland. <b>Country code:</b> IE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="dpdu" class="accordion">DPDU <a href="/text/collections#dpdu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Instituto de difesa delle Plante, Unvinersita degli Studi di Udine, Udine, Italy. <b>Country code:</b> IT. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="dpiwe-fhu" class="accordion">DPIWE-FHU <a href="/text/collections#dpiwe-fhu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Fish Disease Culture Collection, Fish Health Unit, Department of Primary Industries Water Environment, 165 Westbury Road, Launceston, Tasmania, 7250, Australia. <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="dpua" class="accordion">DPUA <a href="/text/collections#dpua" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Departamento de Patologia/ICB, Universidade do Amazonas, Campus Universitario, Estrada do Contorno, S/N, 69.000 Manaus, Amazonas, Brazil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/715" class="">715</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="drl" class="accordion">DRL <a href="/text/collections#drl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Diagnostical and Research Laboratory, Budapest, Hungary. <b>Country code:</b> HU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="dsir" class="accordion">DSIR <a href="/text/collections#dsir" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Scientific and Industrial Research, Mount Albert Research Centre, Auckland, New Zealand. <b>Country code:</b> NZ. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="dsm" class="accordion">DSM <a href="/text/collections#dsm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.dsmz.de/catalogues/catalogue-microorganisms.html" class="">Acronym used by DSMZ - Deutsche Sammlung von Mikroorganismen und Zellkulturen GmbH, Inhoffenstrasse 7B, D-38124 Braunschweig, Germany.</a> <b>Country code:</b> DE. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/274" class="">274</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 12696.</p>
</div>
<button id="dsmz" class="accordion">DSMZ <a href="/text/collections#dsmz" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#dsm" class="">DSM.</a> <b>Country code:</b> DE. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ecacc" class="accordion">ECACC <a href="/text/collections#ecacc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.phe-culturecollections.org.uk/collections/ecacc.aspx" class="">European Collection of Authenticated Cell Cultures, Public Heatlh England, Porton Down, Salisbury, Wiltshire, SP4 OJG.</a> <b>Country code:</b> GB. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/137" class="">137</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ecco" class="accordion">ECCO <a href="/text/collections#ecco" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.eccosite.org/" class="">European Culture Collections’ Organization.</a> <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ecor" class="accordion">ECOR <a href="/text/collections#ecor" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Escherichia coli Reference Collection, Microbial Evolution Laboratory, 165 Food Safety and Toxicology Building, Michigan State University, East Lansing, MI 48824, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="egi" class="accordion">EGI <a href="/text/collections#egi" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://english.egi.cas.cn/au/" class="">Xinjiang Institute of Ecology and Geography, Chinese Academy of Sciences, Ürümqi 830011, People’s Republic of China.</a> <b>Country code:</b> CN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 26.</p>
</div>
<button id="emcc" class="accordion">EMCC <a href="/text/collections#emcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Egypt Microbial Culture Collection, Cairo Microbiological Resources Centre (Cairo MIRCEN), Ain Shams University, Faculty of Agriculture, P.O.Box 68, Shoubra Garden, Cairo, 11241, Egypt. <b>Country code:</b> EG. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/583" class="">583</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="encb-ipn" class="accordion">ENCB-IPN <a href="/text/collections#encb-ipn" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Coleccion de cultivos de la Escuela Nacional de Ciencias Biologicas, Escuela Nacional de Ciencias Biologicas. I.P.N., Carpio y Plan de Ayala s/n, Mexico D.F., Mexico, 11340, Mexico. <b>Country code:</b> MX. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/449" class="">449</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="esap" class="accordion">ESAP <a href="/text/collections#esap" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Instituto Zimotecnico-Z, Escola Superior de Agricultura Luiz de Queiroz-ESALQ-USP, Departamento de Ciencia e Tecnologia Agroindustrial, Av. Padua Dias, 11, 09, Piracicaba, SP, 13418-900, Brazil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/294" class="">294</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="eth" class="accordion">ETH <a href="/text/collections#eth" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Kultursammlungen der Eidgenössischen Technischen Hochschule (ETH), Zürich, Switzerland. <b>Country code:</b> CH. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 4.</p>
</div>
<button id="ethz" class="accordion">ETHZ <a href="/text/collections#ethz" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Eidgenössische Technische Hochschule-Zentrum, Mikrobiologisches Institut, Zürich, Switzerland. <b>Country code:</b> CH. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ex" class="accordion">EX <a href="/text/collections#ex" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Microbiological culture collection, University of Ljubljana, Biotechnical Faculty, Department of Biology, Vecna pot 111, SI-1000 Ljubljana, Slovenia. <b>Country code:</b> SI. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1028" class="">1028</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="fat" class="accordion">FAT <a href="/text/collections#fat" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Faculty of Agriculture, University of Tokyo, Tokyo, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="fbabc" class="accordion">FBABC <a href="/text/collections#fbabc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Freshwater Biological Association Bacterial Collection, Ferry House, Far Sawrey, Ambleside, Cumbria LA 22 0LP, United Kingdom. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="fbgmu" class="accordion">FBGMU <a href="/text/collections#fbgmu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Faculty of Biology, Gadjah Mada University, J1.Teknika Selatan, Yogyakarta, Indonesia. <b>Country code:</b> ID. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/629" class="">629</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="fccm" class="accordion">FCCM <a href="/text/collections#fccm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.natur.cuni.cz/fccm/" class="">Federation of Czechoslovak Collections of Microorganisms.</a> <b>Country code:</b> CZ. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="fda" class="accordion">FDA <a href="/text/collections#fda" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>US Food and Drug Administration, Washington, D.C., USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="fdc" class="accordion">FDC <a href="/text/collections#fdc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Forsyth Dental Center, Boston, Massachussetts 02115, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 4.</p>
</div>
<button id="ferm" class="accordion">FERM <a href="/text/collections#ferm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Patent Microorganism Depository, National Institute of Bioscience and Human-Technology (NIBHT) (formerly the Fermentation Research Institute (FRI), Agency of Industrial Science and Industry, Tsukuba-shi, Ibaraki, 305 Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 25.</p>
</div>
<button id="fgsc" class="accordion">FGSC <a href="/text/collections#fgsc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.fgsc.net/index.html" class="">Fungal Genetics Stock Center, Department of Plant Pathology, Kansas State University.</a> <b>Country code:</b> US. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/115" class="">115</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="firdi" class="accordion">FIRDI <a href="/text/collections#firdi" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Food Industry Research and Development Institute, HsinChu, 30052, Taiwan, ROC. <b>Country code:</b> TW. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 4.</p>
</div>
<button id="fjat" class="accordion">FJAT <a href="/text/collections#fjat" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Fujian Academy of Agriculture Sciences, Fuzhou, 350003, China. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="flrm" class="accordion">FLRM <a href="/text/collections#flrm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Farmitalia Laboratori Ricerche Microbiologia, Milan, Italy. <b>Country code:</b> IT. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="fmj" class="accordion">FMJ <a href="/text/collections#fmj" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Faculty of Medicine, Juntendo University, Tokyo, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="fmr" class="accordion">FMR <a href="/text/collections#fmr" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Facultad de Medicina, Reus, Tarragona, Spain. <b>Country code:</b> ES. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="fncc" class="accordion">FNCC <a href="/text/collections#fncc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Food and Nutrition Culture Collection, Gadjah Mada University, Jl. Teknika Utara, Yogyakarta 55281, Indonesia. <b>Country code:</b> ID. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/755" class="">755</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="fpc" class="accordion">FPC <a href="/text/collections#fpc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Fish Pathogen Collection, University of Tokyo, Tokyo, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="fri" class="accordion">FRI <a href="/text/collections#fri" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Food Research Institute, Ministry of Agriculture, Forestry and Fisheries, Tsukuba, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="frr" class="accordion">FRR <a href="/text/collections#frr" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>CSIRO Division of Food Research, CSIRO Food science, PO Box 52, North Ryde. NSW. 2113, Australia. <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/18" class="">18</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ftcc" class="accordion">FTCC <a href="/text/collections#ftcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Food Technology Culture Collection, Malaysian Agricultural Research and Development Institute, Food Technology Centre, MARDI, GPO Box 12301, Kuala Lumpur, 50774, Malaysia. <b>Country code:</b> MY. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/762" class="">762</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ftk" class="accordion">FTK <a href="/text/collections#ftk" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Forintek Culture Collection of Wood-Inhabiting Fungi, Ottawa, Ontario, Canada. <b>Country code:</b> CA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="gab" class="accordion">GAB <a href="/text/collections#gab" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Greek Aquaculture Bacteria, Laboratory of Ichthyology, Veterinary Medicine, Aristotele University of Thessaloniki and Laboratory of Ichthyopathology, Faculty of Veterinary Medicine, University of Thessaly - Institute of Aquaculture of the Hellenic Center for Marine Research Athen, AUTH campus, PO BOX 395, Thessaloniki 52124, Greece (Hellenic Rep.). <b>Country code:</b> GR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/908" class="">908</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="gam" class="accordion">GAM <a href="/text/collections#gam" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Grupo Actinomicetales Merida Facultad de Medicina, Universidad de Los Andes, P.O. Box 164Merida, 5101A, Venezuela. <b>Country code:</b> VE. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/283" class="">283</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="gbs" class="accordion">GBS <a href="/text/collections#gbs" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Ginseng Genetic Resource Bank, Kyung Hee University, Yongin, Republic of Korea. <b>Country code:</b> KR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="gcc" class="accordion">GCC <a href="/text/collections#gcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Global Collection of Cyanobacteria, Varanasi, VARANASI, Uttar Pradesh, 221005. <b>Country code:</b> IN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1165" class="">1165</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 6.</p>
</div>
<button id="gcl" class="accordion">GCL <a href="/text/collections#gcl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Central Laboratories, Ministry of Health Jerusalem, Jaffa Street 86, Jerusalem, Israel. <b>Country code:</b> IL. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/295" class="">295</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 4.</p>
</div>
<button id="gcmcc" class="accordion">GCMCC <a href="/text/collections#gcmcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#cgmcc" class="">CGMCC.</a> <b>Country code:</b> CN. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="gcmr" class="accordion">GCMR <a href="/text/collections#gcmr" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www1.gifu-u.ac.jp/~g_cmr/index.html" class="">Gifu University Center for Conservation of Microbial Genetic Resource (GCMR), Gifu University, 1-1 Yanagido, Gifu city, Gifu, 5011194, Japan.</a> <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/305" class="">305</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="gdmcc" class="accordion">GDMCC <a href="/text/collections#gdmcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.gimcc.net/" class="">Guangdong Culture Collection Centre of Microbiology, Guangdong Institute of Microbiology, No. 59, Building No. 100, Xianliezhong Road, Guangzhou, 510075, PR China.</a> <b>Country code:</b> CN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/953" class="">953</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 201.</p>
</div>
<button id="giem" class="accordion">GIEM <a href="/text/collections#giem" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Gamaleya Institute of Epidemiology and Microbiology, Academy of Medical Sciences, Moscow, Russia. <b>Country code:</b> RU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="gifu" class="accordion">GIFU <a href="/text/collections#gifu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#gcmr" class="">GCMR.</a> <b>Country code:</b> JP. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 19.</p>
</div>
<button id="gimcc" class="accordion">GIMCC <a href="/text/collections#gimcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#gdmcc" class="">GDMCC.</a> <b>Country code:</b> CN. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="gsf" class="accordion">GSF <a href="/text/collections#gsf" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Research Centre for Environment and Health, Institute of Soil Ecology, D-85764 Neuherberg, Germany. <b>Country code:</b> DE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="gsoil" class="accordion">Gsoil <a href="/text/collections#gsoil" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Acronym used by Wan-Taek Im, Department of Biotechnology, Hankyong National University, Anseong, 17579, Republic of Korea, for strains isolated from Ginseng cultivating soil. <b>Country code:</b> KR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 74.</p>
</div>
<button id="gtc" class="accordion">GTC <a href="/text/collections#gtc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#gcmr" class="">GCMR.</a> <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/901" class="">901</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 24.</p>
</div>
<button id="gtc-gifu" class="accordion">GTC-GIFU <a href="/text/collections#gtc-gifu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Gifu Type Culture Collection (GTC), Gifu University Culture Collection (GIFU), Department of Microbiology, Gifu University School of Medicine, 40 Tsukasa-Machi, Gifu 500-8705, Japan. See: <a href="/text/collections#gcmr" class="">GCMR.</a> <b>Country code:</b> JP. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="hac" class="accordion">HAC <a href="/text/collections#hac" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Faculty of Agriculture, Kobe University, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="hacc" class="accordion">HACC <a href="/text/collections#hacc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Research Laboratories, Hindustan Antibiotics Ltd., India. <b>Country code:</b> IN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="ham" class="accordion">HAM <a href="/text/collections#ham" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institut für Allgemeine Mikrobiologie, Christian-Albrechts-Universität, Kiel, Germany. <b>Country code:</b> DE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="hambi" class="accordion">HAMBI <a href="/text/collections#hambi" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://kotka.luomus.fi/culture/bac" class="">Culture Collection of the Department of Microbiology, Faculty of Agriculture and Forestry, University of Helsinki, Helsinki, Finland.</a> <b>Country code:</b> FI. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/779" class="">779</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 413.</p>
</div>
<button id="hau" class="accordion">HAU <a href="/text/collections#hau" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Huazhong Agricultural University, Wuhan, People's Republic of China. <b>Country code:</b> CN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="hcc" class="accordion">HCC <a href="/text/collections#hcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Hawaii Culture Collection, Marine Bioproducts Engineering Center (MarBEC), University of Hawaii, 2525 Correa Road, HIG 131, Honolulu, HI 96822-2219, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="hdp" class="accordion">HDP <a href="/text/collections#hdp" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centre National de Référence des Streptocoques, Service de Microbiologie, Hôtel-Dieu Paris (HDP), Université Paris VI, 1 place du Parvis Notre-Dame, F-75181 Paris 04, France. <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 4.</p>
</div>
<button id="hki" class="accordion">HKI <a href="/text/collections#hki" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Hans-Knöll-Institut für Naturstoff-Forschung e.V., D-07745 Jena, Germany. <b>Country code:</b> DE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 29.</p>
</div>
<button id="hkucc" class="accordion">HKUCC <a href="/text/collections#hkucc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>The University of Hong Kong Culture Collection, Dept. of Ecology and Biodiversity, University of Hong Kong, Pokfulam Road, China. <b>Country code:</b> HK. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/798" class="">798</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="hmgb" class="accordion">HMGB <a href="/text/collections#hmgb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Hungarian Microbiology Gene Bank, Microbiological Department, Group of the Department of Food Technology and Microbiology of the University of Horticulture, 1064 Budapest, Izabella, Hungary. See: <a href="/text/collections#ncaim" class="">NCAIM.</a> <b>Country code:</b> HU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="hncmb" class="accordion">HNCMB <a href="/text/collections#hncmb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Hungarian National Collection of Medical Bacteria, B. Johan National Center for Epidemiology, Gyali ut 2-6, H-1097 Budapest, Hungary. <b>Country code:</b> HU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/258" class="">258</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="hpktcc" class="accordion">HPKTCC <a href="/text/collections#hpktcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Helicobacter pylori Korean Type Culture Collection, Gyeongsang National University College of Medine, 90 Chiram-dong, Jiju, Gyeongsangnam-do, 660-751, Republic of Korea. <b>Country code:</b> KR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/882" class="">882</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="hscc" class="accordion">HSCC <a href="/text/collections#hscc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of the Research and Development Department, Higeta Shoyu, Co., Ltd., 2-8 Chuo-cho, Choshi, Chiba 288, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 11.</p>
</div>
<button id="hull" class="accordion">HULL <a href="/text/collections#hull" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Biochemistry, The University, Hull HU6 7RX North Humbersid, United Kingdom. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="hut" class="accordion">HUT <a href="/text/collections#hut" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://home.hiroshima-u.ac.jp/hut/" class="">Laboratory for Fermentation, Faculty of Engineering, Hiroshima University, Higashihiroshima, Japan.</a> <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/195" class="">195</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 53.</p>
</div>
<button id="iacr" class="accordion">IACR <a href="/text/collections#iacr" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Long Ashton Research Station, Integrated Approach to Crop Research, Department of Agricultural Sciences, University of Bristol, Long Ashton, Bristol BS18 9AF, United Kingdom. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="iaf" class="accordion">IAF <a href="/text/collections#iaf" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institute Armand Frappier, Centre de Recherche en Bactériologie, Quebec, Canada. <b>Country code:</b> CA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="iafb" class="accordion">IAFB <a href="/text/collections#iafb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Industrial Microorganisms, Institute of Agricultural and Food Biotechnology (IAFB), Rakowiecka 36, PL-02-532 Warsaw, Poland. <b>Country code:</b> PL. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/212" class="">212</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ial" class="accordion">IAL <a href="/text/collections#ial" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Secao de Colecao de Culturas, Instituto Adolfo Lutz, Av. Dr. Arnaldo 355, Sao Paulo 01246-902, Brazil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/282" class="">282</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="iam" class="accordion">IAM <a href="/text/collections#iam" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institute of Applied Microbiology, Culture Collection, The University of Tokyo, Yayoi, Bunko-Ku, Tokyo, Japan. (Collection transferred to JCM). See: <a href="/text/collections#jcm" class="">JCM.</a> <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/190" class="">190</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 279.</p>
</div>
<button id="iamcc" class="accordion">IAMCC <a href="/text/collections#iamcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institute of Applied Microbiology, Culture Collection, The University of Tokyo, Yayoi, Bunko-Ku, Tokyo, Japan. (Collection transferred to JCM). See: <a href="/text/collections#jcm" class="">JCM.</a> <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="iaur" class="accordion">IAUR <a href="/text/collections#iaur" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institute of Antibiotics, University of Recife, Recife, Pernambuco, Brazil. <b>Country code:</b> BR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="iaw" class="accordion">IAW <a href="/text/collections#iaw" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Research and Development Centre for Biotechnology Culture Collection, ul. Staroscinska 5, 02-516 Warszawa, Poland. <b>Country code:</b> PL. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="iba" class="accordion">IBA <a href="/text/collections#iba" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Microorganisms Producing Antibiotics, Institute of Biotechnology and Antibiotics, Staroscinska 5, PL-02-516 Warsaw, Poland. <b>Country code:</b> PL. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/780" class="">780</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ibac" class="accordion">IBAC <a href="/text/collections#ibac" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institute of Botany, Academica Sinica, Beijiing, People's Republic of China. <b>Country code:</b> CN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ibl" class="accordion">IBL <a href="/text/collections#ibl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Botanical Institute, Lisbon Faculty of Sciences, Lisbon, Portugal. <b>Country code:</b> PT. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ibphm" class="accordion">IBPhM <a href="/text/collections#ibphm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Type Culture of Microorganisms, Institute of Biochemistry and Physiology of Microorganisms, URSS Academy of Sciences, Puschino, Moscow Region, Russia. <b>Country code:</b> RU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ibppm" class="accordion">IBPPM <a href="/text/collections#ibppm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://collection.ibppm.ru/" class="">Collection of Rhizosphere Microorganisms, Institute of Biochemistry and Physiology of Plants and Microorganisms RAS, 13 prospekt Entuziastov, Saratov, Saratovskaya Oblast, 410049.</a> <b>Country code:</b> RU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1021" class="">1021</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="ibprm" class="accordion">IBPRM <a href="/text/collections#ibprm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of the Institute of Biochemistry and Physiology of Plants and Microorganisms, RAS, Prospect Entusiastov, 13Saratov, 410015, Russia. <b>Country code:</b> RU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ibrc" class="accordion">IBRC <a href="/text/collections#ibrc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://en.ibrc.ir/index.aspx?fkeyid=&amp;siteid=2&amp;pageid=378" class="">Iranian Biological Resource Center, Academic Center for Education Culture and Research (ACECR), No. 80, West Howeyzeh St., North Sohrevardi Ave., Tehran, 1551916111, Iran.</a> <b>Country code:</b> IR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/950" class="">950</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 61.</p>
</div>
<button id="ibs" class="accordion">IBS <a href="/text/collections#ibs" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institut de Bactériologie de la Faculté de Médecine, Université Louis-Pasteur, Hôpitaux Universitaires de Strasbourg, 3 rue Koeberlé, 6700 Strasbourg, France. <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 9.</p>
</div>
<button id="ibsbf" class="accordion">IBSBF <a href="/text/collections#ibsbf" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Biological Institute Culture Collection of Phytopathogenic Bacteria, Instituto Biologico, Rodovia Heitor Penteado, km 3.5, Caixa Postal 70, Campinas, Sao Paulo, 13001-970, Brazil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/110" class="">110</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 6.</p>
</div>
<button id="ibso" class="accordion">IBSO <a href="/text/collections#ibso" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#cc-ibso" class="">CC IBSO.</a> <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ibt" class="accordion">IBT <a href="/text/collections#ibt" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>IBT Culture Collection of Fungi, Mycology Group, BioCentrum-DTU, Technical University of Denmark, Lyngby, Denmark. <b>Country code:</b> DK. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/758" class="">758</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="icbb" class="accordion">ICBB <a href="/text/collections#icbb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Indonesian Center for Biodiversity and Biotechnology, ICBB Culture Collection for Microorganisms and Cell Culture, Taman Yasmin Sektor VI No. 150, Bogor, West Java, 16006, Indonesia. <b>Country code:</b> ID. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/842" class="">842</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="iccf" class="accordion">ICCF <a href="/text/collections#iccf" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Industrial Microorganisms, National Institute for Chemical Pharmaceutical Research and Development (ICCF), 112 Soseaua Vitan, Bucharest, sector 3, 74373, Romania. <b>Country code:</b> RO. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/232" class="">232</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ici" class="accordion">ICI <a href="/text/collections#ici" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Imperial Chemical Industries Ltd., Welwyn, Hertfordshire, UK. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="icmp" class="accordion">ICMP <a href="/text/collections#icmp" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.landcareresearch.co.nz/resources/collections/icmp" class="">Culture Collection of Plant Diseases Division, New Zealand Department of Scientific and Industrial Research, Landcare Research, Private Bag 92170, Auckland, New Zealand.</a> <b>Country code:</b> NZ. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/589" class="">589</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 190.</p>
</div>
<button id="icpb" class="accordion">ICPB <a href="/text/collections#icpb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.ars.usda.gov/northeast-area/frederick-md/foreign-disease-weed-science-research/" class="">International Collection of Phytopathogenic Bacteria, USDA, Ft. Detrick, MD, USA.</a> <b>Country code:</b> US. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 23.</p>
</div>
<button id="iebc" class="accordion">IEBC <a href="/text/collections#iebc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>International Entomopathogenic Bacillus Centre (WHO), Institut Pasteur, 25 rue du Dr Roux, Paris 75015, France. <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/590" class="">590</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="iegm" class="accordion">IEGM <a href="/text/collections#iegm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.iegm.ru/iegmcol/index.html" class="">Regional Specialized Alkanotrophic Microorganism Collection of the Institute of Ecology and Genetics of Microorganisms, Ural Branch RAS. Goleva Str., 13, Perm, 614081, Russia.</a> <b>Country code:</b> RU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/768" class="">768</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 17.</p>
</div>
<button id="iekc" class="accordion">IEKC <a href="/text/collections#iekc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>The International Escherichia and Klebsiella Centre (WHO), Statens Serum Institut, 5 Artillerivej, Copenhagen 2300 S, Denmark. <b>Country code:</b> DK. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="iem" class="accordion">IEM <a href="/text/collections#iem" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Czech National Collection of Type Cultures, Institute of Hygiene and Epidemiology, Prague, Czech. <b>Country code:</b> CZ. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ifam" class="accordion">IFAM <a href="/text/collections#ifam" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institut für Allgemeine Mikrobiologie, Universität Kiel, Am Botauischen Garten 1-9, Kiel, D-24118, Germany. <b>Country code:</b> DE. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/145" class="">145</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 27.</p>
</div>
<button id="ifbm" class="accordion">IFBM <a href="/text/collections#ifbm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Streptokokken Sammlung, Institut fur Hygiene an der Bundesanstalt fur Milchforschung, Hermann Weigmann Strasse 1, D-2300 Kiel, Germany. <b>Country code:</b> DE. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/253" class="">253</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ifm" class="accordion">IFM <a href="/text/collections#ifm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.pf.chiba-u.ac.jp/kanrishitsu/eindex.html" class="">Research Center for Pathogenic Fungi and Microbial Toxicoses, Chiba University, Chiba, Chiba 260-8673, Japan.</a> <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/60" class="">60</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 81.</p>
</div>
<button id="ifo" class="accordion">IFO <a href="/text/collections#ifo" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institute for Fermentation, Culture Collection of Microorganizms, 17-85, Juso-honmachi, 2-chome, Yodogawa-ku, Osaka 532-8686, Japan. From July 01, 2002, all cultures preserved in the IFO have been transferred to the NBRC. NBRC number corresponds to the same IFO number (e.g. NBRC 12345 = IFO 12345). See: <a href="/text/collections#nbrc" class="">NBRC.</a> <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/191" class="">191</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 1447.</p>
</div>
<button id="igc" class="accordion">IGC <a href="/text/collections#igc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Center of Biology, Gulbenkian Institute of Science, Oeiras, Portugal. <b>Country code:</b> PT. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="igesalq" class="accordion">IGESALQ <a href="/text/collections#igesalq" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Colecao Microorganismos, Departmento de Genetica Escola Superior de Agricultura Luiz de Queiroz, Av.Padua Dias 11-P.O.Box 83, Piracicaba, Sao Paulo, 13400-970, Brazil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/902" class="">902</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ihem" class="accordion">IHEM <a href="/text/collections#ihem" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://bccm.belspo.be/about-us/bccm-ihem" class="">Institute of Hygiene and Epidemiology, Mycology Laboratory, Brussels, Belgium.</a> <b>Country code:</b> BE. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/642" class="">642</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="iibm-unam" class="accordion">IIBM-UNAM <a href="/text/collections#iibm-unam" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Industrial Culture Collection, Instituto de Investigaciones Biomedicas, Universidad Nacional Autónoma de México, 04510, México DF, Mexico. <b>Country code:</b> MX. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/48" class="">48</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="iid" class="accordion">IID <a href="/text/collections#iid" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Laboratory Culture Collection, Institute of Medical Science, University of Tokyo, Tokyo, Japan. <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/208" class="">208</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ijfm" class="accordion">IJFM <a href="/text/collections#ijfm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Instituto Jaime Ferrán de Microbiología Consejo Superior de Investigaciones Científicas, Madrid, Spain. <b>Country code:</b> ES. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="imac" class="accordion">IMAC <a href="/text/collections#imac" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institute of Microbiology, Academica Sinica, Beijiing, People's Republic of China. <b>Country code:</b> CN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="imas" class="accordion">IMAS <a href="/text/collections#imas" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Museum of Cultures, Institute of Microbiology, Academy of Sciences, Beijing, PR China. <b>Country code:</b> CN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="imcc" class="accordion">IMCC <a href="/text/collections#imcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Inha Microbe Culture Collection, Inha University, Incheon 402-751, Republic of Korea. <b>Country code:</b> KR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 66.</p>
</div>
<button id="imd" class="accordion">IMD <a href="/text/collections#imd" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Industrial Microbiology Dublin, Dept. of Industrial Microbiology, University College, Stillorgan Road, Dublin 4, Ireland. <b>Country code:</b> IE. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/227" class="">227</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="imet" class="accordion">IMET <a href="/text/collections#imet" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institute for Microbiology and Experimental Therapy (Zentralinstitut für Mikrobiologie und Experimentelle Therapie), Beutenbergstrasse 11, Jena 69, Germany. <b>Country code:</b> DE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 177.</p>
</div>
<button id="img" class="accordion">IMG <a href="/text/collections#img" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institut für Mikrobiologie, Universität Göttingen, Germany. <b>Country code:</b> DE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="imi" class="accordion">IMI <a href="/text/collections#imi" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#cabi-grc" class="">CABI-GRC.</a> <b>Country code:</b> GB. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="immib" class="accordion">IMMIB <a href="/text/collections#immib" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of the Institute of Medical Microbiology and Immunology of the University of Bonn, Sigmund-Freud Str. 25, D-53127 Bonn, Germany. <b>Country code:</b> DE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 40.</p>
</div>
<button id="imru" class="accordion">IMRU <a href="/text/collections#imru" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institute of Microbiology, Rutgers, The State University of New Jersey, New Brunswick, New Jersey 08903, USA. <b>Country code:</b> JE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 13.</p>
</div>
<button id="imsnu" class="accordion">IMSNU <a href="/text/collections#imsnu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institute of Microbiology, Seoul National University, Seoul 151-742, Republic of Korea. <b>Country code:</b> KR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 89.</p>
</div>
<button id="imur" class="accordion">IMUR <a href="/text/collections#imur" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institute of Mycology, University of Recife, Recife, Brazil. <b>Country code:</b> BR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="imv" class="accordion">IMV <a href="/text/collections#imv" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#ucm" class="">UCM.</a> <b>Country code:</b> UA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="imvs" class="accordion">IMVS <a href="/text/collections#imvs" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.adelaide.edu.au/directory/building/19469.html#" class="">Clinical Microbiology Culture Collection, Institute of Medical and Veterinary Science, PO Box 14, Rundle Mall, Adelaide. SA 5000, Australia.</a> <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/471" class="">471</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="imyza" class="accordion">IMYZA <a href="/text/collections#imyza" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Instituto de Microbiologia y Zoologia Agricola, Instituto Nacional de Tecnologia Agropecuaria, C.C.25 (1712), Castelar, Buenos Aires, Argentina. <b>Country code:</b> AR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/31" class="">31</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ina" class="accordion">INA <a href="/text/collections#ina" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institute for New Antibiotics, Bolshaya Pirogovskaya II, Moscow 119867, Russia. <b>Country code:</b> RU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 108.</p>
</div>
<button id="inacc" class="accordion">InaCC <a href="/text/collections#inacc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://inacc.biologi.lipi.go.id/" class="">Indonesian Culture Collection, a national depository for microorganisms (Culture Collection of Microorganism), under the management of Microbiology Division, Research Center for Biology, the Indonesian Institute of Sciences.</a> <b>Country code:</b> ID. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/769" class="">769</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 18.</p>
</div>
<button id="incqs" class="accordion">INCQS <a href="/text/collections#incqs" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Fundacao Oswaldo Cruz-FIOCRUZ, Instituto Nacional de Controle de Qualidade em Saude-INCQS, Av. Brasil, 4365-Manguinhos, Rio de Janeiro, RJ, 21045-900, Brazil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/575" class="">575</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="indre" class="accordion">INDRE <a href="/text/collections#indre" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Pathogen Fungi and Actinomycetes Collection, Instituto Nacional de Diagnostico y Referencia Epidemiologica S. S., Carpio No. 470. Santo Tomas. M, Mexico, D.F., 700009, Mexico. <b>Country code:</b> MX. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/121" class="">121</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="inifat" class="accordion">INIFAT <a href="/text/collections#inifat" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>INIFAT Fungus Collection, Ministerio de Agricultura, Habana. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/853" class="">853</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="inmi" class="accordion">INMI <a href="/text/collections#inmi" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of the Institute for Microbiology, USSR Academy of Sciences, 7 Bldg 2, Prospekt 60-letiya Oktiyabriya, Moscow GSP-7, 117811, Russia. <b>Country code:</b> RU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 38.</p>
</div>
<button id="inpa" class="accordion">INPA <a href="/text/collections#inpa" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Institute of Amazonia Research, Manaus, Brazil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/719" class="">719</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="inra" class="accordion">INRA <a href="/text/collections#inra" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Microbiologie des Sols, ACRONYM, 17 Rue Sully, B.V. 1540, Dijon Cedex.21034, France. <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/368" class="">368</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ioc" class="accordion">IOC <a href="/text/collections#ioc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institute of Oil Crops, Chinese Academy of Agricultural Sciences, Beijiing, People's Republic of China. <b>Country code:</b> CN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/720" class="">720</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ioeb" class="accordion">IOEB <a href="/text/collections#ioeb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institut d'Oenologie de Bordeaux, Faculté d'Oenologie Université de Bordeaux 2, 351 Cours de la Liberation, 33405 Talence, France. <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/791" class="">791</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="iomcc" class="accordion">IOMCC <a href="/text/collections#iomcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>International Organization for Mycoplasmatology Culture Collection, Purdue University, West Lafayette, IN, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ip" class="accordion">IP <a href="/text/collections#ip" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Insect Pathology, Institute of Entomology, České Budĕjovice, Czech Republic. <b>Country code:</b> CZ. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 13.</p>
</div>
<button id="ipdh" class="accordion">IPDH <a href="/text/collections#ipdh" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institue for Poultry Disease, The School of Veterinary Medicine, D-3000 Hannover, Germany. <b>Country code:</b> DE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="ipf" class="accordion">IPF <a href="/text/collections#ipf" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Industrial Microorganisms, Institute of Fermentation Industry, ul. Rakowiecka 36, 02-532 Warszawa, Poland. <b>Country code:</b> PL. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ipod" class="accordion">IPOD <a href="/text/collections#ipod" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>International Patent Organism Depositary, National Institute of Advanced Industrial Science and Technology, AIST Tsukuba Central 6, 1-1-1 Higashi, Tsukuba, Ibaraki, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ippas" class="accordion">IPPAS <a href="/text/collections#ippas" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Microalgae of the Institute of Plant Physiology, Russian Academy of Sciences, Botanicheskaya 35, Moscow 127276, Russia. <b>Country code:</b> RU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/596" class="">596</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ipr" class="accordion">IPR <a href="/text/collections#ipr" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of the Institute of Plant Physiology, RAS, Botanicheskaja St. 35, Moscow, 127276, Russia. <b>Country code:</b> RU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="ipt" class="accordion">IPT <a href="/text/collections#ipt" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Instituto de Pesquisas Tecnológicas do Estado de São Paulo, Av. Professor Almeida Prado, 532, CEP 05508-901, São Paulo, SP, Brazil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/721" class="">721</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="ipv" class="accordion">IPV <a href="/text/collections#ipv" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Instituto di Patologia Vegetale, Milano, Italia. <b>Country code:</b> IT. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 12.</p>
</div>
<button id="isc" class="accordion">ISC <a href="/text/collections#isc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>International Salmonella Centre (W.H.O.), Institut Pasteur, 28 Rue du Docteur Roux, Paris 75724 Cedex 15, France. <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/63" class="">63</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="isp" class="accordion">ISP <a href="/text/collections#isp" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>International Streptomyces Project, Ohio Wesleyan University, Delaware, Ohio, 43015, USA (Terminated). <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 89.</p>
</div>
<button id="ispb" class="accordion">ISPB <a href="/text/collections#ispb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institut des Sciences Pharmaceutiques et Biologiques, Laboratoire de Microbiologie, 8 avenue Rockefeller, 69373 Lyon cedex 08, France. <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="isri" class="accordion">ISRI <a href="/text/collections#isri" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Indonesian Sugar Research Institute (Pusat Penelitian Perkebunan Gula Indonesia), Jl. Pahlawan 25, Pasuruan 67126, Indonesia. <b>Country code:</b> ID. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/630" class="">630</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="iss" class="accordion">ISS <a href="/text/collections#iss" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Bacteria, Institute of Soil Science, Department of Soil Microbiology, Teodora Drajzera 7, pob 33, Belgrade, Serbia, 11000, Yugoslavia. <b>Country code:</b> RS. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/375" class="">375</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="ita" class="accordion">ITA <a href="/text/collections#ita" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Bacteriology Laboratory, Tasmanian Department of Agriculture, 165 Westbury Road, Launceston. Tas. 7250, Australia. <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="italsl" class="accordion">ITALSL <a href="/text/collections#italsl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Secao de Leite e Derivados, Instituto de Tecnologia de Alimentos, Av. Brasil, 288013073 Campinas, SP, Cx. Postal 139, Brazil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/722" class="">722</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="italsm" class="accordion">ITALSM <a href="/text/collections#italsm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Secao de Microbiologia, Instituto de Tecnologia de Alimentos, Av. Brasil, 288013073 Campinas, SP, Cx. Postal 139, Brazil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/723" class="">723</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="itbcc" class="accordion">ITBCC <a href="/text/collections#itbcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institute of Technology Bandung Culture Collection, Laboratory for Microbiology and Fermentation Technology, Jalan Ganesa 10, Bandung 40132, Indonesia. <b>Country code:</b> ID. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/44" class="">44</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="itcc" class="accordion">ITCC <a href="/text/collections#itcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Indian Type Culture Collection, Division of Mycology and Plant Pathology, Indian Agricultural Research Institute, Mycology Div, I.A.R.I., New Delhi 110012, India. <b>Country code:</b> IN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/430" class="">430</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="itd" class="accordion">ITD <a href="/text/collections#itd" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Coleccion de Cepas Microbianas, Instituto Tecnologico de Durango, Felipe Pescador 1830, Durango, Mexico. <b>Country code:</b> MX. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/99" class="">99</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="itdi" class="accordion">ITDI <a href="/text/collections#itdi" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Industrial Technology Development Institute, Gen. Santos Ave., Bicutan, Taguig, M.M., Philippines. <b>Country code:</b> PH. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/503" class="">503</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="item" class="accordion">ITEM <a href="/text/collections#item" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://server.ispa.cnr.it/ITEM/Collection/" class="">Agri-Food Toxigenic Fungi Culture Collection, Institute of Sciences of Food Production, Bari, Italy.</a> <b>Country code:</b> IT. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1120" class="">1120</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="itg" class="accordion">ITG <a href="/text/collections#itg" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institut français des fromages, 419 Route des Champs Laitiers, La Roche Sur Foron 74801, France. <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/795" class="">795</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ith" class="accordion">ITH <a href="/text/collections#ith" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>W.H.O./F.A.O. Collaborating Centre for Reference and Research on Leptospirosis, Royal Tropical Institute, Dept. of Biomedical Research, Meibergdreef 39, Amsterdam 1105 AZ Z.O, The Netherlands. <b>Country code:</b> NL. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/196" class="">196</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="itm" class="accordion">ITM <a href="/text/collections#itm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://bccm.belspo.be/catalogues/catalogue-search?collection=ITM" class="">Mycobacteria Collection, Eenheid Mycobacteriologie, Instituut voor Tropische Geneeskunde (ITG), Nationalestraat 155, B-2000, Antwerpen, Belgium.</a> <b>Country code:</b> BE. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="iung" class="accordion">IUNG <a href="/text/collections#iung" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Rhizobium Strains, Institute of Soil Sciences (IUNG), Department of Microbiology, ul. Gorskiego 7 (Osada Palacowa), 24-100 Pulawy, Poland. <b>Country code:</b> PL. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="iw" class="accordion">IW <a href="/text/collections#iw" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Veterinary Branch of National Strain Collection, Veterinary Institute, Department of Microbiology, Al. Partyzantow 57, 24-100 Pulawy, Poland. <b>Country code:</b> PL. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="iz" class="accordion">IZ <a href="/text/collections#iz" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Departamento de Tecnologia Rural, Escola Superior de Agricultura Luiz de Queiroz-USP, Av. Padua Dias, 1113400 Piracicaba, SP, Cx. Postal 9, Brazil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/724" class="">724</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="jbri" class="accordion">JBRI <a href="/text/collections#jbri" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Jeju Biodiversity Research Institute, Jeju 690-121, Republic of Korea. <b>Country code:</b> KR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 6.</p>
</div>
<button id="jcm" class="accordion">JCM <a href="/text/collections#jcm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://jcm.brc.riken.jp/en/catalogue_e" class="">Japan Collection of Microorganisms, Institute of Physical and Chemical Research (RIKEN), Wako, Saitama 351-0198, Japan.</a> <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/567" class="">567</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 7575.</p>
</div>
<button id="jct" class="accordion">JCT <a href="/text/collections#jct" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>James Cook Townsville Culture Collection, Department of Microbiology and Immunology, James Cook University, Townsville, QLD 4811, Australia. <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/387" class="">387</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="jfcc" class="accordion">JFCC <a href="/text/collections#jfcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://wdcm.nig.ac.jp/wdcm/JFCC.html" class="">Japan Federation for Culture Collections.</a> <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="jhh" class="accordion">JHH <a href="/text/collections#jhh" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>New York State Herbarium, Albany, NY, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="jscc" class="accordion">JSCC <a href="/text/collections#jscc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.nbrc.nite.go.jp/jscc/idb/search" class="">Japan Society for Culture Collections.</a> <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="jsm" class="accordion">JSM <a href="/text/collections#jsm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Acronym used by the Microbiology section of the College of Biology and Environmental Sciences, College of Chemistry and Chemical Engineering, Jishou University, 416000 Jishou, People’s Republic of China. <b>Country code:</b> CN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 28.</p>
</div>
<button id="kacc" class="accordion">KACC <a href="/text/collections#kacc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://genebank.rda.go.kr/eng/mic/cat/MicrobeSearchView.do#LINK" class="">Korean Agricultural Culture Collection (KACC), National Institute of Agricultural Science and Technology (NIAST), 249 Seodundong Kweonseonku, Suwon, Republic of Korea.</a> <b>Country code:</b> KR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/806" class="">806</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1229.</p>
</div>
<button id="kbs" class="accordion">KBS <a href="/text/collections#kbs" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>W.K. Kellogg Biological Station, Hickory Corners, Michigan, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="kcc" class="accordion">KCC <a href="/text/collections#kcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of Actinomycetes, Kaken Chemical Company Ltd., 6-42 Jujodai-1-Chome, Tokyo 114, Japan. (Collection transferred to JCM). See: <a href="/text/collections#jcm" class="">JCM.</a> <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 42.</p>
</div>
<button id="kccm" class="accordion">KCCM <a href="/text/collections#kccm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.kccm.or.kr/" class="">Korean Culture Center of Microorganisms, Yurim Bild., 361-221, Hongje-dong, Sodaemoon-ku, Seoul 120-091, Republic of Korea.</a> <b>Country code:</b> KR. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 230.</p>
</div>
<button id="kcom" class="accordion">KCOM <a href="/text/collections#kcom" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Korean Collection for Oral Microbiology, Department of Oral Biochemistry, School of Dentistry, Chosun University, Guwangju, Republic of Korea. <b>Country code:</b> KR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1178" class="">1178</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 9.</p>
</div>
<button id="kctc" class="accordion">KCTC <a href="/text/collections#kctc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://kctc.kribb.re.kr/En/Kctc" class="">Korean Collection for Type Cultures, Korea Research Institute of Bioscience and Biotechnology, Yusong, Taejon 305-600, Republic of Korea.</a> <b>Country code:</b> KR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/597" class="">597</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 4654.</p>
</div>
<button id="kemb" class="accordion">KEMB <a href="/text/collections#kemb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://kemb.or.kr/" class="">Korea Environmental Microorganisms Bank, Republic of Korea.</a> <b>Country code:</b> KR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/889" class="">889</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 138.</p>
</div>
<button id="kemc" class="accordion">KEMC <a href="/text/collections#kemc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://kemb.or.kr/eng_index.php" class="">Korea Environmental Microorganism Center, Kyonggi University, 94-6 Yiui-dong, Yeongtong-gu, Suwon, 443-760, Republic of Korea.</a> <b>Country code:</b> KR. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 24.</p>
</div>
<button id="kemh" class="accordion">KEMH <a href="/text/collections#kemh" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>KEMH/PMH Culture Collection, King Edward Memorial Hospital/PMH for Children, Thomas Street, Subiaco. WA. 6008, Australia. <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/11" class="">11</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="kfcc" class="accordion">KFCC <a href="/text/collections#kfcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Korean Federation of Culture Collections, Shinchondong Sodaemunku, Seoul 120-749, Republic of Korea. <b>Country code:</b> KR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/585" class="">585</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="kit" class="accordion">KIT <a href="/text/collections#kit" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.kit.nl/" class="">Laboratorium voor Tropische Hygiene, Koninklijk Instituut voor de Tropen, Meibergdreef 39, 1105 AZ Amsterdam, The Netherlands.</a> <b>Country code:</b> NL. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 46.</p>
</div>
<button id="klmb" class="accordion">KLMB <a href="/text/collections#klmb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>The Key Laboratory of Microbial Diversity in Southwest China, Ministry of Education and Laboratory for Conservation and Utilization of Bio-resources, Yunnan Institute of Microbiology, Yunnan University, Kunming, Yunnan, 650091, PR China. <b>Country code:</b> CN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="kmm" class="accordion">KMM <a href="/text/collections#kmm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://piboc.dvo.ru/en/" class="">Collection of Marine Microorganisms, Pacific Institute of Bioorganic Chemistry, Far-Eastern Branch, Russian Academy of Sciences, 690022 Vladivostok, Prospekt 100 Let Vladivostoku 159, Russia.</a> <b>Country code:</b> RU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/644" class="">644</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 171.</p>
</div>
<button id="kordi" class="accordion">KORDI <a href="/text/collections#kordi" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Korea Ocean Research and Development Institute, Ansan 426-744, Republic of Korea. <b>Country code:</b> KR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="kos" class="accordion">KOS <a href="/text/collections#kos" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Salmonella Microorganisms, Institute of Maritime and Tropical Medicine, National Salmonella Centre, Powstania Styczniowego 9 b, PL-81-519 Gdynia, Poland. <b>Country code:</b> PL. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/784" class="">784</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="kpb" class="accordion">KPB <a href="/text/collections#kpb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Prostate Tissue and microorganism, Korea Prostate Bank, 5010 Catholic Research Institutes 505 Banpo-dong Seocho-gu, Seoul 137-040, Republic of Korea. <b>Country code:</b> KR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/915" class="">915</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="kuen" class="accordion">KUEN <a href="/text/collections#kuen" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>KUKENS - Centre for Research and Application of Culture Collections of Microorganisms, Istanbul Faculty of Medicine, Capa-Istanbul, Turkey. <b>Country code:</b> TR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="kukens" class="accordion">KUKENS <a href="/text/collections#kukens" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centre for Research and Application of Culture Collections of Microorganisms, Istanbul Faculty of Medicine, Department of Microbiology, Temel Bilimler Binasi, TR-34390 Capa-Istanbul, Turkey. <b>Country code:</b> TR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/101" class="">101</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ky" class="accordion">KY <a href="/text/collections#ky" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Tokyo Research Laboratory, Kyowa Hakko Kogyo, Co., Ltd., Tokyo, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 4.</p>
</div>
<button id="lakto-flora" class="accordion">LAKTO-FLORA <a href="/text/collections#lakto-flora" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of Dairy Microorganisms, Milcom Servis a.s., BÅlohorskÁ 128, 169 00 Praha 6, Czech Republic. <b>Country code:</b> CZ. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="lancefield" class="accordion">Lancefield <a href="/text/collections#lancefield" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Lancefield Streptococcus Collection, Laboratory of Bacterial Pathogenesis and Immunology, Box 172, The Rockefeller University, 1230 York Avenue, New York, New York 10021, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="lbg" class="accordion">LBG <a href="/text/collections#lbg" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institute for Agricultural Bacteriology and Fermentation Biology, Confederated Technical High School, Zurich, Switzerland. <b>Country code:</b> CH. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="lcc" class="accordion">LCC <a href="/text/collections#lcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Dairy Cultures (Laboratory of the Culture Collection), Agricultural-Technical Academy, Department of Microbiology, Pl. Cieszynski 1 (= Kortowo Bl. 43), 10-957 Olsztyn, Poland. <b>Country code:</b> PL. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/231" class="">231</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="lcdc" class="accordion">LCDC <a href="/text/collections#lcdc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Laboratory Center for Disease Control, Health and Welfare Canada, Tunney's Pasture, Ottawa, Ontario, K1A OL2, Canada. <b>Country code:</b> CA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 5.</p>
</div>
<button id="lcp" class="accordion">LCP <a href="/text/collections#lcp" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Laboratory of Cryptogamy, National Museum of Natural History, Paris, France. <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/659" class="">659</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="lddc" class="accordion">LDDC <a href="/text/collections#lddc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Livestock Disease Diagnostic Center, University of Kentucky, Lexington, KY 40511, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 8.</p>
</div>
<button id="le" class="accordion">LE <a href="/text/collections#le" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Servico de Microbiologia e Imunologia, Faculdade de Ciencias Medicas - UERJ, Rua Prof. Manuel de Abreu, 48, Rio de Janeiro 20550 RJ, Brazil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/313" class="">313</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="lege" class="accordion">LEGE <a href="/text/collections#lege" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Blue Biotechnology and Ecotoxicology Culture Collection, CIIMAR – Interdisciplinary Centre of Marine and Environmental Research, University of Porto, Rua dos Bragas, 289, Porto, Porto, 4050-123 Porto. <b>Country code:</b> PT. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1089" class="">1089</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 5.</p>
</div>
<button id="lhmc" class="accordion">LHMC <a href="/text/collections#lhmc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Oral Microbiology, Royal London Hospital Medical College, London, United Kingdom. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="lia" class="accordion">LIA <a href="/text/collections#lia" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Museum of Cultures, Leningrad Research Institute of Antibiotics, 23 Ogorodnikov Prospect, Leningrad L-20, Russia. <b>Country code:</b> RU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="lipimc" class="accordion">LIPIMC <a href="/text/collections#lipimc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Lembaga Ilmu Pengetahuan Indonesia (Indonesian Institute for Sciences), Pusat Penenlitian dan Pengembangan Biologi (Research and Development Centre for Biology) Address: Pustlitbang Biologi, JI. Juanda 18, Bogor, Indonesia. <b>Country code:</b> ID. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="lipp" class="accordion">LIPP <a href="/text/collections#lipp" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Leptospirotheque, Institut Pasteur, 28 rue du Dr Roux, Paris 75724 Cedex 15, France. <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/345" class="">345</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="lmau" class="accordion">LMAU <a href="/text/collections#lmau" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Laboratory Microbiology, Agricultural University, Wageningen, Netherlands. <b>Country code:</b> NL. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="lmch" class="accordion">LMCH <a href="/text/collections#lmch" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Laboratoire de Microbiologie, Centre Hospitalier, BP 269, Cahors 46005, France. <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/804" class="">804</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="lmd" class="accordion">LMD <a href="/text/collections#lmd" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Laboratorium voor Microbiologie der Technische Hogeschool, Delft University of Technology, Julianalaan 67A, 2628 BC Delft, The Netherlands. See: <a href="/text/collections#nccb" class="">NCCB.</a> <b>Country code:</b> NL. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 15.</p>
</div>
<button id="lmg" class="accordion">LMG <a href="/text/collections#lmg" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://bccm.belspo.be/catalogues/lmg-catalogue-search" class="">Collection of the Laboratorium voor Microbiologie en Microbiele Genetica, Rijksuniversiteit, Ledeganckstraat 35, B-9000, Gent, Belgium.</a> <b>Country code:</b> BE. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/296" class="">296</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 4277.</p>
</div>
<button id="lms" class="accordion">LMS <a href="/text/collections#lms" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Carolina Biological Supply Company, 2700 York Road, Burlington, North Carolina, 27215-3387, USA. <b>Country code:</b> US. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/530" class="">530</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="lock" class="accordion">LOCK <a href="/text/collections#lock" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Centre of Industrial Microorganisms, Institute of Fermentation Technology and Microbiology, Technical University, ul. Gdanska 166 (= Wolczanska 171/173 - corner), 90-537 Lodz, Poland. <b>Country code:</b> PL. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/105" class="">105</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="lrtl" class="accordion">LRTL <a href="/text/collections#lrtl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Laboratoire de Recherches et Technologies Laitière de Rennes, Rennes, France. <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="lsh" class="accordion">LSH <a href="/text/collections#lsh" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>London School of Hygiene and Tropical Medicine, London, UK. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="lshb" class="accordion">LSHB <a href="/text/collections#lshb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Biochemistry Department, London School of Hygiene and Tropical Medicine, London, UK. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="lsu" class="accordion">LSU <a href="/text/collections#lsu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Louisiana State University, Baton Rouge, Louisiana 70803, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="lth" class="accordion">LTH <a href="/text/collections#lth" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institut für Lebensmitteltechnologie, Universität Hohenheim, Stuttgart, Germany. <b>Country code:</b> DE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 7.</p>
</div>
<button id="lti" class="accordion">LTI <a href="/text/collections#lti" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Cryobank of Microorganisms-Destructors, Department of Molecular biotechnology, Leningrad Lensoviet Institute of Technology, Moscowsky Prospekt, 26, Leningrad 198013, Russian Federation. <b>Country code:</b> RU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/554" class="">554</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="luh" class="accordion">LUH <a href="/text/collections#luh" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection L. Dijkshoorn, Leiden University Medical Center, Leiden, The Netherlands. <b>Country code:</b> NL. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 6.</p>
</div>
<button id="ly" class="accordion">LY <a href="/text/collections#ly" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Laboratoire de Mycologie associé au C.N.R.S., Université Claude Bernard, Lyon I, France. <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 4.</p>
</div>
<button id="maff" class="accordion">MAFF <a href="/text/collections#maff" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.gene.affrc.go.jp/micro/" class="">Ministry of Agriculture, Forestry and Fisheries Genebank, National Institute of Agrobiological Resources, Kannondai 2-1-2, Tsukuba, Ibaraki, 305-8602 Japan.</a> <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/637" class="">637</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 20.</p>
</div>
<button id="mao" class="accordion">MAO <a href="/text/collections#mao" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Mircen Afrique Ouest, ISRA-CNRA, B.P. 53, Bambey, Senegal. <b>Country code:</b> SN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/53" class="">53</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="mar" class="accordion">MAR <a href="/text/collections#mar" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Grasslands Rhizobium Collection, Soil Productivity Research Laboratory, Private Bag 3757, Marondera, Zimbabwe. <b>Country code:</b> ZW. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/34" class="">34</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="marbec" class="accordion">MarBEC <a href="/text/collections#marbec" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>MarBEC Culture Collection, Monto Kumagai, 1955 East-West Road, Agricultural Science Building Rm. 415M, University of Hawaii, Honolulu, Hawaii 96822, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="marseille" class="accordion">Marseille <a href="/text/collections#marseille" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#csur" class="">CSUR.</a> <b>Country code:</b> FR. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 225.</p>
</div>
<button id="mbic" class="accordion">MBIC <a href="/text/collections#mbic" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.mbio.jp/mbic/" class="">Marine Biotechnology Institute Culture Collection, 3-75-1 Heita, Kamaishi, Iwate 026-001, Japan.</a> <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/831" class="">831</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 61.</p>
</div>
<button id="mbicc" class="accordion">MBICC <a href="/text/collections#mbicc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Marine Biotechnology Institute Culture Collection, 3-75-1 Heita, Kamaishi, Iwate 026-001, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="mcc" class="accordion">MCC <a href="/text/collections#mcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.nccs.res.in/index.php/TeamsNCCS/Repositories" class="">Microbial Culture Collection, National Centre for Cell Science, Pune University Campus, Ganeshkhind, Pune, Maharashtra, 411007, India.</a> <b>Country code:</b> IN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/930" class="">930</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 98.</p>
</div>
<button id="mccc" class="accordion">MCCC <a href="/text/collections#mccc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://mccc.org.cn/" class="">Marine Culture Collection of China, China. Also used as acronym of the Maltese Catacombs Culture Collection, University of Malta.</a> <b>Country code:</b> MT. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1051" class="">1051</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 729.</p>
</div>
<button id="mccm" class="accordion">MCCM <a href="/text/collections#mccm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.uni-marburg.de/de/fb20/bereiche/ziei/medmikrobio/institut" class="">Medical Culture Collection Marburg, Institute of Medical Microbiology and Hospital Hygiene, Philipps University, Pilgrimstein 2, D-35037 Marburg, Germany.</a> <b>Country code:</b> DE. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/418" class="">418</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 5.</p>
</div>
<button id="mcc-nies" class="accordion">MCC-NIES <a href="/text/collections#mcc-nies" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#nies" class="">NIES.</a> <b>Country code:</b> JP. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="mcc-uplb" class="accordion">MCC-UPLB <a href="/text/collections#mcc-uplb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Microbial Culture Collection of the Museum of Natural History, University of the Philippines, Los Baños, College, Laguna 4031, Philippines. <b>Country code:</b> PH. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/39" class="">39</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="mcitm" class="accordion">MCITM <a href="/text/collections#mcitm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Bacterial Culture Collection, Institute Tropical Medicine, Nationalestraat 155, Antwerpen B 2000, Belgium. <b>Country code:</b> BE. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/400" class="">400</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="mcm" class="accordion">MCM <a href="/text/collections#mcm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://aripune.org/" class="">MACS Collection of Microorganisms, MACS-Agharkar Research Institute, Gopal Ganesh Agarkar Road, Pune, 411004 Maharashtra, India.</a> <b>Country code:</b> IN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/561" class="">561</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="mcml" class="accordion">MCML <a href="/text/collections#mcml" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Mc Master Culture Collection, CSIRO Division of Animal Health, Private Bag No 1, Cnr. Flemington Road and Park Drive, Melbourne. Vic. 3052, Australia. <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="mda" class="accordion">MDA <a href="/text/collections#mda" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>M.D. Anderson Cancer Center, University of Texas, 1515 Holcombe Blvd, Houston, TX 77030, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 5.</p>
</div>
<button id="mdc" class="accordion">MDC <a href="/text/collections#mdc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Molecular Diagnostics Center, Biomolecular Technologies S.L. and Universidad Miguel Hernández, Orihuela E-03300, Alicante, Spain. <b>Country code:</b> ES. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/803" class="">803</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 5.</p>
</div>
<button id="mdh" class="accordion">MDH <a href="/text/collections#mdh" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Michigan Department of Health, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="mfc" class="accordion">MFC <a href="/text/collections#mfc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Matsushima Fungus Collection, Kobe, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="mim" class="accordion">MIM <a href="/text/collections#mim" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of the Cattedra di Microbiologia Industriale, Università degli Studi di Milano, Italy. <b>Country code:</b> IT. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="mit" class="accordion">MIT <a href="/text/collections#mit" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Massachusetts Institute of Technology, Cambridge, Mass., USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 21.</p>
</div>
<button id="mmca" class="accordion">MMCA <a href="/text/collections#mmca" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Medical Microbiology Culture Collection, Aarhus, Denmark. <b>Country code:</b> DK. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="mml" class="accordion">MML <a href="/text/collections#mml" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Medical Microbiological Laboratory, Ulleval Hospital, Oslo, Norway. <b>Country code:</b> NO. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/432" class="">432</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="mola" class="accordion">MOLA <a href="/text/collections#mola" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://collection.obs-banyuls.fr/catalogue.php" class="">Collection of Microbial Observatory Laboratoire Arago, Laboratoire Arago, avenue Fontaule, Banyuls sur Mer 66650, France.</a> <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/911" class="">911</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 9.</p>
</div>
<button id="mrc" class="accordion">MRC <a href="/text/collections#mrc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Research Institute for Nutritional Diseases, Tygerberg, South Africa. <b>Country code:</b> ZA. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/800" class="">800</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="mscl" class="accordion">MSCL <a href="/text/collections#mscl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://mikro.daba.lv/anglju/" class="">Microbial Strain Collection of Latvia, University of Latvia, Faculty of Biology, Kronvalda Blvd. 4, LV-1586 Riga, Latvia.</a> <b>Country code:</b> LV. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/854" class="">854</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="mscmu" class="accordion">MSCMU <a href="/text/collections#mscmu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Microbiology Section, Chiang Mai University (MSCMU), Department of Biology, Faculty of science, Chang Mai University, Thailand, 239 Huay Kaew Road, Chiang Mai, Muang, 50202, Thailand. <b>Country code:</b> TH. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/692" class="">692</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="msdj" class="accordion">MSDJ <a href="/text/collections#msdj" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of the Laboratoire de Microbiologie des Sols, Institut National de la Recherche Agronomique, F-21034 Dijon Cedex, France. <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="mtcc" class="accordion">MTCC <a href="/text/collections#mtcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.mtccindia.res.in/" class="">Microbial Type Culture Collection and Gene Bank, Institute of Microbial Technology, Sector39-A, Chandigarh, India.</a> <b>Country code:</b> IN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/773" class="">773</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 242.</p>
</div>
<button id="mthu" class="accordion">MTHU <a href="/text/collections#mthu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Bacteriology, Faculty of Medicine, Tahoku University, Miyagi-ken, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="mu" class="accordion">MU <a href="/text/collections#mu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Mugla University Collection of Microorganisms, Mugla Universitesi, Mugla University, Egitim Fakultesi, Mugla, Kotekli, TR-48170, Turkey. <b>Country code:</b> TR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/833" class="">833</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="mucl" class="accordion">MUCL <a href="/text/collections#mucl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://bccm.belspo.be/about-us/bccm-mucl" class="">Mycotheque de l'Universite catholique de Louvain, Earth and Life Institute, Microbiology, Mycology, Croix du Sud 2/L7.05.06, Louvain-la-Neuve, Brabant Wallon, B-1348.</a> <b>Country code:</b> BE. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/308" class="">308</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="mucob" class="accordion">MUCOB <a href="/text/collections#mucob" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Manchester University Collection of Bacteria, Department of Medical Microbiology, University of Manchester, Oxford Road, Manchester M13 9PT, United Kingdom. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="mul" class="accordion">MUL <a href="/text/collections#mul" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Microbiology MUL-B 250, Faculty of Medicine, Laval University, Sainte Foy, Quebec, G1K-7P4, Canada. <b>Country code:</b> CA. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/250" class="">250</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="muscl" class="accordion">MUSCL <a href="/text/collections#muscl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Microbial Strain Collection of Latvia, University of Latvia, Faculty of Biology, Kronvalda Blvd. 4, LV-1586 Riga, Latvia. <b>Country code:</b> LV. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="nadc" class="accordion">NADC <a href="/text/collections#nadc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Animal Disease Center, Ames, Iowa, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="nau" class="accordion">NAU <a href="/text/collections#nau" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Nanjing Agricultural University, Nanjing, People's Republic of China. <b>Country code:</b> CN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="nbbcru" class="accordion">NBBCRU <a href="/text/collections#nbbcru" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>North Bengal University Bacterial Culture Repository Unit, Siliguri- 734430, West Bengal, India. <b>Country code:</b> IN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="nbimcc" class="accordion">NBIMCC <a href="/text/collections#nbimcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.nbimcc.org/" class="">National Bank for Industrial Microorganisms and Cell Cultures, 125 Tsarigradsko chaussee blvd., Bl.2, BG-1113 Sofia, Bulgaria.</a> <b>Country code:</b> BG. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/135" class="">135</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="nbrc" class="accordion">NBRC <a href="/text/collections#nbrc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.nbrc.nite.go.jp/NBRC2/NBRCDispSearchServlet?lang=en" class="">Biological Resource Center, National Institute of Technology and Evaluation (NITE), 2-5-8, Kazusakamatari, Kisarazu-shi, Chiba Pref., 292-0812, Japan.</a> <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/825" class="">825</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 3936.</p>
</div>
<button id="nbrl" class="accordion">NBRL <a href="/text/collections#nbrl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>The US Department of Agriculture at Peoria, Illinois, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="nca" class="accordion">NCA <a href="/text/collections#nca" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Canners Association, San Francisco, California, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ncaim" class="accordion">NCAIM <a href="/text/collections#ncaim" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://ncaim.etk.szie.hu/" class="">National Collection of Agricultural and Industrial Microorganisms, Department of Microbiology and Biotechnology, University of Horticulture and Food Industry, Somlói út. 14-16, H-1118 Budapest, Hungary.</a> <b>Country code:</b> HU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/485" class="">485</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 129.</p>
</div>
<button id="ncam" class="accordion">NCAM <a href="/text/collections#ncam" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Collection of Agricultural Microorganisms, Institute of Microbiology, Abdulla Qadiriy 7 B, Tashkent 700128, Uzbekistan. <b>Country code:</b> UZ. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/862" class="">862</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ncb" class="accordion">NCB <a href="/text/collections#ncb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Culture Bank, Università di Udine, Dip. Biologia Applicata Difesa Piante, Area Rizzi, Via delle Scienze 208, I-33100 Udine, Italy. <b>Country code:</b> IT. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/175" class="">175</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="ncc" class="accordion">NCC <a href="/text/collections#ncc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Nestlé Culture Collection, Nestlé Research Centre, Route du Jorat 57, Vers-Chez-Les-Blanc, 1000 Lausanne 26, Switzerland. <b>Country code:</b> CH. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/856" class="">856</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="nccb" class="accordion">NCCB <a href="/text/collections#nccb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.cbs.knaw.nl/Collections/Biolomics.aspx?Table=NCCB%20strains%20internet" class="">Netherlands Culture Collection of Bacteria (formerly Phabagen and LMD), NCCB/CBS, Uppsalalaan 8, 3584 CT Utrecht, The Netherlands.</a> <b>Country code:</b> NL. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/797" class="">797</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 262.</p>
</div>
<button id="nccp" class="accordion">NCCP <a href="/text/collections#nccp" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://nccp.cdc.go.kr/eng/main.do" class="">National Culture Collection for Pathogens, National Institute of Health, Korea Center for Disease Control and Prevention, 5 Nokbeon-dong Eunpyeong-gu, Seoul 122-701, Republic of Korea.</a> <b>Country code:</b> KR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/852" class="">852</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 20.</p>
</div>
<button id="ncdc" class="accordion">NCDC <a href="/text/collections#ncdc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Collection of Dairy Cultures, National Dairy Research Institute, D.M.Divn, NDRI, Karnal, Haryana, 132001, India. <b>Country code:</b> IN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/775" class="">775</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ncdo" class="accordion">NCDO <a href="/text/collections#ncdo" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Collection of Dairy Organisms. See: <a href="/text/collections#ncfb" class="">NCFB.</a> <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 77.</p>
</div>
<button id="ncfb" class="accordion">NCFB <a href="/text/collections#ncfb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Collection of Food Bacteria (previously named NCDO). Transferred from the IFR (Institute of Food Resarch) Reading to National Collections of Industrial, Food and Marine Bacteria, 23 Machar Drive, Aberdeen, AB24 3RY, Scotland. See: <a href="/text/collections#ncimb" class="">NCIMB.</a> <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 51.</p>
</div>
<button id="nch" class="accordion">NCH <a href="/text/collections#nch" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Chubu Hospital, Obu, Aichi, Japan 474. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="ncib" class="accordion">NCIB <a href="/text/collections#ncib" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Collection of Industrial Bacteria, Torry Research Station, P.O. Box 31, 135 Abbey Rd., Aberdeen AB9 8DG, Scotland, United Kingdom. See: <a href="/text/collections#ncimb" class="">NCIMB.</a> <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 135.</p>
</div>
<button id="ncim" class="accordion">NCIM <a href="/text/collections#ncim" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.ncl.res.in/files/NCIM/Catalogue.aspx?menuid=ql4&amp;childmenustripid=divSubQL4" class="">National Collection of Industrial Microorganisms, National Chemical Laboratory, Poona 8, Maharashtra, India.</a> <b>Country code:</b> IN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/3" class="">3</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 28.</p>
</div>
<button id="ncimb" class="accordion">NCIMB <a href="/text/collections#ncimb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.ncimb.com/BioloMICS.aspx?Table=Website%20catalogue&amp;info=Help%20on%20queries" class="">National Collection of Industrial and Marine Bacteria, National Collections of Industrial, Food and Marine Bacteria, NCIMB Ltd, Ferguson Building, Craibstone Estate, Bucksburn, Aberdeen, AB21 9YA, UK Scotland.</a> <b>Country code:</b> GB. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/653" class="">653</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 1055.</p>
</div>
<button id="ncma" class="accordion">NCMA <a href="/text/collections#ncma" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://ncma.bigelow.org/" class="">National Center for Marine Algae and Microbiota, Bigelow Laboratory for Ocean Sciences, East Boothbay, ME, USA.</a> <b>Country code:</b> US. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="ncmb" class="accordion">NCMB <a href="/text/collections#ncmb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Collection of Marine Bacteria, Torry Research Station Aberdeen, Scotland, United Kingdom. See: <a href="/text/collections#ncimb" class="">NCIMB.</a> <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 17.</p>
</div>
<button id="ncmh" class="accordion">NCMH <a href="/text/collections#ncmh" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>The North Carolina Memorial Hostital, University of North Carolina, Chapel Hill, NC, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ncpf" class="accordion">NCPF <a href="/text/collections#ncpf" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.phe-culturecollections.org.uk/collections/ncpf.aspx" class="">National Collection of Pathogenic Fungi, Public Heatlh England, Porton Down, Salisbury, Wiltshire, SP40JG.</a> <b>Country code:</b> GB. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/184" class="">184</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ncppb" class="accordion">NCPPB <a href="/text/collections#ncppb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://ncppb.fera.defra.gov.uk/" class="">National Collection of Plant Pathogenic Bacteria, Central Science Laboratory, Sand Hutton, York YO41 1LZ, United Kingdom.</a> <b>Country code:</b> GB. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/126" class="">126</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 157.</p>
</div>
<button id="ncpv" class="accordion">NCPV <a href="/text/collections#ncpv" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.phe-culturecollections.org.uk/collections/ncpv.aspx" class="">National Collection of Pathogenic Viruses, Public Health England, Porton Down, Salisbury, Wiltshire, SP4 0JG.</a> <b>Country code:</b> GB. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/814" class="">814</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ncsc" class="accordion">NCSC <a href="/text/collections#ncsc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Center of Streptococcus Collection, Department of Microbiology, Faculty of Medical Science, Chulalongkorn University, Rama 4 Road, Chulalongkorn University, Bangkok, 10330, Thailand. <b>Country code:</b> TH. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/664" class="">664</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="nctc" class="accordion">NCTC <a href="/text/collections#nctc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.phe-culturecollections.org.uk/collections/nctc.aspx" class="">National Collection of Type Cultures, Central Public Health Laboratory, Colindale Ave., London NW9 5HT, England, United Kingdom.</a> <b>Country code:</b> GB. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/154" class="">154</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 968.</p>
</div>
<button id="ncyc" class="accordion">NCYC <a href="/text/collections#ncyc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.ncyc.co.uk/" class="">National Collection of Yeast Cultures, Institute of Food Research, Norwich Research Park, Colney, Norwich, NR4 7UA.</a> <b>Country code:</b> GB. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/169" class="">169</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="neau" class="accordion">NEAU <a href="/text/collections#neau" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://english.neau.edu.cn/index.htm" class="">Northeast Agricultural University, No. 59 Mucai Street, Xiangfang District, Harbin 150030, People's Republic of China.</a> <b>Country code:</b> CN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 135.</p>
</div>
<button id="nem" class="accordion">NEM <a href="/text/collections#nem" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Faculté de Médecine Necker-Enfants Malades, 75730 Paris Cedex 15, France. <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="neu" class="accordion">NEU <a href="/text/collections#neu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Microorganisms, University of Neuchâtel, Switzerland. <b>Country code:</b> CH. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="ngr" class="accordion">NGR <a href="/text/collections#ngr" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Plant Pathology, Department of Primary Industry, P.O. Box 2417, Konedobu, Port Moresby, 7250, Papua New Guinea. <b>Country code:</b> PG. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/356" class="">356</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="nhl" class="accordion">NHL <a href="/text/collections#nhl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Institute of Hygienic Sciences, Tokyo, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ni" class="accordion">NI <a href="/text/collections#ni" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Nagao Institute, Tokyo, Japan (defunct). <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="niaes" class="accordion">NIAES <a href="/text/collections#niaes" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Cultures of the Microbiology Division, National Institute of Agro-Environmental Sciences, Yatabe, Ibaraki, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="niah" class="accordion">NIAH <a href="/text/collections#niah" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Institute of Animal Health, Ibaraki, Japan. <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/638" class="">638</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="niaid" class="accordion">NIAID <a href="/text/collections#niaid" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Institute of Allergy and Infectious Diseases, Hamilton, Montana 59840, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="nibh" class="accordion">NIBH <a href="/text/collections#nibh" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Institute of Bioscience and Human-Technology, Higashi 1-Chome, Tsukubashi, Ibaraki, 305-8566, Japan. <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/746" class="">746</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="nies" class="accordion">NIES <a href="/text/collections#nies" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://mcc.nies.go.jp/" class="">National Institute for Environmental Studies, Microbial Culture Collection, 16-2, Onogawa, Tsukuba, Ibaraki, 305-8506, Japan.</a> <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/591" class="">591</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 12.</p>
</div>
<button id="nih" class="accordion">NIH <a href="/text/collections#nih" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Institute of Health, Bethesda, Maryland, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="nihj" class="accordion">NIHJ <a href="/text/collections#nihj" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Institute of Health, Tokyo, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="niph" class="accordion">NIPH <a href="/text/collections#niph" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection A. Nemec, National Institute of Public Health, Srobárova 48, 10042 Prague, Czech Republic. <b>Country code:</b> CZ. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 17.</p>
</div>
<button id="nisl" class="accordion">NISL <a href="/text/collections#nisl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Noda Institute for Scientific Research, Noda, Chiba, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="niva-cya" class="accordion">NIVA-CYA <a href="/text/collections#niva-cya" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://niva-cca.no/" class="">Norwegian Institute for Water Research, NIVA Culture Collection of Algae, P.O. Box 173 Kjelsås, N-0411 Oslo, Norway.</a> <b>Country code:</b> NO. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/498" class="">498</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="nizo" class="accordion">NIZO <a href="/text/collections#nizo" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.nizo.com" class="">NIZO Food Research, P.O. Box 20, 6710 BA Ede, The Netherlands.</a> <b>Country code:</b> NL. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/985" class="">985</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="nlep" class="accordion">NLEP <a href="/text/collections#nlep" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>The National Laboratory for Enteric Pathogens (NLEP), Health Canada, 1015 Arlington St, Winnipeg, Manitoba, Canada. <b>Country code:</b> CA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="nmh" class="accordion">NMH <a href="/text/collections#nmh" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>North Middlesex Hospital, London, United Kingdom. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="nml" class="accordion">NML <a href="/text/collections#nml" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Microbiology Laboratory Health Canada Culture Collections, National Microbiology Laboratory-Health Canada, 1015 Arlington Street suite H5040, Winnipeg, Manitoba, R3E 3R2, Canada. <b>Country code:</b> CA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 12.</p>
</div>
<button id="nml-hccc" class="accordion">NML-HCCC <a href="/text/collections#nml-hccc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Microbiology Laboratory Health Canada Culture Collections, National Microbiology Laboratory-Health Canada, 1015 Arlington Street suite H5040, Winnipeg, Manitoba, R3E 3R2, Canada. See: <a href="/text/collections#nml" class="">NML.</a> <b>Country code:</b> CA. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/840" class="">840</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="nrc" class="accordion">NRC <a href="/text/collections#nrc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Research Council of Canada Culture Collection, 100 Sussex Drive, Ottawa, Ontario K1A OR6, Canada. <b>Country code:</b> CA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 10.</p>
</div>
<button id="nrcc" class="accordion">NRCC <a href="/text/collections#nrcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Research Council of Canada Culture Collection, 100 Sussex Drive, Ottawa, Ontario K1A OR6, Canada. <b>Country code:</b> CA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="nrcm" class="accordion">NRCM <a href="/text/collections#nrcm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Reference Centre for Mycobacteriology, National Microbiology Laboratory, Population and Public Health Branch, Health Canada, Winnipeg, Manitoba, Canada R3E 3R2. <b>Country code:</b> CA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="nric" class="accordion">NRIC <a href="/text/collections#nric" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://jcm.brc.riken.jp/en/catalogue_e" class="">NODAI Research Institute Culture Collection, Tokyo University of Agriculture, Sakuragaoka 1-1-1, Setagaya-ku, Tokyo 156-8502, Japan.</a> <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/747" class="">747</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 111.</p>
</div>
<button id="nrl" class="accordion">NRL <a href="/text/collections#nrl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Reference Laboratory, National Institute of Public Health, Prague, Czech Republic. <b>Country code:</b> CZ. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/350" class="">350</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="nrrl" class="accordion">NRRL <a href="/text/collections#nrrl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://nrrl.ncaur.usda.gov/cgi-bin/usda/process.html?mv_doit=return&amp;mv_nextpage=prokaryote%2fnrrl&amp;mv_click=nrrl&amp;query_type=nrrl&amp;id=qem2chXj" class="">Northen Regional Research Center, Agricultural Research Service Culture Collection, National Center for Agricultural Utilization Research, US Department of Agriculture, 1815 North University Street, Peoria, Illinois 61604, USA.</a> <b>Country code:</b> US. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/97" class="">97</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 1806.</p>
</div>
<button id="nrzec" class="accordion">NRZEC <a href="/text/collections#nrzec" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Nationales Referenzzentrum für Escherichia coli, Berlin, Germany. <b>Country code:</b> DE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="nscnfb" class="accordion">NSCNFB <a href="/text/collections#nscnfb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Novi Sad Collection of Nitrogen Fixing Bacteria, Institute of Field and Vegetable Crops, Bul.King Petar I 67, Novi Sad, Vojvodina, 21000, Yugoslavia. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/754" class="">754</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ntcci" class="accordion">NTCCI <a href="/text/collections#ntcci" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection, Microbiology and Cell Biology Laboratory, Indian Institute of Science, Bangalore, Karnatka, 560012, India. <b>Country code:</b> IN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/107" class="">107</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ntccm" class="accordion">NTCCM <a href="/text/collections#ntccm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Namibian Type Culture Collection for Microorganisms, at the UNAM University of Namibia, Windhoek. <b>Country code:</b> NA. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 5.</p>
</div>
<button id="nthc" class="accordion">NTHC <a href="/text/collections#nthc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>North Technical Hogskolles Collection, Department of Biochemistry, Technical University of Norway, Trondheim MTH, Norway. <b>Country code:</b> NO. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="nua" class="accordion">NUA <a href="/text/collections#nua" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Microbiology, Medical School, National University of Athens, 75M. Asias Str., Goudi - 115 27, Athens 115 27, Greece. <b>Country code:</b> GR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/281" class="">281</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="num" class="accordion">NUM <a href="/text/collections#num" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Microbiology, Nihon University School of Dentistry at Matsudo, Matsudo, Chiba 271, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 14.</p>
</div>
<button id="nusdm" class="accordion">NUSDM <a href="/text/collections#nusdm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Microbiology, National University of Singapore, Lower Kent Ridge Road, Singapore. <b>Country code:</b> SG. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/568" class="">568</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="nzdri" class="accordion">NZDRI <a href="/text/collections#nzdri" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Maybe identical to NZRD. See: <a href="/text/collections#nzrd" class="">NZRD.</a> <b>Country code:</b> NZ. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="nzfs" class="accordion">NZFS <a href="/text/collections#nzfs" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Forest Research Culture Collection, New Zealand Forest Research Institute, Private Bag 3020, Rotorua, New Zealand. <b>Country code:</b> NZ. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/62" class="">62</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="nzp" class="accordion">NZP <a href="/text/collections#nzp" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>New Zealand Department of Scientific and Industrial Research, Applied Biochemistry Division, Palmerston North, New Zealand. <b>Country code:</b> NZ. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="nzrcc" class="accordion">NZRCC <a href="/text/collections#nzrcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#icmp" class="">ICMP.</a> (Or NZRD or NZRM or NZRP or WARC). <b>Country code:</b> NZ. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="nzrd" class="accordion">NZRD <a href="/text/collections#nzrd" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>New Zealand Reference Culture Collection of Microorganisms, Dairy Section, New Zealand Dairy Research Institute, Palmerston North, New Zealand. <b>Country code:</b> NZ. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/318" class="">318</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="nzrm" class="accordion">NZRM <a href="/text/collections#nzrm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.esr.cri.nz/our-services/products-and-tools/nz-culture-collection/" class="">New Zealand Reference Culture Collection, Medical Section, Communicable Disease Group, ESR Kenepuru Science Centre, PO Box 50 348, Porirua, New Zealand.</a> <b>Country code:</b> NZ. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/457" class="">457</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="nzrp" class="accordion">NZRP <a href="/text/collections#nzrp" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>New Zealand Reference Culture Collection and Soil Section, c/o Plant Disease Division, Auckland, DSIR, Private bag, New Zealand. <b>Country code:</b> NZ. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/335" class="">335</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="oac" class="accordion">OAC <a href="/text/collections#oac" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Botany and Genetics, University of Guelph, Ont., Canada. <b>Country code:</b> CA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ocm" class="accordion">OCM <a href="/text/collections#ocm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://methanogens.pdx.edu/" class="">Oregon Collection of Methanogens, Portland State University, PO Box 19600, Portland, OR 97291-1000, USA.</a> <b>Country code:</b> US. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/592" class="">592</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 100.</p>
</div>
<button id="oeu" class="accordion">OEU <a href="/text/collections#oeu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Tennoji Branch, Osaka University of Liberal Arts and Education, Minami-Kawabori-Cho, Tennojiku, Osaka, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ogc" class="accordion">OGC <a href="/text/collections#ogc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Oregon Graduate Center Collection, Beaverton, Oregon 97006-1992, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="ogi" class="accordion">OGI <a href="/text/collections#ogi" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Methanogenic Archaeobacteria, Oregon Graduate Institute of Science and Technology See: <a href="/text/collections#ocm" class="">OCM.</a> <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="oki" class="accordion">OKI <a href="/text/collections#oki" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Hungarian National Collection of Medical Bacteria, B. Johan National Center for Epidemiology, Gyali ut 2-6, H-1097 Budapest, Hungary. <b>Country code:</b> HU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="omz" class="accordion">OMZ <a href="/text/collections#omz" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institut für Orale Mikrobiologie und Allgemeine Immunologie, Zentrum für Zahn-, Mund- und Kieferheilkunde der Universität Zürich, Plattenstrasse 11, CH-8028, Zürich, Switzerland. <b>Country code:</b> CH. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 4.</p>
</div>
<button id="oob" class="accordion">OOB <a href="/text/collections#oob" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Observatoire Océanologique de Banyuls, F-66650 Banyuls-sur-Mer, France. <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 7.</p>
</div>
<button id="ors" class="accordion">ORS <a href="/text/collections#ors" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of the Laboratory of Soil Microbiology, ORSTOM, Dakar, Sénégal. <b>Country code:</b> SN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 9.</p>
</div>
<button id="out" class="accordion">OUT <a href="/text/collections#out" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Fermentation Technology, Faculty of Engineering, Osaka University, Osaka, Japan. <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/748" class="">748</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="pah" class="accordion">PAH <a href="/text/collections#pah" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Princess Alexandra Hospital, Brisbane, Australia. <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="pamc" class="accordion">PAMC <a href="/text/collections#pamc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Polar and Alpine Microbial Collection, Korea Polar Research Institute, Incheon, Republic of Korea. <b>Country code:</b> KR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1064" class="">1064</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 17.</p>
</div>
<button id="pbc" class="accordion">PBC <a href="/text/collections#pbc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Pacific Bacterial Collection, 3190 Maile Way, St John Plant Science Building 315, Honolulu Hi 96822, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="pbf" class="accordion">PBF <a href="/text/collections#pbf" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Perum Bio Farma, Jl. Pasteur 28, Bandung, 40161, Indonesia. <b>Country code:</b> ID. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/633" class="">633</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="pcc" class="accordion">PCC <a href="/text/collections#pcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://catalogue-crbip.pasteur.fr/recherche_catalogue.xhtml" class="">Pasteur Culture Collection of Cyanobacteria, Unité de Physiologie Microbienne, Institut Pasteur, 28 rue du Docteur Roux, 75724 Paris Cedex 15, France.</a> <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/481" class="">481</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 13.</p>
</div>
<button id="pci" class="accordion">PCI <a href="/text/collections#pci" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Penicillin Control and Immunology Section, Food and Drug Administration, Washington DC, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="pcm" class="accordion">PCM <a href="/text/collections#pcm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.iitd.pan.wroc.pl/en/PCM/" class="">Polish Collection of Microorganisms (Central Centre of Microorganisms Collections), Ludwik Hirszfeld Institute of Immunology and Experimental Therapy of the Polish Academy of Sciences, ul. Czerska 12, 53-114 Wroclaw, Poland.</a> <b>Country code:</b> PL. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/106" class="">106</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 58.</p>
</div>
<button id="pcu" class="accordion">PCU <a href="/text/collections#pcu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Microbiology, Faculty of Pharmaceutical Sciences, Chulalongkorn University, Culture Collection (PCU), Bangkok 10330, Thailand. <b>Country code:</b> TH. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/662" class="">662</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 71.</p>
</div>
<button id="pd" class="accordion">PD <a href="/text/collections#pd" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of Plant Pathogenic Bacteria, Plant Protection Service, P.O.Box 9102, Geertjesweg 15, Wageningen 6700 HC, The Netherlands. <b>Country code:</b> NL. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/618" class="">618</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="pddcc" class="accordion">PDDCC <a href="/text/collections#pddcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of Plant Diseases Division, New Zealand Department of Scientific and Industrial Research, Landcare Research, Private Bag 92170, Auckland, New Zealand. <b>Country code:</b> NZ. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 11.</p>
</div>
<button id="pgsc" class="accordion">PGSC <a href="/text/collections#pgsc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Pseudomonas Genetic Stock Center, East Carolina University, School of Medicine in Greenville, North Carolina, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="phls" class="accordion">PHLS <a href="/text/collections#phls" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collaborating Center for Research And Reference for Leptospirosis, County Hospital, Hereford HR1 2ER, United Kingdom. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="phlswho" class="accordion">PHLS/WHO <a href="/text/collections#phlswho" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collaborating Center for Research And Reference for Leptospirosis, County Hospital, Hereford HR1 2ER, United Kingdom. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="picc" class="accordion">PICC <a href="/text/collections#picc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Incorrect acronym for CIP. See: <a href="/text/collections#cip" class="">CIP.</a> <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="pir" class="accordion">PIR <a href="/text/collections#pir" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Bulgarian Research Culture Collection, N. Poushkarov-Institute of Soil Science and Agroecology, Bul. Makedonia No.8, Sofia 1606, Bulgaria. <b>Country code:</b> BG. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/373" class="">373</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="pncm" class="accordion">PNCM <a href="/text/collections#pncm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#pncm-biotech" class="">PNCM-BIOTECH.</a> <b>Country code:</b> PH. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="pncm-biotech" class="accordion">PNCM-BIOTECH <a href="/text/collections#pncm-biotech" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://ovcre.uplb.edu.ph/extension/analytical-research-services/item/374-biotech-philippine-national-collection-of-microorganisms" class="">Philippine National Collection of Microorganisms, National Institute of Molecular Biology and Biotechnology, BIOTECH-UPLB, College Laguna, 4031, Philippines.</a> <b>Country code:</b> PH. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/620" class="">620</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ppcc" class="accordion">PPCC <a href="/text/collections#ppcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Plant Pathology Culture Collection, Plant Pathology Branch, Department of Primary Industry, Meiers Road, Indooroopilly. Qld. 4069, Australia. <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/27" class="">27</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ppppb" class="accordion">PPPPB <a href="/text/collections#ppppb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>South African Plant Pathogenic and Plant Protecting Bacteria, Agricultural Research Council, Plant Protection Research Institute, Private Bag X 134, Pretoria 0001, South Africa. <b>Country code:</b> ZA. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/818" class="">818</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="prl" class="accordion">PRL <a href="/text/collections#prl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Prairie Regional Laboratory, Saskatoon, Canada. <b>Country code:</b> CA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="psa" class="accordion">PSA <a href="/text/collections#psa" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Progetto Sistematica Actinomiceti, Institute of Microbiology, Milano University, Milano, Italy. <b>Country code:</b> IT. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ptcc" class="accordion">PTCC <a href="/text/collections#ptcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.irost.org/en/ptcc/index.asp?code=1" class="">Pakistan Type Culture Collections, Biotechnology and Food Research Center. Pakistan Council of Scientific and Industrial Research, Lahore, Punjab, 54600, Pakistan.</a> <b>Country code:</b> PK. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/753" class="">753</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ptcci" class="accordion">PTCCI <a href="/text/collections#ptcci" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://irost.org/ptcc/en/" class="">Persian Type Culture Collection, Iranian Research Organization for Science and Technology (IROST), Biotechnology Research Center, No.71, Forsat st, Ferdowsi sq, Tehran, I.R.Iran.</a> <b>Country code:</b> IR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/124" class="">124</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="pycc" class="accordion">PYCC <a href="/text/collections#pycc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://pycc.bio-aware.com/" class="">Portuguese Yeast Culture Collection, C. R. M., New University of Lisbon, Lisbon, Portugal.</a> <b>Country code:</b> PT. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/595" class="">595</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="pzh" class="accordion">PZH <a href="/text/collections#pzh" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Cultures, Institute of Hygiene, Warsow, Poland. <b>Country code:</b> PL. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="qm" class="accordion">QM <a href="/text/collections#qm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Quartermaster Research and Development Center, US Army, Natick, MA, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="qualicontm" class="accordion">QualiconTM <a href="/text/collections#qualicontm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Qualicon Europe Ltd, Drakes Court, Wythall, 302 Alcester Road, Birmingham B47 6JR, United Kingdom. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="rb" class="accordion">RB <a href="/text/collections#rb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Raiffeisen-Bioforschung GmbH, Tulln, Austria. <b>Country code:</b> AT. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 17.</p>
</div>
<button id="rbcar" class="accordion">RBCAR <a href="/text/collections#rbcar" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.rbcar.ro/index.htm" class="">Romanian Bioresource Centre and Advanced Research, Sector 6, Bucharest Romania.</a> <b>Country code:</b> RO. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/928" class="">928</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="rbf" class="accordion">RBF <a href="/text/collections#rbf" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Raiffeisen Bioforschung, Tullun, Austria. <b>Country code:</b> AT. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="rcam" class="accordion">RCAM <a href="/text/collections#rcam" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.arriam.spb.ru/eng/lab10/" class="">All-Russian Research Institute for Agricultural Microbiology, St. Petersburg, Russia.</a> <b>Country code:</b> RU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/966" class="">966</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 4.</p>
</div>
<button id="rcc" class="accordion">RCC <a href="/text/collections#rcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.sb-roscoff.fr/Phyto/RCC/" class="">Roscoff Culture Collection of Marine Phytoplancton, Station Biologique, Place G. Tessier, 29680 Roscoff, France.</a> <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/829" class="">829</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 7.</p>
</div>
<button id="rcdm" class="accordion">RCDM <a href="/text/collections#rcdm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Republican Centre for Deposition of Microorganisms of the National Academy of Sciences and Ministry of Education and Science of Armenia, Arzni str.6, Abovian 378510, Armenia. <b>Country code:</b> AM. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="rcs" class="accordion">RCS <a href="/text/collections#rcs" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Imperial College of Science and Technology, London University, Prince Consort Road, London SW7 2BB, United Kingdom. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="rdcm" class="accordion">RDCM <a href="/text/collections#rdcm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Culture Collection of Armenia for Microorganisms. <b>Country code:</b> AM. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="rgm" class="accordion">RGM <a href="/text/collections#rgm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#cchrgm" class="">CChRGM.</a> <b>Country code:</b> CL. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="rh" class="accordion">RH <a href="/text/collections#rh" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Dr R Hugh, George Washington University, Washington, DC, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 8.</p>
</div>
<button id="rhmu" class="accordion">RHMU <a href="/text/collections#rhmu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Pathology, Faculty of Medical Science, Ramathibordi Hospital, Mahidol University, Rama VI Road, Bangkok, Payathai, 10400, Thailand. <b>Country code:</b> TH. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/15" class="">15</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ria" class="accordion">RIA <a href="/text/collections#ria" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of the Institute for New Antibiotics, Russian Academy of Medical Sciences, Bolshaja Pirogovskaja 11, Moscow, 119867, Russia. <b>Country code:</b> RU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/337" class="">337</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 427.</p>
</div>
<button id="rib" class="accordion">RIB <a href="/text/collections#rib" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Research Institute of Brewing, 3-7-1 Kagamiyama, Higashi-hiroshima, Hiroshima, 739-0046, Japan. <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/640" class="">640</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="rifis" class="accordion">RIFIS <a href="/text/collections#rifis" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of Microorganisms with Application in the Fodder Industry, Food Research Institute, Radiová 7, 102 31 Praha 10, Czech Republic. <b>Country code:</b> CZ. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="rify" class="accordion">RIFY <a href="/text/collections#rify" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Research Institute of Fermentation, Yamanashi University, Kofu, Japan. <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/749" class="">749</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="rimd" class="accordion">RIMD <a href="/text/collections#rimd" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Research Institute for Microbial Diseases, Research Center for Emerging Infectious Diseases, Osaka University, 3-1 Yamadaoka, Suita, Osaka, 565-0071, Japan. <b>Country code:</b> JP. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/301" class="">301</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ritfc" class="accordion">RITFC <a href="/text/collections#ritfc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Research Institute for Tobacco and Fibre Crops Address: J1. Raya Karang Ploso, P.O.Box 199, Malang, Indonesia. <b>Country code:</b> ID. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/625" class="">625</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="rkm" class="accordion">RKM <a href="/text/collections#rkm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>The Republic collection of microorganisms, The National center for biotechnology of the Republic of Kazakhstan, Valihanova, 43, Astana 010000, Kazakhstan. <b>Country code:</b> KZ. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/907" class="">907</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="rlcc" class="accordion">RLCC <a href="/text/collections#rlcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Roussel Laboratories Culture Collection, Microbiological QC, Roussel Laboratories Ltd, Kingfisher Drive, Covingham, Swindon, Wiltshire, United Kingdom. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="rm" class="accordion">RM <a href="/text/collections#rm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Rumen Microorganisms, Grasslands Research Centre, AgResearch, Private Bag 11008, Palmerston North, New Zealand. <b>Country code:</b> NZ. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/764" class="">764</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 4.</p>
</div>
<button id="rmf" class="accordion">RMF <a href="/text/collections#rmf" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Rocky Mountain Herbarium, Fungi, University of Wyoming, Laramie, WY, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="rmit" class="accordion">RMIT <a href="/text/collections#rmit" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Royal Melbourne Institute of Technology, Melbourne, Australia 3001. <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="rml" class="accordion">RML <a href="/text/collections#rml" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>National Institute of Allergy and Infectious Diseases, Rocky Mountain Laboratories Collection, Hamilton, Montana 59840, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="rrlb" class="accordion">RRLB <a href="/text/collections#rrlb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Microbiology, Regional Research Laboratory, Bhubaneswar 751 013, Orissa, India. <b>Country code:</b> IN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="rscs" class="accordion">RSCS <a href="/text/collections#rscs" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Republican Specialized Centre of Surgery, Medical Culture Collection, Farkhadskaya str., 10, Tashkent, 700115, Uzbekistan. <b>Country code:</b> UZ. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/877" class="">877</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="rskk" class="accordion">RSKK <a href="/text/collections#rskk" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Refik Saydam National Type Culture Collection, Refik Saydam National Institute of Hygiene, Cemal Gursel Cad. No:18, Sihhiye, Ankara 06100, Turkey. <b>Country code:</b> TR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/828" class="">828</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="rtci" class="accordion">RTCI <a href="/text/collections#rtci" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Research Laboratories, Takeda Chemical Industries Ltd., Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="rv" class="accordion">RV <a href="/text/collections#rv" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Leptospira Strains, Istituto Superiore di Sanita, Roma-Nomentano, Italy. <b>Country code:</b> IT. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/421" class="">421</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="rvau" class="accordion">RVAU <a href="/text/collections#rvau" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Strains Collection, Department of Veterinary Microbiology, The Royal Veterinary and Agricultural University, Bülowsvej 13, DK-1870, Frederiksberg C, Denmark. <b>Country code:</b> DK. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="sabammrccc" class="accordion">SABAMMRCCC <a href="/text/collections#sabammrccc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>South American Biotechnology and Applied Microbiology, Microbiological Resource Center Culture Collection (United Nations Educational, Scientific, and Cultural Organization), Tucumán, Argentina. <b>Country code:</b> AR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="sag" class="accordion">SAG <a href="/text/collections#sag" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://uni-goettingen.de/en/45175.html" class="">Sammlung von Algenkulturen, Universität Göttingen, Albrecht-von-Haller-Institut für Pflanzenwissenschaften, Untere Karspüle 2, D-37073 Göttingen, Germany.</a> <b>Country code:</b> DE. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/192" class="">192</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 15.</p>
</div>
<button id="saitp" class="accordion">SAITP <a href="/text/collections#saitp" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>School of Pharmacy and Medical Sciences, University of South Australia, North Terrace, Adelaide. SA. 5000, Australia. <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/569" class="">569</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="sarc" class="accordion">SARC <a href="/text/collections#sarc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.arc.agric.za" class="">South African Rhizobium Collection, Pretoria, South Africa.</a> <b>Country code:</b> ZA. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/968" class="">968</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="sarcc" class="accordion">SARCC <a href="/text/collections#sarcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>South African Rhizobium Collection, Pretoria, South Africa. See: <a href="/text/collections#sarc" class="">SARC.</a> <b>Country code:</b> ZA. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 6.</p>
</div>
<button id="sbt" class="accordion">SBT <a href="/text/collections#sbt" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Technology and Research Institute, Snow Brand Milk Products Co., Ltd, Kawagoe, Saitama, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="sc" class="accordion">SC <a href="/text/collections#sc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Squibb Institute for Medical Research, New Brunswick, New Jersey, USA. <b>Country code:</b> JE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 15.</p>
</div>
<button id="sccm" class="accordion">SCCM <a href="/text/collections#sccm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Sporometrics Culture Collection of Microorganisms, Sporometrics Inc., 219 Dufferin Street, Suite 20C, Toronto, Ontario, M6K 1Y9, Canada. <b>Country code:</b> CA. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/920" class="">920</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="scsio" class="accordion">SCSIO <a href="/text/collections#scsio" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>South China Sea Institute of Oceanology, Chinese Academy of Sciences, Sanya, 572000, PR China. <b>Country code:</b> CN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 32.</p>
</div>
<button id="sebr" class="accordion">SEBR <a href="/text/collections#sebr" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Sanofi ELF Biorecherches, Labège Innopole, BP 137, 31676 Labège Cedex, France. <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 15.</p>
</div>
<button id="semia" class="accordion">SEMIA <a href="/text/collections#semia" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Colecao de Culturas de Rhizobium da Fepagro, Fundacao Estadual de Pesquisa Agropecuaria (FEPAGRO), Rua Goncalves Dias, 570, CEP90 130.060, Porto Alegre, Rio Grande do sul, Brazil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/443" class="">443</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 8.</p>
</div>
<button id="sfri" class="accordion">SFRI <a href="/text/collections#sfri" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Soil and Fertilizer Research Institute, Chinese Academy of Agricultural Sciences, Beijiing, People's Republic of China. <b>Country code:</b> CN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="sg" class="accordion">SG <a href="/text/collections#sg" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Schott and Gen. Jena, Mikrobiologisches Labor, Jena, Germany. <b>Country code:</b> DE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 20.</p>
</div>
<button id="sgsc" class="accordion">SGSC <a href="/text/collections#sgsc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.ucalgary.ca/~kesander/" class="">Salmonella Genetic Stock Centre, Department of Biological Sciences, 2500 University Dr. N.W., Calgary, Alberta, Canada.</a> <b>Country code:</b> CA. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/338" class="">338</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="sicgh" class="accordion">SICGH <a href="/text/collections#sicgh" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Social Insurance Central General Hospital, Tokyo, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="siia" class="accordion">SIIA <a href="/text/collections#siia" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Sichuan Industrial Institute of Antibiotics, Chengdu, Sichuan, People's Republic of China. <b>Country code:</b> CN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="skf" class="accordion">SK&amp;F <a href="/text/collections#skf" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Smith Kline and French Laboratories, Philadelphia, Pennsylvania 19101, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 4.</p>
</div>
<button id="skuk" class="accordion">SKUK <a href="/text/collections#skuk" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Simpanan Kultur Universiti Kebangsaan, Universiti Kebangsaan Malaysia, Bangi, Selangor, Malaysia. <b>Country code:</b> MY. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/565" class="">565</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="slcc" class="accordion">SLCC <a href="/text/collections#slcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Special Listeria Culture Collection, Institute of Hygiene and Microbiology, University of Würzburg, Würzburg, Germany. <b>Country code:</b> DE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 5.</p>
</div>
<button id="smcc" class="accordion">SMCC <a href="/text/collections#smcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Soil Microbiology Culture Collection, CSIRO Division of Soils, Private Bag No 2, Glen Osmond. SA. 5064, Australia. Also used as acronym of the Subsurface Microbial Culture Collection, Portland State University, Portland, Oregon, USA. <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 10.</p>
</div>
<button id="smcc-w" class="accordion">SMCC-W <a href="/text/collections#smcc-w" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Subsurface Microbial Culture Collection, Western Branch, Oregon Graduate Institute of Science and Technology, Portland, Oregon 97291-1000, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="smg" class="accordion">SMG <a href="/text/collections#smg" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Sammlung für Mikroorganismen Göttingen, Gottingen, Germany. See: <a href="/text/collections#dsmz" class="">DSMZ.</a> <b>Country code:</b> DE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 26.</p>
</div>
<button id="smtwa" class="accordion">SMTWA <a href="/text/collections#smtwa" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>School of Medical Technology Western Australia, School of Medical Technology, Curtin University of Technology, GPO Box U1987, Perth. WA. 6001, Australia. <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/90" class="">90</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="smum" class="accordion">SMUM <a href="/text/collections#smum" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>St Marianna University School of Medicine, Kawasaki, Kanagawa, 216-8511, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="sn" class="accordion">SN <a href="/text/collections#sn" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#amp" class="">AMP.</a> <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 17.</p>
</div>
<button id="spmcc" class="accordion">SPMCC <a href="/text/collections#spmcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Sungei Putih Microbial Culture Collection, Sungei Putih Research Center for Estate Crops Address: P.O.Box 416, Medan 20000, Indonesia. <b>Country code:</b> ID. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/624" class="">624</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="sraicc" class="accordion">SRAICC <a href="/text/collections#sraicc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>SRAI's culture collection, Scientific Research Agricultural Institute, Gvardeiskiy, Zhambylskaya oblast', 485444, Kazakhstan. <b>Country code:</b> KZ. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/848" class="">848</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="src-ccm" class="accordion">SRC-CCM <a href="/text/collections#src-ccm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Cultures of Microorganisms, VECTOR - State Research Center of Virology and Biotechnology, 633159 Koltsovo, Novosibirsk region, Russia. See: <a href="/text/collections#src" class="">SRC.</a> <b>Country code:</b> RU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="sri" class="accordion">SRI <a href="/text/collections#sri" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Sugar Research Institute, Mackay, Australia. <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="srrc" class="accordion">SRRC <a href="/text/collections#srrc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Southern Regional Research Center, Agricultural Research Service, US Department of Agriculture, New Orleans, LA, USA. <b>Country code:</b> US. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/751" class="">751</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ssi" class="accordion">SSI <a href="/text/collections#ssi" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>The International Escherichia and Klebsiella Centre (WHO), Statens Serum Institut, 5 Artillerivej, Copenhagen 2300 S, Denmark. <b>Country code:</b> DK. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/158" class="">158</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ssic" class="accordion">SSIC <a href="/text/collections#ssic" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collaborating Centre for Reference and Research on Escherichia and Klebsiella, Statens Serum Institute, 5 Artillerivei, Copenhagen 2300 S, Denmark. <b>Country code:</b> DK. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="st-ivel" class="accordion">ST-IVEL <a href="/text/collections#st-ivel" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Starter and Development Laboratory, St Ivel, Station Road, Wooton Barrett, Wiltshire, United Kingdom. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="stm" class="accordion">STM <a href="/text/collections#stm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Laboratoire des Symbioses Tropicales et Méditerranéennes, UMR 113, Campus International de Baillarguet TA 10/J, 34398 Montpellier Cedex 05, France. <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 18.</p>
</div>
<button id="swc" class="accordion">SWC <a href="/text/collections#swc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Suzugamine Women's College, Hiroshima, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="sysu" class="accordion">SYSU <a href="/text/collections#sysu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.sysu.edu.cn/en/index.htm" class="">State Key Laboratory of Biocontrol and Guangdong Provincial Key Laboratory of Plant Resources, Sun Yat-Sen University, Guangzhou, 510275, PR China.</a> <b>Country code:</b> CN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1176" class="">1176</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 59.</p>
</div>
<button id="tama" class="accordion">TAMA <a href="/text/collections#tama" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Mycology and Metabolic Diversity Research Center, Tamagawa University Research Institute, Machida, Tokyo, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="tau-mac" class="accordion">TAU-MAC <a href="/text/collections#tau-mac" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://cyanolab.bio.auth.gr/" class="">Thessaloniki Aristotle University Microalgae and Cyanobacteria Collection, School of Biology, Aristotle University Campus, Box 109, Thessaloniki, Macedonia, 54124 Greece.</a> <b>Country code:</b> GR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1156" class="">1156</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 10.</p>
</div>
<button id="tbrc" class="accordion">TBRC <a href="/text/collections#tbrc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.tbrcnetwork.org/" class="">Thailand Bioresource Research Center, National Center for Genetic Engineering and Biotechnology Innovation Cluster 2 (Tower B, 8th Floor), 143 Thailand Science Park, Phahonyothin Road, Khlong Nueng, Khlong Luang, Pathum Thani 12120, Thailand.</a> <b>Country code:</b> TH. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1090" class="">1090</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 85.</p>
</div>
<button id="tc" class="accordion">TC <a href="/text/collections#tc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Thaxter Collection, Farlow Herbarium, Harvard University, Boston, Massachusetts 02138, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 12.</p>
</div>
<button id="tcb" class="accordion">TCB <a href="/text/collections#tcb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.liverpool.ac.uk/infection-and-global-health/research/tick-cell-biobank/" class="">Tick Cell Biobank, Institute of Infection and Global Health, University of Liverpool, Liverpool, UK.</a> <b>Country code:</b> GB. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="tcc" class="accordion">TCC <a href="/text/collections#tcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www6.inrae.fr/carrtel-collection_eng/" class="">Thonon Culture Collection, 75 av. de Corzen, BP 511, Thonon-Les-Bains, Savoie, 74203.</a> <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1030" class="">1030</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="tcfb" class="accordion">TCFB <a href="/text/collections#tcfb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Tasmanian Collection of Fish Bacteria, Fish Health Unit, Department of Primary Industries and Water, 165 Westbury Road, Launceston, Tasmania, 7250, Australia. <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/802" class="">802</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="thg" class="accordion">THG <a href="/text/collections#thg" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>An acronym frequently used by mainly Korean researchers. Despite repeated attempts by LPSN to contact the corresponding authors of publications that use this acronym, LPSN was unable to obtain information about its meaning. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 73.</p>
</div>
<button id="ti" class="accordion">TI <a href="/text/collections#ti" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Herbarium of the Department of Botany, Faculty of Science, University of Tokyo, Tokyo, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="timm" class="accordion">TIMM <a href="/text/collections#timm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institute of Medical Mycology, Teikyo University, Hachioji, Tokyo. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/750" class="">750</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="tistr" class="accordion">TISTR <a href="/text/collections#tistr" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.tistr.or.th/tistr_culture/" class="">Thailand Institute of Scientific and Technological Research, 196 Phahonyothin Rd, Chatuchak, Bangkok 10900, Thailand.</a> <b>Country code:</b> TH. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/383" class="">383</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 126.</p>
</div>
<button id="tkbc" class="accordion">TKBC <a href="/text/collections#tkbc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institute of Biological Sciences, University of Tsukuba, Tsukuba, Ibaraki, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="tmc" class="accordion">TMC <a href="/text/collections#tmc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.trudeauinstitute.org/" class="">Trudeau Mycobacterium Collection, Trudeau Institute, 100 Algonquin Avenue, Saranac Lake, NY 12983, USA.</a> <b>Country code:</b> US. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/858" class="">858</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="tmi" class="accordion">TMI <a href="/text/collections#tmi" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Tottori Mycological Institute, Japan Kinoko Research Center Foundation, Tottori, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="tmw" class="accordion">TMW <a href="/text/collections#tmw" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Technische Mikrobiologie Weihenstephan, Technische Universität München, Lehrstuhl für Technische Mikrobiologie, Weihenstephaner Steig 16, 85350 Freising, Germany. <b>Country code:</b> DE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 16.</p>
</div>
<button id="tncc" class="accordion">TNCC <a href="/text/collections#tncc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www1a.biotec.or.th/TNCC/" class="">Thailand Network on Culture Collections.</a> <b>Country code:</b> TH. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="tph" class="accordion">TPH <a href="/text/collections#tph" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Microbiological Culture Collection, Public Health Laboratory, Ontario Department of Health, Toronto 116, Canada. <b>Country code:</b> CA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="trm" class="accordion">TRM <a href="/text/collections#trm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.taru.edu.cn/" class="">College of Life Science, Tarim University, Alar 843300, PR China.</a> <b>Country code:</b> CN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 41.</p>
</div>
<button id="tua" class="accordion">TUA <a href="/text/collections#tua" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Agricultural Chemistry, Tokyo University of Agriculture, Sakuraga-oka 1-1-1n Setagaya-ku, Tokyo 156, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="uamh" class="accordion">UAMH <a href="/text/collections#uamh" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.uamh.ca/" class="">UAMH Center for Global Microfungal Biodiversity, Dalla Lana School of Public Health, University of Toronto, 223 College St., Toronto ON, Canada M5T 1R4.</a> <b>Country code:</b> CA. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/73" class="">73</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="uasm" class="accordion">UASM <a href="/text/collections#uasm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>University of Alberta Soil Microbiology, Edmonton, Alberta T6G 2E9, Canada. <b>Country code:</b> CA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 4.</p>
</div>
<button id="uba" class="accordion">UBA <a href="/text/collections#uba" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Microbiological Resource Center Culture Collection, South American Biotechnology and Applied Microbiology, Tucuman, Argentina. <b>Country code:</b> AR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ubc" class="accordion">UBC <a href="/text/collections#ubc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>University of British Columbia, Vancouver, B.C., Canada. <b>Country code:</b> CA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ubocc" class="accordion">UBOCC <a href="/text/collections#ubocc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.univ-brest.fr/ubocc" class="">Université de Bretagne Occidentale Culture Collection, Centre de Ressources UBOCC ESIAB, Technopôle Brest-Iroise, Parvis Blaise Pascal, 29280 Plouzané, France.</a> <b>Country code:</b> FR. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 9.</p>
</div>
<button id="uc" class="accordion">UC <a href="/text/collections#uc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Upjohn Culture Collection, The Upjohn Co. Kalamazoo, MI, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 6.</p>
</div>
<button id="uccm" class="accordion">UCCM <a href="/text/collections#uccm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>University of Calabar Collection of Microorganisms, University of Calabar, Dept. of Biological Sciences, Calabar, Cross River, Nigeria. <b>Country code:</b> NG. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/652" class="">652</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ucd" class="accordion">UCD <a href="/text/collections#ucd" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://phaffcollection.ucdavis.edu/index.htm" class="">University of California, Dept. of Food Science and Technology, Davis, California, USA.</a> <b>Country code:</b> US. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="ucl" class="accordion">UCL <a href="/text/collections#ucl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Catholic University of Louvain, Av. Hippocrate 54, B-1200 Brussels, Belgium. <b>Country code:</b> BE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="uclaf" class="accordion">UCLAF <a href="/text/collections#uclaf" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>HMR/Romainville, Hoechst Marion Roussel, 102 Route de Noisy, 93235 Romainville, France. <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/552" class="">552</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ucm" class="accordion">UCM <a href="/text/collections#ucm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://ucm.org.ua/" class="">Ukrainian Collection of Microorganisms, Zabolotny Institute of Microbiology and Virology, 143 Zabolotny Srt. 252143 Kyiv, Ukraine.</a> <b>Country code:</b> UA. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1203" class="">1203</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 23.</p>
</div>
<button id="ufpeda" class="accordion">UFPEDA <a href="/text/collections#ufpeda" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Universidade Federal de Pernambuco, Departmento de Antibioticos, Av. Prof. Moraes Rego, S/N, Recife, Pernambuco, 50739, Brazil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/114" class="">114</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ufrjim" class="accordion">UFRJIM <a href="/text/collections#ufrjim" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Departamento de Microbiologia Medica, Instituto de Microbiologia, Universidade Federal do Rio de Janeiro, Av. Brigadeiro Trompowski, S/N, CCS, Cidade Universitaria, 21.944 Rio de Janeiro, RJ, Cx. Postal 68040, Brazil. <b>Country code:</b> BR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/725" class="">725</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="uicc" class="accordion">UICC <a href="/text/collections#uicc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>University of Indonesia Culture Collection, Department of Biology, Faculty of Mathematics and Sciences, University of Indonesia, Depok 16424, Indonesia. <b>Country code:</b> ID. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/563" class="">563</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="ujb" class="accordion">UJB <a href="/text/collections#ujb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>University of Jaffna Botany, Dept. of Botany, Jaffna, Sri Lanka. <b>Country code:</b> LK. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/619" class="">619</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ukkp" class="accordion">UKKP <a href="/text/collections#ukkp" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Universiti Kebangsaan Kultur Perubatan, Universiti Kebangsaan Malaysia, Jalan Raja Muda, Kuala Lumpur, Wilayah Persekutuan, 50300, Malaysia. <b>Country code:</b> MY. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/43" class="">43</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ukncc" class="accordion">UKNCC <a href="/text/collections#ukncc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.ukncc.co.uk/" class="">United Kingdom National Culture Collection (The United Kingdom National Culture Collection co-ordinates the activities, marketing and research of the UK national service collections).</a> <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ulc" class="accordion">ULC <a href="/text/collections#ulc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://bccm.belspo.be/catalogues/catalogue-search?collection=ULC" class="">BCCM/ULC Culture Collection of (sub)polar cyanobacteria, University of Liège, Allee du 6 Août 11, B-4000 Liège.</a> <b>Country code:</b> BE. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/982" class="">982</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 6.</p>
</div>
<button id="umass" class="accordion">UMASS <a href="/text/collections#umass" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>University of Massachusetts, Institute of Microbiology, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="umfftd" class="accordion">UMFFTD <a href="/text/collections#umfftd" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Food and Fermentation Technology Division, Dept. of Chemical Technology, University of Mumbai, Nathalal Parekh Marg, Mumbai, Maharashtra, 400 019, India. <b>Country code:</b> IN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/562" class="">562</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="umh" class="accordion">UMH <a href="/text/collections#umh" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>University of Missouri Dunn-Palmer Herbarium, University of Missouri-Columbia, Columbia, MO 65211, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="umip" class="accordion">UMIP <a href="/text/collections#umip" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection de Champignons et Actinomycètes Pathogènes, Institut Pasteur, 28 rue du Dr Roux, Paris 75724 Cedex 15, France. <b>Country code:</b> FR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/344" class="">344</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="uniqem" class="accordion">UNIQEM <a href="/text/collections#uniqem" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.fbras.ru/en/services/ckp/tskp-kollektsiya-uniqem" class="">Unique and Extremophilic Microorganisms Collection of Winogradsky Institute of Microbiology RAS, Prospect 60 let Oktyabrya, 7/2, 117312 Moscow, Russia.</a> <b>Country code:</b> RU. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 182.</p>
</div>
<button id="uniquem" class="accordion">UNIQUEM <a href="/text/collections#uniquem" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Incorrect acronym for UNIQEM. See: <a href="/text/collections#uniqem" class="">UNIQEM.</a> <b>Country code:</b> RU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="unsw" class="accordion">UNSW <a href="/text/collections#unsw" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>University of New South Wales Culture Collection, The Culture Collection, School of Microbiology and Immunology, University of NSW, NSW 2052, Australia. The UNSW Microbiology Culture Collection no longer exists (it closed down over 5 years ago). We transferred many of our strains to [...] <a href="http://www.ifmqs.com.au" class="">IFM Quality Services Pty Ltd</a> [...] (Jones, K., pers. comm., February 2020). <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="unswcc" class="accordion">UNSWCC <a href="/text/collections#unswcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>University of New South Wales Culture Collection, The Culture Collection, School of Microbiology and Immunology, University of NSW, NSW 2052, Australia. The UNSW Microbiology Culture Collection no longer exists (it closed down over 5 years ago). We transferred many of our strains to [...] <a href="http://www.ifmqs.com.au" class="">IFM Quality Services Pty Ltd</a> [...] (Jones, K., pers. comm., February 2020). <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="upcc" class="accordion">UPCC <a href="/text/collections#upcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Natural Sciences Research Institute Culture Collection, University of the Philippines, Southeast Corner Quirino Avenue and Velasquez Street, Quezon City 1101, Philippines. <b>Country code:</b> PH. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/310" class="">310</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="upl" class="accordion">UPL <a href="/text/collections#upl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Université Louis Pasteur, Strasbourg, France. <b>Country code:</b> FR. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="upm" class="accordion">UPM <a href="/text/collections#upm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Departamento de Microbiologia, E.T.S. de Ingenerios Agronomos, Universidad Politecnica, Madrid, Spain. <b>Country code:</b> ES. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="upmr" class="accordion">UPMR <a href="/text/collections#upmr" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Universiti Pertanian Malaysia Rhizobium Collection, Department of Soil Science, Universiti Pertanian Malaysia, Serdang, Selangor, Malaysia. <b>Country code:</b> MY. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/25" class="">25</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="uprm" class="accordion">UPRM <a href="/text/collections#uprm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Rhizobium Culture Collection, University of Puerto Rico, BNF Laboratory, Dept.of Agronomy and Soils, Mayaguez, Puerto Rico, 00681-9030. <b>Country code:</b> PR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/76" class="">76</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="upsc" class="accordion">UPSC <a href="/text/collections#upsc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Fungal Culture Collection at the Botanical Museum, Uppsala University, Uppsala, Sweden. <b>Country code:</b> SE. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/603" class="">603</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="uqb" class="accordion">UQB <a href="/text/collections#uqb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>University of Queensland Microbiology Collection, University of Queensland, Queensland, Australia. <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="uqm" class="accordion">UQM <a href="/text/collections#uqm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection, Department of Microbiology, University of Queensland, St. Lucia, Queensland 4067, Australia. See: <a href="/text/collections#acm" class="">ACM.</a> <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 26.</p>
</div>
<button id="usba" class="accordion">USBA <a href="/text/collections#usba" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Unidad de Saneamiento y Biotecnología Ambiental, Departamento de Biología, Pontificia Universidad Javeriana, POB 56710, Bogotá, Colombia. <b>Country code:</b> CO. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 5.</p>
</div>
<button id="uscc" class="accordion">USCC <a href="/text/collections#uscc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>University of Surrey Culture Collection, Department of Microbiology, University of Surrey, Guilford, UK. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="usda" class="accordion">USDA <a href="/text/collections#usda" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.ars-grin.gov/Rhizobium" class="">Beltsville Rhizobium Culture Collection, Beltsville Agricultural Research Center, United States Department of Agriculture, Beltsville, Md., USA.</a> <b>Country code:</b> US. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 18.</p>
</div>
<button id="usfcc" class="accordion">USFCC <a href="/text/collections#usfcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>U.S. Federation for Culture Collections. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="utcc" class="accordion">UTCC <a href="/text/collections#utcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#cpcc" class="">CPCC.</a> <b>Country code:</b> CA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="utex" class="accordion">UTEX <a href="/text/collections#utex" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://utex.org/" class="">The Culture Collection of Algae at the University of Texas Austin, MCDB 1 University Station A6700, University of Texas, Austin, TX 78712-0183, USA.</a> <b>Country code:</b> US. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/606" class="">606</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 13.</p>
</div>
<button id="utmb" class="accordion">UTMB <a href="/text/collections#utmb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.utmb.edu/pathology" class="">University of Texas Medical Branch, Department of Pathology, Galveston, Texas, USA.</a> <b>Country code:</b> US. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="utmc" class="accordion">UTMC <a href="/text/collections#utmc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>University of Tehran Microorganisms Collection, Enghelab Ave., Tehran, P.O. Box 14155-6455, Tehran, 1417864411. <b>Country code:</b> IR. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/937" class="">937</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 8.</p>
</div>
<button id="uuc" class="accordion">UUC <a href="/text/collections#uuc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Janet A. Robertson Collection of Ureaplasma urealyticum Cultures, Department of Medical Microbiology, University of Alberta, Medical Sciences Building, Edmonton, Alberta, T6G 2H7, Canada. <b>Country code:</b> CA. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/745" class="">745</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="uwo" class="accordion">UWO <a href="/text/collections#uwo" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>University of Western Ontario Culture Collection, University of Western Ontario, London, Ontario N6A 587, Canada. <b>Country code:</b> CA. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/91" class="">91</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 5.</p>
</div>
<button id="vcp" class="accordion">VCP <a href="/text/collections#vcp" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Victorian College of Pharmacy, Victorian College of Pharmacy, 381 Royal Parade, Parkville. Vic. 3052, Australia. <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="vcrc" class="accordion">VCRC <a href="/text/collections#vcrc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Volcani Center Rhizobium Collection, Dept. of Agronomy and Natural Resources Agriculture Research Organization The Volcani Center, P.O. Box 6, Bet Dagan 50 250, Israel. <b>Country code:</b> IL. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/144" class="">144</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="viam" class="accordion">VIAM <a href="/text/collections#viam" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Institute of Applied Microbiology, University of Agricultural Sciences, Vienna, Austria. <b>Country code:</b> AT. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="vizr" class="accordion">VIZR <a href="/text/collections#vizr" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of the Institute of Plant Protection, RAS, Shosse Podbelskogo, 3, Puskin-6, St.Petersburg, 189620, Russia. <b>Country code:</b> RU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/760" class="">760</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="vkm" class="accordion">VKM <a href="/text/collections#vkm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.vkm.ru/" class="">All-Russian Collection of Microorganisms, Russian Academy of Sciences, Institute of Biochemistry and Physiology of Microorganisms, 142292 Pushchino, Moscow Region, Russia.</a> <b>Country code:</b> RU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/342" class="">342</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 1229.</p>
</div>
<button id="vkpm" class="accordion">VKPM <a href="/text/collections#vkpm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://eng.genetika.ru/service-offer/vkpm/" class="">Russian National Collection of Industrial Microorganisms at the Institute of Genetics and Selection of Industrial Microorganisms, Dorozhnyi Proezd, 1, Moscow, 113545, Russia.</a> <b>Country code:</b> RU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/588" class="">588</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 8.</p>
</div>
<button id="vniiscm" class="accordion">VNIISCM <a href="/text/collections#vniiscm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection of the Institute of Agricultural Microbiology, Russian Academy of Agricultural Sciences, Shosse Podbelskogo 3, Pushkin-6, St.Petersburg, 189620, Russia. <b>Country code:</b> RU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="vpb" class="accordion">VPB <a href="/text/collections#vpb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Veterinary Pathology and Bacteriology Collection, University of Sydney, New South Wales 2006, Australia. <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 7.</p>
</div>
<button id="vpi" class="accordion">VPI <a href="/text/collections#vpi" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Anaerobe Laboratory, Virginia Polytechnic Institute and State University, Blacksburg, Virginia 24061, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 94.</p>
</div>
<button id="vpri" class="accordion">VPRI <a href="/text/collections#vpri" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Plant Research Institute Herbarium, Plant Research Institute Herbarium, Swan Street, Burnley. Vic. 3121, Australia. <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/851" class="">851</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="vruc" class="accordion">VRUC <a href="/text/collections#vruc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Vergata Rome University Culture Collection, Rome, Italy. <b>Country code:</b> IT. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="vsb" class="accordion">VSB <a href="/text/collections#vsb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Veterinary Pathology Bacteriology, Department of Veterinary Anatomy and Pathology, University of Sydney, Sydney. NSW. 2006, Australia. <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="vtcc" class="accordion">VTCC <a href="/text/collections#vtcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://vtcc.imbt.vnu.edu.vn/" class="">Vietnam Type Culture Collection, Institute of Microbiology and Biotechnology (IMBT), Vietnam National University, E2 Building, 144 Xuan Thuy street, Hanoi city, Hanoi, 84-043, Viet Nam.</a> <b>Country code:</b> VN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/933" class="">933</a>. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 27.</p>
</div>
<button id="vtt" class="accordion">VTT <a href="/text/collections#vtt" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://culturecollection.vtt.fi/" class="">Technical Research Center of Finland (Valtion Teknillinen Tutkimuskeskus), Biotechnology and Food Research, Culture Collection, PO Box 1501, FIN-02044 VTT, Finland.</a> <b>Country code:</b> FI. <b>Active BRC:</b> yes. <b>Linked:</b> yes. <b>Number of deposits in LPSN:</b> 9.</p>
</div>
<button id="vttcc" class="accordion">VTTCC <a href="/text/collections#vttcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://culturecollection.vtt.fi/" class="">VTT Culture Collection, VTT Technical Research Centre of Finland, P.O. Box 1000, FI-02044 VTT, Street address: Tietotie 2, Espoo, Finland.</a> <b>Country code:</b> FI. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/139" class="">139</a>. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="vut" class="accordion">VUT <a href="/text/collections#vut" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>School of Veterinary Medicine, Faculty of Agriculture, University of Tokyo, Tokyo, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="wa" class="accordion">WA <a href="/text/collections#wa" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Plant Research Division Culture Collection, Western Australian Department of Agriculture, Baron-May Court, South Perth. WA. 6151, Australia. <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 4.</p>
</div>
<button id="wac" class="accordion">WAC <a href="/text/collections#wac" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Plant Research Division Culture Collection, Western Australian Department of Agriculture, Baron-May Court, South Perth. WA. 6151, Australia. <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/77" class="">77</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="wacc" class="accordion">WACC <a href="/text/collections#wacc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Western Australian Culture Collection, State Health Laboratory Service, GPO Box F312, Perth. WA. 6001, Australia. <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/452" class="">452</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="waite" class="accordion">WAITE <a href="/text/collections#waite" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Insect Pathology Pathogen Collection, WAITE Agricultural Research Institute, 46 Sunnyside Road, Glen Osmond. SA. 5064, Australia. <b>Country code:</b> AU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/35" class="">35</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="wal" class="accordion">WAL <a href="/text/collections#wal" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Wadsworth Anaerobe Laboratory, Wadsworth Hospital Center, Veterans Administration, Wilshire and Sawtelle Blvds., Los Angeles, CA, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 25.</p>
</div>
<button id="warc" class="accordion">WARC <a href="/text/collections#warc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>New Zealand Reference Culture Collection, Wallaceville Animal Research Centre, Private Bag, Wellington, New Zealand. <b>Country code:</b> NZ. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/376" class="">376</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="wb" class="accordion">WB <a href="/text/collections#wb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Department of Bacteriology, University of Wisconsin, Madison, WI, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 4.</p>
</div>
<button id="wcum" class="accordion">WCUM <a href="/text/collections#wcum" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Working Collection, University of Maryland Biotechnology Institute, Center of Marine Biotechnology, 701 E. Pratt Street, Baltimore, MD, 21202, USA. <b>Country code:</b> US. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/56" class="">56</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="wdcm" class="accordion">WDCM <a href="/text/collections#wdcm" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.wdcm.org/" class="">Culture Collections in the World, Information Network Center, Institute of Microbiology, Chinese Academy of Sciences, 1 West Beichen Road, Chaoyang District, Beijing 100101, China.</a> <b>Country code:</b> CN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="wdds" class="accordion">WDds <a href="/text/collections#wdds" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Raul Lopez Sanchez, University of Granma, Bayamo, Granma, Cuba, Cuba. <b>Country code:</b> CU. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/812" class="">812</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="wfcc" class="accordion">WFCC <a href="/text/collections#wfcc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="http://www.wfcc.info/" class="">World Federation for Culture Collections.</a> <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="wfpl" class="accordion">WFPL <a href="/text/collections#wfpl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Western Forest Products Laboratory, Vancouver, British Columbia, Canada. <b>Country code:</b> CA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="who" class="accordion">WHO <a href="/text/collections#who" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p><a href="https://www.health.qld.gov.au/healthsupport/businesses/forensic-and-scientific-services/testing-analysis/diseases/leptospirosis" class="">WHO/FAO/OIE Collaborating Centre for Reference and Research on Leptospirosis, Western Pacific Region, Communicable Diseases, Queensland Health Forensic and Scientific Services, Brisbane, Australia.</a> <b>Country code:</b> AU. <b>Active BRC:</b> yes. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 3.</p>
</div>
<button id="windsor" class="accordion">WINDSOR <a href="/text/collections#windsor" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Culture Collection, University of Windsor, Windsor, Ontario, Canada. <b>Country code:</b> CA. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="wpbs" class="accordion">WPBS <a href="/text/collections#wpbs" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Welsh Plant Breeding Station, Nitrogen Fixation and Nutrient Cycling Group, Plant and Cell Biology Department, Plas Gogerddan, Aberystwyth, Dyfed SY23 3EB, United Kingdom. <b>Country code:</b> GB. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/607" class="">607</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="wr" class="accordion">WR <a href="/text/collections#wr" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Azotobacteraceae Collection, Queensland Wheat Research Institute, PO Box 5282, Toowoomba. Qld. 4350, Australia. <b>Country code:</b> AU. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 11.</p>
</div>
<button id="wri" class="accordion">WRI <a href="/text/collections#wri" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Worcester Royal Infirmary, Worcester, England. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="wrl" class="accordion">WRL <a href="/text/collections#wrl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>The Wellcome Bacterial Collection, PHLS Central Public Health Laboratory, 61 Colindale Avenue, London NW9 5HT, United Kingdom. <b>Country code:</b> GB. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/142" class="">142</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="wrrl" class="accordion">WRRL <a href="/text/collections#wrrl" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Western Utilization Research and Development Division, U.S. Department of Agriculture, Albany, California, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="ws" class="accordion">WS <a href="/text/collections#ws" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>General collection of bacteria, Unit of Microbiology, Zentralinstitut für Ernährungs- und Lebensmittelforschung (ZIEL), Technische Universität München, Freising-Weihenstephan, Germany. <b>Country code:</b> DE. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/1163" class="">1163</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 26.</p>
</div>
<button id="wsbc" class="accordion">WSBC <a href="/text/collections#wsbc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Research collection of Bacillus cereus group species, Unit of Microbiology, Zentralinstitut für Ernährungs- und Lebensmittelforschung (ZIEL), Technische Universität München, Freising-Weihenstephan, Germany. <b>Country code:</b> DE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 2.</p>
</div>
<button id="wsf" class="accordion">WSF <a href="/text/collections#wsf" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Wisconsin Soil Fungi Collection, Madison, WI, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="wslc" class="accordion">WSLC <a href="/text/collections#wslc" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Research collection of Listeria, Unit of Microbiology, Zentralinstitut für Ernährungs- und Lebensmittelforschung (ZIEL), Technische Universität München, Freising-Weihenstephan, Germany. <b>Country code:</b> DE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="wsro" class="accordion">WSRO <a href="/text/collections#wsro" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Collection of Dairy Cultures (Laboratory of the Culture Collection), Agricultural-Technical Academy, Department of Microbiology, Pl. Cieszynski 1 (= Kortowo Bl. 43), 10-957 Olsztyn, Poland. <b>Country code:</b> PL. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="wvb" class="accordion">WVB <a href="/text/collections#wvb" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Wuhan Institute of Virology, Academia Sinica Wuhan, Hubei, People's Republic of China. <b>Country code:</b> CN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="wvdh" class="accordion">WVDH <a href="/text/collections#wvdh" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>West Virginia Hygienic Laboratory, West Virginia Department of Health, 167 11th Avenue, South Charleston, West Virginia, 25303, USA. <b>Country code:</b> US. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/411" class="">411</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="wvu" class="accordion">WVU <a href="/text/collections#wvu" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>West Virginia University, Department of Microbiology, Medical Center, Morgantown, West Virginia 26506, USA. <b>Country code:</b> US. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 1.</p>
</div>
<button id="yblf" class="accordion">YBLF <a href="/text/collections#yblf" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Yamanouchi Pharmaceutical Co., Ltd., Tokyo, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="yfi" class="accordion">YFI <a href="/text/collections#yfi" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#rify" class="">RIFY.</a> <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="yim" class="accordion">YIM <a href="/text/collections#yim" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Yunnan Institute of Microbiology, Yunnan University, Kunming 650091, P.R. China. <b>Country code:</b> CN. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 330.</p>
</div>
<button id="yit" class="accordion">YIT <a href="/text/collections#yit" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Yakult Central Institute for Microbiological Research, 1796 Yaho, Kunitachi, Tokyo 186-8650, Japan. <b>Country code:</b> JP. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 33.</p>
</div>
<button id="ym" class="accordion">YM <a href="/text/collections#ym" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Strains Collection of Yunnan Institute of Microbiology, Yunnan University, Kunming, Yunnan, China, 650091. <b>Country code:</b> CN. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/832" class="">832</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 32.</p>
</div>
<button id="zeneca" class="accordion">ZENECA <a href="/text/collections#zeneca" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Jealott's Hill Research Station, Plant Pathology Department, Imperial Chemical Industries, Jealott's Hill, Bracknell, Berks. RG12 6EY, United Kingdom. <b>Country code:</b> GB. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>
</div>
<button id="zim" class="accordion">ZIM <a href="/text/collections#zim" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>Zbirka Industrijskih Mikrorganizmov (Collection of Industrial Microorganisms), Biotechnical Faculty, Jamnikarjeva 101, SI-1000 Ljubljana, Slovenia. <b>Country code:</b> SI. <b>WDCM number:</b> <a href="http://ccinfo.wdcm.org/collection/by_id/810" class="">810</a>. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 8.</p>
</div>
<button id="zimet" class="accordion">ZIMET <a href="/text/collections#zimet" class="anchorlink">   </a> </button>
              
              <div class="panel" style="border: 0px solid rgb(48, 76, 178);">

                <p>See: <a href="/text/collections#imet" class="">IMET.</a> <b>Country code:</b> DE. <b>Active BRC:</b> no. <b>Linked:</b> no. <b>Number of deposits in LPSN:</b> 0.</p>'''

m = re.findall(r'id=".*?"', texte)

str_collections = '('
for elmt in m:
    if str_collections != '(':
        str_collections += '|'
    
    short_elmt = elmt.replace('id=', '').strip('"')
    str_collections += short_elmt

str_collections += ')'
print(str_collections)



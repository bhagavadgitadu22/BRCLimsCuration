"""import psycopg2

def get_cursor(db_name):
    conn = psycopg2.connect(user="postgres",
                                  password="hercule1821",
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()

def main():
    # on établit les connections avec les 2 bdds
    cursor = get_cursor("brc_db")
    cursor_curated = get_cursor("brc_db_curated")

    str_base = open("../curation/validation_curation/25_toutes_souches_avec_infos.sql", "r").read()

    cursor.execute(str_base+" WHERE sch_identifiant = 'CRBIP3.1430'")
    record = cursor.fetchone()

    cursor_curated.execute(str_base+" WHERE sch_identifiant = 'CRBIP3.1430'")
    record_curated = cursor_curated.fetchone()

    if record != record_curated:
        if record[len(record)-7] != 401 or record_curated[len(record_curated)-7] != 401:
            print("difference")
            print(record)
            print(record_curated)
            print(record[len(record)-7])
            print(record_curated[len(record_curated)-7])
        else:
            print("fine")
            print(record[0])
            print(record_curated)

main()"""

import csv

array  = [56373, 564321, 59103, 60070, 4754104, 563467, 591873, 591889, 591905, 593772, 591921, 565474, 56136, 56167, 561569, 582280, 562057, 556250, 554774, 568804, 555265, 557001, 556303, 557018, 557033, 557474, 557490, 555297, 556216, 582297, 566492, 582331, 582347, 558636, 565511, 567374, 568329, 568855, 571900, 571916, 576762, 585318, 585333, 591231, 591796, 592746, 593706, 593676, 594262, 595562, 595583, 595990, 597037, 598215, 599272, 62865, 56991, 583498, 571066, 61883, 582165, 58103, 62463, 575420, 593658, 590067, 597826, 597764, 583402, 565441, 60563, 584945, 583610, 596032, 598436, 562991, 570080, 58196, 58379, 64261, 583990, 64756, 64321, 597485, 585527, 582379, 61932, 63882, 586808, 59015, 560515, 597647, 588476, 590911, 589363, 571772, 592362, 572307, 589834, 589865, 589546, 554551, 59726, 597669, 60385, 60721, 562910, 
569245, 585288, 568952, 581077, 582200, 560531, 63463, 559904, 559921, 560580, 560597, 560646, 560846, 560893, 560909, 560976, 561098, 561129, 561434, 562648, 562811, 563172, 563188, 565030, 565045, 565096, 566555, 569742, 570049, 570558, 570606, 570622, 570638, 572012, 572159, 573490, 573506, 573522, 573538, 575265, 575679, 577453, 577470, 577486, 579658, 589483, 56151, 584150, 584214, 585231, 585379, 585395, 588945, 589589, 589055, 589515, 589531, 589620, 590146, 589560, 590192, 590208, 590316, 590377, 556757, 558202, 64637, 55786, 565294, 558719, 554982, 62290, 62780, 555001, 555018, 555152, 555168, 555575, 555591, 555606, 555621, 555673, 555655, 556073, 556125, 556920, 557099, 557131, 556625, 557393, 557409, 557425, 557440, 557589, 557623, 557768, 558280, 558265, 558668, 562006, 562187, 562218, 562234, 562331, 563290, 582363, 565848, 565814, 566064, 565901, 566458, 566708, 566803, 566915, 567016, 567033, 567081, 567293, 567654, 568297, 569054, 569152, 571214, 571329, 571475, 571539, 571851, 571867, 571884, 571948, 572358, 572374, 572389, 572405, 572962, 572927, 573110, 573059, 574082, 574116, 574236, 576980, 592258, 591406, 592916, 592964, 593550, 593566, 593920, 593643, 593756, 594544, 597903, 64046, 60837, 68403, 4276141, 4276142, 4276148, 4276161, 4276162, 4276163, 4276167, 4276187, 4276228, 4276242, 4276269, 4276270, 4276282, 4276465, 4276466, 4276467, 4276468, 4276469, 4276470, 4276481, 4276482, 4276483, 4276484, 4276485, 4276486, 4276487, 4276488, 4276489, 4276490, 4276501, 4276502, 4276503, 4276504, 4276505, 4276506, 4276507, 4276508, 4276509, 4276510, 4276521, 4276522, 4276523, 4276524, 4276525, 4276526, 4276527, 4276528, 4276529, 4277644, 4277645, 4277646, 4277647, 4277648, 4277649, 4277650, 4277661, 4277662, 4277663, 4277664, 4277665, 4277666, 4277667, 4277668, 4277669, 4277670, 4277681, 4277682, 4277683, 4277684, 4277685, 4277686, 4277687, 4277688, 4277689, 4277690, 4277701, 4277702, 4277703, 4277704, 4277705, 4277706, 4277707, 4277708, 4277709, 4277710, 4277721, 4277722, 4277723, 4277724, 4277725, 4277726, 4277727, 4277728, 4277729, 4277730, 4277741, 4277742, 4277743, 4277744, 4277745, 4277746, 4277747, 4277748, 4277749, 4277750, 4277762, 4277763, 4277764, 4277765, 4277766, 4277767, 4277768, 4277769, 4277770, 4277781, 4277782, 4277783, 4277784, 4277785, 4277786, 4277787, 4277788, 4277789, 4277790, 4277801, 4277802, 4277803, 4277804, 4277805, 4277806, 4277807, 4277808, 4277809, 4277810, 4277821, 4277822, 4277823, 4277824, 4277825, 4277826, 4277827, 
4277828, 4277829, 4277830, 4277841, 4277842, 4277843, 4277844, 4277845, 4277846, 4277847, 4277848, 4277849, 4277850, 4277861, 4277862, 4277863, 4277864, 4277865, 4277866, 4277867, 4277868, 4277869, 4277870, 4277881, 4277882, 4277883, 4277884, 4277885, 4277886, 4277887, 4277888, 4278446, 4278904, 4278949, 4280527, 4280528, 4280529, 4280530, 4280541, 4280542, 4280543, 4280544, 4280545, 4280546, 4280547, 4280548, 4280549, 4280550, 4280561, 4280562, 4280563, 4280564, 4280565, 4280566, 4280567, 4280568, 4280569, 4280570, 4280581, 4280582, 4280583, 4280584, 4280585, 4280586, 4280587, 4280588, 4280589, 4280590, 4280601, 4280602, 4280603, 4280604, 4280605, 4280606, 4280607, 4280608, 4280609, 4280610, 4280621, 4280622, 4280623, 4280624, 4280625, 4280626, 4280627, 4280628, 4280629, 4280630, 4280641, 4280642, 4280643, 4280644, 4280645, 4280646, 4280647, 4280683, 4280684, 4280685, 4281129, 4281130, 4281141, 4281142, 4281143, 4281144, 4281145, 4281146, 4281147, 4281148, 4281149, 4281150, 4281161, 4281162, 4281163, 4281164, 589222, 589302, 4283189, 4283190, 4283201, 4283202, 4283203, 4283204, 4283205, 4283206, 4283207, 4283285, 4283286, 4283287, 4283288, 4283289, 4283290, 4283304, 4283308, 4283309, 4283310, 4283321, 4283323, 4283325, 4283327, 4283328, 4283330, 4283343, 4283344, 4283346, 4283347, 4283348, 4283349, 589317, 4312567, 4312568, 4312570, 4312581, 4312583, 4312586, 4312587, 4312589, 4312601, 4312607, 598026, 598112, 597786, 589332, 567182, 583658, 572028, 564166, 587879, 596160, 585426, 61791, 559208, 559444, 559477, 559509, 562957, 564097, 562172, 566176, 566191, 589191, 562266, 554521, 555705, 555721, 556465, 556496, 587753, 562074, 587768, 569019, 562091, 587895, 559192, 565610, 582264, 62795, 596095, 582441, 560070, 560087, 560104, 560548, 567148, 571650, 561924, 561990, 562039, 555447, 556143, 556338, 556640, 556655, 556904, 557358, 557459, 559561, 
557718, 557734, 557751, 557865, 557934, 557950, 558316, 558332, 562299, 562315, 563342, 563562, 563580, 563615, 565423, 565528, 567097, 567523, 567792, 568313, 568485, 568582, 568616, 568634, 568710, 568773, 569326, 568967, 569134, 574100, 574182, 574202, 576615, 576664, 584581, 584596, 584611, 584626, 584641, 584869, 584884, 584915, 584930, 584960, 584975, 584990, 585006, 585036, 585477, 585348, 585303, 556480, 569069, 592933, 558900, 578779, 578795, 578811, 584445, 584461, 589379, 589394, 589423, 589438, 589453, 589468, 589499, 589160, 590161, 554829, 555737, 556002, 558984, 565916, 566111, 566128, 566145, 571804, 571820, 571835, 591518, 591534, 591549, 591488, 592057, 592273, 592730, 592777, 593185, 592996, 593833, 573279, 573295, 571360, 562580, 564367, 569952, 570816, 570834, 570957, 571116, 571132, 571179, 571980, 572195, 572213, 572260, 572276, 572323, 574694, 575249, 554926, 554964, 555088, 558442, 558653, 561906, 565459, 565780, 567065, 567199, 567326, 571390, 572422, 572455, 572519, 572535, 572552, 572698, 572911, 572944, 573026, 590895, 591361, 591423, 557880, 573075, 581558, 581418, 562283, 568821, 581126, 581324, 581623, 581687, 581703, 582052, 559330, 559363, 559378, 559396, 559412, 559461, 559577, 559709, 559758, 559804, 559837, 560333, 560481, 560814, 561347, 561364, 561382, 561400, 561417, 561551, 561586, 561854, 561871, 561888, 562547, 562762, 562828, 563007, 563059, 564216, 564232, 564248, 564267, 564303, 564499, 564516, 564553, 569523, 569775, 569791, 569920, 570128, 570145, 573811, 574046, 575232, 575827, 575846, 576379, 577957, 578246, 579346, 584552, 585666, 585792, 585954, 586148, 586180, 586229, 586323, 586370, 586433, 
586449, 586919, 586967, 587041, 587056, 587071, 587374, 587647, 587942, 587958, 587972, 588960, 588976, 589253, 589347, 590561, 590576, 560054, 560696, 583942, 583448, 583975, 63322, 570769, 67551, 597012, 594445, 593891, 593999, 594028, 594131, 596704, 596900, 596930, 596958, 597086, 597510, 597538, 597563, 597585, 597608, 597628, 597688, 597707, 597746, 597806, 597845, 597884, 597922, 597940, 597959, 597979, 597865, 598133, 598068, 571996, 557148, 562441, 562457, 555137, 565312, 565660, 565279, 582149, 582411, 582216, 582232, 582248, 583082, 583180, 583417, 583465, 583926, 565713, 572242, 572667, 572847, 581798, 562698, 572046, 572076, 572093, 572143, 592852, 592883, 570685, 573627, 56418, 560878, 560282, 582688, 564447, 561226, 561278, 561315, 566160, 564115, 564184, 565196, 566350, 569889, 570479, 570542, 570574, 570590, 570701, 575506, 575538, 575591, 577322, 577354, 577369, 577520, 584306, 584522, 584537, 587421, 588184, 588491, 588506, 589880, 571964, 572126, 572108, 573409, 576430, 577306, 583818, 584006, 585363, 585843, 
587011, 587530, 587581, 588446, 589009, 589025, 589040, 589128, 589145, 590113, 554793, 595180, 568532, 568565, 568903, 594056, 593723, 593739, 595206, 595250, 595385, 595452, 595473, 595515, 595604, 595689, 595711, 595732, 595775, 595667, 595796, 595904, 595926, 595947, 596011, 596053, 596138, 596620, 596986, 597062, 596676, 597136, 597110, 598047, 598658, 598875, 599081, 55745, 555249, 556738, 4532355, 4532358, 590786, 4532343, 62851, 55572, 64592, 594211, 594421]

f = open('../../output/hors_cip_modifies.csv', 'w', newline='')
writer = csv.writer(f, delimiter=';')
writer.writerows(map(lambda x: [x], array))
f.close()


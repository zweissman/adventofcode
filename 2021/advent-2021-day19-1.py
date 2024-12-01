import operator

DATA_TEST = [
    "--- scanner 0 ---",
    "404,-588,-901",
    "528,-643,409",
    "-838,591,734",
    "390,-675,-793",
    "-537,-823,-458",
    "-485,-357,347",
    "-345,-311,381",
    "-661,-816,-575",
    "-876,649,763",
    "-618,-824,-621",
    "553,345,-567",
    "474,580,667",
    "-447,-329,318",
    "-584,868,-557",
    "544,-627,-890",
    "564,392,-477",
    "455,729,728",
    "-892,524,684",
    "-689,845,-530",
    "423,-701,434",
    "7,-33,-71",
    "630,319,-379",
    "443,580,662",
    "-789,900,-551",
    "459,-707,401",
    "",
    "--- scanner 1 ---",
    "686,422,578",
    "605,423,415",
    "515,917,-361",
    "-336,658,858",
    "95,138,22",
    "-476,619,847",
    "-340,-569,-846",
    "567,-361,727",
    "-460,603,-452",
    "669,-402,600",
    "729,430,532",
    "-500,-761,534",
    "-322,571,750",
    "-466,-666,-811",
    "-429,-592,574",
    "-355,545,-477",
    "703,-491,-529",
    "-328,-685,520",
    "413,935,-424",
    "-391,539,-444",
    "586,-435,557",
    "-364,-763,-893",
    "807,-499,-711",
    "755,-354,-619",
    "553,889,-390",
    "",
    "--- scanner 2 ---",
    "649,640,665",
    "682,-795,504",
    "-784,533,-524",
    "-644,584,-595",
    "-588,-843,648",
    "-30,6,44",
    "-674,560,763",
    "500,723,-460",
    "609,671,-379",
    "-555,-800,653",
    "-675,-892,-343",
    "697,-426,-610",
    "578,704,681",
    "493,664,-388",
    "-671,-858,530",
    "-667,343,800",
    "571,-461,-707",
    "-138,-166,112",
    "-889,563,-600",
    "646,-828,498",
    "640,759,510",
    "-630,509,768",
    "-681,-892,-333",
    "673,-379,-804",
    "-742,-814,-386",
    "577,-820,562",
    "",
    "--- scanner 3 ---",
    "-589,542,597",
    "605,-692,669",
    "-500,565,-823",
    "-660,373,557",
    "-458,-679,-417",
    "-488,449,543",
    "-626,468,-788",
    "338,-750,-386",
    "528,-832,-391",
    "562,-778,733",
    "-938,-730,414",
    "543,643,-506",
    "-524,371,-870",
    "407,773,750",
    "-104,29,83",
    "378,-903,-323",
    "-778,-728,485",
    "426,699,580",
    "-438,-605,-362",
    "-469,-447,-387",
    "509,732,623",
    "647,635,-688",
    "-868,-804,481",
    "614,-800,639",
    "595,780,-596",
    "",
    "--- scanner 4 ---",
    "727,592,562",
    "-293,-554,779",
    "441,611,-461",
    "-714,465,-776",
    "-743,427,-804",
    "-660,-479,-426",
    "832,-632,460",
    "927,-485,-438",
    "408,393,-506",
    "466,436,-512",
    "110,16,151",
    "-258,-428,682",
    "-393,719,612",
    "-211,-452,876",
    "808,-476,-593",
    "-575,615,604",
    "-485,667,467",
    "-680,325,-822",
    "-627,-443,-432",
    "872,-547,-609",
    "833,512,582",
    "807,604,487",
    "839,-516,451",
    "891,-625,532",
    "-652,-548,-490",
    "30,-46,-14",
]
DATA_TEST1 = [
    "--- scanner 0 ---",
    "-618,-824,-621",
    "-537,-823,-458",
    "-447,-329,318",
    "404,-588,-901",
    "544,-627,-890",
    "528,-643,409",
    "-661,-816,-575",
    "390,-675,-793",
    "423,-701,434",
    "-345,-311,381",
    "459,-707,401",
    "-485,-357,347",
    "",
    "--- scanner 1 ---",
    "686,422,578",
    "605,423,415",
    "515,917,-361",
    "-336,658,858",
    "-476,619,847",
    "-460,603,-452",
    "729,430,532",
    "-322,571,750",
    "-355,545,-477",
    "413,935,-424",
    "-391,539,-444",
    "553,889,-390",
]
DATA = [
    "--- scanner 0 ---",
    "-594,397,693",
    "-451,-583,331",
    "-597,843,-847",
    "-661,524,591",
    "730,571,661",
    "651,-549,-489",
    "41,0,24",
    "630,563,701",
    "696,-602,543",
    "-553,706,-847",
    "-838,-658,-361",
    "354,874,-727",
    "125,167,100",
    "-525,-540,451",
    "-848,-529,-478",
    "349,917,-644",
    "-576,447,702",
    "656,-361,-480",
    "-403,-575,353",
    "686,-447,-369",
    "625,-510,651",
    "-421,729,-852",
    "-856,-616,-408",
    "666,-425,576",
    "703,540,868",
    "385,731,-682",
    "",
    "--- scanner 1 ---",
    "560,474,-555",
    "479,629,-526",
    "-426,444,-864",
    "325,-544,-582",
    "365,-495,-573",
    "672,-474,608",
    "-439,442,-612",
    "-887,-506,499",
    "-431,-816,-652",
    "-560,-824,-525",
    "568,-500,758",
    "-786,-558,418",
    "804,739,574",
    "-804,411,560",
    "-654,460,580",
    "494,408,-481",
    "797,614,447",
    "455,-566,-686",
    "-464,-715,-596",
    "825,740,572",
    "547,-506,737",
    "-327,440,-725",
    "-776,422,551",
    "-19,-173,-3",
    "-856,-449,417",
    "",
    "--- scanner 2 ---",
    "479,583,-260",
    "565,-830,543",
    "-784,411,557",
    "436,645,-355",
    "397,414,625",
    "723,-724,570",
    "-625,478,-617",
    "-902,-751,-590",
    "-919,-899,-626",
    "-523,-598,625",
    "-2,-63,44",
    "-192,-138,91",
    "302,-614,-449",
    "-916,-786,-624",
    "-549,395,-481",
    "327,450,569",
    "316,-700,-320",
    "-566,-674,492",
    "585,-808,629",
    "-744,377,527",
    "-700,488,513",
    "-525,399,-657",
    "-670,-689,594",
    "257,-546,-310",
    "593,589,-352",
    "447,469,651",
    "",
    "--- scanner 3 ---",
    "710,-694,815",
    "903,381,694",
    "657,478,-524",
    "-518,-827,-571",
    "553,493,-422",
    "-270,621,380",
    "-736,443,-500",
    "522,-699,-738",
    "-329,467,390",
    "611,-753,887",
    "-498,-654,336",
    "-578,337,-473",
    "-630,-769,-453",
    "-598,359,-559",
    "906,268,696",
    "595,-812,-722",
    "-495,-556,454",
    "510,569,-555",
    "496,-735,-673",
    "889,416,660",
    "516,-708,800",
    "-525,-828,-499",
    "-315,553,519",
    "125,-167,93",
    "16,-15,13",
    "-370,-655,495",
    "",
    "--- scanner 4 ---",
    "561,-530,-578",
    "518,836,898",
    "-765,-682,897",
    "738,-500,-611",
    "84,74,9",
    "810,681,-732",
    "461,642,874",
    "-620,444,957",
    "380,-730,787",
    "-427,-566,-453",
    "422,-564,848",
    "-404,-493,-286",
    "646,-571,-503",
    "-613,773,-672",
    "476,645,904",
    "681,556,-764",
    "-452,398,888",
    "-713,-797,796",
    "-435,-466,-493",
    "831,660,-738",
    "-500,863,-743",
    "-509,903,-694",
    "-830,-722,811",
    "-537,495,906",
    "408,-627,767",
    "",
    "--- scanner 5 ---",
    "-749,-404,454",
    "600,598,580",
    "-764,-722,-519",
    "-875,-376,579",
    "-540,572,619",
    "-874,-397,581",
    "-609,-641,-548",
    "431,-746,-679",
    "365,-633,765",
    "339,-529,615",
    "-420,537,517",
    "610,493,-501",
    "371,-654,744",
    "650,593,-493",
    "492,527,672",
    "-24,-64,49",
    "-695,874,-847",
    "-127,84,-93",
    "-531,567,431",
    "-543,-707,-474",
    "-778,869,-804",
    "-733,838,-661",
    "525,557,495",
    "409,-876,-575",
    "360,-836,-566",
    "817,520,-470",
    "",
    "--- scanner 6 ---",
    "713,-860,-483",
    "-565,-584,-526",
    "100,-153,47",
    "-482,692,399",
    "-286,-557,524",
    "822,486,680",
    "611,-926,794",
    "-663,-602,-640",
    "-588,385,-667",
    "914,492,566",
    "557,597,-538",
    "-600,596,-670",
    "619,-807,-494",
    "-655,774,415",
    "-515,-597,533",
    "819,430,523",
    "-551,-666,-726",
    "693,680,-462",
    "-598,750,484",
    "598,-862,-374",
    "-608,455,-544",
    "517,676,-438",
    "-330,-610,594",
    "577,-849,775",
    "-5,-41,-71",
    "547,-951,862",
    "",
    "--- scanner 7 ---",
    "347,-463,316",
    "37,47,-20",
    "-409,-753,-482",
    "487,-380,-338",
    "-866,443,-723",
    "417,442,795",
    "-638,-290,735",
    "339,-411,364",
    "295,-397,-338",
    "-546,-740,-576",
    "313,-463,-352",
    "279,553,-771",
    "-814,544,-838",
    "375,436,604",
    "-621,-276,818",
    "-131,93,71",
    "360,466,601",
    "-427,-818,-485",
    "-647,-495,786",
    "-638,434,454",
    "-721,383,403",
    "321,492,-605",
    "381,-538,307",
    "-553,452,357",
    "307,573,-668",
    "-931,529,-763",
    "",
    "--- scanner 8 ---",
    "-851,737,-565",
    "468,-753,-432",
    "644,-742,574",
    "-826,811,-521",
    "470,612,765",
    "603,790,-395",
    "-397,-456,784",
    "469,768,-379",
    "387,442,803",
    "-760,789,-468",
    "-811,-501,-674",
    "48,-160,0",
    "699,-792,548",
    "663,-862,492",
    "530,-710,-337",
    "354,794,-363",
    "-125,-20,-33",
    "-752,315,722",
    "-888,-482,-640",
    "-813,431,779",
    "-913,-414,-704",
    "-465,-607,847",
    "524,-596,-429",
    "299,529,760",
    "-377,-643,805",
    "-749,371,855",
    "",
    "--- scanner 9 ---",
    "-809,-724,-432",
    "592,728,-735",
    "-510,726,361",
    "-872,-608,-395",
    "-481,864,341",
    "-639,727,-781",
    "561,620,361",
    "597,650,379",
    "747,616,345",
    "514,-386,-686",
    "712,-382,-620",
    "501,-755,571",
    "438,641,-767",
    "405,-768,421",
    "-858,-603,-430",
    "-70,109,-125",
    "-435,860,415",
    "-771,-746,729",
    "-555,804,-737",
    "522,656,-585",
    "-831,-620,822",
    "-81,-15,69",
    "-595,838,-767",
    "625,-261,-632",
    "-886,-729,828",
    "479,-683,438",
    "",
    "--- scanner 10 ---",
    "881,663,713",
    "-677,-726,-668",
    "538,-558,-909",
    "404,-483,-855",
    "813,-747,329",
    "-753,-461,502",
    "-762,-650,-629",
    "-854,-740,-677",
    "648,699,-925",
    "-873,498,-874",
    "-693,-539,543",
    "644,513,-909",
    "-752,692,432",
    "-573,-457,481",
    "20,-167,-56",
    "614,549,-891",
    "801,-728,320",
    "802,-904,423",
    "-758,544,524",
    "400,-529,-929",
    "-783,387,-810",
    "825,660,670",
    "-897,489,-883",
    "840,642,633",
    "-785,624,530",
    "-90,-17,-180",
    "",
    "--- scanner 11 ---",
    "-55,84,120",
    "383,423,-460",
    "348,-628,-638",
    "-734,-705,-302",
    "569,-829,498",
    "-634,422,900",
    "-143,-36,27",
    "-768,-740,-288",
    "383,620,573",
    "-770,-853,-285",
    "-584,-636,606",
    "415,533,727",
    "565,605,657",
    "-702,382,927",
    "492,-856,638",
    "-750,388,887",
    "413,457,-420",
    "-566,-546,639",
    "-801,445,-679",
    "-761,524,-579",
    "481,-552,-681",
    "-668,-630,636",
    "369,534,-504",
    "-625,441,-655",
    "450,-643,-534",
    "576,-774,631",
    "",
    "--- scanner 12 ---",
    "-965,-651,-291",
    "675,621,-532",
    "341,345,727",
    "701,436,-619",
    "-523,483,917",
    "-925,-701,-381",
    "423,-662,-330",
    "-97,-57,82",
    "-626,522,926",
    "-617,-714,416",
    "623,-582,490",
    "375,489,727",
    "763,601,-604",
    "380,-631,-342",
    "-598,-603,550",
    "-872,-648,-484",
    "-595,-557,449",
    "585,-564,593",
    "-882,368,-270",
    "-925,420,-460",
    "-911,390,-258",
    "556,-524,395",
    "468,-691,-253",
    "-703,542,962",
    "351,473,678",
    "",
    "--- scanner 13 ---",
    "-600,-593,480",
    "-388,-344,-865",
    "-711,624,322",
    "719,-602,-590",
    "-804,740,-434",
    "832,427,-610",
    "-65,77,-30",
    "-644,-690,357",
    "565,-704,548",
    "-544,-298,-850",
    "-780,797,-628",
    "-497,-310,-793",
    "-810,782,-625",
    "-649,549,390",
    "109,-60,58",
    "515,-735,488",
    "826,448,-589",
    "455,-671,399",
    "883,768,814",
    "826,686,845",
    "779,-568,-700",
    "-553,-771,482",
    "858,577,-714",
    "835,-690,-669",
    "-656,754,352",
    "774,767,744",
    "",
    "--- scanner 14 ---",
    "752,-458,532",
    "-612,-635,-844",
    "383,-370,-637",
    "-641,-643,368",
    "18,72,-67",
    "621,-442,593",
    "680,-645,557",
    "-778,702,603",
    "-703,-712,366",
    "350,579,624",
    "-585,644,-791",
    "321,-320,-693",
    "-746,548,516",
    "-550,-539,-840",
    "385,594,-893",
    "-378,-637,-814",
    "-592,777,-846",
    "334,393,628",
    "-596,618,588",
    "449,705,-803",
    "376,603,-917",
    "-669,637,-873",
    "366,-445,-773",
    "368,543,594",
    "-720,-840,359",
    "",
    "--- scanner 15 ---",
    "-765,498,475",
    "612,-411,653",
    "-12,130,-66",
    "-569,-479,650",
    "309,-718,-754",
    "-128,16,-175",
    "-905,-715,-446",
    "295,-753,-759",
    "-651,406,481",
    "289,722,-873",
    "-879,709,-937",
    "572,-381,687",
    "353,803,665",
    "377,627,669",
    "-608,501,419",
    "-499,-423,614",
    "-619,-505,595",
    "358,-716,-875",
    "453,763,586",
    "409,701,-818",
    "-947,773,-962",
    "-860,743,-860",
    "-754,-778,-514",
    "528,-367,576",
    "-718,-736,-426",
    "398,607,-871",
    "",
    "--- scanner 16 ---",
    "-624,-579,-747",
    "700,461,-545",
    "516,593,232",
    "595,648,288",
    "-367,-350,437",
    "-450,-388,607",
    "417,-369,-461",
    "-279,-393,524",
    "-698,649,683",
    "-643,-661,-867",
    "-634,828,-826",
    "-42,-55,-43",
    "485,-306,-612",
    "-463,754,-776",
    "397,-348,-648",
    "-679,-605,-797",
    "96,84,-153",
    "772,588,-461",
    "451,711,296",
    "774,543,-518",
    "833,-374,426",
    "-823,583,641",
    "-676,614,537",
    "772,-431,310",
    "-364,800,-825",
    "769,-298,366",
    "",
    "--- scanner 17 ---",
    "-535,-668,-567",
    "-643,495,929",
    "719,-570,605",
    "572,-601,696",
    "-634,486,953",
    "-593,-475,827",
    "384,440,-344",
    "-689,-636,-480",
    "-694,478,-558",
    "-619,-486,-552",
    "338,514,-348",
    "-460,-482,882",
    "498,-668,-370",
    "-600,-559,909",
    "595,692,910",
    "-658,460,-588",
    "505,740,818",
    "16,143,132",
    "413,460,-482",
    "581,701,733",
    "542,-682,-481",
    "458,-638,-404",
    "-844,444,-592",
    "-532,559,839",
    "-105,25,44",
    "676,-703,681",
    "",
    "--- scanner 18 ---",
    "-646,448,-358",
    "421,-453,552",
    "611,592,834",
    "-668,-586,773",
    "-794,510,-405",
    "-550,432,452",
    "-618,472,479",
    "648,561,653",
    "384,630,-628",
    "338,-471,611",
    "-584,-580,743",
    "-711,659,-371",
    "673,546,767",
    "-590,-476,-272",
    "596,-648,-389",
    "433,457,-559",
    "456,-496,563",
    "656,-736,-522",
    "-468,-470,-245",
    "498,676,-566",
    "-502,438,492",
    "640,-637,-412",
    "13,78,59",
    "-686,-496,740",
    "-428,-603,-267",
    "",
    "--- scanner 19 ---",
    "-535,718,531",
    "759,469,-617",
    "49,6,-150",
    "-647,632,595",
    "873,-717,-496",
    "-291,693,-778",
    "-549,518,613",
    "-405,771,-809",
    "-270,-532,640",
    "635,486,390",
    "-349,811,-862",
    "729,475,337",
    "795,-867,-501",
    "-586,-492,-476",
    "-729,-621,-473",
    "593,-783,348",
    "-499,-541,600",
    "614,366,335",
    "-38,-71,17",
    "563,-870,246",
    "-708,-633,-457",
    "837,-715,-605",
    "627,-802,271",
    "657,401,-631",
    "-314,-602,587",
    "744,319,-742",
    "",
    "--- scanner 20 ---",
    "118,-4,-45",
    "-313,-645,461",
    "-371,-761,376",
    "492,433,672",
    "725,-694,306",
    "842,470,-625",
    "-593,271,-452",
    "852,342,-674",
    "-597,410,-353",
    "-563,580,534",
    "-595,523,-465",
    "813,-634,395",
    "518,618,585",
    "-629,654,468",
    "-608,-635,-567",
    "-1,-181,-107",
    "570,-585,-437",
    "637,-527,-342",
    "608,-567,-540",
    "-408,609,453",
    "-678,-655,-690",
    "430,598,657",
    "-289,-588,392",
    "818,486,-674",
    "770,-665,383",
    "-467,-643,-693",
    "",
    "--- scanner 21 ---",
    "-814,-466,669",
    "425,811,436",
    "-460,911,-535",
    "-500,884,-603",
    "558,590,-653",
    "662,-304,-469",
    "434,-719,739",
    "-602,-595,-476",
    "468,800,471",
    "468,623,-671",
    "-519,-671,-612",
    "-574,596,688",
    "-589,710,663",
    "-523,-695,-436",
    "501,-814,797",
    "443,752,353",
    "-603,-463,681",
    "-744,-589,689",
    "472,-616,757",
    "-75,109,56",
    "-620,529,626",
    "627,-318,-503",
    "-466,871,-487",
    "552,620,-569",
    "775,-301,-467",
    "",
    "--- scanner 22 ---",
    "913,595,571",
    "80,66,-93",
    "-752,-661,-816",
    "-504,563,-357",
    "703,696,-638",
    "-480,486,-489",
    "-543,504,-522",
    "-562,-609,-859",
    "-384,650,330",
    "948,-550,562",
    "831,666,546",
    "851,-578,416",
    "897,-559,-689",
    "-490,-408,741",
    "-418,-428,829",
    "-477,572,302",
    "-764,-639,-845",
    "846,593,-665",
    "986,-684,-672",
    "36,185,57",
    "-403,-593,767",
    "-416,607,354",
    "884,584,439",
    "732,-583,568",
    "703,652,-622",
    "880,-756,-726",
    "",
    "--- scanner 23 ---",
    "-602,652,-708",
    "-729,781,-700",
    "-942,-759,-577",
    "434,-593,570",
    "422,325,-390",
    "483,408,527",
    "-424,-783,440",
    "340,356,-333",
    "-77,37,73",
    "474,436,538",
    "440,-799,-469",
    "341,426,-442",
    "-673,748,-599",
    "445,-797,-552",
    "503,558,576",
    "-565,-858,471",
    "-689,773,558",
    "428,-800,646",
    "-818,-808,-561",
    "416,-776,-520",
    "-941,786,560",
    "512,-688,549",
    "-802,885,556",
    "-870,-728,-568",
    "-613,-726,424",
    "",
    "--- scanner 24 ---",
    "616,666,-720",
    "559,-451,438",
    "653,780,380",
    "-725,733,-842",
    "-686,657,-757",
    "718,562,-705",
    "-820,-373,698",
    "585,-401,383",
    "667,-569,-861",
    "-425,854,320",
    "-445,825,458",
    "-848,-372,428",
    "683,740,346",
    "-744,-322,-718",
    "581,-589,-839",
    "-686,-382,-817",
    "-499,900,324",
    "641,-331,419",
    "-694,-315,-874",
    "585,519,-629",
    "640,-727,-755",
    "-774,-422,599",
    "-63,69,-70",
    "-677,643,-934",
    "697,696,457",
    "",
    "--- scanner 25 ---",
    "674,721,-553",
    "-334,789,662",
    "602,-473,579",
    "-695,-823,616",
    "6,6,-9",
    "-682,-410,-584",
    "841,401,569",
    "-680,-885,451",
    "814,723,-484",
    "-618,433,-463",
    "801,-846,-654",
    "824,660,-585",
    "-714,-386,-627",
    "651,-463,707",
    "651,-497,563",
    "850,504,530",
    "-536,803,632",
    "-346,760,684",
    "-621,-358,-549",
    "-555,466,-481",
    "-594,301,-540",
    "847,-905,-646",
    "-608,-797,431",
    "818,-945,-832",
    "886,581,510",
    "",
    "--- scanner 26 ---",
    "-509,460,-504",
    "596,-943,651",
    "-393,-890,-842",
    "-353,-804,-907",
    "782,570,-465",
    "705,-460,-568",
    "-345,-780,303",
    "524,808,634",
    "644,-782,676",
    "542,-754,603",
    "52,-106,-94",
    "646,710,599",
    "-504,510,569",
    "-582,293,-481",
    "190,-89,58",
    "697,459,-388",
    "-545,585,484",
    "659,-667,-613",
    "645,-493,-541",
    "715,468,-338",
    "-511,-841,345",
    "-278,-789,-790",
    "-609,500,-512",
    "-575,618,661",
    "572,830,642",
    "-448,-760,331",
    "",
    "--- scanner 27 ---",
    "655,601,-428",
    "-587,941,-352",
    "-727,-430,-470",
    "581,667,-494",
    "484,-623,497",
    "554,-351,-259",
    "-642,763,733",
    "-760,859,-336",
    "563,-302,-299",
    "450,-373,-389",
    "524,635,505",
    "-634,622,607",
    "-677,-417,589",
    "-912,-443,-531",
    "610,822,-413",
    "-579,-435,703",
    "-109,111,68",
    "272,637,492",
    "411,633,393",
    "611,-631,626",
    "-691,-499,789",
    "-644,917,-421",
    "-654,552,730",
    "540,-522,530",
    "-956,-390,-461",
    "",
    "--- scanner 28 ---",
    "549,558,-705",
    "-358,771,-570",
    "-599,-543,-592",
    "987,-345,-830",
    "-399,672,-445",
    "-704,619,441",
    "-575,-405,-631",
    "769,592,421",
    "-553,-568,794",
    "818,515,520",
    "595,499,-600",
    "834,628,447",
    "749,-476,817",
    "-791,574,536",
    "667,500,-593",
    "46,-19,65",
    "761,-356,681",
    "744,-569,703",
    "-628,-726,803",
    "171,27,-72",
    "921,-320,-745",
    "-541,-437,-576",
    "833,-393,-860",
    "-240,673,-573",
    "-536,-553,833",
    "-719,633,635",
    "",
    "--- scanner 29 ---",
    "453,-648,732",
    "357,421,614",
    "-572,366,-732",
    "275,437,787",
    "619,545,-687",
    "-651,-297,848",
    "594,-522,740",
    "369,-440,-561",
    "-640,411,-593",
    "-784,428,710",
    "-584,-392,790",
    "-777,-793,-452",
    "-726,425,-722",
    "-622,-495,808",
    "-925,-810,-416",
    "452,-516,-425",
    "-827,440,741",
    "-164,106,178",
    "299,506,730",
    "-812,-807,-418",
    "563,702,-690",
    "15,-56,45",
    "557,588,-782",
    "373,-416,-385",
    "664,-645,720",
    "-739,351,681",
    "",
    "--- scanner 30 ---",
    "415,780,-484",
    "570,-850,-776",
    "609,756,-427",
    "853,770,486",
    "478,-790,647",
    "695,-882,-647",
    "-864,-850,-538",
    "-441,-641,557",
    "71,24,16",
    "606,786,-442",
    "-416,728,429",
    "-833,-907,-456",
    "756,788,571",
    "348,-812,543",
    "388,-861,534",
    "807,839,654",
    "-341,687,-600",
    "-763,-798,-457",
    "-408,-540,613",
    "591,-856,-797",
    "-530,710,493",
    "12,-115,-109",
    "-400,768,600",
    "-371,632,-470",
    "-537,-532,486",
    "-409,625,-675",
]


def run(data):
    diffs = []
    board = []
    scanner = {}

    for row in data:
        if row == "":
            continue
        if row.startswith("---"):
            scanner = []
            board.append(scanner)
            continue

        scanner.append(tuple([int(x) for x in row.split(",")]))

    scanner_count = len(board)
    board2 = [None] * scanner_count

    for scanner in board:
        diff = {}
        for s1 in range(len(scanner)):
            for s2 in range(s1 + 1, len(scanner)):
                diff[(s1, s2)] = sorted(
                    (
                        abs(scanner[s1][0] - scanner[s2][0]),
                        abs(scanner[s1][1] - scanner[s2][1]),
                        abs(scanner[s1][2] - scanner[s2][2]),
                    )
                )

        diff = dict(sorted(diff.items(), key=lambda x: (x[1][0], x[1][1], x[1][2])))
        diffs.append(diff)

    matches = {}
    for s1 in range(scanner_count):
        for s2 in range(s1 + 1, scanner_count):
            matches[(s1, s2)] = []
            match = matches[(s1, s2)]

            for k0, v0 in diffs[s1].items():
                for k1, v1 in diffs[s2].items():
                    if v0 == v1:
                        match.append((k0, k1))

    decodes = {}
    for s1 in range(scanner_count):
        for s2 in range(s1 + 1, scanner_count):
            decodes[(s1, s2)] = {}
            decode = decodes[(s1, s2)]

            for match in matches[(s1, s2)]:
                if match[0][0] not in decode:
                    decode[match[0][0]] = list(match[1])
                else:
                    if isinstance(decode[match[0][0]], list):
                        # We still have more than one possible mapping. Figure out the overlap, that should be the right map
                        common = set(decode[match[0][0]]).intersection(match[1])
                        if len(common) == 1:
                            value = list(common)[0]
                            decode[match[0][0]] = value
                            decode = remove_value(value, decode)
                        else:
                            assert False, "BAD A"

                if match[0][1] not in decode:
                    decode[match[0][1]] = list(match[1])
                else:
                    if isinstance(decode[match[0][1]], list):
                        common = set(decode[match[0][1]]).intersection(match[1])
                        if len(common) == 1:
                            value = list(common)[0]
                            decode[match[0][1]] = value
                            decode = remove_value(value, decode)
                        else:
                            assert False, "BAD B"

    # Determine orientation and scanner location
    board2[0] = board[0]
    scanner_locations = {}
    scanner_locations[0] = (0, 0, 0)

    while len(scanner_locations) != scanner_count:
        for decode in decodes:
            skip = False
            s1, s2 = decode[0], decode[1]

            if len(decodes[(s1, s2)]) < 12:
                # We do not have enough overlaps here, skip
                continue
            if s1 in scanner_locations and s2 in scanner_locations:
                # We already found this one.
                continue

            if s2 in scanner_locations:
                # We already found this one.
                skip = True

            if board2[s1] is None:
                # We don't have this source sonar updated to values in reference to 0 yet, skip
                skip = True

            if not skip:
                scanner_location = get_scanner_location(
                    s1, s2, decodes[(s1, s2)], board, board2
                )
                print(f"{s1} --> {s2} == {scanner_location}")
                scanner_locations[s2] = scanner_location

                continue

            # Try the inverse map
            skip = False
            if s1 in scanner_locations:
                # We already found this one.
                skip = True

            if board2[s2] is None:
                # We don't have this source sonar updated to values in reference to 0 yet, skip
                skip = True

            if skip == False:
                decode = {v: k for k, v in decodes[(s1, s2)].items()}
                scanner_location = get_scanner_location(s2, s1, decode, board, board2)
                print(f"{s1} <-- {s2} == {scanner_location}")
                scanner_locations[s1] = scanner_location

    all_beacons = set()
    for index, beacons in enumerate(board2):
        if beacons == None:
            print(f"Unmapped scanner {index}")
        else:
            all_beacons.update(beacons)

    results = len(all_beacons)
    return results


def get_scanner_location(
    s1,
    s2,
    decode,
    board,
    board2,
    x_op=operator.add,
    y_op=operator.add,
    z_op=operator.add,
    x_index=0,
    y_index=1,
    z_index=2,
):
    try:
        xs, ys, zs = [], [], []
        x, y, z = None, None, None

        for k, v in decode.items():
            xs.append(x_op(board2[s1][k][0], board[s2][v][x_index]))
            ys.append(y_op(board2[s1][k][1], board[s2][v][y_index]))
            zs.append(z_op(board2[s1][k][2], board[s2][v][z_index]))

        print(
            f"{s1} --> {s2} [{x_index}][{y_index}][{z_index}], {x_op} {xs[0:3]} - {y_op} {ys[0:3]} - {z_op} {zs[0:3]}"
        )
        if len(list(set(xs))) == 1:
            x = list(xs)[0]
        else:
            if x_op == operator.add:
                x_op = operator.sub
            else:
                x_op = None

        if len(list(set(ys))) == 1:
            y = list(ys)[0]
        else:
            if y_op == operator.add:
                y_op = operator.sub
            else:
                y_op = None

        if len(list(set(zs))) == 1:
            z = list(zs)[0]
        else:
            if z_op == operator.add:
                z_op = operator.sub
            else:
                z_op = None

        if x is not None and y is not None and z is not None:
            # update sonar's coordinates to be in relationship to sonar 0
            new_board = []
            for beacon in board[s2]:
                new_board.append(
                    (
                        x_op(x, -beacon[x_index]),
                        y_op(y, -beacon[y_index]),
                        z_op(z, -beacon[z_index]),
                    )
                )
            board2[s2] = new_board

            return (x, y, z)

        if x is y is z is x_op is y_op is z_op is None:
            x_index, y_index, z_index = y_index, z_index, x_index
            x_op = operator.add
            y_op = operator.add
            z_op = operator.add
        elif x is y is x_op is y_op is None:
            x_index, y_index = y_index, x_index
            x_op = operator.add
            y_op = operator.add
        elif y is z is y_op is z_op is None:
            y_index, z_index = z_index, y_index
            y_op = operator.add
            z_op = operator.add
        elif x is z is x_op is z_op is None:
            x_index, z_index = z_index, x_index
            x_op = operator.add
            z_op = operator.add

        return get_scanner_location(
            s1, s2, decode, board, board2, x_op, y_op, z_op, x_index, y_index, z_index
        )
    except Exception as e:
        print(e)


def remove_value(value, decode):
    for k, v in decode.items():
        if isinstance(v, list) and value in v:
            v.remove(value)
            if len(v) == 1:
                decode[k] = v.pop()

    return decode


if __name__ == "__main__":
    results = run(DATA)
    print(results)


# 442 is high

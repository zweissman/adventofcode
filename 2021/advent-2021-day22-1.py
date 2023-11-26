DATA_TEST = [
    "on x=10..12,y=10..12,z=10..12",
    "on x=11..13,y=11..13,z=11..13",
    "off x=9..11,y=9..11,z=9..11",
    "on x=10..10,y=10..10,z=10..10",
]
DATA_TEST2 = [
    "on x=-20..26,y=-36..17,z=-47..7",
    "on x=-20..33,y=-21..23,z=-26..28",
    "on x=-22..28,y=-29..23,z=-38..16",
    "on x=-46..7,y=-6..46,z=-50..-1",
    "on x=-49..1,y=-3..46,z=-24..28",
    "on x=2..47,y=-22..22,z=-23..27",
    "on x=-27..23,y=-28..26,z=-21..29",
    "on x=-39..5,y=-6..47,z=-3..44",
    "on x=-30..21,y=-8..43,z=-13..34",
    "on x=-22..26,y=-27..20,z=-29..19",
    "off x=-48..-32,y=26..41,z=-47..-37",
    "on x=-12..35,y=6..50,z=-50..-2",
    "off x=-48..-32,y=-32..-16,z=-15..-5",
    "on x=-18..26,y=-33..15,z=-7..46",
    "off x=-40..-22,y=-38..-28,z=23..41",
    "on x=-16..35,y=-41..10,z=-47..6",
    "off x=-32..-23,y=11..30,z=-14..3",
    "on x=-49..-5,y=-3..45,z=-29..18",
    "off x=18..30,y=-20..-8,z=-3..13",
    "on x=-41..9,y=-7..43,z=-33..15",
    "on x=-54112..-39298,y=-85059..-49293,z=-27449..7877",
    "on x=967..23432,y=45373..81175,z=27513..53682",
]
DATA = [
    "on x=-36..10,y=-44..1,z=-18..28",
    "on x=-7..46,y=-3..48,z=-32..13",
    "on x=-11..41,y=-24..30,z=-20..31",
    "on x=-20..30,y=-47..-2,z=-27..21",
    "on x=-11..36,y=-22..32,z=-9..44",
    "on x=-48..5,y=-40..9,z=-49..3",
    "on x=-23..21,y=-15..33,z=-27..24",
    "on x=-44..7,y=-18..28,z=-28..20",
    "on x=-4..48,y=-30..15,z=-5..40",
    "on x=-25..28,y=-6..45,z=-12..37",
    "off x=-1..15,y=-20..-7,z=40..49",
    "on x=-9..35,y=-49..3,z=-14..39",
    "off x=-42..-30,y=-3..13,z=-31..-21",
    "on x=-10..35,y=-35..17,z=-16..31",
    "off x=13..32,y=21..34,z=31..41",
    "on x=-45..8,y=-14..35,z=-38..8",
    "off x=-7..12,y=-38..-21,z=3..22",
    "on x=2..48,y=-35..13,z=-26..18",
    "off x=-2..13,y=-45..-34,z=21..31",
    "on x=-10..38,y=-25..29,z=-7..39",
    "on x=-28883..-15508,y=-45719..-19250,z=56543..85023",
    "on x=-12548..-2670,y=30162..59686,z=48743..65546",
    "on x=-78921..-48935,y=-58375..-40461,z=-10520..6680",
    "on x=60459..69694,y=-39118..-9610,z=23410..40752",
    "on x=-58993..-46464,y=34788..49715,z=24225..58919",
    "on x=-65933..-59172,y=-59855..-28101,z=15518..30376",
    "on x=71139..80625,y=2500..13619,z=2217..25098",
    "on x=4121..18569,y=-18050..2029,z=60597..88243",
    "on x=-62229..-28636,y=-71733..-45733,z=27808..50457",
    "on x=51593..76990,y=38902..45907,z=-369..26292",
    "on x=68985..96599,y=-17288..2120,z=-22861..271",
    "on x=33104..64386,y=29057..55665,z=40253..58523",
    "on x=-81466..-54567,y=8733..27282,z=-41215..-36144",
    "on x=-34804..-15638,y=58589..76038,z=-7633..20193",
    "on x=63492..75206,y=-46967..-27894,z=-31857..-14808",
    "on x=15351..28152,y=13194..20955,z=70126..86947",
    "on x=15635..22669,y=5152..32704,z=73208..87128",
    "on x=68794..83406,y=-35783..-25729,z=-34499..611",
    "on x=-56069..-53663,y=-54346..-28657,z=-34834..-22216",
    "on x=43156..76066,y=27637..45059,z=-47820..-23733",
    "on x=-7711..3045,y=-15369..-10641,z=-79312..-63232",
    "on x=43441..54152,y=-50110..-43904,z=37321..47410",
    "on x=37294..75033,y=38364..67854,z=-20476..1157",
    "on x=33388..53211,y=-67459..-48539,z=-10662..13639",
    "on x=-79542..-57726,y=22115..25011,z=-45772..-23453",
    "on x=58873..78039,y=-50697..-37524,z=-12235..18506",
    "on x=-48962..-34784,y=11652..37386,z=45532..84431",
    "on x=-76170..-57572,y=46417..54598,z=15783..30309",
    "on x=-15755..6100,y=-61498..-53921,z=50597..61974",
    "on x=-6806..20000,y=-23020..12532,z=70539..85001",
    "on x=-5720..16234,y=-55004..-34338,z=-72531..-66790",
    "on x=52008..79539,y=-29253..-1374,z=20347..53617",
    "on x=-17897..-9708,y=-37245..-4510,z=-87664..-60248",
    "on x=-61794..-42398,y=38848..66317,z=-44362..-16971",
    "on x=-24978..-4568,y=52963..66034,z=43492..60015",
    "on x=7791..33094,y=56170..69087,z=33048..42256",
    "on x=-28232..-9944,y=-58134..-55076,z=39582..72486",
    "on x=13368..20524,y=-15360..9002,z=-91847..-66065",
    "on x=21517..29129,y=8445..19558,z=-86160..-74234",
    "on x=7605..17401,y=-27480..-3051,z=66012..93068",
    "on x=48250..69867,y=-31582..-11779,z=-56446..-41985",
    "on x=30111..42304,y=-78761..-42351,z=37002..41561",
    "on x=-36891..-9404,y=-86518..-61745,z=26166..39934",
    "on x=-63590..-34919,y=15132..31704,z=-63932..-48407",
    "on x=-77664..-60473,y=-30186..-15049,z=-49261..-26017",
    "on x=-10394..7444,y=9391..11534,z=61309..96960",
    "on x=-61302..-46820,y=-61513..-47545,z=6430..32125",
    "on x=-53453..-50770,y=24345..56020,z=-57501..-25958",
    "on x=35507..53900,y=-45542..-16679,z=47346..57922",
    "on x=49907..69107,y=16930..38051,z=-55262..-38287",
    "on x=-42743..-9759,y=60466..91647,z=-15118..2553",
    "on x=-38266..-19863,y=55550..63311,z=-53318..-27055",
    "on x=16905..41490,y=-69890..-56924,z=-44140..-8205",
    "on x=-7784..7941,y=75866..85826,z=9452..37078",
    "on x=-74561..-58611,y=-46579..-25328,z=-30557..3529",
    "on x=-1196..34343,y=-70013..-55588,z=-53911..-45594",
    "on x=-84676..-65369,y=41869..61576,z=-9248..2231",
    "on x=-72551..-47185,y=-9381..6167,z=37047..52656",
    "on x=-11907..5784,y=4948..19640,z=73120..80649",
    "on x=60584..84455,y=-24861..-3368,z=-48749..-21563",
    "on x=29668..44628,y=57549..74598,z=-32991..-15066",
    "on x=-8097..12767,y=-95426..-64216,z=-31088..-18926",
    "on x=-90928..-65347,y=4057..22029,z=8907..23501",
    "on x=67918..80236,y=5507..41836,z=15812..32291",
    "on x=-54150..-29579,y=-5372..22568,z=47613..65289",
    "on x=17728..44669,y=-74646..-42398,z=-65777..-28928",
    "on x=2093..29295,y=2422..21121,z=-80503..-62049",
    "on x=-65522..-55148,y=46700..59432,z=-9362..25101",
    "on x=-7488..12850,y=-63622..-27400,z=-76767..-56877",
    "on x=60992..81192,y=-11975..19873,z=-3571..8236",
    "on x=44146..78572,y=-9134..16963,z=-66784..-33238",
    "on x=-67138..-46342,y=14132..43100,z=30402..56588",
    "on x=-70324..-52042,y=-31051..-13658,z=-47636..-26736",
    "on x=21928..31761,y=-73324..-55278,z=28922..52429",
    "on x=-4143..594,y=-42034..-14668,z=-84348..-68488",
    "on x=-77510..-53349,y=-32972..-14462,z=-35462..-12815",
    "on x=-70793..-40538,y=39761..54365,z=11991..30477",
    "on x=-71944..-51391,y=37600..68072,z=-32488..-15952",
    "on x=-48143..-30165,y=59536..78681,z=-32203..-16092",
    "on x=-22818..-7935,y=24969..33664,z=60669..81438",
    "on x=40670..63322,y=-72933..-51831,z=-30393..-10006",
    "on x=-70534..-53025,y=-16537..2105,z=32890..66787",
    "on x=47454..79394,y=-35253..-20693,z=18988..57611",
    "on x=73161..82246,y=-8780..22720,z=-8294..13514",
    "on x=-14026..7081,y=18421..45722,z=65918..73183",
    "on x=71629..83673,y=-10335..8808,z=29998..38745",
    "on x=-18224..-5442,y=69881..95741,z=6388..30178",
    "on x=-19490..4842,y=20201..45030,z=56709..85888",
    "on x=-21272..1593,y=49547..63167,z=38145..67363",
    "on x=-24949..-15012,y=-55330..-20572,z=-82713..-59674",
    "on x=-46843..-24448,y=50679..73327,z=10520..44286",
    "on x=-70925..-39700,y=24871..27793,z=44234..49938",
    "on x=-69305..-53956,y=-59578..-31239,z=-25502..-7568",
    "on x=7557..28629,y=-88776..-75206,z=-7437..10667",
    "on x=29471..53359,y=68936..73945,z=-4133..20290",
    "on x=-52402..-36243,y=19080..37365,z=50135..59326",
    "on x=3810..25116,y=69407..81609,z=9528..20530",
    "on x=18211..49212,y=44337..71877,z=49052..60986",
    "on x=28678..50797,y=-32839..-20421,z=48041..67561",
    "on x=-58157..-42217,y=-31760..-17143,z=-62357..-53538",
    "on x=38952..50290,y=-6367..203,z=50379..82544",
    "on x=-64714..-50678,y=-61423..-47693,z=8332..35457",
    "on x=-28002..-6142,y=-56131..-47383,z=-63420..-52948",
    "on x=-63668..-38918,y=-65020..-36544,z=11622..50689",
    "on x=2203..24329,y=-61091..-52282,z=-76789..-51275",
    "on x=56581..84220,y=29670..43186,z=-37910..-9928",
    "on x=-3024..19466,y=54892..76361,z=-46362..-26851",
    "on x=-76700..-44506,y=-13884..9365,z=-64510..-49973",
    "on x=-98589..-75961,y=-6842..5373,z=11405..14256",
    "on x=65044..94963,y=3807..18057,z=-27060..-1035",
    "on x=61066..70500,y=-44968..-27340,z=-21797..5949",
    "on x=52464..65749,y=-40619..-28476,z=-37598..-15955",
    "on x=-49101..-23335,y=51397..82890,z=-45440..-19364",
    "on x=-20109..-2856,y=-30361..-20065,z=62578..78115",
    "on x=-74043..-52114,y=-39430..-25290,z=16802..43618",
    "on x=66008..75716,y=-23679..8708,z=-50980..-18608",
    "on x=-86101..-58392,y=-18786..15377,z=17168..41798",
    "on x=-55661..-31358,y=-71798..-47063,z=18694..36502",
    "on x=62286..80814,y=-48258..-23908,z=-30461..-15403",
    "on x=33889..57622,y=13502..43857,z=-77450..-62147",
    "on x=13184..26706,y=64762..81475,z=19767..24962",
    "on x=17019..43275,y=-16424..-4301,z=70607..85745",
    "on x=-53965..-36029,y=-68815..-48815,z=-7800..9952",
    "on x=18884..42169,y=60155..75959,z=12031..18073",
    "on x=-588..28626,y=16567..43074,z=-79903..-63075",
    "on x=-76497..-54641,y=-46269..-25830,z=-17322..15993",
    "on x=-6746..10944,y=62505..90487,z=-15775..16197",
    "on x=28300..46689,y=68064..75699,z=-7771..9898",
    "on x=-64368..-42702,y=-27174..-17167,z=-65200..-54350",
    "on x=56910..75581,y=-25585..-10411,z=36135..70404",
    "on x=27504..56469,y=26502..50082,z=52431..67864",
    "on x=-47454..-37493,y=-67803..-57848,z=-29137..878",
    "on x=40122..63672,y=10395..35054,z=52859..66240",
    "on x=-24265..-4217,y=67213..89517,z=9977..26874",
    "on x=50270..58887,y=-41794..-23584,z=40880..59729",
    "on x=68731..78696,y=-29443..-10975,z=-30363..-12403",
    "on x=-615..6005,y=-84686..-66275,z=-50736..-37214",
    "on x=8778..42467,y=-13464..-446,z=69383..77050",
    "on x=33082..59847,y=-40174..-16924,z=-63761..-39798",
    "on x=-53945..-40416,y=37398..54780,z=28513..47277",
    "on x=29636..49940,y=-34924..-2346,z=49599..74490",
    "on x=-20966..1270,y=53988..61813,z=32916..53496",
    "on x=-78940..-45838,y=-26622..2631,z=38955..63550",
    "on x=17146..39670,y=-85003..-58477,z=2984..42382",
    "on x=-47551..-28981,y=-69198..-57064,z=-44298..-22310",
    "on x=-89258..-74497,y=-16850..5067,z=-12367..-5955",
    "on x=35772..53724,y=27657..48119,z=31033..63316",
    "on x=-62854..-41757,y=35022..54608,z=-35013..-12195",
    "on x=-30556..1226,y=-73571..-54097,z=-57803..-47669",
    "on x=13295..34276,y=-39163..-28171,z=-76250..-46210",
    "on x=-24292..6457,y=-91190..-66574,z=-31565..-5150",
    "on x=-16536..6036,y=-96225..-64362,z=-2492..9962",
    "on x=-57058..-30220,y=-18364..-2584,z=53719..63761",
    "on x=-43431..-16673,y=-38683..-22112,z=55769..74887",
    "on x=51701..67855,y=27295..46226,z=10849..38820",
    "on x=-35845..-7342,y=69450..89187,z=11752..29177",
    "on x=12543..45244,y=12075..38035,z=-87164..-50531",
    "on x=42339..73473,y=18241..51391,z=23838..43287",
    "on x=-438..24585,y=-66283..-35680,z=-64361..-46114",
    "on x=2725..22019,y=-82057..-72900,z=-1614..14652",
    "on x=14414..28316,y=-89722..-59311,z=9219..41520",
    "on x=-30825..-5463,y=-69878..-54745,z=-57852..-36139",
    "on x=-42896..-18813,y=-26684..7083,z=69312..90303",
    "on x=-27862..8215,y=27378..63022,z=-78357..-58765",
    "on x=52982..82324,y=-39425..-17991,z=19533..52779",
    "on x=55425..68878,y=-13141..10398,z=46593..62864",
    "on x=-76576..-55809,y=-40969..-19894,z=3576..33104",
    "on x=-45307..-29762,y=35548..70551,z=-52791..-40213",
    "on x=-84553..-64887,y=31408..56688,z=-11919..-300",
    "on x=57673..92102,y=20171..35124,z=-9934..27320",
    "on x=19319..44889,y=59566..70621,z=-52354..-34667",
    "on x=-58420..-23963,y=33856..56920,z=-66732..-50674",
    "on x=28594..47830,y=15367..45508,z=58553..69000",
    "on x=28763..35947,y=27403..56374,z=56409..73208",
    "on x=-74680..-63533,y=-38056..-6996,z=-33003..-18382",
    "on x=-38982..-10495,y=51354..78493,z=14740..42196",
    "on x=-46516..-10037,y=58846..77938,z=-33954..-19867",
    "on x=-54547..-39672,y=56254..74136,z=23189..29880",
    "on x=-61220..-53773,y=-12236..3866,z=56997..61730",
    "on x=-50154..-29903,y=-76428..-48553,z=31157..51784",
    "on x=-3181..17338,y=-80949..-72492,z=772..12702",
    "on x=-52042..-18254,y=49025..64175,z=21945..52993",
    "on x=-78058..-63586,y=-2293..19310,z=-36720..-25831",
    "on x=15904..36582,y=-91457..-60504,z=7939..32474",
    "on x=60022..93528,y=8546..20580,z=-27953..-11390",
    "on x=27563..49707,y=-69314..-63488,z=7268..35058",
    "on x=10646..21929,y=-94609..-61003,z=-22912..-276",
    "on x=-7047..-5297,y=68888..78769,z=-39475..-17434",
    "on x=-51536..-39822,y=43126..53870,z=-56736..-20372",
    "on x=-63164..-52556,y=-54428..-38069,z=24521..42713",
    "on x=-9022..12417,y=-80149..-46957,z=37357..45570",
    "on x=-22997..-2789,y=-95315..-56998,z=12379..39404",
    "on x=4898..15841,y=-81249..-73910,z=-32251..-9796",
    "on x=45502..60898,y=-37324..-31476,z=-54682..-27792",
    "on x=-37888..-21927,y=50938..67533,z=28289..58560",
    "on x=48655..63250,y=-26438..8352,z=56367..77784",
    "on x=-70807..-50021,y=-53252..-46314,z=-24297..4509",
    "on x=-80873..-68066,y=-11712..4769,z=-38161..-7193",
    "on x=-61783..-29833,y=-9380..1417,z=-77655..-50187",
    "on x=3605..15598,y=40600..75869,z=49206..60071",
    "on x=-65903..-61409,y=-47405..-24492,z=21618..49883",
    "off x=-23920..-8406,y=-17972..2067,z=-81283..-75868",
    "on x=-51193..-26274,y=-60490..-42301,z=38488..65879",
    "on x=50827..65635,y=-57757..-39886,z=-30611..-26720",
    "off x=10778..32144,y=52231..74635,z=-59687..-31847",
    "on x=68985..85992,y=28873..51019,z=-15998..-6295",
    "on x=55740..70763,y=35214..53322,z=-31223..-11358",
    "off x=-46538..-9788,y=58032..67324,z=40222..49034",
    "on x=18545..29590,y=14108..34635,z=-74700..-62707",
    "off x=-73624..-41200,y=-52536..-46813,z=14770..34179",
    "on x=-85523..-67379,y=-36300..-19906,z=-11338..6871",
    "on x=5293..28679,y=-85681..-52644,z=28833..41645",
    "off x=-51969..-35153,y=1198..17984,z=51124..72722",
    "off x=-17375..11682,y=18325..41509,z=-87033..-61425",
    "off x=-22666..7568,y=73727..92674,z=-28360..-7249",
    "off x=2661..24254,y=57090..84315,z=-42803..-25128",
    "on x=67178..86929,y=-41603..-21134,z=-346..8549",
    "on x=35402..59738,y=27059..52875,z=40124..50352",
    "on x=-77706..-63549,y=-759..30679,z=-256..20062",
    "off x=-80738..-61445,y=-13769..19667,z=19760..24546",
    "on x=-69653..-38658,y=22405..42680,z=-49778..-26262",
    "off x=-51542..-25536,y=-71500..-51185,z=4129..28507",
    "on x=30425..45199,y=-30596..-9292,z=-81014..-57309",
    "off x=22726..47883,y=-41245..-17684,z=-71414..-46137",
    "on x=66872..87978,y=-22706..13112,z=-43536..-20972",
    "off x=72640..92993,y=7096..22204,z=-21297..-19581",
    "off x=21559..34912,y=-13473..3913,z=-90125..-71617",
    "on x=744..7099,y=37714..55130,z=-78023..-47590",
    "off x=34748..53357,y=35764..63887,z=19808..38379",
    "on x=25985..47421,y=38665..52801,z=36388..65665",
    "on x=55491..76208,y=38300..48792,z=4819..32069",
    "off x=-85210..-68567,y=27276..41154,z=-8241..7567",
    "on x=63368..77016,y=14285..35196,z=17323..34006",
    "off x=-60020..-46013,y=-73070..-54235,z=22512..40151",
    "on x=-64581..-46760,y=-65678..-38839,z=-11746..21206",
    "off x=65614..85707,y=-40016..-9936,z=9078..15465",
    "on x=-9441..19579,y=-3745..15148,z=63724..88861",
    "on x=26670..47587,y=44470..53665,z=-63802..-36681",
    "off x=52461..72456,y=-41431..-31911,z=-53314..-36616",
    "on x=-60681..-44210,y=-60182..-40629,z=-24793..-16265",
    "on x=-31104..2318,y=-86070..-52791,z=28552..42162",
    "off x=56152..74985,y=-56214..-43026,z=-27304..2627",
    "off x=-58202..-26230,y=-45050..-25862,z=55000..65772",
    "off x=-59248..-38705,y=-33544..-18000,z=-57812..-36852",
    "off x=-40613..-22939,y=39403..42071,z=-74302..-53828",
    "on x=58073..86025,y=19542..52637,z=19540..25772",
    "on x=-42291..-19252,y=-80500..-52486,z=720..19957",
    "off x=10093..18140,y=62563..85515,z=28642..49390",
    "off x=-64723..-55102,y=15882..40874,z=27744..48116",
    "on x=-76209..-64298,y=-23310..-3022,z=-44907..-32933",
    "off x=-4161..22460,y=-26759..-12671,z=59101..80357",
    "on x=-69122..-56614,y=-57446..-26219,z=30581..49966",
    "off x=-61329..-48995,y=45179..68334,z=-44523..-16756",
    "off x=-24020..7983,y=-36028..-14601,z=-80855..-74658",
    "off x=61787..80253,y=-29352..-27483,z=-15894..3760",
    "on x=-1854..34165,y=15342..20798,z=-92676..-69474",
    "off x=58756..72759,y=-62605..-44134,z=-21424..-1787",
    "on x=-47927..-19270,y=-27779..-11020,z=-71061..-55792",
    "off x=-64633..-41666,y=-15311..4190,z=52613..67692",
    "off x=-52623..-22282,y=-67672..-60890,z=-41105..-5342",
    "on x=-67475..-41123,y=-29899..-11967,z=54507..64513",
    "off x=76435..88917,y=8907..20588,z=-13737..11171",
    "off x=51043..69285,y=46979..54200,z=-37046..-15549",
    "off x=-4759..21371,y=-30523..-17915,z=-85776..-63473",
    "on x=-3021..6979,y=-81245..-51685,z=31497..53887",
    "on x=-42289..-13283,y=-92861..-62635,z=-18257..-6390",
    "on x=-51969..-28706,y=44357..69139,z=-39332..-9477",
    "off x=-33356..-13804,y=36523..58443,z=50012..60983",
    "on x=-77633..-57968,y=-19312..-3510,z=6439..28195",
    "on x=-18502..12035,y=81..13762,z=-84168..-60344",
    "on x=-74341..-54080,y=35210..49882,z=28945..49835",
    "on x=-38013..-25461,y=-18541..7865,z=-77418..-60933",
    "on x=59594..82825,y=-28804..-8293,z=-10951..20475",
    "off x=-52646..-29322,y=-40881..-10533,z=-78124..-55227",
    "off x=-15749..8718,y=4472..14637,z=-91734..-64978",
    "off x=-85443..-73836,y=12784..39748,z=-16386..772",
    "on x=45947..61764,y=-35058..-17779,z=-64178..-45494",
    "off x=67007..86564,y=-48178..-21841,z=-7916..21903",
    "off x=-70444..-42983,y=29771..42787,z=-46211..-27338",
    "off x=-8655..2415,y=-91243..-75694,z=-10069..21248",
    "on x=-28009..-6226,y=-23740..-9157,z=-91944..-63046",
    "on x=-53152..-30990,y=-44975..-30727,z=52775..71982",
    "on x=-49716..-41146,y=-73921..-57473,z=11332..24465",
    "off x=-2468..25267,y=14929..32548,z=67505..84462",
    "on x=-68710..-62616,y=28813..52525,z=-10067..25405",
    "on x=-83946..-68639,y=-19770..10504,z=-33827..-25268",
    "off x=28131..44635,y=-50172..-27160,z=-62100..-58549",
    "off x=-5052..-648,y=-56625..-47094,z=-74342..-45910",
    "on x=-33892..-13031,y=18611..36918,z=-92168..-71425",
    "on x=12323..33021,y=-80108..-64718,z=-10537..4349",
    "on x=-65196..-43458,y=49295..56256,z=24974..37959",
    "off x=2343..28904,y=-66431..-45886,z=40141..44839",
    "off x=-43465..-41019,y=17236..49935,z=-74235..-53337",
    "off x=-18022..-9342,y=61778..91679,z=-11289..2632",
    "off x=27708..51714,y=32957..50756,z=-58390..-57621",
    "on x=2882..33961,y=57329..91039,z=-28800..8934",
    "on x=-28292..-11351,y=-12966..17150,z=59094..83553",
    "on x=-31558..-13040,y=-59193..-40820,z=48349..64602",
    "off x=-70755..-50969,y=-29136..-18641,z=-49761..-40422",
    "on x=19772..43254,y=-70111..-52042,z=29212..49446",
    "on x=20916..52515,y=-18713..-9635,z=-86771..-70085",
    "off x=-66621..-56476,y=33941..67405,z=-29611..-13697",
    "on x=-16965..3932,y=4803..22490,z=-82564..-77111",
    "on x=68709..71323,y=7232..38254,z=-30840..-18351",
    "off x=5053..18207,y=-90431..-74952,z=18441..31217",
    "off x=-74398..-51344,y=-2219..21971,z=-61004..-37925",
    "off x=74068..94286,y=-42547..-9453,z=-26993..4323",
    "off x=41826..54877,y=-63131..-48823,z=-42712..-13977",
    "off x=13230..36879,y=32795..49062,z=45626..77570",
    "off x=23178..54380,y=41412..62986,z=-66089..-51283",
    "off x=-52700..-47103,y=46951..63017,z=-23336..-3928",
    "on x=55437..83769,y=14588..38653,z=-53752..-37763",
    "on x=52203..65253,y=-47076..-16647,z=-44344..-39083",
    "on x=-24677..-13564,y=-93290..-68207,z=-5248..30373",
    "on x=58276..75450,y=15533..26129,z=36700..50632",
    "on x=33595..45488,y=-46844..-26635,z=46199..78178",
    "off x=55930..57540,y=-5693..10566,z=48756..60854",
    "off x=-43978..-26866,y=27173..53069,z=52366..76519",
    "off x=12681..30594,y=-86555..-56687,z=-1032..21854",
    "off x=6723..32769,y=-11041..11447,z=-81198..-62638",
    "on x=9134..15625,y=2017..27628,z=60348..76873",
    "off x=-67518..-40657,y=51003..78100,z=-26418..-11016",
    "off x=21010..26746,y=7821..43523,z=-88644..-58412",
    "off x=-19309..1323,y=63051..88447,z=-37925..-14723",
    "off x=-48511..-16244,y=56142..80658,z=-41680..-13036",
    "off x=13205..26460,y=-1684..20312,z=74227..85935",
    "on x=-49930..-24221,y=-54440..-30185,z=51665..80505",
    "on x=33932..55567,y=63494..66224,z=-10823..17738",
    "off x=-72574..-60303,y=-40445..-32434,z=14706..50012",
    "off x=-62145..-40946,y=-20722..-11341,z=-69258..-49860",
    "on x=-6554..15879,y=-66512..-52368,z=-71414..-48612",
    "on x=-60210..-31346,y=-68773..-53452,z=-45457..-19495",
    "off x=-22760..15679,y=64480..84538,z=4557..24345",
    "off x=40880..60578,y=-77805..-51810,z=-11706..22124",
    "off x=54298..63931,y=-50276..-24575,z=-36735..-19199",
    "off x=-2702..16842,y=-68238..-54782,z=51640..59991",
    "off x=-17862..105,y=-70163..-52096,z=-48967..-37649",
    "on x=-23272..-8212,y=10790..16944,z=75341..78080",
    "off x=48941..60207,y=-58116..-34953,z=-181..16162",
    "off x=5924..29813,y=-83457..-61519,z=23528..43432",
    "off x=-32079..-4914,y=42932..60356,z=-60990..-43336",
    "on x=-4510..5766,y=-7403..18802,z=64415..93546",
    "off x=26759..39620,y=48484..70752,z=-40115..-22503",
    "on x=-31250..-18094,y=-66695..-60649,z=36011..46860",
    "off x=-6978..17301,y=-82714..-67715,z=-35229..-13936",
    "on x=47265..63370,y=30543..57312,z=-46051..-16607",
    "on x=-14629..-7679,y=7650..29132,z=65592..94972",
    "on x=-66456..-38183,y=-52095..-46968,z=23915..46975",
    "off x=17676..42736,y=20462..26192,z=-81379..-67528",
    "off x=-67513..-46555,y=-24343..-99,z=-60193..-24652",
    "off x=-54467..-29572,y=-21268..-454,z=-66862..-49810",
    "off x=-19627..11711,y=-4455..22317,z=-83580..-68034",
    "on x=-38582..-13323,y=-58703..-34875,z=40913..79387",
    "on x=19178..32973,y=-59328..-56472,z=-68131..-40152",
    "off x=-45576..-23539,y=26133..50542,z=53177..62216",
    "off x=-77778..-52243,y=-48364..-42612,z=11905..32815",
    "on x=-79500..-68229,y=30167..46383,z=-6940..2452",
    "on x=31596..49128,y=598..18219,z=-81334..-54801",
    "off x=-81143..-68496,y=-16944..5539,z=-24074..-1450",
    "on x=-65649..-54882,y=-38296..-2979,z=29377..53941",
    "on x=6682..17340,y=-7921..-151,z=59077..85403",
    "off x=57914..76253,y=-4380..31345,z=-46399..-38698",
    "on x=32232..45129,y=-63185..-26040,z=36983..65363",
    "off x=-73881..-60419,y=-1795..21,z=37655..53767",
    "off x=15120..32138,y=63066..68156,z=16751..50217",
    "off x=23124..35098,y=36183..54646,z=47845..65258",
    "on x=51869..75912,y=6923..45250,z=-32268..-21057",
    "off x=49292..70804,y=-36314..-9052,z=-43544..-23519",
    "on x=21711..48338,y=2359..36023,z=60816..80004",
    "on x=-53507..-26657,y=-25557..-8931,z=-69305..-62052",
    "off x=60112..97989,y=-944..17784,z=-13750..15620",
    "on x=-28375..-10818,y=-52043..-34064,z=-65489..-55145",
    "on x=-58165..-43070,y=-12854..8136,z=-72321..-48657",
    "off x=51577..74648,y=-47469..-30666,z=8713..27929",
    "off x=-44464..-19855,y=-1741..22412,z=-79221..-59565",
    "off x=-89466..-59198,y=26732..49125,z=-11133..14327",
    "on x=53250..69420,y=44980..62695,z=4186..26328",
    "off x=26415..41630,y=-39332..-16373,z=-67936..-61161",
    "off x=-48619..-43433,y=-67120..-39586,z=28870..57974",
    "on x=17598..33705,y=30681..37573,z=43332..75560",
    "on x=-25540..-21306,y=-17465..4532,z=-91226..-71533",
    "off x=47293..62013,y=-25617..-8386,z=35935..50569",
    "off x=-49057..-28405,y=41861..63380,z=-51878..-39569",
    "off x=-5394..11201,y=39779..75186,z=-67429..-37636",
    "on x=-51758..-18083,y=-43700..-16277,z=44231..68503",
    "on x=-18052..11201,y=77165..95962,z=-18606..1615",
    "on x=-9094..15499,y=15118..29503,z=-88833..-67237",
    "on x=66146..81534,y=20925..38637,z=-16229..3378",
    "on x=-2669..13134,y=-80079..-65621,z=19565..43795",
    "on x=-71806..-67382,y=21162..50405,z=-6138..23589",
    "off x=19123..48071,y=-56188..-37077,z=48894..63329",
    "off x=-47660..-36230,y=40998..63389,z=-55710..-23610",
    "on x=-38780..-32773,y=62994..69808,z=32158..51582",
    "off x=63417..87982,y=-12566..21930,z=-30645..-20624",
    "on x=16242..53065,y=45895..74140,z=-57938..-26423",
    "on x=31963..45067,y=-36330..-22881,z=45365..68062",
    "on x=11053..33024,y=51385..80679,z=-47716..-39036",
    "off x=-30370..4676,y=22695..32755,z=67839..82155",
    "on x=1929..17141,y=-85885..-64577,z=-41851..-20316",
    "off x=46391..68161,y=47902..58287,z=-42465..-24023",
]
import numpy as np

OFFSET = 50


def run(board, data):
    results = 0
    for row in data:
        set, coords = row.split(" ")
        xr, yr, zr = coords.split(",")
        x1, x2 = xr[2:].split("..")
        y1, y2 = yr[2:].split("..")
        z1, z2 = zr[2:].split("..")
        print(set, xr, yr, zr)
        if set == "on":
            set = 1
        else:
            set = 0

        x1 = max(int(x1), OFFSET * -1) + OFFSET
        y1 = max(int(y1), OFFSET * -1) + OFFSET
        z1 = max(int(z1), OFFSET * -1) + OFFSET
        x2 = min(int(x2), OFFSET) + OFFSET
        y2 = min(int(y2), OFFSET) + OFFSET
        z2 = min(int(z2), OFFSET) + OFFSET

        for x in range(int(x1), int(x2) + 1):
            for y in range(int(y1), int(y2) + 1):
                for z in range(int(z1), int(z2) + 1):
                    board[x][y][z] = set
        print(f"sum {np.sum(board)}")
    results = np.sum(board)
    return results


if __name__ == "__main__":
    data = DATA
    board = np.zeros((OFFSET * 2 + 1, OFFSET * 2 + 1, OFFSET * 2 + 1))
    results = run(board, data)
    print(results)

import heapq

DATA_TEST = ['1163751742','1381373672','2136511328','3694931569','7463417111','1319128137','1359912421','3125421639','1293138521','2311944581']
DATA = ['3987747866912372378699589111691685987927655781731129891993417991549751299519163199614135992288259915','1298468647995818583786612276689623248185357694429712964833898932189561826128699577847128196528897619','9837311379191999519115682454597118537613483181915586394732473772994298997639661517161972887398121988','7668599952946712556341843271115878918719366648112619895686729828256178998863298512929718714715392919','1929853317875494137821196666891592794189989988817889479991989729313186981824497989752417279218877663','5924639123234787619929121414997517981485119877851618373249649587621991771281822369848969149583697517','7819896518795973795186577396198836319248914996997889992944437951837619289428995167525152945151124452','7329415932432117461279987773799811867699866858119259983694719381912437118828915675138999689916492312','4892271953741944119453159711873397748529898291791999991767971277999412992421769281559929888763691971','4495956566793739971931875548699487999277259897383562935292186511968837923969215176996347887768989971','1132488414433789473442968988799499831958157996796847169831622257996981238551597884171114772967988697','2741913298249919173975588999669523336184912668958391943959942817781539292839797389976225699525893326','4888497967819539598257152981159881267899262798176661119919855243399795594171171363689693185656593194','3953398928734328192877491496121291969949612682988218219289141719871748453119839897157184299359291913','1942721843891479948789333719361693843169791919763997275997227139782398283878994144329991961216958729','3212974463695832845951819131791525658129577219335948467936961847191976916725596917897993828268334689','5299642899597976991113911891337376876513116191942514768598719391698655628779993268513191914349179928','8821697765648971724962613295764154982826771599159999943496591929429282511368396118882678342188178916','1322319567727922398717991814958997159469713499621711725594919477398839828999799181573289781897114737','5357394896821977689521893995331873959725361133757955793581989894892551526833148464438979862918556948','7744172589764696856981591587469881191239683798625647174386174975419847123923817636927979988189154199','9249837641138391933693998597965392215881922139235234649667683117163694981181416623527979711882926519','1999942381931459128381113754867797717812997266991765839899942919565678316628739917213597819341299488','3299981997597813971149291981349339448863699728127619189871167559249757289999929993539138237765921773','6192539879199493229625789797261478565298231567929273352334632388442467717977951478225793996328971196','1127629184232746642388748881414446666881795295717291981632758967546891736171133257813179792374941916','3282391483565954989861663869412999989735635216649963491948114772798938772543372781695747121521189881','9999183761948979821785718369979735723911815486989232656257717441184118261749699851957137589721444769','3794856111831283759149261957873924676715727929648971321793168836678188171611649291879289969987992671','9815889925519325467993112819921999818541939117676296994821956496599796985968215931942118479162535532','7521182683563929947693851989899712768195833919161769182151629219111396773989215325189627483696959819','6253743891259963455971958157395619689897953967889775388223461279485198119182563849951415318961968993','1317331959889621169211318793399793181237394915288887517498191575218991942958697177934984298988186718','3561584368717889859691618891831149657786834914486191178218832244353289948268393788527998942824289386','4179818651186137398889398319179911516139285999111893113479829739988398599289325818291589986698988828','6198765318999434649196658516939859999288781352558574887229183117973891563712655561251729993745171342','3991121426947959681185174365698576153576926612771187489792259196992895719592455393271626972931361367','9959981389589693579287378469187538499999896837236287689599842876946289398936969868189179786695286797','8491514839865139774984138715811281288818816856967382855868976896278692122291492951861439914792576568','8298995159167911575965511891237591836589686787935287719897313848958993182842899887912719198142136957','4931228537399168779867818719934993491921765992295919989216998199779318589592124995259912779611559548','9947978219386795985624125198921839249831267999897124665353936122182972997113239771948612811486413343','9136871917923168937891911994618827592543189639291934898789694939729994554895844298495947448941898995','9916462361451258774449629288949995291492927118443595166349892221587216864598727588894619124232729921','6157145955679371971116189694468944553199479919216614443549777791159277498949941297399198687919698113','4754157894411299151928983433916835479971396719615265654639189999191947181689168213199675739421488985','3792389854256287755499275283378189774595891168949679238336593868399464449516865826757392863569135947','8817779899978122689636847237588795591963918248878979844298217896981933793949349387899811987139153696','9992178418183893366299533177992439457683779882592396384351988419161863135918986411296253783147816699','7519399876643486958588928463356668895568199979421915196738915991199391117678126583498915188583892958','1989396525978812986718694578811249916999126179761717519599815359998986939688121586899763144211191699','7889839919762137551489154267166355631226931294289193999259258899574117619233919487994881918598993249','2974991392873692692925999398365299823596371122843864593228745219267711547459787246249723791385119747','1219539228881511219644395768936929988899818758131174583257899998329939782639972165849568495355978985','3695329793197963178869962815233156883999144549497127969711366994749877882881393961931467466116994214','4129797987899991197819797569959225398289491141725297823989825276934169418348299218681388511196165647','9918151646913785991575379596178339996931799179918974918911691799351143341788914546192191495275253438','7285918592444378519561815899893241187918699764689564787914758739534649659499998227763151827944753169','9999874998278595127442329891355829418692185986971397983679379912984495884989998978156979937929842799','9232614577999128841119936647955917396188258997789864519745919187599871196998942169182229118783398765','9813829898689736964672866997312613551251499218281468659498256911533648957919971985255191846999215653','8998233646912331996944964663266619213921717553931951159988632381354189215951161413787868799279829532','7694999889699942426179748121657617963189973789817189919881392564769717992349291289961282197894957219','6947868592998191162549329819956383924991634893487198285182198889592395821712741287863147891559831499','8999112885485648397519967499544474144591689542997194895791917999891979491821319751164513289869381957','1991692949496198491758751311571677851651387121939984798938486276921973987451199542199686491951231722','9863379299698231811298683649398634594852449231889616429857984496799916642986554413391818389392966461','5941618753539995999121859548997995198628913814614977189927924899169258919655299872695969995491725399','5539986738297497865537399115235532879195978948699831741999199919993198421559378992124467361929989578','7765443948377671521569616851529928699942593798719183149271829859792199899951899583997396716233918219','1251217821683779797263628823768352991943589799181368332916176391966539476641397927197697753598219569','2925495231774876483329321237627893844811275479896199919813319741397826867114191514796187999641513826','3499282961932527896783918996176393279986156143748113861947225996598937983637891378489165193293589526','7879699719781478144397157376716593517972766196436254947683862889939817917968453977856174584212464962','3859894795798289842917897339523581937929198796839892628291934947743839829319891779122288951995832262','3963348259278259868288978888886999225389998726551642944716586439577131275814344379767417729972898494','2351563967718779382956962397918686399426489313536727988986473188238169148386853768288894911123995972','4566894549389199668929615898915821395131227285989339399886932982572817913814912274389481982768619129','6738278929925918376262191161527336799649477171199639928748797233984294792191779374597398594799922299','4998894122988259643856987247717122712665863871197196387495185871758239847998772488253281839311877985','4429828328796272766887311377994857996859162671999845399626993191988189981724164282921498983269979678','1164569681748757669913489823321998818325331691698198277553319951698769919949989955191921899599718575','6177428972194882751172831163613968496965988236195965945888319619599138793231789814797151565397998582','9495996991853259415828712492971495399144997161578933743231999443999151132926778998837894149149189189','9795397685686999379898981486233499654231185599352788618915165549688176991453935641879665967957961356','3856933141899312599697316683385849666511314177119618659889328615766597193991844919427596649416189444','3611348969793649671119437127894498885785425988876191218668993889175996994871296179153666946862675923','9284262311988999662188694877549898129911979448721188958785156928199331221775138116328365671219795894','8556124136987993777567989912927619231991159743421981873749126993891691217686428177453479672551991332','8758919777271663183499673146492769947178989539921978169981167832679239329381716223926135393569857399','9693639113228695749898869586974119129637695875398818278812599496513536925919139539195361761661997836','1971971157589715317685259116989971887359199792269892587955992578121399797719625935192667159719162949','4378473742379198691797958494911995854877334823298829996799688897467111969879419436285486624919919791','9776793917968144796191784469416491951792981976317498578433926785487921979129199377925358358946686899','1911749635854781158839458197267791497421955896242793138979383929341192216619471649997556718296191982','3922593894796259637836649698224899545878914266119635916953791716819481756437297991978997359238671292','9959952814925947145762596837698663199777378115973946993711329399178242178934383199849654154114529948','6111989752116239899485879148998691759892998977899172616119478299829332924575132618979412614691511195','9183473625115559878297612713929779999988194828441892889773271387893175317763491576739892293297229943','1456473931721698787995562828993762297498689998699535455881892534296898196126756968597779913784918896']


def run(data, start, end):

    paths = [(0, start[0], start[1])]

    visited = [[0] * len(row) for row in data]

    while True:
        rf, x, y = heapq.heappop(paths)

        if visited[x][y]:
            continue

        if (x, y) == end:
            return rf

        visited[x][y] = 1

        for x2, y2 in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            #if 0 < x2 < len(data) and 0 < y2 < len(data[0]):

            if visited[x2][y2] or not 0 <= x2 < len(data) or not 0 <= y2 < len(data[0]):
                continue
            heapq.heappush(paths, (rf + data[x2][y2], x2, y2))

if __name__ == "__main__":
    board = []
    data = DATA_TEST
    for row in data:
        board.append([int(x) for x in row])

    for row in board:
        print(row)

    results = run(board, (0, 0), (len(data) - 1, len(data[0]) - 1))
    print(results)
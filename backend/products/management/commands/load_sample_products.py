from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Load sample product(s) into the database'

    def handle(self, *args, **kwargs):
        product_data = [
         {
               "name": "Expanded intangible info-mediaries",
        "price": 10.64,
        "original_price": 76.76,
        "image": "https://source.unsplash.com/400x400/?product,0",
        "rating": 5.0,
        "reviews": 1410,
        "category": "Clothing",
        "description": "Event especially few type rich and blood firm plan."
    },
    {
               "name": "Advanced analyzing toolset",
        "price": 749.95,
        "original_price": 756.49,
        "image": "https://source.unsplash.com/400x400/?product,1",
        "rating": 4.4,
        "reviews": 1524,
        "category": "Toys",
        "description": "Despite eat truth happen agreement it who whole inside edge quickly receive bill onto compare."
    },
    {
               "name": "Open-source asynchronous core",
        "price": 617.31,
        "original_price": 645.98,
        "image": "https://source.unsplash.com/400x400/?product,2",
        "rating": 3.1,
        "reviews": 4320,
        "category": "Toys",
        "description": "Thank them international small weight business hard difficult worker with where two station."
    },
    {
               "name": "Multi-lateral methodical matrix",
        "price": 683.71,
        "original_price": 707.25,
        "image": "https://source.unsplash.com/400x400/?product,3",
        "rating": 3.3,
        "reviews": 1500,
        "category": "Home",
        "description": "Field throw nature camera work seem five establish paper thought pay book star test ten."
    },
    {
               "name": "Open-architected eco-centric synergy",
        "price": 158.42,
        "original_price": 232.51,
        "image": "https://source.unsplash.com/400x400/?product,4",
        "rating": 3.1,
        "reviews": 2886,
        "category": "Home",
        "description": "Civil toward leg travel democratic lot across rule scientist realize it space church."
    },
    {
               "name": "Mandatory clear-thinking conglomeration",
        "price": 581.43,
        "original_price": 586.6,
        "image": "https://source.unsplash.com/400x400/?product,5",
        "rating": 4.6,
        "reviews": 3724,
        "category": "Electronics",
        "description": "Find structure ok capital maintain hand loss there environmental rise."
    },
    {
               "name": "Profit-focused 5thgeneration superstructure",
        "price": 854.15,
        "original_price": 874.0,
        "image": "https://source.unsplash.com/400x400/?product,6",
        "rating": 4.9,
        "reviews": 569,
        "category": "Home",
        "description": "Kitchen show serious democratic century start public."
    },
    {
               "name": "Enhanced contextually-based methodology",
        "price": 942.37,
        "original_price": 1032.45,
        "image": "https://source.unsplash.com/400x400/?product,7",
        "rating": 4.0,
        "reviews": 1665,
        "category": "Electronics",
        "description": "Situation particularly direction program agency production spend foot indeed big."
    },
    {
               "name": "Visionary interactive portal",
        "price": 755.35,
        "original_price": 821.41,
        "image": "https://source.unsplash.com/400x400/?product,8",
        "rating": 3.5,
        "reviews": 2367,
        "category": "Home",
        "description": "Campaign wife bank hair note claim here role same return ever price will."
    },
    {
                "name": "Secured bifurcated portal",
        "price": 935.61,
        "original_price": 1034.9,
        "image": "https://source.unsplash.com/400x400/?product,9",
        "rating": 3.9,
        "reviews": 4034,
        "category": "Toys",
        "description": "Mind school couple moment born remember policy allow his easy summer friend administration not idea source."
    },
    {
                "name": "Progressive systemic initiative",
        "price": 538.13,
        "original_price": 544.49,
        "image": "https://source.unsplash.com/400x400/?product,10",
        "rating": 3.1,
        "reviews": 514,
        "category": "Books",
        "description": "Parent miss have recognize cell learn security bad condition indeed paper."
    },
    {
                "name": "Object-based bifurcated installation",
        "price": 947.18,
        "original_price": 1008.56,
        "image": "https://source.unsplash.com/400x400/?product,11",
        "rating": 3.4,
        "reviews": 1724,
        "category": "Clothing",
        "description": "Wonder effect floor always almost entire though ahead wrong fill meet music southern."
    },
    {
                "name": "Multi-lateral asymmetric support",
        "price": 577.76,
        "original_price": 620.53,
        "image": "https://source.unsplash.com/400x400/?product,12",
        "rating": 4.3,
        "reviews": 3989,
        "category": "Toys",
        "description": "Speak past air force appear performance career rule thing none heavy no."
    },
    {
                "name": "Networked transitional complexity",
        "price": 297.0,
        "original_price": 373.04,
        "image": "https://source.unsplash.com/400x400/?product,13",
        "rating": 3.7,
        "reviews": 1392,
        "category": "Home",
        "description": "Parent result reality break seem with none bag expect line perhaps arrive wide sell."
    },
    {
                "name": "Multi-layered eco-centric policy",
        "price": 809.66,
        "original_price": 897.48,
        "image": "https://source.unsplash.com/400x400/?product,14",
        "rating": 4.8,
        "reviews": 3853,
        "category": "Clothing",
        "description": "Out become book loss her seem group such meet today work full."
    },
    {
                "name": "Open-source content-based pricing structure",
        "price": 298.73,
        "original_price": 315.4,
        "image": "https://source.unsplash.com/400x400/?product,15",
        "rating": 4.4,
        "reviews": 2828,
        "category": "Books",
        "description": "During reflect thought include impact production federal local upon mission our."
    },
    {
                "name": "Integrated radical installation",
        "price": 44.24,
        "original_price": 77.93,
        "image": "https://source.unsplash.com/400x400/?product,16",
        "rating": 4.5,
        "reviews": 1906,
        "category": "Home",
        "description": "Court moment attention good number past its visit return check least voice customer thousand of."
    },
    {
                "name": "Inverse neutral core",
        "price": 893.33,
        "original_price": 952.58,
        "image": "https://source.unsplash.com/400x400/?product,17",
        "rating": 3.7,
        "reviews": 3485,
        "category": "Clothing",
        "description": "Couple civil all whom campaign major lot free beautiful suddenly score always."
    },
    {
                "name": "Re-engineered non-volatile emulation",
        "price": 170.3,
        "original_price": 200.97,
        "image": "https://source.unsplash.com/400x400/?product,18",
        "rating": 4.7,
        "reviews": 3243,
        "category": "Clothing",
        "description": "Yes position detail feeling difficult attention purpose response program."
    },
    {
                "name": "Up-sized fresh-thinking product",
        "price": 34.71,
        "original_price": 131.73,
        "image": "https://source.unsplash.com/400x400/?product,19",
        "rating": 3.9,
        "reviews": 3774,
        "category": "Books",
        "description": "Ball school factor national occur establish field trip."
    },
    {
                "name": "Optimized 24/7 synergy",
        "price": 480.77,
        "original_price": 571.05,
        "image": "https://source.unsplash.com/400x400/?product,20",
        "rating": 4.1,
        "reviews": 1954,
        "category": "Home",
        "description": "Born much seven off ask half during give mention fund few talk area."
    },
    {
                "name": "Open-architected interactive process improvement",
        "price": 688.44,
        "original_price": 777.15,
        "image": "https://source.unsplash.com/400x400/?product,21",
        "rating": 4.5,
        "reviews": 3271,
        "category": "Electronics",
        "description": "Institution author form sister benefit would through in condition stock the small meeting become word."
    },
    {
                "name": "Enterprise-wide actuating parallelism",
        "price": 861.31,
        "original_price": 958.86,
        "image": "https://source.unsplash.com/400x400/?product,22",
        "rating": 4.3,
        "reviews": 3208,
        "category": "Home",
        "description": "During work imagine own let specific window too less."
    },
    {
                "name": "Triple-buffered background process improvement",
        "price": 717.78,
        "original_price": 807.93,
        "image": "https://source.unsplash.com/400x400/?product,23",
        "rating": 4.7,
        "reviews": 1226,
        "category": "Books",
        "description": "Decision size several performance long city plan blood culture adult service."
    },
    {
                "name": "Optional mobile analyzer",
        "price": 944.78,
        "original_price": 987.54,
        "image": "https://source.unsplash.com/400x400/?product,24",
        "rating": 3.2,
        "reviews": 580,
        "category": "Electronics",
        "description": "Worry out agency whom family rather theory behind else poor look language."
    },
    {
                "name": "Function-based grid-enabled monitoring",
        "price": 68.1,
        "original_price": 120.78,
        "image": "https://source.unsplash.com/400x400/?product,25",
        "rating": 4.5,
        "reviews": 2133,
        "category": "Clothing",
        "description": "Include hospital speak protect letter notice big common unit audience federal lawyer."
    },
    {
                "name": "Re-contextualized 24hour array",
        "price": 536.87,
        "original_price": 544.13,
        "image": "https://source.unsplash.com/400x400/?product,26",
        "rating": 3.9,
        "reviews": 1187,
        "category": "Clothing",
        "description": "Control easy sit choice economic as they get company finish clear position source else easy."
    },
    {
                "name": "Managed eco-centric methodology",
        "price": 176.86,
        "original_price": 197.01,
        "image": "https://source.unsplash.com/400x400/?product,27",
        "rating": 3.2,
        "reviews": 2309,
        "category": "Electronics",
        "description": "Citizen box kid computer commercial picture plan."
    },
    {
                "name": "Synergized didactic throughput",
        "price": 706.2,
        "original_price": 734.38,
        "image": "https://source.unsplash.com/400x400/?product,28",
        "rating": 3.7,
        "reviews": 4851,
        "category": "Electronics",
        "description": "Will spend spend wear and senior use stand husband same fall ok talk suggest image."
    },
    {
                "name": "Universal asynchronous hub",
        "price": 62.26,
        "original_price": 139.81,
        "image": "https://source.unsplash.com/400x400/?product,29",
        "rating": 4.9,
        "reviews": 4874,
        "category": "Books",
        "description": "Throw dark should great matter example house cost represent trade hot television street fall explain."
    },
    {
                "name": "Vision-oriented next generation productivity",
        "price": 71.53,
        "original_price": 162.08,
        "image": "https://source.unsplash.com/400x400/?product,30",
        "rating": 3.3,
        "reviews": 4557,
        "category": "Home",
        "description": "Indeed power why determine environmental kitchen quickly also yourself item maintain yard accept store."
    },
    {
                "name": "Universal didactic orchestration",
        "price": 337.91,
        "original_price": 344.4,
        "image": "https://source.unsplash.com/400x400/?product,31",
        "rating": 4.1,
        "reviews": 900,
        "category": "Home",
        "description": "Allow unit movie director sit own research care through cell executive success nature difficult."
    },
    {
                "name": "Profit-focused tangible software",
        "price": 371.2,
        "original_price": 437.25,
        "image": "https://source.unsplash.com/400x400/?product,32",
        "rating": 4.7,
        "reviews": 4739,
        "category": "Books",
        "description": "Operation affect particular indicate around player wife young world democratic reason color beyond pay."
    },
    {
                "name": "Synergized responsive encryption",
        "price": 704.69,
        "original_price": 795.95,
        "image": "https://source.unsplash.com/400x400/?product,33",
        "rating": 3.6,
        "reviews": 2227,
        "category": "Electronics",
        "description": "News enough identify see senior dream base establish somebody bring like unit."
    },
    {
                "name": "Ergonomic local infrastructure",
        "price": 73.87,
        "original_price": 95.0,
        "image": "https://source.unsplash.com/400x400/?product,34",
        "rating": 3.9,
        "reviews": 4681,
        "category": "Electronics",
        "description": "Rest grow represent join page perhaps agree."
    },
    {
                "name": "Intuitive composite flexibility",
        "price": 550.93,
        "original_price": 577.13,
        "image": "https://source.unsplash.com/400x400/?product,35",
        "rating": 5.0,
        "reviews": 4468,
        "category": "Books",
        "description": "Discover south include class common someone perform few industry range run senior whom."
    },
    {
                "name": "Pre-emptive local function",
        "price": 85.56,
        "original_price": 184.87,
        "image": "https://source.unsplash.com/400x400/?product,36",
        "rating": 4.2,
        "reviews": 2457,
        "category": "Clothing",
        "description": "Hard art often job study system themselves tree eight lawyer."
    },
    {
                "name": "Triple-buffered intermediate collaboration",
        "price": 161.9,
        "original_price": 180.37,
        "image": "https://source.unsplash.com/400x400/?product,37",
        "rating": 3.0,
        "reviews": 216,
        "category": "Toys",
        "description": "Myself talk somebody where assume really and least school moment industry begin loss manage."
    },
    {
                "name": "Versatile zero-defect customer loyalty",
        "price": 290.98,
        "original_price": 370.55,
        "image": "https://source.unsplash.com/400x400/?product,38",
        "rating": 3.9,
        "reviews": 2073,
        "category": "Toys",
        "description": "Level evening concern identify poor benefit wall serve land kind like."
    },
    {
                "name": "Organized contextually-based infrastructure",
        "price": 506.41,
        "original_price": 546.55,
        "image": "https://source.unsplash.com/400x400/?product,39",
        "rating": 4.2,
        "reviews": 1951,
        "category": "Clothing",
        "description": "Nature prove result American western region explain itself baby population line rest claim sense mission lay."
    },
    {
                "name": "Mandatory zero tolerance intranet",
        "price": 633.68,
        "original_price": 695.41,
        "image": "https://source.unsplash.com/400x400/?product,40",
        "rating": 4.7,
        "reviews": 3435,
        "category": "Toys",
        "description": "Later increase affect guess during author force thank affect road."
    },
    {
                "name": "Compatible uniform software",
        "price": 884.43,
        "original_price": 895.8,
        "image": "https://source.unsplash.com/400x400/?product,41",
        "rating": 4.8,
        "reviews": 226,
        "category": "Electronics",
        "description": "Drive well son value rate treatment also pattern free what sea day."
    },
    {
                "name": "Open-architected tangible analyzer",
        "price": 522.8,
        "original_price": 567.9,
        "image": "https://source.unsplash.com/400x400/?product,42",
        "rating": 4.1,
        "reviews": 2374,
        "category": "Clothing",
        "description": "Eat community enter week include east poor deal peace candidate social picture participant."
    },
    {
                "name": "Balanced zero administration strategy",
        "price": 952.37,
        "original_price": 970.53,
        "image": "https://source.unsplash.com/400x400/?product,43",
        "rating": 4.3,
        "reviews": 1722,
        "category": "Clothing",
        "description": "Activity over relate poor son true dinner tough everybody stop perform organization read develop clear."
    },
    {
                "name": "Horizontal high-level database",
        "price": 118.51,
        "original_price": 129.04,
        "image": "https://source.unsplash.com/400x400/?product,44",
        "rating": 3.9,
        "reviews": 4527,
        "category": "Toys",
        "description": "Partner decade manager baby technology effort effort from."
    },
    {
                "name": "Triple-buffered modular initiative",
        "price": 896.7,
        "original_price": 905.49,
        "image": "https://source.unsplash.com/400x400/?product,45",
        "rating": 5.0,
        "reviews": 4831,
        "category": "Home",
        "description": "Gas street parent machine mention both serious national focus have kitchen road fly both address nothing."
    },
    {
                "name": "Optimized heuristic neural-net",
        "price": 462.98,
        "original_price": 517.72,
        "image": "https://source.unsplash.com/400x400/?product,46",
        "rating": 3.6,
        "reviews": 82,
        "category": "Books",
        "description": "Field much over might brother reach environmental affect life few land nothing movement ready social past."
    },
    {
                "name": "Multi-layered fresh-thinking project",
        "price": 579.68,
        "original_price": 647.72,
        "image": "https://source.unsplash.com/400x400/?product,47",
        "rating": 3.4,
        "reviews": 642,
        "category": "Toys",
        "description": "Language nothing rock should plan marriage important guy someone more science late prove store second."
    },
    {
                "name": "Proactive even-keeled service-desk",
        "price": 958.34,
        "original_price": 975.1,
        "image": "https://source.unsplash.com/400x400/?product,48",
        "rating": 4.1,
        "reviews": 1504,
        "category": "Electronics",
        "description": "Enter but population read performance reflect hope language month bag read sound sound take owner."
    },
    {
                "name": "Re-engineered real-time solution",
        "price": 26.46,
        "original_price": 92.37,
        "image": "https://source.unsplash.com/400x400/?product,49",
        "rating": 4.4,
        "reviews": 2562,
        "category": "Clothing",
        "description": "Maybe water defense last office should either white population wonder onto."
    },
    {
                "name": "Diverse holistic superstructure",
        "price": 475.96,
        "original_price": 523.66,
        "image": "https://source.unsplash.com/400x400/?product,50",
        "rating": 3.2,
        "reviews": 3676,
        "category": "Clothing",
        "description": "Pm especially learn here final himself onto air various address PM his."
    },
    {
                "name": "Seamless systematic time-frame",
        "price": 531.16,
        "original_price": 580.26,
        "image": "https://source.unsplash.com/400x400/?product,51",
        "rating": 4.7,
        "reviews": 1538,
        "category": "Books",
        "description": "Low assume world condition size page serve however former five want effect prove face."
    },
    {
                "name": "Automated regional matrix",
        "price": 962.35,
        "original_price": 994.57,
        "image": "https://source.unsplash.com/400x400/?product,52",
        "rating": 4.7,
        "reviews": 912,
        "category": "Home",
        "description": "New ahead keep fire hour young his relationship brother plan."
    },
    {
                "name": "Innovative context-sensitive secured line",
        "price": 720.17,
        "original_price": 800.62,
        "image": "https://source.unsplash.com/400x400/?product,53",
        "rating": 3.0,
        "reviews": 4922,
        "category": "Clothing",
        "description": "Tell activity life increase pattern draw shoulder."
    },
    {
                "name": "Sharable transitional knowledge user",
        "price": 334.55,
        "original_price": 396.85,
        "image": "https://source.unsplash.com/400x400/?product,54",
        "rating": 4.4,
        "reviews": 1616,
        "category": "Home",
        "description": "The language authority pay direction clear husband girl charge upon."
    },
    {
                "name": "Total systemic ability",
        "price": 250.83,
        "original_price": 337.14,
        "image": "https://source.unsplash.com/400x400/?product,55",
        "rating": 3.8,
        "reviews": 4734,
        "category": "Home",
        "description": "Life while run avoid authority write head benefit maintain quality often sometimes."
    },
    {
                "name": "Public-key next generation capacity",
        "price": 699.97,
        "original_price": 727.9,
        "image": "https://source.unsplash.com/400x400/?product,56",
        "rating": 3.6,
        "reviews": 914,
        "category": "Home",
        "description": "Figure audience threat against hand authority PM PM old whether account."
    },
    {
                "name": "Networked global data-warehouse",
        "price": 386.1,
        "original_price": 464.38,
        "image": "https://source.unsplash.com/400x400/?product,57",
        "rating": 3.9,
        "reviews": 3207,
        "category": "Home",
        "description": "Light company begin effect let forget support forward everything for audience some social dark common gas."
    },
    {
                "name": "Mandatory multimedia database",
        "price": 388.79,
        "original_price": 415.24,
        "image": "https://source.unsplash.com/400x400/?product,58",
        "rating": 4.1,
        "reviews": 2524,
        "category": "Electronics",
        "description": "Write once throw picture piece property culture too activity magazine."
    },
    {
                "name": "Exclusive composite initiative",
        "price": 830.38,
        "original_price": 871.25,
        "image": "https://source.unsplash.com/400x400/?product,59",
        "rating": 4.1,
        "reviews": 819,
        "category": "Toys",
        "description": "Performance who at everybody recognize rise kid drop project glass."
    },
    {
                "name": "Digitized fresh-thinking matrix",
        "price": 726.21,
        "original_price": 747.75,
        "image": "https://source.unsplash.com/400x400/?product,60",
        "rating": 4.5,
        "reviews": 4622,
        "category": "Home",
        "description": "Tonight save history what field hit form because."
    },
    {
                "name": "Automated logistical framework",
        "price": 137.47,
        "original_price": 220.79,
        "image": "https://source.unsplash.com/400x400/?product,61",
        "rating": 3.2,
        "reviews": 3020,
        "category": "Home",
        "description": "On candidate listen easy wide pass ever today bit child painting financial century during."
    },
    {
                "name": "Customizable directional capability",
        "price": 886.24,
        "original_price": 916.92,
        "image": "https://source.unsplash.com/400x400/?product,62",
        "rating": 4.8,
        "reviews": 3052,
        "category": "Toys",
        "description": "Identify long approach minute worry bit face artist staff culture."
    },
    {
                "name": "Face-to-face dynamic extranet",
        "price": 770.07,
        "original_price": 821.46,
        "image": "https://source.unsplash.com/400x400/?product,63",
        "rating": 3.2,
        "reviews": 2766,
        "category": "Clothing",
        "description": "Officer behavior reveal opportunity dog growth amount fast series one specific."
    },
    {
                "name": "Devolved national workforce",
        "price": 661.58,
        "original_price": 745.74,
        "image": "https://source.unsplash.com/400x400/?product,64",
        "rating": 4.0,
        "reviews": 2679,
        "category": "Books",
        "description": "Threat quickly surface site thousand try staff phone assume beat long natural artist."
    },
    {
                "name": "Fully-configurable reciprocal approach",
        "price": 936.61,
        "original_price": 994.65,
        "image": "https://source.unsplash.com/400x400/?product,65",
        "rating": 4.2,
        "reviews": 1830,
        "category": "Electronics",
        "description": "Effect Mrs this pull almost individual sport."
    },
    {
                "name": "Multi-channeled tangible archive",
        "price": 867.96,
        "original_price": 902.86,
        "image": "https://source.unsplash.com/400x400/?product,66",
        "rating": 3.1,
        "reviews": 327,
        "category": "Toys",
        "description": "Soldier strong serious care some trip education western executive road control pass back memory should law."
    },
    {
                "name": "Enterprise-wide 6thgeneration groupware",
        "price": 918.45,
        "original_price": 932.46,
        "image": "https://source.unsplash.com/400x400/?product,67",
        "rating": 4.2,
        "reviews": 3282,
        "category": "Toys",
        "description": "Lead final natural health prevent seem must."
    },
    {
                "name": "Compatible motivating portal",
        "price": 317.0,
        "original_price": 406.97,
        "image": "https://source.unsplash.com/400x400/?product,68",
        "rating": 4.2,
        "reviews": 2310,
        "category": "Home",
        "description": "Teach finish pretty soon computer analysis third car rock issue answer head risk girl."
    },
    {
                "name": "Quality-focused zero administration alliance",
        "price": 262.69,
        "original_price": 318.5,
        "image": "https://source.unsplash.com/400x400/?product,69",
        "rating": 3.0,
        "reviews": 754,
        "category": "Home",
        "description": "This according these easy after different inside two itself worker person cup billion."
    },
    {
                "name": "Reverse-engineered system-worthy array",
        "price": 934.93,
        "original_price": 993.04,
        "image": "https://source.unsplash.com/400x400/?product,70",
        "rating": 4.2,
        "reviews": 1134,
        "category": "Electronics",
        "description": "Begin I Republican rich history state deep."
    },
    {
                "name": "Stand-alone global monitoring",
        "price": 525.18,
        "original_price": 606.36,
        "image": "https://source.unsplash.com/400x400/?product,71",
        "rating": 3.2,
        "reviews": 4652,
        "category": "Clothing",
        "description": "Word against lot still seat base weight realize."
    },
    {
                "name": "Business-focused scalable core",
        "price": 19.11,
        "original_price": 50.23,
        "image": "https://source.unsplash.com/400x400/?product,72",
        "rating": 3.9,
        "reviews": 1726,
        "category": "Home",
        "description": "Statement case watch thank not situation edge push tree none compare character focus former between modern."
    },
    {
                "name": "Vision-oriented attitude-oriented projection",
        "price": 718.12,
        "original_price": 745.35,
        "image": "https://source.unsplash.com/400x400/?product,73",
        "rating": 4.5,
        "reviews": 601,
        "category": "Toys",
        "description": "Morning cell cold believe start find police interesting."
    },
    {
                "name": "Multi-channeled uniform orchestration",
        "price": 479.11,
        "original_price": 543.74,
        "image": "https://source.unsplash.com/400x400/?product,74",
        "rating": 4.5,
        "reviews": 1651,
        "category": "Clothing",
        "description": "Third computer eight direction benefit our class property few time know check mean try best."
    },
    {
                "name": "Team-oriented even-keeled instruction set",
        "price": 376.6,
        "original_price": 386.54,
        "image": "https://source.unsplash.com/400x400/?product,75",
        "rating": 4.0,
        "reviews": 2078,
        "category": "Books",
        "description": "Cultural item approach car interest dark every necessary central."
    },
    {
                "name": "Triple-buffered bi-directional initiative",
        "price": 297.53,
        "original_price": 309.85,
        "image": "https://source.unsplash.com/400x400/?product,76",
        "rating": 4.2,
        "reviews": 3107,
        "category": "Clothing",
        "description": "Many camera and address both happen responsibility effort project teacher eight federal commercial possible physical."
    },
    {
                "name": "Organic multimedia implementation",
        "price": 246.0,
        "original_price": 310.7,
        "image": "https://source.unsplash.com/400x400/?product,77",
        "rating": 3.3,
        "reviews": 1057,
        "category": "Clothing",
        "description": "Family any clear grow seek that produce the staff drop."
    },
    {
                "name": "Reverse-engineered disintermediate help-desk",
        "price": 790.96,
        "original_price": 804.88,
        "image": "https://source.unsplash.com/400x400/?product,78",
        "rating": 3.3,
        "reviews": 3813,
        "category": "Books",
        "description": "Person at bring write beautiful scientist suffer method two smile it."
    },
    {
                "name": "Monitored transitional Graphic Interface",
        "price": 683.59,
        "original_price": 718.72,
        "image": "https://source.unsplash.com/400x400/?product,79",
        "rating": 3.8,
        "reviews": 4087,
        "category": "Books",
        "description": "Public few daughter lead east poor case."
    },
    {
                "name": "Integrated homogeneous functionalities",
        "price": 488.0,
        "original_price": 506.56,
        "image": "https://source.unsplash.com/400x400/?product,80",
        "rating": 4.5,
        "reviews": 1662,
        "category": "Books",
        "description": "Town politics sound ball fight work executive others ahead loss trip both official require who."
    },
    {
                "name": "Ameliorated attitude-oriented extranet",
        "price": 720.02,
        "original_price": 731.21,
        "image": "https://source.unsplash.com/400x400/?product,81",
        "rating": 4.8,
        "reviews": 1669,
        "category": "Toys",
        "description": "Near sure build always agree offer watch while response admit particularly per."
    },
    {
                "name": "Proactive logistical project",
        "price": 903.58,
        "original_price": 938.6,
        "image": "https://source.unsplash.com/400x400/?product,82",
        "rating": 3.3,
        "reviews": 2645,
        "category": "Toys",
        "description": "Decade six organization put special industry suffer."
    },
    {
                "name": "Front-line leadingedge projection",
        "price": 926.29,
        "original_price": 969.63,
        "image": "https://source.unsplash.com/400x400/?product,83",
        "rating": 3.8,
        "reviews": 3553,
        "category": "Toys",
        "description": "Coach entire woman power town music treat politics society last."
    },
    {
                "name": "Devolved 3rdgeneration infrastructure",
        "price": 146.26,
        "original_price": 245.82,
        "image": "https://source.unsplash.com/400x400/?product,84",
        "rating": 4.2,
        "reviews": 4798,
        "category": "Home",
        "description": "Charge let play allow happy fill home husband something goal share whole nothing sister."
    },
    {
                "name": "Compatible tangible info-mediaries",
        "price": 531.42,
        "original_price": 624.55,
        "image": "https://source.unsplash.com/400x400/?product,85",
        "rating": 4.6,
        "reviews": 2255,
        "category": "Electronics",
        "description": "Each consider hand he few per strategy upon usually quite top story age firm half."
    },
    {
                "name": "Fundamental methodical application",
        "price": 394.75,
        "original_price": 458.2,
        "image": "https://source.unsplash.com/400x400/?product,86",
        "rating": 3.5,
        "reviews": 3214,
        "category": "Clothing",
        "description": "Soldier pass summer audience small nothing onto care decision it seat finally sell shoulder since."
    },
    {
                "name": "Face-to-face disintermediate interface",
        "price": 279.32,
        "original_price": 336.71,
        "image": "https://source.unsplash.com/400x400/?product,87",
        "rating": 4.7,
        "reviews": 4911,
        "category": "Electronics",
        "description": "Also source represent lot open skill arm cultural only standard quite dark kind three."
    },
    {
                "name": "Networked multi-tasking frame",
        "price": 348.5,
        "original_price": 401.2,
        "image": "https://source.unsplash.com/400x400/?product,88",
        "rating": 4.6,
        "reviews": 2705,
        "category": "Electronics",
        "description": "House site finally speech nation situation party yet brother open collection against."
    },
    {
                "name": "Quality-focused bi-directional info-mediaries",
        "price": 458.24,
        "original_price": 496.33,
        "image": "https://source.unsplash.com/400x400/?product,89",
        "rating": 3.9,
        "reviews": 3929,
        "category": "Books",
        "description": "Collection true visit remember baby church medical."
    },
    {
                "name": "Function-based full-range knowledgebase",
        "price": 70.28,
        "original_price": 109.54,
        "image": "https://source.unsplash.com/400x400/?product,90",
        "rating": 4.3,
        "reviews": 193,
        "category": "Toys",
        "description": "Lead can pressure store up space least material left return again mean."
    },
    {
                "name": "Self-enabling stable moderator",
        "price": 810.44,
        "original_price": 842.13,
        "image": "https://source.unsplash.com/400x400/?product,91",
        "rating": 3.0,
        "reviews": 751,
        "category": "Electronics",
        "description": "Tax executive sell east themselves keep degree."
    },
    {
                "name": "Innovative systemic functionalities",
        "price": 280.93,
        "original_price": 341.93,
        "image": "https://source.unsplash.com/400x400/?product,92",
        "rating": 3.6,
        "reviews": 2491,
        "category": "Electronics",
        "description": "Same major none light hot evening sometimes memory like rest."
    },
    {
                "name": "Team-oriented analyzing product",
        "price": 489.27,
        "original_price": 582.29,
        "image": "https://source.unsplash.com/400x400/?product,93",
        "rating": 3.6,
        "reviews": 1843,
        "category": "Toys",
        "description": "Third commercial respond new similar town issue street same knowledge grow."
    },
    {
                "name": "Public-key 24hour secured line",
        "price": 469.8,
        "original_price": 541.8,
        "image": "https://source.unsplash.com/400x400/?product,94",
        "rating": 4.8,
        "reviews": 4398,
        "category": "Electronics",
        "description": "Dinner real push compare according surface someone a agent whole positive phone single."
    },
    {
                "name": "Secured grid-enabled info-mediaries",
        "price": 620.13,
        "original_price": 641.43,
        "image": "https://source.unsplash.com/400x400/?product,95",
        "rating": 4.6,
        "reviews": 4807,
        "category": "Toys",
        "description": "Accept whole late anything spend debate crime pass generation like environmental as black operation customer college."
    },
    {
                "name": "User-centric bottom-line budgetary management",
        "price": 573.25,
        "original_price": 665.96,
        "image": "https://source.unsplash.com/400x400/?product,96",
        "rating": 4.2,
        "reviews": 1582,
        "category": "Home",
        "description": "Son show public sit money anything by land any hot chair paper enjoy health."
    },
    {
                "name": "Persistent real-time neural-net",
        "price": 974.48,
        "original_price": 985.67,
        "image": "https://source.unsplash.com/400x400/?product,97",
        "rating": 3.9,
        "reviews": 1029,
        "category": "Electronics",
        "description": "Appear minute few sit their star analysis."
    },
    {
                "name": "User-friendly web-enabled infrastructure",
        "price": 569.32,
        "original_price": 628.94,
        "image": "https://source.unsplash.com/400x400/?product,98",
        "rating": 3.8,
        "reviews": 1709,
        "category": "Home",
        "description": "No bar just experience occur rate note we practice door story about Congress against back city."
    },
    {
        
        "name": "Stand-alone 24hour structure",
        "price": 744.05,
        "original_price": 790.17,
        "image": "https://source.unsplash.com/400x400/?product,99",
        "rating": 4.4,
        "reviews": 3589,
        "category": "Books",
        "description": "Store peace foreign care dream notice seat."
    }
        ]

        for data in product_data:
            Product.objects.create(**data)

        self.stdout.write(self.style.SUCCESS(f"✅ {len(product_data)} product(s) inserted successfully."))

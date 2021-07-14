


DROP table if exists total_vaccinations;




CREATE TABLE total_vaccinations (

date VARCHAR(255) NOT NULL,
location VARCHAR(255) NOT NULL,
distributed INT NOT NULL,
distributed_Janssen INT NOT NULL,
distributed_Moderna INT NOT NULL,
distributed_Pfizer INT NOT NULL,
distributed_per_100k INT NOT NULL,
distributed_per_100k_12Plus INT NOT NULL,
distributed_per_100k_18Plus INT NOT NULL,
distributed_per_100k_65Plus INT NOT NULL,
administered INT NOT NULL,
administered_12Plus INT NOT NULL,
administered_18Plus INT NOT NULL,
administered_65Plus INT NOT NULL,
administered_Janssen INT NOT NULL,
administered_Moderna INT NOT NULL,
administered_Pfizer INT NOT NULL,
PRIMARY KEY (date, location));





INSERT INTO total_vaccinations VALUES ('07/13/2021','OH',12528435,655500,5255040,6617895,107180,125276,137508,612242,10850538,10850288,10372340,3361930,438362,4427144,5971236);
INSERT INTO total_vaccinations VALUES ('07/13/2021','LTC',66409995,2474700,19536540,44398755,0,0,0,0,7901183,0,0,0,24966,2003814,5865186);
INSERT INTO total_vaccinations VALUES ('07/13/2021','WV',1917545,110200,870880,936465,106997,123090,133853,522476,1478665,1477764,1414341,534366,37405,678674,762236);
INSERT INTO total_vaccinations VALUES ('07/13/2021','IL',14866895,850700,5842500,8173695,117322,137176,150873,727617,13239927,13199818,12432905,3330081,468609,5185299,7574271);
INSERT INTO total_vaccinations VALUES ('07/13/2021','KY',4532515,266500,1989420,2276595,101451,119083,130816,603881,4069039,4067983,3903773,1195012,169321,1773699,2125460);
INSERT INTO total_vaccinations VALUES ('07/13/2021','WI',6208215,318700,2634440,3255075,106626,124169,136269,610298,6025434,6025070,5738629,1837595,240952,2472193,3311615);
INSERT INTO total_vaccinations VALUES ('07/13/2021','KS',3130345,173500,1369140,1587705,107450,127681,141448,658345,2529234,2529110,2425644,786433,85014,1105063,1338418);
INSERT INTO total_vaccinations VALUES ('07/13/2021','MD',8587760,440400,3366380,4780980,142048,166336,182292,895122,7015970,7015616,6576601,1666897,269585,2708481,4030381);
INSERT INTO total_vaccinations VALUES ('07/13/2021','US',387241530,21435300,159562800,206243430,116640,136571,149943,707981,334942236,334592838,317898069,91185125,12869516,136001959,185798639);
INSERT INTO total_vaccinations VALUES ('07/13/2021','FM',78800,10200,68600,0,76030,89030,97614,448722,53230,53217,53192,4385,6232,46998,0,0,151,0,151,0,89,0,89,0);
INSERT INTO total_vaccinations VALUES ('07/13/2021','PA',15864775,1060700,6748040,8056035,123924,143164,156036,662866,14155007,14150880,13497646,4372206,549722,5851598,7753219);
INSERT INTO total_vaccinations VALUES ('07/13/2021','RP',24600,3800,20800,0,137376,160868,176382,810811,25416,25416,25416,3113,2113,23302,1);
INSERT INTO total_vaccinations VALUES ('07/13/2021','WY',519885,34000,250280,235605,89828,105943,116822,524189,436027,436005,421807,146325,17975,206129,211690);
INSERT INTO total_vaccinations VALUES ('07/13/2021','ND',725260,36500,316940,371820,95171,113812,124638,605165,650150,649124,627059,193983,29071,276905,344174);
INSERT INTO total_vaccinations VALUES ('07/13/2021','NY',24360185,1253900,9969300,13136985,0,125222,145233,157924,739051,22281273,22279513,21224789,5413173,976110,8858930,12440354);
INSERT INTO total_vaccinations VALUES ('07/13/2021','DD2',4397410,186300,1843300,2367810,0,0,0,0,4393186,4390581,4228686,352324,159509,1779203,2453314);
INSERT INTO total_vaccinations VALUES ('07/13/2021','NM',2397305,138500,1044180,1214625,114330,134120,147891,634869,2423844,2423614,2284487,657482,84403,1061510,1274050);
INSERT INTO total_vaccinations VALUES ('07/13/2021','WA',9521955,495000,3847920,5179035,125044,146471,159984,787119,8787696,8786877,8287837,2130116,363082,3487384,4931755);
INSERT INTO total_vaccinations VALUES ('07/13/2021','GU',215770,19500,74200,122070,130164,152421,167116,768220,194949,194932,179190,29315,4985,71069,118895);
INSERT INTO total_vaccinations VALUES ('07/13/2021','DE',1298745,65800,532100,700845,133374,154648,168626,687509,1060601,1060415,1005074,334903,45930,423097,591041);
INSERT INTO total_vaccinations VALUES ('07/13/2021','AK',840365,59300,360780,420285,114875,138019,152361,917549,683718,681754,644988,142173,26883,286455,370205);
INSERT INTO total_vaccinations VALUES ('07/13/2021','IH2',1760015,74700,923300,762015,84502,0,0,0,1459940,1459444,1371555,276647,26190,775632,658118);
INSERT INTO total_vaccinations VALUES ('07/13/2021','VA',10514845,545400,4101940,5867505,123189,143902,157534,773773,9417569,9387393,8820744,2279711,338484,3585258,5491240);
INSERT INTO total_vaccinations VALUES ('07/13/2021','MO',6214485,311400,2542080,3361005,101256,118694,130369,585148,5223740,5223411,5010837,1646450,175197,1981544,3066501);
INSERT INTO total_vaccinations VALUES ('07/13/2021','TN',6443560,367800,2680420,3395340,94353,110419,121140,563547,5556029,5555375,5376248,1788930,172838,2251305,3117930);
INSERT INTO total_vaccinations VALUES ('07/13/2021','SC',5370875,313300,2324560,2733015,104315,121514,133024,573185,4273022,4265215,4121899,1497483,151791,1727646,2392499);
INSERT INTO total_vaccinations VALUES ('07/13/2021','RI',1529185,61600,620820,846765,144350,164873,178880,817545,1297715,1297619,1226320,345101,47425,511186,738949);
INSERT INTO total_vaccinations VALUES ('07/13/2021','VI',81030,900,24300,55830,77407,90643,99383,456842,79952,79880,77555,24158,1041,24410,54501);
INSERT INTO total_vaccinations VALUES ('07/13/2021','BP2',205990,10600,86220,109170,0,0,0,0,197069,197068,197068,6397,8640,81369,107060);
INSERT INTO total_vaccinations VALUES ('07/13/2021','ID',1707030,100100,714940,891990,95521,114152,127498,587274,1345021,1344996,1344466,457352,53048,575840,715124);
INSERT INTO total_vaccinations VALUES ('07/13/2021','AR',2879090,178900,1299520,1400670,95403,112585,124225,549568,2292296,2287369,2205086,747267,79775,1063948,1147937);
INSERT INTO total_vaccinations VALUES ('07/13/2021','MS',2701255,164600,1194740,1341915,90763,107132,118603,555022,2051000,2050886,2001874,707013,61033,927284,1061704);
INSERT INTO total_vaccinations VALUES ('07/13/2021','MI',11712540,651800,4915600,6145140,117280,136272,149339,663449,9582679,9582325,9121439,2847289,331733,3916440,5333112);
INSERT INTO total_vaccinations VALUES ('07/13/2021','PR',4236710,190000,1823740,2222970,132659,148746,161647,780345,3839872,3838647,3597324,1031627,108725,1650033,2080776);
INSERT INTO total_vaccinations VALUES ('07/13/2021','HI',1957730,81700,774460,1101570,138270,161648,175423,729277,1698213,1693658,1605743,485313,37454,593233,973762);
INSERT INTO total_vaccinations VALUES ('07/13/2021','TX',32258525,1894600,12998320,17365605,111252,133847,149372,863860,26327776,26322585,24860596,5975811,1041765,10683632,14601500);
INSERT INTO total_vaccinations VALUES ('07/13/2021','AZ',8246730,431000,3425380,4390350,113299,132882,146258,630179,6898130,6897313,6553673,2128415,246532,2925029,3719585);
INSERT INTO total_vaccinations VALUES ('07/13/2021','FL',25260095,1694500,10227580,13338015,117611,135109,146454,561668,21603473,21595225,20827509,7912210,1054867,8594766,11900473);
INSERT INTO total_vaccinations VALUES ('07/13/2021','OK',4058650,222300,1780420,2055930,102570,122056,135075,639025,3330922,3330732,3207616,1009404,99108,1475367,1756363);
INSERT INTO total_vaccinations VALUES ('07/13/2021','VA2',6245680,522400,2988600,2734680,0,0,0,0,5381564,5381407,5379885,2851360,176105,2784105,2421350);
INSERT INTO total_vaccinations VALUES ('07/13/2021','IA',3506995,188700,1460140,1858155,111154,131040,144426,634229,3076964,3076932,2934987,960187,129047,1298453,1649336);
INSERT INTO total_vaccinations VALUES ('07/13/2021','ME',1874470,103100,805220,966150,139447,158192,171127,657098,1637747,1637649,1551895,508522,106729,689818,840738);
INSERT INTO total_vaccinations VALUES ('07/13/2021','NV',3151460,184300,1248880,1718280,102315,120202,131997,635411,2851032,2850991,2730970,772473,128864,1108783,1613371);
INSERT INTO total_vaccinations VALUES ('07/13/2021','NE',2113750,108100,838920,1166730,109271,130687,144943,676491,1892114,1891835,1797196,547774,69586,748709,1070227);
INSERT INTO total_vaccinations VALUES ('07/13/2021','NC',11827760,646500,4879220,6302040,112773,131631,144464,675450,9443201,9429466,8995246,2811821,352257,3747117,5343389);
INSERT INTO total_vaccinations VALUES ('07/13/2021','AS',54030,600,15600,37830,97021,113611,124565,572594,48722,48715,45015,4980,477,11972,36273);
INSERT INTO total_vaccinations VALUES ('07/13/2021','NH',1864020,116700,749040,998280,137089,155520,168772,734259,1564776,1564165,1479699,434335,59081,650002,855671);
INSERT INTO total_vaccinations VALUES ('07/13/2021','MP',72330,2600,20200,49530,127158,148901,163258,750467,57764,57764,52934,5345,458,8045,49261);
INSERT INTO total_vaccinations VALUES ('07/13/2021','IN',6779950,427500,2699020,3653430,100709,118841,131286,624453,5908921,5908599,5648536,1815030,219930,2310670,3360060);
INSERT INTO total_vaccinations VALUES ('07/13/2021','OR',5690905,310200,2352400,3028305,134928,156011,169818,742860,4645898,4631958,4378911,1248694,178126,1824046,2640909);
INSERT INTO total_vaccinations VALUES ('07/13/2021','CA',49704865,2615800,20205120,26883945,125796,147728,162341,851386,43692413,43565619,40994055,9886842,1601523,17614179,24469260);
INSERT INTO total_vaccinations VALUES ('07/13/2021','DC',1072695,54400,425780,592515,151994,175923,185722,1228140,881592,881513,858502,170922,28342,346474,506388);
INSERT INTO total_vaccinations VALUES ('07/13/2021','CO',7107335,340300,2916760,3850275,123418,143988,157968,843689,6312560,6292868,5925406,1422522,226489,2616673,3465974);
INSERT INTO total_vaccinations VALUES ('07/13/2021','MA',9830140,444700,3934020,5451420,142621,163380,177449,840663,8971161,8942786,8403053,2074941,296680,3569768,5104502);
INSERT INTO total_vaccinations VALUES ('07/13/2021','AL',4885650,281300,2240860,2363490,99642,116690,128068,574893,3434360,3434039,3347746,1204920,115508,1588351,1730497);
INSERT INTO total_vaccinations VALUES ('07/13/2021','MH',51300,10800,40500,0,87823,102839,112755,518339,34349,34321,34264,2020,1034,33315,0);
INSERT INTO total_vaccinations VALUES ('07/13/2021','VT',931860,52800,402420,476640,149339,169137,182723,745255,861233,861081,810319,253965,39595,362290,458688);
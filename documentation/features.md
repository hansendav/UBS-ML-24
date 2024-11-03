# Feature descriptions
**This supplementary document includes the explanations for all 105 features 
that are present in the dataset after its generation using the scripts of 
this repository.**




| Feature         | Description | Type |
|:----------------|:------------|------:|
| Tnr             |'Traktnummer': Identifier of grid points **unique across Germany**. | Numerical/Identifier |
| Enr             |'Eckennummer: Identifer of the sampling plot **1-4 unique for each grid point** | Numerical identifier |
| Bnr             |'Baumnummer: Treenumber **unique within each sampling plot** | Numerical identifier | 
| Av              |Measurement/estimation methods used | Categorical |
| Ba              |'Baumart: Tree species | Categorical **TARGET**|
| Al_ba           |'Baumalter: Tree age [$a$] | Numerical |
| Bs              |'Bestandesschicht': Canopy layer | Categorical |
| Bhd             |'Brusthöhendurchmesser: Diamerter at breast height [$mm$] | Numerical |
| Hoehe           |'Höhe': Height [$dm$ | Numerical |
| D7              |Diameter at 0.7 percentile of tree height | Numerical |
| D03             |Diameter at 0.3 percentile of tree hieght | Numerical 
| G               |'Grundfläche': Basal area [$m^2$] | Numerical | 
| VolR            |'Volumen Vorratsfestmeter': Volume with bark [$m^3$] | Numerical |
| VolR_FAO        |'Volumen Vorratsfestmeter - FAO': Volume with bark [$m^3$] | Numerical |
| VolE            |'Volumen Erntefestmeter': Volume without bark [$m^3] | Numerical |
| vVolE           |'verwendbarer Erntefestmeter': Volume without bark sawwood ready [$m^3$] | Numerical |
| N_ha            |'Stammzahl je Hektar': Number of trees per hectar | Numerical |
| Stf             |'Standfläche': 'Canopy footprint' [$m^2$] | Numerical |
| StfM            |Normalized version of Stf (to fit 1ha) |
| Bhdst1          |'Brusthöhendurchmesserstufe - 1cm': DBH in 1cm bins | Numerical |
| Bhdst5          |'Brusthöhendurchmesserstufe - 5cm': DBH in 5cm bins |Numerical |
| Alkl5           |'Altersklasse Jahresstufe - 5': Age in 5 year bins | Numerical |
| GrGr2           |'Größenklassenstufe': Height and diameter binning | Categorical |
| jSchael_x       |'Frische Schälschäden': New (<12 months) damages bark peeling (Yes / No) | Numerical |
| Biom_o          |'Biomasse oberirdisch': Aboveground biomass [$kg$] | Numerical |
| Biom_u          |'Biomasse unterirdisch': Belowground biomass [$kg$] |Numerical |
| Biov_o          |'Biomasse überirdisch' : Aboveground biomass[$m^3$] | Numerical |
| Gexp            |'Geländexposition': Aspect [$gon$] | Numerical | 
| GExpKl4         |'Geländeexpositionsklasse': Aspect in classes (4) | Numerical |
| GExpKl8         |'Geländeexpositionsklasse: Aspect in classes (8) | Numerical |
| Gform           |'Geländeform': Terrain | Categorical |
| Gneig           |'Geländeneigung': Slope [$\%$] | Numerical |
| GneigKl5        |'Geländeneigunsklassen - 5': Slope categories (5) [$\%$] | Numerical |
| natHoe          |'natürliche Höhenstufe': natural height class | Categorical |
| potNatWg        |'potenzielle natürliche Waldgesellschaft': potential natural forest community | Categorical |
| HoeheNN         |'Höhe NN': Height above German normal height [$m$] | Numerical |
| hnnSt100        |'Höhenstufe 100': Height in 100m bins | Categorical
| hnnSt250        |'Höhenstufe 250': Height in 250m bins |  / Categorical
| Zaun            |'Zaun': Fenced (Yes/No) | Categorical 
| Be              |'Betriebsart': Operation catgeory | Categorical |
| NatNaeheHaupt   |'Ermittelte Naturnähe (durch Hauptbestand WZP-4)': Estimated closeness to nature (using the main canopy layer) |  Categorical |
| NatNaeheLT7cm   |'Ermittelte Natunähe (bis Größeklasse 6) Probekreise 1-4m: Estimated closeness to nature (up to height class 6 and sample radii 1-4m) |  Categorical |
| ForestType      |European Forest Type | Categorical |
| RAN             |'Anzahl Wald und Bestandesränder': Number of forest/foreststand edges | Numerical | 
| Situation       |'Besondere Bestandessituation': Special forest stand situation | Categorical |
| TOT             |'Anzahl Totholzstücke': Pieces of deadwood | Numerical | 
| Kaefer          |'Käferlöcher': Bettle boreholes (Yes / No) | Categorical |
| jSchael_y       |**same as jSchael_x - doubled entry** |
| aeSchael        |'Ältere Schälschäden': Older peeling damages (> 12 months) (Yes / No) | Categorical |
| Bkl             |'Baumklasse': Tree social class | Categorical |
| Ast             |'Astung'| Categorical |
| tot             |'Zeitpunkt tot': Tree is dead or not | Categorical | 
| AnzSchad        |'Anzahl Schäden am Baum bis 8': Number of damages (max 8) | Numerical |
| Ruecke          |'Rücke- oder Fällschäden': Damages due to felling or logging (Yes / No) | Categorical |
| Specht          |'Specht': Woodpecker (Yes / No) | Categorical |
| Pilz            |'Pilzkonsolen': Mushroom (Yes / No) | Categorical |
| Harz            |'Harz': Resin (Yes / No) | Categorical | 
| BestockAb       |'Bestockungsaufbau': Forest stories | Categorical |
| Al_baDiff       | Difference 2012-2002 Al_ba | Numerical |
| BhdDiff         | Difference 2012-2002 BhdDiff | Numerical |
| HoeheDiff       | Difference 2012-2002 Hoehe | Numerical |
| GDiff           | Difference 2012-2002 G | Numerical |
| VolRDiff        | Difference 2012-2002 VolR | Numerical |
| VolEDiff        | Difference 2012-2002 VolE | Numerical |
| vVolEDiff       | Difference 2012-2002 vVolE | Numerical |
| Biom_oDiff      | Difference 2012-2002 Biom_o | Numerical |
| Biom_uDiff      | Difference 2012-2002 Biom_u | Numerical |
| Biov_oDiff      | Difference 2012-2002 Biov_o | Numerical |
| LAND            |**REMOVE THIS**
| SOEH_NR         |**REMOVE THIS**
| SOEH_KRZ        |**REMOVE THIS**
| SOEH_VAR        |**REMOVE THIS**
| BODTYP          |'Bodentyp': Soiltype | Categorical |
| NAEHR           |'Nährstoffkraft': Nutritive power | Categorical |
| WASSER          |'Wasserhaushaltstufe': Water budget bin | Categorical |
| NumHTypes       |'Anzahl Horizonttypen': Number of soil horizont types | Numerical |
| nfk_30          |'Feldkapazität 30cm': Water holding capacity in 30cm | Numerical |
| nfk_60          |'Feldkapazität 30cm': Water holding capacity in 30cm | Numerical |
| nfk_80          |'Feldkapazität 30cm': Water holding capacity in 30cm | Numerical |
| nfk_90          |'Feldkapazität 30cm': Water holding capacity in 30cm | Numerical |
| nfk_100         |'Feldkapazität 30cm': Water holding capacity in 30cm | Numerical |
| nfk_160         |'Feldkapazität 30cm': Water holding capacity in 30cm | Numerical |
| bl              |**REMOVE THIS** |
| year_first      |**REMOVE THIS** |
| year_last       |**REMOVE THIS** |
| bio_1           |Annual mean temperature (1992-2002) as the mean of the monthly temperatures in [$°C$] | Numerical |
| bio_2           |Mean diurnal range (1992-2002) as the mean of monthly (max temp - min temp) in [$°C$] | Numerical |
| bio_3           |Isothermality (1992-2002) in [$°C$] | Numerical |
| bio_4           |Temperature seasonality (1992-2002) in [$°C$] | Numerical |
| bio_5           |Max temperature of warmest month (1992-2002) in [$°C$] | Numerical |
| bio_6           |Min temperature of coldest month (1992-2002) in [$°C$] | Numerical |
| bio_7           |Temperature annual range (1992-2002) (bio_5 - bio_6) in [$°C$] | Numerical |
| bio_8           |Mean temperature of wettest quarter (1992-2002) in [$°C$] | Numerical |
| bio_9           |Mean temperature of driest quarter (1992-2002) in [$°C$] | Numerical |
| bio_10          |Mean temperature of warmest quarter (1992-2002) in [$°C$] | Numerical |
| bio_11          |Mean temperature of coldest quarter (1992-2002) in [$°C$] | Numerical |
| bio_12          |Annual precipitation (1992-2002) in [$mm$] | Numerical |
| bio_13          |Precipitation of wettest month (1992-2002) in [$mm$] | Numerical |
| bio_14          |Precipitation of driest month (1992-2002) in [$mm$] | Numerical |
| bio_15          |Precipitation seasonality (1992-2002) in [$mm$] | Numerical |
| bio_16          |Precipitation of wettest quarter (1992-2002) in [$mm$] | Numerical |
| bio_17          |Precipitation of driest quarter (1992-2002) in [$mm$] | Numerical |
| bio_18          |Precipitation of warmest quarter (1992-2002) in [$mm$] | Numerical |
| bio_19          |Precipitation of coldest quarter (1992-2002) in [$mm$] | Numerical |
# Feature descriptions
**This supplementary document includes the explanations for all 105 features 
that are present in the dataset after its generation using the scripts of 
this repository.**




| Feature         | Description | Type |
|:----------------|:------------|------:|
| Tnr             |'Traktnummer': Identifier of grid points **unique across Germany**. | Numerical/Identifier |
| Enr             |'Eckennummer: Identifer of the sampling plot **1-4 unique for each grid point** | Numerical identifier |
| Bnr             |'Baumnummer: Treenumber **unique within each sampling plot** | Numerical identifier | 
| Av              |**REMOVE THIS**
| Ba              |'Baumart: Tree species | Nominal **TARGET**|
| Al_ba           |'Baumalter: Tree age [$a$] | Discrete |
| Bs              |'Bestandesschicht': Canopy layer | Nominal |
| Bhd             |'Brusthöhendurchmesser: Diamerter at breast height [$mm$] | Continuous |
| Hoehe           |'Höhe': Height [$dm$ | Continuous |
| D7              |**REMOVE THIS** (not always measured) |
| D03             |**REMOVE THIS** (not always measured) |
| G               |'Grundfläche': Basal area [$m^2$] | Continuous | 
| VolR            |'Volumen Vorratsfestmeter': Volume with bark [$m^3$] | Continuous |
| VolR_FAO        |'Volumen Vorratsfestmeter - FAO': Volume with bark [$m^3$] | Continuous |
| VolE            |'Volumen Erntefestmeter': Volume without bark [$m^3] | Continuous |
| vVolE           |'verwendbarer Erntefestmeter': Volume without bark sawwood ready [$m^3$] | Continuous |
| N_ha            |'Stammzahl je Hektar': Number of trees per hectar | Continuous |
| Stf             |'Standfläche': 'Canopy footprint' [$m^2$] | Continuous |
| StfM            |**REMOVE THIS** Normalized version of Stf (to fit 1ha) |
| Bhdst1          |'Brusthöhendurchmesserstufe - 1cm': DBH in 1cm bins | Discrete |
| Bhdst5          |'Brusthöhendurchmesserstufe - 5cm': DBH in 5cm bins |Discrete |
| Alkl5           |'Altersklasse Jahresstufe - 5': Age in 5 year bins | Discrete |
| GrGr2           |'Größenklassenstufe': Height binning | Nominal (DBH and Height mixed) |
| jSchael_x       |'Frische Schälschäden': New (<12 months) damages bark peeling (Yes / No) | Discrete / Ordinal |
| Biom_o          |'Biomasse oberirdisch': Aboveground biomass [$kg$] | Continuous |
| Biom_u          |'Biomasse unterirdisch': Belowground biomass [$kg$] |Continuous |
| Biov_o          |'Biomasse überirdisch' : Aboveground biomass[$m^3$] | Continuous |
| Gexp            |'Geländexposition': Aspect [$gon$] | Continuous/Discrete
| GExpKl4         |'Geländeexpositionsklasse': Aspect in classes (4) | Discrete |
| GExpKl8         |'Geländeexpositionsklasse: Aspect in classes (8) | Discrete |
| Gform           |'Geländeform': Terrain | Nominal |
| Gneig           |'Geländeneigung': Slope [$\%$] | Discrete / Continuous |
| GneigKl5        |'Geländeneigunsklassen - 5': Slope categories (5) [$\%$] | Discrete |
| natHoe          |'natürliche Höhenstufe': natural height class | Ordinal |
| potNatWg        |'potenzielle natürliche Waldgesellschaft': potential natural forest community | Nominal |
| HoeheNN         |'Höhe NN': Height above German normal height [$m$] | Continuous |
| hnnSt100        |'Höhenstufe 100': Height in 100m bins | Discrete / Ordinal
| hnnSt250        |'Höhenstufe 250': Height in 250m bins | Discrete / Ordinal
| Zaun            |'Zaun': Fenced (Yes/No) | Discrete / Ordinal 
| Be              |'Betriebsart': Operation catgeory | Nominal |
| NatNaeheHaupt   |'Ermittelte Naturnähe (durch Hauptbestand WZP-4)': Estimated closeness to nature (using the main canopy layer) | Nominal / Ordinal |
| NatNaeheLT7cm   |'Ermittelte Natunähe (bis Größeklasse 6) Probekreise 1-4m: Estimated closeness to nature (up to height class 6 and sample radii 1-4m) | Nominal / Ordinal |
| ForestType      |European Forest Type | Nominal |
| RAN             |'Anzahl Wald und Bestandesränder': Number of forest/foreststand edges | Discrete | 
| Situation       |'Besondere Bestandessituation': Special forest stand situation | Discrete |
| TOT             |'Anzahl Totholzstücke': Pieces of deadwood | Discrete | 
| Kaefer          |'Käferlöcher': Bettle boreholes (Yes / No) | Discrete / Ordinal |
| jSchael_y       |**REMOVE THIS DOUBLE ENTRY** |
| aeSchael        |'Ältere Schälschäden': Older peeling damages (> 12 months) (Yes / No) | Discrete / Ordinal |
| Bkl             |'Baumklasse': Tree social class | Ordinal |
| Ast             |'Astung': **ADD ENGLISH DESCRIPTION** | Nominal |
| tot             |'Zeitpunkt tot': Time of death (**USE FOR FILTERING**) | Nominal | 
| AnzSchad        |'Anzahl Schäden am Baum bis 8': Number of damages (max 8) | Discrete |
| Ruecke          |'Rücke- oder Fällschäden': Damages due to felling or logging (Yes / No) | Discrete / Ordinal |
| Specht          |'Specht': Woodpecker (Yes / No) | Discrete / Ordinal |
| Pilz            |'Pilzkonsolen': Mushroom (Yes / No) | Discre / Ordinal |
| Harz            |'Harz': Resin (Yes / No) | Discrete / Ordinal | 
| BestockAb       |'Bestockungsaufbau': Forest stories | Nominal |
| Al_baDiff       | Difference 2012-2002 Al_ba | Continuous |
| BhdDiff         | Difference 2012-2002 BhdDiff | Continuous |
| HoeheDiff       | Difference 2012-2002 Hoehe | Continuous |
| GDiff           | Difference 2012-2002 G | Continuous |
| VolRDiff        | Difference 2012-2002 VolR | Continuous |
| VolEDiff        | Difference 2012-2002 VolE | Continuous |
| vVolEDiff       | Difference 2012-2002 vVolE | Continuous |
| Biom_oDiff      | Difference 2012-2002 Biom_o | Continuous |
| Biom_uDiff      | Difference 2012-2002 Biom_u | Continuous |
| Biov_oDiff      | Difference 2012-2002 Biov_o | Continuous |
| LAND            |**REMOVE THIS**
| SOEH_NR         |**REMOVE THIS**
| SOEH_KRZ        |**REMOVE THIS**
| SOEH_VAR        |**REMOVE THIS**
| BODTYP          |'Bodentyp': Soiltype | Nominal |
| NAEHR           |'Nährstoffkraft': Nutritive power | Nominal / Ordinal 
| WASSER          |'Wasserhaushaltstufe': Water budget bin | Nominal |
| NumHTypes       |'Anzahl Horizonttypen': Number of soil horizont types | Continuous |
| nfk_30          |'Feldkapazität 30cm': Water holding capacity in 30cm | Continuous |
| nfk_60          |'Feldkapazität 30cm': Water holding capacity in 30cm | Continuous |
| nfk_80          |'Feldkapazität 30cm': Water holding capacity in 30cm | Continuous |
| nfk_90          |'Feldkapazität 30cm': Water holding capacity in 30cm | Continuous |
| nfk_100         |'Feldkapazität 30cm': Water holding capacity in 30cm | Continuous |
| nfk_160         |'Feldkapazität 30cm': Water holding capacity in 30cm | Continuous |
| bl              |**REMOVE THIS** |
| year_first      |**REMOVE THIS** |
| year_last       |**REMOVE THIS** |
| bio_1           |Annual mean temperature (2001-2010) as the mean of the monthly temperatures in [$°C$] | Continuous |
| bio_2           |Mean diurnal range (2001-2010) as the mean of monthly (max temp - min temp) in [$°C$] | Continuous |
| bio_3           |Isothermality (2001-2010) in [$°C$] | Continuous |
| bio_4           |Temperature seasonality (2001-2010) in [$°C$] | Continuous |
| bio_5           |Max temperature of warmest month (2001-2010) in [$°C$] | Continuous |
| bio_6           |Min temperature of coldest month (2001-2010) in [$°C$] | Continuous |
| bio_7           |Temperature annual range (2001-2010) (bio_5 - bio_6) in [$°C$] | Continuous |
| bio_8           |Mean temperature of wettest quarter (2001-2010) in [$°C$] | Continuous |
| bio_9           |Mean temperature of driest quarter (2001-2010) in [$°C$] | Continuous |
| bio_10          |Mean temperature of warmest quarter (2001-2010) in [$°C$] | Continuous |
| bio_11          |Mean temperature of coldest quarter (2001-2010) in [$°C$] | Continuous |
| bio_12          |Annual precipitation (2001-2010) in [$mm$] | Continuous |
| bio_13          |Precipitation of wettest month (2001-2010) in [$mm$] | Continuous |
| bio_14          |Precipitation of driest month (2001-2010) in [$mm$] | Continuous |
| bio_15          |Precipitation seasonality (2001-2010) in [$mm$] | Continuous |
| bio_16          |Precipitation of wettest quarter (2001-2010) in [$mm$] | Continuous |
| bio_17          |Precipitation of driest quarter (2001-2010) in [$mm$] | Continuous |
| bio_18          |Precipitation of warmest quarter (2001-2010) in [$mm$] | Continuous |
| bio_19          |Precipitation of coldest quarter (2001-2010) in [$mm$] | Continuous |
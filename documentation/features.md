# Feature descriptions
**This supplementary document includes the explanations for all 105 features 
that are present in the dataset after its generation using the scripts of 
this repository.**




| Feature         | Description | Type |
|:----------------|:------------|------:|
| Tnr             |'Traktnummer': Identifier of grid points **unique across Germany**. | Numerical/Identifier |
| Enr             |'Eckennummer: Identifer of the sampling plot **1-4 unique for each grid point** | Numerical identifier |
| Bnr             |'Baumnummer: Treenumber **unique within each sampling plot** | Numerical identifier | 
| Av              |'Aufnahmeverfahren': **REMOVE THIS**
| Ba              |'Baumart: Tree species | Nominal |
| Al_ba           |'Baumalter: Tree age [$a$] | Continuous/Discrete |
| Bs              |'Bestandesschicht': Canopy layer | Nominal |
| Bhd             |'Brusthöhendurchmesser: Diamerter at breast height [$mm$] | Continuous |
| Hoehe           |'Höhe': Height [$dm$ | Continuous |
| D7              |**REMOVE THIS MAYBE**
| D03             |**REMOVE THIS MAYBE**
| G               |'Grundfläche': Basal area [$m^2$] | Continuous | 
| VolR            |'Volumen Vorratsfestmeter': Volume with bark [$m^3$] | Continuous |
| VolR_FAO        |'Volumen Vorratsfestmeter - FAO': Volume with bark [$m^3$] | Continuous |
| VolE            |'Volumen Erntefestmeter': Volume without bark [$m^3] | Continuous |
| vVolE           |'verwendbarer Erntefestmeter': Volume without bark sawwood ready [$m^3$] | Continuous |
| N_ha            |'Stammzahl je Hektar': Number of trees per hectar | Continuous |
| Stf             |'Standfläche': 'Canopy footprint' [$m^2$] | Continuous |
| StfM            |**REMOVE THIS MAYBE**
| Bhdst1          |'Brusthöhendurchmesserstufe - 1cm': DBH in 1cm bins | Discrete |
| Bhdst5          |'Brusthöhendurchmesserstufe - 5cm': DBH in 5cm bins |Discrete |
| Alkl5           |'Altersklasse Jahresstufe - 5': Age in 5 year bins | Discrete |
| GrGr2           |'Größenklassenstufe': Height binning | Nominal (DBH and Height mixed) |
| jSchael_x       |'Frische Schälschäden': New (<12 months) damages bark peeling | Discrete / Ordinal |
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
| Zaun            |'Zaun': Fence | Discrete Ordinal 
| Be              | 'Betri
| NatNaeheHaupt   |
| NatNaeheLT7cm   |
| ForestType      |
| RAN             |
| Situation       |
| TOT             |
| Kaefer          |
| jSchael_y       |
| aeSchael        |
| Bkl             |
| Ast             |
| tot             |
| AnzSchad        |
| Ruecke          |
| Specht          |
| Pilz            |
| Harz            |
| BestockAb       |
| Al_baDiff       |
| BhdDiff         |
| HoeheDiff       |
| GDiff           |
| VolRDiff        |
| VolEDiff        |
| vVolEDiff       |
| Biom_oDiff      |
| Biom_uDiff      |
| Biov_oDiff      |
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
| bl              |**???**
| year_first      |**REMOVE THIS**
| year_last       |**REMOVE THIS**
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


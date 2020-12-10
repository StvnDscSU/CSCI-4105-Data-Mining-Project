/* Find Population in United States in 2018 and Total Covid-19 Cases in 2020*/
WITH covid AS (
  SELECT country_code, aggregation_level, subregion2_code, subregion1_name AS State, subregion2_name AS County, SUM(new_confirmed) AS `Total_Cases`
  FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE aggregation_level = 2
AND country_code = 'US'
GROUP BY country_code, aggregation_level, subregion2_code, subregion1_name, subregion2_name
ORDER BY Total_cases DESC
),

gdp AS (
  SELECT GeoFIPS, population, year
  FROM `bigquery-public-data.sdoh_bea_cainc30.fips`
  WHERE Year = '2018-01-01'
)

SELECT covid.State, gdp.GeoFIPS, County, gdp.population, covid.total_cases
FROM covid join gdp on GeoFIPS = subregion2_code
ORDER BY Total_cases DESC;


/* Calculate GDP per Capita per County */
SELECT GeoFIPS, geoname, Percapita_personal_income, Population
FROM `bigquery-public-data.sdoh_bea_cainc30.fips` 
WHERE Year = '2018-01-01' and Population > 0
ORDER BY Percapita_personal_income ASC;

-- New Jersey --
SELECT Year, GeoFIPS, geoname, Percapita_personal_income, Population
FROM `bigquery-public-data.sdoh_bea_cainc30.fips` 
WHERE Year = '2018-01-01' and Population > 0 and GeoName like "%NJ%"
ORDER BY Percapita_personal_income ASC;

/* Covid-19 Stats */
-- Display State, county, FIPS, new cases, and new deceased for one day in December. --
SELECT
  subregion2_code, subregion1_name, subregion2_name, new_confirmed, new_deceased
FROM
  `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE
  country_code = "US"
  AND aggregation_level = 2
  AND date BETWEEN '2020-12-02' AND '2020-12-02'
ORDER BY new_confirmed DESC, new_deceased DESC;


--New Jersey Information --
SELECT
  subregion2_code, subregion2_name, new_confirmed, new_deceased
FROM
  `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE
  country_code = "US"
  AND subregion1_code = "NJ"
  AND aggregation_level = 2
  AND date BETWEEN '2020-12-02' AND '2020-12-02';


/* Show for each county: subregion2_code, state name, county name, new_case, new_death, population */
SELECT
  covid.subregion2_code, gdp.GeoFIPS, covid.subregion1_name, covid.subregion2_name, gdp.population, gdp.percapita_personal_income, covid.new_confirmed, covid.new_deceased
FROM
  `bigquery-public-data.covid19_open_data.covid19_open_data` as covid
FULL JOIN `bigquery-public-data.sdoh_bea_cainc30.fips` as gdp on covid.subregion2_code = gdp.GeoFIPS
WHERE
  country_code = "US"
  AND aggregation_level = 2
  AND date BETWEEN '2020-12-02' AND '2020-12-02'
  AND YEAR = '2018-01-01'
  AND new_confirmed is not null
ORDER BY percapita_personal_income DESC;

/*** For July 2020, show: GeoFIPS, State, County, Population, percapita_personal_income, new_confirmed, new_cases_per_1000, new_deceased, new_deceased_per_1000 ***/
WITH covid AS (
  SELECT country_code, subregion2_code, subregion1_name, subregion2_name, SUM(new_confirmed) AS new_confirmed, SUM(new_deceased) AS new_deceased
  FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
  WHERE date BETWEEN '2020-07-01' AND '2020-07-30'
  AND country_code = "US"
  AND aggregation_level = 2
  AND new_confirmed is not null
  group by country_code, subregion2_code, subregion1_name, subregion2_name
),

gdp AS (
  SELECT GeoFIPS, population, percapita_personal_income, year
  FROM `bigquery-public-data.sdoh_bea_cainc30.fips`
  WHERE year = '2018-01-01'
),

covid_income_trends AS (
  SELECT gdp.GeoFIPS, covid.subregion1_name AS State, covid.subregion2_name AS County, gdp.population AS Population, gdp.percapita_personal_income, covid.new_confirmed, Round(covid.new_confirmed/(gdp.population/1000), 4) AS new_cases_per_1000, covid.new_deceased, ROUND(covid.new_deceased/(gdp.population/1000), 4) AS new_deceased_per_1000
  FROM covid
FULL JOIN gdp on covid.subregion2_code = gdp.GeoFIPS
ORDER BY new_cases_per_1000 DESC
)

SELECT *
FROM covid_income_trends;
-- WHERE new_confirmed_per_1000 > 1
-- WHERE new_confirmed_per_1000 > 2
import pytest

from pydataweaver.lib.process import make_sql
from pydataweaver.lib.scripts import SCRIPT_LIST

expected_query = {
    "mammal-community-sites-bioclim": (
        "SELECT T1.abundance_data_format "
        "AS T1_abundance_data_format, T1.abundance_data_present AS "
        "T1_abundance_data_present, T1.country AS T1_country, T1.elevation_high "
        "AS T1_elevation_high, T1.elevation_low AS T1_elevation_low, "
        "T1.habitat_code AS T1_habitat_code, T1.habitat_description AS "
        "T1_habitat_description, T1.latitude AS T1_latitude, T1.location "
        "AS T1_location, T1.longitude AS T1_longitude, T1.n_years AS T1_n_years, "
        "T1.notes AS T1_notes, T1.reference_id AS T1_reference_id, T1.site_id "
        "AS T1_site_id, T1.spatial_extent AS T1_spatial_extent, T1.state "
        "AS T1_state, T1.study_duration AS T1_study_duration, T1.time_series "
        "AS T1_time_series, T1.uncertainty_radius AS "
        "T1_uncertainty_radius ,ST_Value(as_0.rast_bioclim_bio1, 1, "
        "ST_PointFromText(FORMAT('POINT(%s %s)', "
        "cast(T1.longitude as varchar), cast(T1.latitude as varchar)), 4326)) "
        "as feature_rast_bioclim_bio1 \nINTO {result_dbi}.{result_tablei} \n\n\nFROM "
        "(SELECT  site_id, reference_id, location, country, state, latitude, "
        "longitude, uncertainty_radius, elevation_low, elevation_high, "
        "habitat_description, habitat_code, abundance_data_present, "
        "abundance_data_format, spatial_extent, study_duration, "
        "time_series, n_years, notes  \nFROM mammal_community_db.sites  \n"
        "WHERE CAST(latitude AS TEXT) NOT LIKE '%NULL%' AND latitude "
        "IS NOT NULL AND CAST(longitude AS TEXT) NOT LIKE '%NULL%' AND "
        "longitude IS NOT NULL  ) T1 \nLEFT OUTER JOIN \n\t("
        "SELECT rast AS rast_bioclim_bio1 \n\tFROM bioclim.bio1) AS as_0 \n"
        "ON ST_Intersects(as_0.rast_bioclim_bio1, ST_PointFromText(FORMAT('POINT(%s %s)', "
        "cast(T1.longitude as varchar), cast(T1.latitude as varchar)), 4326))"),
    "mammal-diet-mammal-life-history":
        ("SELECT as_0.animal AS as_0_animal, as_0.bird AS as_0_bird, as_0.datasource "
         "AS as_0_datasource, as_0.family AS as_0_family, as_0.fillcode "
         "AS as_0_fillcode, as_0.fish AS as_0_fish, as_0.folivore "
         "AS as_0_folivore, as_0.frugivore AS as_0_frugivore, as_0.fruit "
         "AS as_0_fruit, as_0.genus AS as_0_genus, as_0.granivore "
         "AS as_0_granivore, as_0.herbaceous AS as_0_herbaceous, as_0.herptile "
         "AS as_0_herptile, as_0.insectivore AS as_0_insectivore, as_0.invertebrate "
         "AS as_0_invertebrate, as_0.leaf AS as_0_leaf, as_0.mammal "
         "AS as_0_mammal, as_0.mammaleater AS as_0_mammaleater, as_0.nectar "
         "AS as_0_nectar, as_0.other AS as_0_other, as_0.plant "
         "AS as_0_plant, as_0.root AS as_0_root, as_0.seed AS as_0_seed, as_0.species "
         "AS as_0_species, as_0.taxonid AS as_0_taxonid, as_0.taxonomicnote "
         "AS as_0_taxonomicnote, as_0.taxonorder AS as_0_taxonorder, as_0.trophiclevel "
         "AS as_0_trophiclevel, as_0.vertebrate AS as_0_vertebrate, as_0.woody "
         "AS as_0_woody  \ninto {result_dbi}.{result_tablei} \n\n\n"
         "FROM mammal_life_hist.species  AS T1 \nLEFT OUTER JOIN \n\t("
         "SELECT animal, bird, datasource, family, fillcode, fish, "
         "folivore, frugivore, fruit, genus, granivore, herbaceous, herptile, "
         "insectivore, invertebrate, leaf, mammal, mammaleater, nectar, other, "
         "plant, root, seed, species, taxonid, taxonomicnote, taxonorder, trophiclevel, "
         "vertebrate, woody \n\tFROM mammal_diet.diet ) AS as_0 \nON "
         "T1.species=as_0.species AND T1.genus=as_0.genus"),
    "mammal-community-sites-harvard-linear-features": (
        "SELECT T1.abundance_data_format AS T1_abundance_data_format, "
        "T1.abundance_data_present AS T1_abundance_data_present, T1.country "
        "AS T1_country, T1.elevation_high AS T1_elevation_high, T1.elevation_low "
        "AS T1_elevation_low, T1.habitat_code AS T1_habitat_code, T1.habitat_description "
        "AS T1_habitat_description, T1.latitude AS T1_latitude, T1.location "
        "AS T1_location, T1.longitude AS T1_longitude, T1.n_years "
        "AS T1_n_years, T1.notes AS T1_notes, T1.reference_id "
        "AS T1_reference_id, T1.site_id AS T1_site_id, T1.spatial_extent "
        "AS T1_spatial_extent, T1.state AS T1_state, T1.study_duration "
        "AS T1_study_duration, T1.time_series AS T1_time_series, T1.uncertainty_radius "
        "AS T1_uncertainty_radius, as_0.gid AS as_0_gid, as_0.type "
        "AS as_0_type ,ST_PointFromText(FORMAT('POINT(%s %s)', "
        "cast(T1.longitude as varchar), cast(T1.latitude as varchar)), 4326)  "
        "as feature_geom_harvard_forest_linear_features \n"
        "INTO {result_dbi}.{result_tablei} \n\n\nFROM ("
        "SELECT  site_id, reference_id, location, country, state, "
        "latitude, longitude, uncertainty_radius, elevation_low, "
        "elevation_high, habitat_description, habitat_code, abundance_data_present, "
        "abundance_data_format, spatial_extent, study_duration, time_series, "
        "n_years, notes  \nFROM mammal_community_db.sites  \n"
        "WHERE CAST(latitude AS TEXT) NOT LIKE '%NULL%' AND latitude IS "
        "NOT NULL AND CAST(longitude AS TEXT) NOT LIKE '%NULL%' AND "
        "longitude IS NOT NULL  ) T1 \nLEFT OUTER JOIN \n\t(SELECT geom "
        "AS geom_harvard_forest_linear_features, gid, notes, type \n\t"
        "FROM harvard_forest.linear_features) AS as_0  \nON "
        "ST_Within(ST_PointFromText(FORMAT('POINT(%s %s)', "
        "cast(T1.longitude as varchar), cast(T1.latitude as varchar)), 4326) , "
        "as_0.geom_harvard_forest_linear_features)"),
    "mammal-sites-bioclim-1-2": (
        "SELECT T1.abundance_data_format AS T1_abundance_data_format, "
        "T1.abundance_data_present AS T1_abundance_data_present, T1.country "
        "AS T1_country, T1.elevation_high AS T1_elevation_high, T1.elevation_low "
        "AS T1_elevation_low, T1.habitat_code AS T1_habitat_code, "
        "T1.habitat_description AS T1_habitat_description, T1.latitude "
        "AS T1_latitude, T1.location AS T1_location, T1.longitude "
        "AS T1_longitude, T1.n_years AS T1_n_years, T1.notes AS "
        "T1_notes, T1.reference_id AS T1_reference_id, T1.site_id "
        "AS T1_site_id, T1.spatial_extent AS T1_spatial_extent, T1.state "
        "AS T1_state, T1.study_duration AS T1_study_duration, T1.time_series "
        "AS T1_time_series, T1.uncertainty_radius AS "
        "T1_uncertainty_radius ,ST_Value(as_0.rast_bioclim_bio1, 1, "
        "ST_PointFromText(FORMAT('POINT(%s %s)', cast(T1.longitude as varchar), "
        "cast(T1.latitude as varchar)), 4326)) as "
        "feature_rast_bioclim_bio1, ST_Value(as_1.rast_bioclim_bio2, 1, "
        "ST_PointFromText(FORMAT('POINT(%s %s)', "
        "cast(T1.longitude as varchar), cast(T1.latitude as varchar)), 4326)) "
        "as feature_rast_bioclim_bio2 \nINTO {result_dbi}.{result_tablei} \n\n\n"
        "FROM (SELECT  site_id, reference_id, location, country, state, latitude, "
        "longitude, uncertainty_radius, elevation_low, elevation_high, "
        "habitat_description, habitat_code, abundance_data_present, "
        "abundance_data_format, spatial_extent, study_duration, time_series, "
        "n_years, notes  \nFROM mammal_community_db.sites  \nWHERE CAST(latitude AS TEXT) "
        "NOT LIKE '%NULL%' AND latitude IS NOT NULL AND CAST(longitude AS TEXT) "
        "NOT LIKE '%NULL%' AND longitude IS NOT NULL  ) T1 \nLEFT OUTER JOIN \n\t("
        "SELECT rast AS rast_bioclim_bio1 \n\tFROM bioclim.bio1) AS as_0 \n"
        "ON ST_Intersects(as_0.rast_bioclim_bio1, ST_PointFromText(FORMAT('POINT(%s %s)', "
        "cast(T1.longitude as varchar), cast(T1.latitude as varchar)), 4326))\n\n"
        "LEFT OUTER JOIN \n\t(SELECT rast AS rast_bioclim_bio2 \n\t"
        "FROM bioclim.bio2) AS as_1 \nON ST_Intersects(as_1.rast_bioclim_bio2, "
        "ST_PointFromText(FORMAT('POINT(%s %s)', cast(T1.longitude as varchar), "
        "cast(T1.latitude as varchar)), 4326))"),
    "mammal-community-bioclim": (
        "SELECT T1.abundance AS T1_abundance, T1.initial_year AS "
        "T1_initial_year, T1.mass AS T1_mass, T1.presence_only "
        "AS T1_presence_only, T1.site_id AS T1_site_id, T1.species_id "
        "AS T1_species_id, as_0.abundance_data_format "
        "AS as_0_abundance_data_format, as_0.abundance_data_present "
        "AS as_0_abundance_data_present, as_0.country "
        "AS as_0_country, as_0.elevation_high AS as_0_elevation_high, as_0.elevation_low "
        "AS as_0_elevation_low, as_0.habitat_code "
        "AS as_0_habitat_code, as_0.habitat_description "
        "AS as_0_habitat_description, as_0.location "
        "AS as_0_location, as_0.reference_id "
        "AS as_0_reference_id, as_0.spatial_extent "
        "AS as_0_spatial_extent, as_0.state AS as_0_state, as_0.uncertainty_radius "
        "AS as_0_uncertainty_radius, as_1.family AS as_1_family, as_1.genus "
        "AS as_1_genus, as_1.species AS as_1_species, as_1.species_level "
        "AS as_1_species_level ,as_0.lat_mammal_community_db_sites, "
        "as_0.long_mammal_community_db_sites, ST_Value(as_2.rast_bioclim_bio1, 1, "
        "ST_PointFromText(FORMAT('POINT(%s %s)', "
        "cast(as_0.long_mammal_community_db_sites as varchar), "
        "cast(as_0.lat_mammal_community_db_sites as varchar)), 4326)) "
        "as feature_rast_bioclim_bio1 \ninto {result_dbi}.{result_tablei} \n\n\n"
        "FROM mammal_community_db.communities  AS T1 \n"
        "LEFT OUTER JOIN  \n\t(SELECT  abundance_data_format, "
        "abundance_data_present, country, elevation_high, elevation_low, "
        "habitat_code, habitat_description, latitude AS lat_mammal_community_db_sites, "
        "location, longitude AS long_mammal_community_db_sites, reference_id, "
        "site_id, spatial_extent, state, uncertainty_radius \n"
        "FROM (SELECT  abundance_data_format, abundance_data_present, "
        "country, elevation_high, elevation_low, habitat_code, habitat_description, "
        "latitude, location, longitude, reference_id, site_id, spatial_extent, "
        "state, uncertainty_radius \nFROM mammal_community_db.sites \n\n\t"
        "WHERE latitude Not LIKE '%NULL%' \n\tAND latitude IS NOT NULL \n\t"
        "AND longitude Not LIKE '%NULL%' \n\tAND longitude IS NOT NULL ) temp) as_0 \n"
        "ON T1.site_id=as_0.site_id\nLEFT OUTER JOIN \n\t("
        "SELECT family, genus, species, species_id, species_level \n\t"
        "FROM mammal_community_db.species ) AS as_1 \nON T1.species_id=as_1.species_id\n"
        "LEFT OUTER JOIN \n\t(SELECT rast AS rast_bioclim_bio1 \n\tFROM bioclim.bio1) "
        "AS as_2 \nON ST_Intersects(as_2.rast_bioclim_bio1, ST_PointFromText(FORMAT('POINT(%s %s)', "
        "cast(as_0.long_mammal_community_db_sites as varchar), "
        "cast(as_0.lat_mammal_community_db_sites as varchar)), 4326))"),
    "mammal-community-sites-harvard-linear-features-soils": (
        "SELECT T1.abundance_data_format AS T1_abundance_data_format, "
        "T1.abundance_data_present AS T1_abundance_data_present, T1.country "
        "AS T1_country, T1.elevation_high AS T1_elevation_high, T1.elevation_low "
        "AS T1_elevation_low, T1.habitat_code AS T1_habitat_code, T1.habitat_description "
        "AS T1_habitat_description, T1.latitude AS T1_latitude, T1.location "
        "AS T1_location, T1.longitude AS T1_longitude, T1.n_years AS T1_n_years, T1.notes "
        "AS T1_notes, T1.reference_id AS T1_reference_id, T1.site_id "
        "AS T1_site_id, T1.spatial_extent AS T1_spatial_extent, T1.state "
        "AS T1_state, T1.study_duration AS T1_study_duration, T1.time_series "
        "AS T1_time_series, T1.uncertainty_radius "
        "AS T1_uncertainty_radius, as_0.type AS as_0_type, as_1.drainage_c "
        "AS as_1_drainage_c, as_1.mesic_soil AS as_1_mesic_soil, as_1.simmons_so "
        "AS as_1_simmons_so ,ST_PointFromText(FORMAT('POINT(%s %s)', "
        "cast(T1.longitude as varchar), cast(T1.latitude as varchar)), 4326)  "
        "as feature_geom_harvard_forest_linear_features, "
        "ST_PointFromText(FORMAT('POINT(%s %s)', cast(T1.longitude as varchar), "
        "cast(T1.latitude as varchar)), 4326)  as feature_geom_harvard_forest_soils \n"
        "INTO {result_dbi}.{result_tablei} \n\n\nFROM ("
        "SELECT  site_id, reference_id, location, country, state, latitude, "
        "longitude, uncertainty_radius, elevation_low, elevation_high, "
        "habitat_description, habitat_code, abundance_data_present, abundance_data_format, "
        "spatial_extent, study_duration, time_series, n_years, notes  \n"
        "FROM mammal_community_db.sites  \nWHERE CAST(latitude AS TEXT) "
        "NOT LIKE '%NULL%' AND latitude IS NOT NULL AND CAST(longitude AS TEXT) "
        "NOT LIKE '%NULL%' AND longitude IS NOT NULL  ) T1 \nLEFT OUTER JOIN \n\t("
        "SELECT geom AS geom_harvard_forest_linear_features, type \n\t"
        "FROM harvard_forest.linear_features) AS as_0  \n"
        "ON ST_Within(ST_PointFromText(FORMAT('POINT(%s %s)', "
        "cast(T1.longitude as varchar), cast(T1.latitude as varchar)), 4326) , "
        "as_0.geom_harvard_forest_linear_features) \nLEFT OUTER JOIN \n\t("
        "SELECT drainage_c, geom AS geom_harvard_forest_soils, mesic_soil, simmons_so \n\t"
        "FROM harvard_forest.soils) AS as_1  \nON ST_Within(ST_PointFromText(FORMAT('POINT(%s %s)', "
        "cast(T1.longitude as varchar), cast(T1.latitude as varchar)), 4326) , as_1.geom_harvard_forest_soils) "
    ),
    "breed-bird-routes-bioclim":
        ("SELECT T1.active AS T1_active, T1.bcr AS T1_bcr, "
         "T1.countrynum AS T1_countrynum, T1.latitude AS T1_latitude, "
         "T1.longitude AS T1_longitude, T1.route AS T1_route, T1.routename "
         "AS T1_routename, T1.routetypedetailid AS T1_routetypedetailid, T1.routetypeid "
         "AS T1_routetypeid, T1.statenum AS T1_statenum, T1.stratum "
         "AS T1_stratum ,ST_Value(as_0.rast_bioclim_bio1, 1, "
         "ST_PointFromText(FORMAT('POINT(%s %s)', cast(T1.longitude as varchar), "
         "cast(T1.latitude as varchar)), 4326)) as feature_rast_bioclim_bio1 \n"
         "INTO {result_dbi}.{result_tablei} \n\n\nFROM ("
         "SELECT  countrynum, statenum, route, routename, active, latitude, "
         "longitude, stratum, bcr, routetypeid, routetypedetailid  \n"
         "FROM breed_bird_survey.routes  \nWHERE CAST(latitude AS TEXT) NOT "
         "LIKE '%NULL%' AND latitude IS NOT NULL AND CAST(longitude AS TEXT) "
         "NOT LIKE '%NULL%' AND longitude IS NOT NULL  ) T1 \n"
         "LEFT OUTER JOIN \n\t(SELECT rast AS rast_bioclim_bio1 \n\t"
         "FROM bioclim.bio1) AS as_0 \nON "
         "ST_Intersects(as_0.rast_bioclim_bio1, ST_PointFromText(FORMAT('POINT(%s %s)', "
         "cast(T1.longitude as varchar), cast(T1.latitude as varchar)), 4326))"),
    "mammal-community-sites-all-bioclim":
        ("SELECT T1.abundance_data_format AS T1_abundance_data_format, "
         "T1.abundance_data_present AS T1_abundance_data_present, T1.country "
         "AS T1_country, T1.elevation_high AS T1_elevation_high, T1.elevation_low "
         "AS T1_elevation_low, T1.habitat_code "
         "AS T1_habitat_code, T1.habitat_description "
         "AS T1_habitat_description, T1.latitude AS T1_latitude, T1.location "
         "AS T1_location, T1.longitude AS T1_longitude, T1.n_years "
         "AS T1_n_years, T1.notes AS T1_notes, T1.reference_id "
         "AS T1_reference_id, T1.site_id AS T1_site_id, T1.spatial_extent "
         "AS T1_spatial_extent, T1.state AS T1_state, T1.study_duration "
         "AS T1_study_duration, T1.time_series "
         "AS T1_time_series, T1.uncertainty_radius "
         "AS T1_uncertainty_radius ,ST_Value(as_0.rast_bioclim_bio1, 1, "
         "ST_PointFromText(FORMAT('POINT(%s %s)', cast(T1.longitude as varchar), "
         "cast(T1.latitude as varchar)), 4326)) as "
         "feature_rast_bioclim_bio1, ST_Value(as_1.rast_bioclim_bio2, 1, "
         "ST_PointFromText(FORMAT('POINT(%s %s)', cast(T1.longitude as varchar), "
         "cast(T1.latitude as varchar)), 4326)) as feature_rast_bioclim_bio2 \n"
         "INTO {result_dbi}.{result_tablei} \n\n\nFROM ("
         "SELECT  site_id, reference_id, location, country, state, "
         "latitude, longitude, uncertainty_radius, elevation_low, "
         "elevation_high, habitat_description, habitat_code, abundance_data_present, "
         "abundance_data_format, spatial_extent, study_duration, "
         "time_series, n_years, notes  \nFROM mammal_community_db.sites  \n"
         "WHERE CAST(latitude AS TEXT) NOT LIKE '%NULL%' AND latitude IS "
         "NOT NULL AND CAST(longitude AS TEXT) NOT LIKE '%NULL%' "
         "AND longitude IS NOT NULL  ) T1 \nLEFT OUTER JOIN \n\t("
         "SELECT rast AS rast_bioclim_bio1 \n\tFROM bioclim.bio1) "
         "AS as_0 \nON ST_Intersects(as_0.rast_bioclim_bio1, "
         "ST_PointFromText(FORMAT('POINT(%s %s)', cast(T1.longitude as varchar), "
         "cast(T1.latitude as varchar)), 4326))\n\nLEFT OUTER JOIN \n\t("
         "SELECT rast AS rast_bioclim_bio2 \n\tFROM bioclim.bio2) "
         "AS as_1 \nON ST_Intersects(as_1.rast_bioclim_bio2, "
         "ST_PointFromText(FORMAT('POINT(%s %s)', "
         "cast(T1.longitude as varchar), cast(T1.latitude as varchar)), 4326))"),
    "mammal-community-sites-harvard-soil":
        ("SELECT T1.abundance_data_format AS T1_abundance_data_format, "
         "T1.abundance_data_present AS T1_abundance_data_present, T1.country "
         "AS T1_country, T1.elevation_high AS T1_elevation_high, T1.elevation_low "
         "AS T1_elevation_low, T1.habitat_code AS T1_habitat_code, "
         "T1.habitat_description AS T1_habitat_description, T1.latitude "
         "AS T1_latitude, T1.location AS T1_location, T1.longitude "
         "AS T1_longitude, T1.n_years AS T1_n_years, T1.notes "
         "AS T1_notes, T1.reference_id AS T1_reference_id, T1.site_id "
         "AS T1_site_id, T1.spatial_extent AS T1_spatial_extent, T1.state "
         "AS T1_state, T1.study_duration AS T1_study_duration, T1.time_series "
         "AS T1_time_series, T1.uncertainty_radius "
         "AS T1_uncertainty_radius, as_0.drainage_c "
         "AS as_0_drainage_c, as_0.gid AS as_0_gid, as_0.mesic_soil "
         "AS as_0_mesic_soil, as_0.simmons_so AS as_0_simmons_so, as_0.type_ "
         "AS as_0_type_ ,ST_PointFromText(FORMAT('POINT(%s %s)', "
         "cast(T1.longitude as varchar), "
         "cast(T1.latitude as varchar)), 4326)  as feature_geom_harvard_forest_soils \n"
         "INTO {result_dbi}.{result_tablei} \n\n\n"
         "FROM (SELECT  site_id, reference_id, location, country, state, "
         "latitude, longitude, uncertainty_radius, elevation_low, elevation_high, "
         "habitat_description, habitat_code, abundance_data_present, "
         "abundance_data_format, spatial_extent, study_duration, "
         "time_series, n_years, notes  \nFROM mammal_community_db.sites  \n"
         "WHERE CAST(latitude AS TEXT) NOT LIKE '%NULL%' AND latitude IS "
         "NOT NULL AND CAST(longitude AS TEXT) NOT LIKE '%NULL%' "
         "AND longitude IS NOT NULL  ) T1 \nLEFT OUTER JOIN \n\t("
         "SELECT drainage_c, geom AS geom_harvard_forest_soils, gid, "
         "mesic_soil, notes, simmons_so, type_ \n\tFROM harvard_forest.soils) "
         "AS as_0  \nON ST_Within(ST_PointFromText(FORMAT('POINT(%s %s)', "
         "cast(T1.longitude as varchar), cast(T1.latitude as varchar)), 4326) , "
         "as_0.geom_harvard_forest_soils)"),
    "fia-alabama-plot-cond":
        ("SELECT T1.cn AS T1_cn, T1.plt_cn AS T1_plt_cn, T1.prev_tre_cn "
         "AS T1_prev_tre_cn, as_0.invyr AS as_0_invyr, as_0.measday "
         "AS as_0_measday, as_0.measmon AS as_0_measmon, as_0.measyear "
         "AS as_0_measyear, as_0.prev_plt_cn "
         "AS as_0_prev_plt_cn, as_1.fortypcd AS as_1_fortypcd, as_1.siteclcd "
         "AS as_1_siteclcd, as_1.stdage AS as_1_stdage  \n"
         "into {result_dbi}.{result_tablei} \n\n\nFROM fia_alabama.tree  "
         "AS T1 \nLEFT OUTER JOIN \n\t("
         "SELECT cn, invyr, measday, measmon, measyear, prev_plt_cn \n\t"
         "FROM fia_alabama.plot ) AS as_0 \nON as_0.cn=T1.plt_cn\n"
         "LEFT OUTER JOIN \n\t(SELECT cn, fortypcd, plt_cn, siteclcd, stdage \n\t"
         "FROM fia_alabama.cond ) AS as_1 \nON as_1.cn=T1.cn"),
}

parameters = [key for key, value in expected_query.items()]


@pytest.mark.parametrize("key", parameters)
def test_make_sql(key):
    script_list = SCRIPT_LIST()
    for i in script_list:
        if i.name == key:
            output_query = make_sql(i).strip().replace("\n", "")
            assert output_query == expected_query[key].strip().replace("\n", "")
# -*- coding: utf-8 -*-
# Read raw data
# Author: Jimmy Royer
# jimmy.royer@analysisgroup.com
# May 15, 2016

import pandas as pd

# Training Sample -- All the Mutations
data= pd.read_csv("./eth.csv",
                  usecols =
                   ["y",
					"SNP_P_1673425_C15T_promoter_fabG1.inhA", "SNP_CN_1673449_A10C_T4P_fabG1",
					"SNP_CN_4326333_C1141G_A381P_ethA", "SNP_CN_4326341_G1133A_P378L_ethA", "SNP_P_1673423_G17T_promoter_fabG1.inhA", "SNP_CN_1674263_T62C_I21T_inhA", "SNP_CN_4326116_G1358A_T453I_ethA",
					"SNP_CN_1674481_T280G_S94A_inhA", "DEL_CF_4327442_d32C_11_ethA", "SNP_CN_4326996_G478C_P160A_ethA", "SNP_CZ_4326724_G750C_Y250._ethA", "SNP_CZ_4326600_G874A_R292._ethA", 
					"INS_CF_4326722_i752C_251_ethA", "SNP_P_1673432_T8C_promoter_fabG1.inhA", "DEL_CF_4326184_d1290G_430_ethA", "SNP_CN_4326439_G1035T_N345K_ethA", "SNP_CN_4327445_A29C_V10G_ethA",
					"SNP_CN_4327380_A94C_Y32D_ethA", "SNP_CZ_4326714_G760A_Q254._ethA", "SNP_CN_4327416_C58A_A20S_ethA", "SNP_CN_4326676_G798C_S266R_ethA", "SNP_CN_1674782_T581C_I194T_inhA",
					"SNP_P_4327484_T11C_promoter_ethA", "SNP_CZ_4326278_G1196T_S399._ethA", "INS_CF_4326719_i755GC_252_ethA", "INS_CI_4326506_i968GTC_323_ethA", "SNP_CN_4326860_A614G_L205P_ethA",
					"DEL_CF_4326614_d860T_287_ethA", "DEL_CF_4327334_d140A_47_ethA", "SNP_CN_1674434_T233G_V78G_inhA", "SNP_CN_4327325_T149C_Y50C_ethA", "SNP_CN_4327376_G98C_A33G_ethA",
					"INS_CF_4326414_i1060ATCT_354_ethA", "SNP_CN_4327367_T107C_E36G_ethA", "SNP_CN_4326630_A844C_F282V_ethA", "DEL_CF_4327409_d65T_22_ethA", "SNP_CN_4327350_C124T_G42S_ethA",
					"SNP_CN_4327311_A163C_S55A_ethA", "SNP_CN_4326305_G1169A_S390F_ethA", "SNP_P_4327480_A7G_promoter_ethA", "SNP_CN_4326713_T761G_Q254P_ethA", "SNP_CZ_4326250_G1224T_Y408._ethA",
					"INS_CF_4326141_i1333C_445_ethA", "SNP_CN_4327145_G329C_S110W_ethA", "SNP_CN_4326705_G769C_P257A_ethA", "SNP_CZ_4326603_G871A_Q291._ethA", "SNP_CN_4327293_T181C_T61A_ethA",
					"SNP_P_1673432_T8A_promoter_fabG1.inhA", "SNP_CN_4326113_G1361A_P454L_ethA", "SNP_CN_1674262_A61G_I21V_inhA", "SNP_CN_4327409_T65G_H22P_ethA", "INS_CF_4326802_i672C_224_ethA",
					"DEL_CF_4327133_d341T_114_ethA", "SNP_CZ_4326858_G616A_Q206._ethA", "DEL_CF_4326420_d1054C_352_ethA", "SNP_CZ_4326399_G1075A_Q359._ethA", "SNP_CN_4326263_C1211A_R404L_ethA",
					"INS_CF_4327160_i314A_105_ethA", "SNP_CN_4326996_G478A_P160S_ethA", "SNP_CN_4326111_A1363G_W455R_ethA", "SNP_CZ_4326755_C719T_W240._ethA", "SNP_P_1673432_T8G_promoter_fabG1.inhA",
					"SNP_CN_4327065_A409G_C137R_ethA", "SNP_CN_4326553_G921T_H307Q_ethA", "SNP_CZ_4326608_C866T_W289._ethA", "SNP_CN_4326759_G715A_R239W_ethA", "SNP_CN_4326452_G1022A_A341V_ethA",
					"SNP_CN_4326182_A1292G_F431S_ethA", "SNP_CN_4326980_T494G_Q165P_ethA", "SNP_CN_4326908_G566T_T189K_ethA", "SNP_CZ_4326639_G835A_R279._ethA", "SNP_CN_4327121_A353C_V118G_ethA",
					"SNP_CN_4326449_G1025T_T342K_ethA", "DEL_CF_4326440_d1034T_345_ethA", "SNP_CN_4326476_A998C_L333R_ethA", "SNP_CN_4327313_C161A_R54L_ethA", "SNP_CN_4326380_G1094A_T365M_ethA",
					"SNP_CZ_4327081_G393T_C131._ethA", "DEL_CF_4326877_d597G_199_ethA", "SNP_CN_4326632_T842C_H281R_ethA", "SNP_CN_4326977_T497G_H166P_ethA", "SNP_CN_1673822_A383G_Q128R_fabG1",
					"SNP_CN_4327022_A452G_F151S_ethA", "DEL_CF_4326722_d752CTGTACACGGC_251_ethA", "SNP_CN_4326297_G1177C_L393V_ethA", "INS_CF_4327213_i261GC_87_ethA", "SNP_CN_4326135_G1339A_P447S_ethA",
					"SNP_CN_4326470_G1004T_A335D_ethA", "INS_CF_4326370_i1104G_368_ethA", "SNP_CN_4327322_G152A_P51L_ethA", "DEL_CF_4326173_d1301A_434_ethA", "SNP_CN_4327289_A185T_L62Q_ethA", 
					"SNP_CN_4326611_G863C_P288R_ethA", "SNP_CN_4326749_T725G_N242T_ethA", "SNP_CZ_4326669_G805A_Q269._ethA", "SNP_CN_4326858_G616C_Q206E_ethA", "DEL_CF_4326187_d1287C_429_ethA",
					"SNP_CN_4326273_A1201C_F401V_ethA", "SNP_CN_4326612_G862C_P288A_ethA", "SNP_CN_1673818_A379G_M127V_fabG1", "INS_CF_4326083_i1391T_464_ethA", "SNP_CN_4326800_A674G_L225P_ethA", 
					"INS_CF_4327294_i180G_60_ethA", "SNP_CZ_4327148_C326T_W109._ethA", "SNP_CN_4327058_C416T_G139D_ethA", "SNP_CN_4327211_G263A_T88I_ethA", "DEL_CF_4326771_d703A_235_ethA", 
					"SNP_CN_4327424_A50G_V17A_ethA", "SNP_CN_4326815_C659T_G220D_ethA", "SNP_CN_4327073_A401G_L134P_ethA", "SNP_CZ_4326715_G759T_C253._ethA", "INS_CF_4326585_i889GCACC_297_ethA",
					"SNP_CN_4327448_A26G_I9T_ethA", "SNP_P_1673406_C34T_promoter_fabG1.inhA", "DEL_CD_4326366_d1108TGTAGGCCATCG_370_ethA", "SNP_CN_4327301_T173G_D58A_ethA",
					"SNP_CZ_4326099_G1375A_Q459._ethA",
					"SNP_CN_4327347_C127T_G43S_ethA", "SNP_P_4327501_G28A_promoter_ethA", "SNP_CZ_4326396_G1078A_Q360._ethA", "SNP_CN_4326717_A757G_C253R_ethA", "SNP_CN_4326327_T1147G_T383P_ethA", 
					"INS_CF_4326217_i1257G_419_ethA", "SNP_CN_4327471_C3T_M1I_ethA", "SNP_CN_4327311_A163G_S55P_ethA", "SNP_CN_4327136_T338C_E113G_ethA", "SNP_CZ_4326213_G1261A_R421._ethA"
                    ])

# List of Features to Keep in the Analysis
features = ["SNP_P_1673425_C15T_promoter_fabG1.inhA", "SNP_CN_1673449_A10C_T4P_fabG1", "SNP_CN_4326333_C1141G_A381P_ethA", "SNP_CN_4326341_G1133A_P378L_ethA", "SNP_P_1673423_G17T_promoter_fabG1.inhA", 
            "SNP_CN_1674263_T62C_I21T_inhA", "SNP_CN_4326116_G1358A_T453I_ethA", "SNP_CN_1674481_T280G_S94A_inhA", "DEL_CF_4327442_d32C_11_ethA", "SNP_CN_4326996_G478C_P160A_ethA", 
            "SNP_CZ_4326724_G750C_Y250._ethA", "SNP_CZ_4326600_G874A_R292._ethA", "INS_CF_4326722_i752C_251_ethA", "SNP_P_1673432_T8C_promoter_fabG1.inhA", "DEL_CF_4326184_d1290G_430_ethA", 
            "SNP_CN_4326439_G1035T_N345K_ethA", "SNP_CN_4327445_A29C_V10G_ethA", "SNP_CN_4327380_A94C_Y32D_ethA", "SNP_CZ_4326714_G760A_Q254._ethA", "SNP_CN_4327416_C58A_A20S_ethA", 
            "SNP_CN_4326676_G798C_S266R_ethA", "SNP_CN_1674782_T581C_I194T_inhA",
		"SNP_P_4327484_T11C_promoter_ethA", "SNP_CZ_4326278_G1196T_S399._ethA", "INS_CF_4326719_i755GC_252_ethA", "INS_CI_4326506_i968GTC_323_ethA", "SNP_CN_4326860_A614G_L205P_ethA",
		"DEL_CF_4326614_d860T_287_ethA", "DEL_CF_4327334_d140A_47_ethA", "SNP_CN_1674434_T233G_V78G_inhA", "SNP_CN_4327325_T149C_Y50C_ethA", "SNP_CN_4327376_G98C_A33G_ethA",
		"INS_CF_4326414_i1060ATCT_354_ethA", "SNP_CN_4327367_T107C_E36G_ethA", "SNP_CN_4326630_A844C_F282V_ethA", "DEL_CF_4327409_d65T_22_ethA", "SNP_CN_4327350_C124T_G42S_ethA",
		"SNP_CN_4327311_A163C_S55A_ethA", "SNP_CN_4326305_G1169A_S390F_ethA", "SNP_P_4327480_A7G_promoter_ethA", "SNP_CN_4326713_T761G_Q254P_ethA", "SNP_CZ_4326250_G1224T_Y408._ethA",
		"INS_CF_4326141_i1333C_445_ethA", "SNP_CN_4327145_G329C_S110W_ethA", "SNP_CN_4326705_G769C_P257A_ethA", "SNP_CZ_4326603_G871A_Q291._ethA", "SNP_CN_4327293_T181C_T61A_ethA",
		"SNP_P_1673432_T8A_promoter_fabG1.inhA", "SNP_CN_4326113_G1361A_P454L_ethA", "SNP_CN_1674262_A61G_I21V_inhA", "SNP_CN_4327409_T65G_H22P_ethA", "INS_CF_4326802_i672C_224_ethA",
		"DEL_CF_4327133_d341T_114_ethA", "SNP_CZ_4326858_G616A_Q206._ethA", "DEL_CF_4326420_d1054C_352_ethA", "SNP_CZ_4326399_G1075A_Q359._ethA", "SNP_CN_4326263_C1211A_R404L_ethA",
		"INS_CF_4327160_i314A_105_ethA", "SNP_CN_4326996_G478A_P160S_ethA", "SNP_CN_4326111_A1363G_W455R_ethA", "SNP_CZ_4326755_C719T_W240._ethA", "SNP_P_1673432_T8G_promoter_fabG1.inhA",
		"SNP_CN_4327065_A409G_C137R_ethA", "SNP_CN_4326553_G921T_H307Q_ethA", "SNP_CZ_4326608_C866T_W289._ethA", "SNP_CN_4326759_G715A_R239W_ethA", "SNP_CN_4326452_G1022A_A341V_ethA",
		"SNP_CN_4326182_A1292G_F431S_ethA", "SNP_CN_4326980_T494G_Q165P_ethA", "SNP_CN_4326908_G566T_T189K_ethA", "SNP_CZ_4326639_G835A_R279._ethA", "SNP_CN_4327121_A353C_V118G_ethA",
		"SNP_CN_4326449_G1025T_T342K_ethA", "DEL_CF_4326440_d1034T_345_ethA", "SNP_CN_4326476_A998C_L333R_ethA", "SNP_CN_4327313_C161A_R54L_ethA", "SNP_CN_4326380_G1094A_T365M_ethA",
		"SNP_CZ_4327081_G393T_C131._ethA", "DEL_CF_4326877_d597G_199_ethA", "SNP_CN_4326632_T842C_H281R_ethA", "SNP_CN_4326977_T497G_H166P_ethA", "SNP_CN_1673822_A383G_Q128R_fabG1",
		"SNP_CN_4327022_A452G_F151S_ethA", "DEL_CF_4326722_d752CTGTACACGGC_251_ethA", "SNP_CN_4326297_G1177C_L393V_ethA", "INS_CF_4327213_i261GC_87_ethA", "SNP_CN_4326135_G1339A_P447S_ethA",
		"SNP_CN_4326470_G1004T_A335D_ethA", "INS_CF_4326370_i1104G_368_ethA", "SNP_CN_4327322_G152A_P51L_ethA", "DEL_CF_4326173_d1301A_434_ethA", "SNP_CN_4327289_A185T_L62Q_ethA", 
		"SNP_CN_4326611_G863C_P288R_ethA", "SNP_CN_4326749_T725G_N242T_ethA", "SNP_CZ_4326669_G805A_Q269._ethA", "SNP_CN_4326858_G616C_Q206E_ethA", "DEL_CF_4326187_d1287C_429_ethA",
		"SNP_CN_4326273_A1201C_F401V_ethA", "SNP_CN_4326612_G862C_P288A_ethA", "SNP_CN_1673818_A379G_M127V_fabG1", "INS_CF_4326083_i1391T_464_ethA", "SNP_CN_4326800_A674G_L225P_ethA", 
		"INS_CF_4327294_i180G_60_ethA", "SNP_CZ_4327148_C326T_W109._ethA", "SNP_CN_4327058_C416T_G139D_ethA", "SNP_CN_4327211_G263A_T88I_ethA", "DEL_CF_4326771_d703A_235_ethA", 
		"SNP_CN_4327424_A50G_V17A_ethA", "SNP_CN_4326815_C659T_G220D_ethA", "SNP_CN_4327073_A401G_L134P_ethA", "SNP_CZ_4326715_G759T_C253._ethA", "INS_CF_4326585_i889GCACC_297_ethA",
		"SNP_CN_4327448_A26G_I9T_ethA", "SNP_P_1673406_C34T_promoter_fabG1.inhA", "DEL_CD_4326366_d1108TGTAGGCCATCG_370_ethA", "SNP_CN_4327301_T173G_D58A_ethA",
		"SNP_CZ_4326099_G1375A_Q459._ethA", "SNP_CN_4327347_C127T_G43S_ethA", "SNP_P_4327501_G28A_promoter_ethA", "SNP_CZ_4326396_G1078A_Q360._ethA", "SNP_CN_4326717_A757G_C253R_ethA", 
           "SNP_CN_4326327_T1147G_T383P_ethA", "INS_CF_4326217_i1257G_419_ethA", "SNP_CN_4327471_C3T_M1I_ethA", "SNP_CN_4327311_A163G_S55P_ethA", "SNP_CN_4327136_T338C_E113G_ethA", 
           "SNP_CZ_4326213_G1261A_R421._ethA"]
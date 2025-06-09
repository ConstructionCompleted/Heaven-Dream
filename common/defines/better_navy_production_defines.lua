NDefines.NAI.SHIPS_PRODUCTION_BASE_COST = 25000;					-- Used by the AI to normalize IC values when picking what ship to build.
NDefines.NAI.CAPITAL_TASKFORCE_MAX_CAPITAL_COUNT = 8; 		-- optimum capital count for capital taskforces
NDefines.NAI.SCREEN_TASKFORCE_MAX_SHIP_COUNT = 8;			-- optimum screen count for screen taskforces
NDefines.NAI.SUB_TASKFORCE_MAX_SHIP_COUNT = 8 ;				-- optimum sub count for sub taskforces
NDefines.NAI.MIN_CAPITALS_FOR_CARRIER_TASKFORCE = 6;			-- carrier fleets will at least have this amount of capitals
NDefines.NAI.MIN_MAIN_SHIP_RATIO = 0.6;                      -- if main ship ratio is below this; steal other ships.
NDefines.NAI.MIN_SUPPORT_SHIP_RATIO = 0.8;                   -- if support ship ratio is below this; steal other ships.
NDefines.NAI.MIN_MAIN_SHIP_RATIO_TO_REINFORCE = 0.75;         -- the main ships will be tried to reinforce this level.
NDefines.NAI.MAIN_SHIP_RATIO_TO_SPLIT = 2.0;                 -- if main ship ratio in a task force is larger than this; split it. (If a carrier TF wants 4 carriers (see 
NDefines.NAI.SCREENS_TO_CAPITAL_RATIO = 5.0;					-- screens to capital/carrier count in carrier & capital taskforces
NDefines.NNavy.ANTI_AIR_TARGETTING_TO_CHANCE = 0.5;			-- Balancing value to convert averaged equipment stats (anti_air_targetting and naval_strike_agility) to probability chances of airplane being hit by navies AA.
NDefines.NNavy.ANTI_AIR_ATTACK_TO_AMOUNT = 0.005;				-- Balancing value to convert equipment stat anti_air_attack to the random % value of airplanes being hit.
NDefines.NNavy.NAVAL_COMBAT_RESULT_TIMEOUT_YEARS = 24;							-- after that many years; we clear the naval combat results; so they don't get stuck forever in the memory.
NDefines.NNavy.CONVOY_LOSS_HISTORY_TIMEOUT_MONTHS = 24;						-- after this many months remove the history of lost convoys to not bloat savegames and memory since there is no way to see them anyway
NDefines.NNavy.NAVAL_COMBAT_AIR_CAPITAL_TARGET_SCORE = 50;
NDefines.NNavy.NAVAL_COMBAT_AIR_CARRIER_TARGET_SCORE = 100;
NDefines.NNavy.HIGHER_SHIP_RATIO_POSITIONING_PENALTY_FACTOR					= 0.75; -- if one side has more ships than the other; that side will get this penalty for each +100% ship ratio it has
NDefines.NNavy.SUB_DETECTION_CHANCE_BASE_SPOTTING_EFFECT = 1.0;				-- effect of base spotting for initial spotting of pure submarine forces. this along with next value is added together and rolled against a random to start spotting
NDefines.NNavy.SUB_DETECTION_CHANCE_SPOTTING_SPEED_EFFECT = 4.0;				-- effect of spotting speed for initial spotting of pure submarine forces. this along with prev value is added together and rolled against a random to start spotting
NDefines.NNavy.SUB_DETECTION_CHANCE_BASE_SPOTTING_POW_EFFECT = 3.0;			-- effect of spotting speed will be powered by this for initial spotting of pure submarine forces. this along with prev value is added together and rolled against a random to start spotting
NDefines.NAI.REFIT_SHIP_RELUCTANCE = 1;
NDefines.NAI.REFIT_SHIP_PERCENTAGE_OF_FORCES = 0.2;
NDefines.NAI.NAVY_PREFERED_MAX_SIZE = 75;
NDefines.NAI.PRODUCTION_MAX_PROGRESS_TO_SWITCH_NAVAL = 0.05;
NDefines.NNavy.AGGRESSION_SETTINGS_VALUES = { -- ships will use this values while deciding to attack enemies
		0,		-- do not engage
		1.0,	-- low
		1.5,	-- medium
		2.5,	-- high
		10000,	-- I am death incarnate!
	};
NDefines.NNavy.WAR_SCORE_GAIN_FOR_SUNK_SHIP_MANPOWER_FACTOR = 0.002;			-- war score gained for every manpower killed when sinking a ship
NDefines.NNavy.WAR_SCORE_GAIN_FOR_SUNK_SHIP_PRODUCTION_COST_FACTOR = 0.01;		-- war score gained for every IC of the sunk ship
NDefines.NAI.MIN_NAVAL_MISSION_PRIO_TO_ASSIGN = {  -- priorities for regions to get assigned to a mission
		0, -- HOLD (consumes fuel HOLD_MISSION_MOVEMENT_COST fuel while moving)
		200, -- PATROL
		200, -- STRIKE FORCE
		100, -- CONVOY RAIDING
		100, -- CONVOY ESCORT
		100, -- MINES PLANTING
		100, -- MINES SWEEPING
		300, -- TRAIN
		0, -- RESERVE_FLEET
		100, -- NAVAL INVASION SUPPORT
	};

NDefines.NAI.HIGH_PRIO_NAVAL_MISSION_SCORES = {  -- priorities for regions to get assigned to a mission
		0, -- HOLD (consumes fuel HOLD_MISSION_MOVEMENT_COST fuel while moving)
		10000, -- PATROL
		5000, -- STRIKE FORCE
		500, -- CONVOY RAIDING
		1000, -- CONVOY ESCORT
		-1, -- MINES PLANTING
		300, -- MINES SWEEPING
		0, -- TRAIN
		0, -- RESERVE_FLEET
		1000, -- NAVAL INVASION SUPPORT
	};
NDefines.NAI.WANTED_UNITS_INDUSTRY_FACTOR = 2.00;                        -- How many units a country wants is partially based on how much military industry that is available
NDefines.NNavy.EXPERIENCE_LOSS_FACTOR = 0.50;                 					-- percentage of experienced solders who die when manpower is removed
NDefines.NNavy.UNIT_EXPERIENCE_PER_COMBAT_HOUR = 5.0;  
NDefines.NNavy.EXPERIENCE_FACTOR_CARRIER_GAIN = 0.04;							-- Xp gain by carrier ships in the combat
NDefines.NNavy.NAVY_MAX_XP = 200;
NDefines.NAir.NAVAL_STRIKE_DAMAGE_TO_STR = 0.5;					-- Balancing value to convert damage ( naval_strike_attack * hits ) to Strength reduction.
NDefines.NAir.NAVAL_STRIKE_DAMAGE_TO_ORG = 0.75;					-- Balancing value to convert damage ( naval_strike_attack * hits ) to Organisation reduction.
NDefines.NAir.NAVAL_STRIKE_CARRIER_MULTIPLIER = 30.0;              -- damage bonus when planes are in naval combat where their carrier is present (and can thus sortie faster and more effectively)
NDefines.NAir.NAVAL_STRIKE_TARGETTING_TO_AMOUNT = 0.5;			-- Balancing value to convert the naval_strike_targetting equipment stats to chances of how many airplanes managed to do successfull strike.
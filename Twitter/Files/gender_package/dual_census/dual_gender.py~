# Encoding: utf8
# Copyright 2010 Amaç Herdağdelen

from name_gender import NameGender
from web_name_gender import WebNameGender

def master_score(newname):
	#make name lower case
	lowname = newname.strip().lower()
	print lowname
	#pass name through both guessers
	prim_int = get_decision(primary_guesser, lowname)
	sec_int = get_decision(secondary_guesser, lowname)
	#get an average score
	avg_int = (prim_int + sec_int)/2
	return avg_int

def get_decision(guesser, name):
    m,f = guesser.get_gender_scores(name)
    if m > 0.5:
		return m
    elif f > 0.5:
		fe = f * -1
		return fe
    else:
        return 0

# Give precedence to us_census data.
primary_guesser = NameGender("us_census_1990_males", "us_census_1990_females")
secondary_guesser = NameGender("popular_1960_2010_males","popular_1960_2010_females")


    




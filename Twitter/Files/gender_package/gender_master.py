import gender_package.getgender
from gender_package.dual_census.dual_gender import master_score

def masta_genda(name):
	sexmachine = gender_package.getgender.sexmachine(name)
	dual_census = master_score(name)
	if sexmachine == 0:
		masta_int = dual_census
	if dual_census == 0:
		masta_int = sexmachine
	if (sexmachine != 0) & (dual_census != 0):
		masta_int = (sexmachine + dual_census)/2
	return masta_int
	


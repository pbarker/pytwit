import sexmachine.detector as gender
import dual_census


d = gender.Detector()



def sexmachine(firsty):
    numgender1 = 0
    thegender = d.get_gender(firsty, 'usa')
    if thegender == "male":
	numgender1 = 1
    elif thegender == "female":
	numgender1 = -1
    elif thegender == "mostly_male":
	numgender1 = .75
    elif thegender == "mostly_female":
	numgender1 = -.75
    elif thegender == "andy":
	numgender1 = 0
    return numgender1



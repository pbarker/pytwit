import sexmachine.detector as gender
import getgendersub

d = gender.Detector()



def sexmachine(firsty):
    thegender = d.get_gender(firsty, 'usa')
    return thegender




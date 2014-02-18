""" Functions for retrieving IPA data from protuguese text """
# coding=UTF-8
import urllib
import urllib2

sampa2IPA = ["g","ɡ","r","ɾ","R","ʀ","E","ɛ","J","ɲ","L","ʎ","O","ɔ","S","ʃ","Z","ʒ","\"","ˈ","@","ɘ","6","ɐ","~","̃","%","ˌ"]
word = ""
ipaData = ""


def getSampaFromString(data):
    """ Scrapes SAMPA data from normal encoding"""

    url = "http://www.co.it.pt/%7Elabfala/g2p/g2p_exec.php"
    values = {'grafemas' : data}

    packed_values = urllib.urlencode(values)
    req = urllib2.Request(url, packed_values)
    response = urllib2.urlopen(req)

    page = response.read()
    page = stripNewlineCR(page)
    return page

def stripNewlineCR(data):
    data = data[:-2]
    return data

def stripStress(data):
	newStr = data.replace("ˈ","")
	return newStr

def getIpaFromSampa(sampaStr):

    newStr = ""
    matched = False

    for i in xrange(len(sampaStr)):
        matched = False

        for j in xrange(len(sampa2IPA)):
            if sampaStr[i] == sampa2IPA[j] and matched == False:
                newStr += sampa2IPA[j+1]
                matched = True
                break

        if matched == False:
            newStr += sampaStr[i]

    return newStr

def wrapAndReturn(data):
	word = getSampaFromString(data)
	ipaData = getIpaFromSampa(word)
	ipaData = stripStress(ipaData)
	return ipaData

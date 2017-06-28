import re
#CONTRACCIONES
def isContraction(lema):
	m = re.match(r"(\w+)\+(\w+)", lema)
	if(m == None):
		return False
	else:
		return True

def getContractionForms(lema):
	m = re.match("(\w+)\+(\w+)", lema)
	form1 = str(m.group(1))
	form2 = str(m.group(2))
	if(form1 == "a"):
		lema1 = "a"
		tag1= "SP"
	else:
		lema1 = "de"
		tag1 = "SP"
	lema2= "el"
	tag2= "DA0MS0"
	t = (form1,form2)
	return t

def getContractionLemas(lema):
	m = re.match("(\w+)\+(\w+)", lema)
	form1 = str(m.group(1))
	form2 = str(m.group(2))
	if(form1 == "a"):
		lema1 = "a"
		tag1= "SP"
	else:
		lema1 = "de"
		tag1 = "SP"
	lema2= "el"
	tag2= "DA0MS0"
	t = (lema1,lema2)
	return t

def getContractionTags(lema):
	m = re.match("(\w+)\+(\w+)", lema)
	form1 = str(m.group(1))
	form2 = str(m.group(2))
	if(form1 == "a"):
		lema1 = "a"
		tag1= "SP"
	else:
		lema1 = "de"
		tag1 = "SP"
	lema2= "el"
	tag2= "DA0MS0"
	t = (tag1,tag2)
	return t

#UPOSTAG, FEATS y MISC
def getTagFeatsMisc(Stag):
    Stag = Stag + '_'*(7-len(Stag))
    tag = ""
    feats = ""
    misc = "O"
    #adjective
    if Stag[0] == 'A':
        tag = "ADJ"
        #type
        if Stag[1] == 'O':
            feats = feats + "AdjType=Ordinal|"
        elif Stag[1] == 'Q':
            feats = feats + "AdjType=Qualificative|"
        elif Stag[1] == 'P':
            feats = feats + "AdjType=Possessive|"
        #degree
        if Stag[2] == 'S':
            feats = feats + "AdjType=Superlative|"
        elif Stag[2] == 'V':
            feats = feats + "AdjType=Evaluative|"
        #gender
        if Stag[3] == 'F':
            feats = feats + "Gender=Fem|"
        elif Stag[3] == 'M':
            feats = feats + "Gender=Masc|"
        elif Stag[3] == 'C':
            feats = feats + "Gender=Com|"
        #number
        if Stag[4] == 'S':
            feats = feats + "Number=Sing|"
        elif Stag[4] == 'P':
            feats = feats + "Number=Plur|"
        elif Stag[4] == 'N':
            feats = feats + "Number=Inv|"
    #conjunction
    elif Stag[0] == 'C':
		# type coordinating
        tag = "CONJ"
        #type subordinating
        if Stag[1] == 'S':
            tag = "SCONJ"
    #determiner
    elif Stag[0] == 'D':
        tag = "DET"
        #type
        if Stag[1] == 'A':
            feats = feats + "PronType=Art|"
        elif Stag[1] == 'D':
            feats = feats + "PronType=Demonstrative|"
        elif Stag[1] == 'I':
            feats = feats + "PronType=Indefinite|"
        elif Stag[1] == 'P':
            feats = feats + "PronType=Possessive|"
        elif Stag[1] == 'T':
            feats = feats + "PronType=Interrogative|"
        elif Stag[1] == 'E':
            feats = feats + "PronType=Exclamative|"
        #person
        if Stag[2] == '1':
            feats = feats + "Person=1|"
        elif Stag[2] == '2':
            feats = feats + "Person=2|"
        elif Stag[2] == '3':
            feats = feats + "Person=3|"     
        #gender
        if Stag[3] == 'F':
            feats = feats + "Gender=Fem|"
        elif Stag[3] == 'M':
            feats = feats + "Gender=Masc|"
        elif Stag[3] == 'C':
            feats = feats + "Gender=Com|"
        #number
        if Stag[4] == 'S':
            feats = feats + "Number=Sing|"
        elif Stag[4] == 'P':
            feats = feats + "Number=Plur|"
        elif Stag[4] == 'N':
            feats = feats + "Number=Inv|"
        
    #noun
    elif Stag[0] == 'N':
		#type common noun
        tag = "NOUN"
        #type proper noun
        if Stag[1] == 'P':
            tag = "PROPN"
        #gender
        if Stag[2] == 'F':
            feats = feats + "Gender=Fem|"
        elif Stag[2] == 'M':
            feats = feats + "Gender=Masc|"
        elif Stag[2] == 'C':
            feats = feats + "Gender=Com|"
        #number
        if Stag[3] == 'S':
            feats = feats + "Number=Sing|"
        elif Stag[3] == 'P':
            feats = feats + "Number=Plur|"  
        elif Stag[3] == 'N':
            feats = feats + "Number=Inv|"
        #class
        if Stag[4] == 'S':
           misc = 'PER'
        elif Stag[4] == 'G':
           misc = "LOC"
        elif Stag[4] == 'O':
           misc = "ORG"
        else:
           misc = "O"
        #degree
        if Stag[6] == 'V':
            feats = feats + "Degree=Evaluative|"
    #pronoun
    elif Stag[0] == 'P':
        tag = "PRON"
        #type
        if Stag[1] == 'D':
            feats = feats + "PronType=Demonstrative|"
        elif Stag[1] == 'E':
            feats = feats + "PronType=Exclamative|"
        elif Stag[1] == 'I':
            feats = feats + "PronType=Indefinite|"
        elif Stag[1] == 'P':
            feats = feats + "PronType=Personal|"
        elif Stag[1] == 'R':
            feats = feats + "PronType=Relative|"
        elif Stag[1] == 'T':
            feats = feats + "PronType=Interrogative|"
        #person
        if Stag[2] == '1':
            feats = feats + "Person=1|"
        elif Stag[2] == '2':
            feats = feats + "Person=2|"
        elif Stag[2] == '3':
            feats = feats + "Person=3|"
        #gender
        if Stag[3] == 'F':
            feats = feats + "Gender=Fem|"
        elif Stag[3] == 'M':
            feats = feats + "Gender=Masc|"
        elif Stag[3] == 'C':
            feats = feats + "Gender=Com|"
        #number
        if Stag[4] == 'S':
            feats = feats + "Number=Sing|"
        elif Stag[4] == 'P':
            feats = feats + "Number=Plur|"
        elif Stag[4] == 'N':
            feats = feats + "Number=Inv|"
        #case
        if Stag[5] == 'N':
            feats = feats + "Case=Nominative|"
        elif Stag[5] == 'A':
            feats = feats + "Case=Accusative|"
        elif Stag[5] == 'D':
            feats = feats + "Case=Dative|"
        elif Stag[5] == 'O':
            feats = feats + "Case=Oblique|"
        #polite
        if Stag[6] == 'P':
            feats = feats + "Polite=Yes|"
    #adverb
    elif Stag[0] == 'R':
        tag = "ADV"
        if Stag[1] == 'N':
            feats = "Negative=Yes|"
        elif Stag[1] == 'G':
            feats = "Negative=No|"
    #adposition
    elif Stag[0] == 'S':
        tag = "ADP"
        if Stag[1] == 'P':
            feats = feats + "AdpType=Preposition|"
    #verb
    elif Stag[0] == 'V':
        tag = "VERB"
        #type
        if Stag[1] == 'M':
            feats = feats + "VerbType=Main|"
        elif Stag[1] == 'A':
            feats = feats + "VerbType=Auxiliary|"
        elif Stag[1] == 'S':
            feats = feats + "VerbType=Semiauxiliary|"
        #mood
        if Stag[2] == 'I':
            feats = feats + "Mood=Indicative|"
        elif Stag[2] == 'S':
            feats = feats + "Mood=Subjunctive|"
        elif Stag[2] == 'M':
            feats = feats + "Mood=Imperative|"
        elif Stag[2] == 'P':
            feats = feats + "Mood=Participle|"
        elif Stag[2] == 'G':
            feats = feats + "Mood=Gerund|"
        elif Stag[2] == 'N':
            feats = feats + "Mood=Infinitive|"
        #tense
        if Stag[3] == 'P':
            feats = feats + "Tense=Present|"
        elif Stag[3] == 'I':
            feats = feats + "Tense=Imperfect|"
        elif Stag[3] == 'F':
            feats = feats + "Tense=Future|"
        elif Stag[3] == 'S':
            feats = feats + "Tense=Past|"
        elif Stag[3] == 'C':
            feats = feats + "Tense=Conditional|"
        #person
        if Stag[4] == '1':
            feats = feats + "Person=1|"
        elif Stag[4] == '2':
            feats = feats + "Person=2|"
        elif Stag[4] == '3':
            feats = feats + "Person=3|" 
        #number
        if Stag[5] == 'S':
            feats = feats + "Number=Sing|"
        elif Stag[5] == 'P':
            feats = feats + "Number=Plur|"
        #gender
        if Stag[6] == 'F':
            feats = feats + "Gender=Fem|"
        elif Stag[6] == 'M':
            feats = feats + "Gender=Masc|"
        elif Stag[6] == 'C':
            feats = feats + "Gender=Com|"
    #number
    elif Stag[0] == 'Z':
        tag = "NUM"
        #type
        if Stag[1] == 'D':
            feats = feats + "NumType=Partitive|"
        elif Stag[1] == 'M':
            feats = feats + "NumType=Currency|"
        elif Stag[1] == 'P':
            feats = feats + "NumType=Percentage|"
        elif Stag[1] == 'U':
            feats = feats + "NumType=Unit|"
    #date
    elif Stag[0] == 'W':
        tag = "DATE"
    #interjection
    elif Stag[0] == 'I':
        tag = "INTJ"
    #punctuation
    elif Stag[0] == 'F':
        tag = "PUNCT"
    if not tag:
        tag = "_"
    if not feats:
        feats = "_"
    else:
        feats = feats[0:len(feats)-1]
    return (tag, feats, misc)

#NAME ENTITY RECOGNITION
def isGrupoNominal(gn):
	m = re.match(r"([^_]+_[^_]+)+", gn)
	if(m == None):
		return False
	else:
		return True
	
def ner(Stag):
	if(re.match("^N\w\w\wS.*",Stag)):
		return "PER"
	else:
		if(re.match("^N\w\w\wG.*",Stag)):
			return "LOC"	
		else:
			if(re.match("^N\w\w\wO.*",Stag)):
				return "ORG"
			else:
				return "O"
	
	

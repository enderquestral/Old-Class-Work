alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
import random
import math
random.seed()

#############################################################
# The following code doesn't need to be edited. It allows
# you to read a text file and store it in a single string, 
# and also to write a single string to a text file. This is
# not an ideal way to work with files, but it will suffice
# for this assignment.
#############################################################

def file_to_string(filename):
    with open(filename, "r") as f:
        x = f.read()
    return x

def string_to_file(filename, s):
    with open(filename, "w") as f:
        f.write(s)



#############################################################
# A working Caesar cipher
#############################################################

def simplify_string(s):
    newstring = ""
    for i in s:
        if i.upper() in alpha:
            newstring = newstring + i.upper()
    return newstring

def num_to_let(x):
    return alpha[x % 26]

def let_to_num(a):
    #Input a capital letter, return corresponding number
    for i in alpha:
        if i == a:
            return alpha.find(i)

def shift_char(char, shift):
#The output is the result of shifting the first letter by the amount specified by the second.
    return(num_to_let(let_to_num(char) + let_to_num(shift)))

def caesar_enc(plain, key):
    #Takes in simplified string, and then a Cap letter as the key
    #Returns cipehertext, made by shifting each value in the plaintext forward by the key amount
    encoded = ""
    plain = simplify_string(plain)

    for i in plain:
        encoded +=  shift_char(i, key)
    return encoded

def caesar_dec(cipher, key):
    #Takes encoded input, shifts it BACK by key amount
    decoded = ""
    cipher = simplify_string(cipher)
    for i in cipher:
        decoded += shift_char(i, num_to_let(26 - let_to_num(key)))
    return decoded
    

    #f = open("hitchhikers.txt", "r") for full text of file
    # c = f.read()
    #f.close()
    #then do caesar_enc(c)

#############################################################
# Breaking the Caesar cipher
#############################################################
#The most common letter is clearly E, with A, I, O, and T all very common as well. 
#The simplest frequency-based attack would be to simply find the most common letter and 
#assume that it is meant to be E, and try whatever key would decrypt that letter to E. That will work pretty often.


def letter_counts(s):
    #dictionary, listing how often letters appear. 26 keys, one for each letter. 
    newdict = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0, "O":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0, "V":0, "W":0, "X":0, "Y":0, "Z":0}
    for i in s:
        newdict[i] = newdict[i] +1
    return newdict

def normalize(counts):
    #Normalize should take as input a dictionary of counts and should modify the dictionary (not return a new one) 
    # by dividing each count by the total of all the counts in the dictionary. 
    #(We'll use this again later with a dictionary with different keys, so do not assume that the keys are always the 26 letters. This function should work with any dictionary where all the values are positive integers.)

    totalcounts = 0
    for j in counts:
        totalcounts += counts[j]

    #totalcounts = len(counts)
    for i in counts:
        counts[i] = counts[i] / totalcounts

# Uncomment the code below once the functions above are complete
english_freqs = letter_counts(simplify_string(file_to_string("twocities_full.txt")))
normalize(english_freqs)

def distance(observed, expected):
    #Here x represents a letter, and we're summing over all possible letters. 
    #obsx is the frequency of x observed in the string, while expx is the expected frequency in standard English.
    # distance = (obsx - expx)^2 / expx [for all letters]
 
    #First input is a set of frequencies observed in some particular piece of text, and the second is known frequencies for standard English. 
    #It should output a positive real number.
    sumtotal = 0
    for i in alpha:
        sumtotal += ((observed[i] - expected[i])**2)/expected[i]
    return sumtotal


def caesar_break(cipher, frequencies): # Assignment says break_caesar, but file given says caesar_break?
    #Its output should be a list of two elements. 
    #The first is a single-character string equal to the key used to encrypt/decrypt the ciphertext. The second is the recovered plaintext.

    #For each one, decrypt the ciphertext to get a possible plaintext. 
    #Then measure the distance between letter frequencies in that plaintext and letter frequencies in standard English. 
    #Return whatever key gives you the lowest distance value, and the plaintext that goes with it.
    newlist = []
    lowestval = distance(letter_counts(simplify_string(cipher)),frequencies)
    statuslet = ""
    decodedmes = ""
    for i in alpha:
        newdecode = caesar_dec(cipher, i)
        newint = distance(letter_counts(simplify_string(newdecode)),frequencies)
        if newint < lowestval:
            lowestval = newint
            statuslet = i
            decodedmes = newdecode

    newlist.append(statuslet)
    newlist.append(decodedmes)
    return newlist



#############################################################
# A working Vigenere cipher
#############################################################

def vigenere_enc(plain, key):
    #It should take two inputs, the first being a (simplified) plaintext, 
    #and the second being the key, represented as a string of capital letters. 
    #The output should be the correct ciphertext encrypting that plaintext under that key.

    encoded = ""
    q = len(key)
    v = 0
    while v < len(plain):
        encoded +=  shift_char(plain[v], key[(v % q) ])
        v += 1
    return encoded


def vigenere_dec(cipher, key):
    decoded = ""
    q = len(key)
    v = 0
    while v < len(cipher):
        decoded +=  shift_char(cipher[v], num_to_let(26 - let_to_num(key[(v % q)])))
        v += 1
    return decoded

#############################################################
# Breaking the Vigenere cipher
#############################################################

def split_string(s, parts):
    #The function takes two inputs, a string and an integer. 
    #The integer can be thought of as the length of the cipher's key, 
    #and it specifies the number of parts that the string should be divided into. 
    #The output should be a list of that many strings, each equal to the letters that would be encrypted using a particular letter of the key.
    listofstrs = []
    i =0
    j =0
    while i <parts:
        listofstrs.append("")
        i +=1

    while j <len(s):
        listofstrs[j%parts] = listofstrs[j%parts] + s[j]
        j+=1

    return listofstrs


def vig_break_for_length(cipher, klen, frequencies):
    #TEST = You understand reality while everyone else is running around confused and angry and upset because they think reality is something happening to them rather than something they are making every moment with every thought.
    # Simplified: YOUUNDERSTANDREALITYWHILEEVERYONEELSEISRUNNINGAROUNDCONFUSEDANDANGRYANDUPSETBECAUSETHEYTHINKREALITYISSOMETHINGHAPPENINGTOTHEMRATHERTHANSOMETHINGTHEYAREMAKINGEVERYMOMENTWITHEVERYTHOUGHT

    # Seems to have an issue with the letter A? Try that and Z?

    # KEY = GCAT
    # EQUNTFEKYVAGJTETRKTRCJIEKGVXXAOGKGLLKKSKAPNBTIAKUWNWIQNYAUEWGPDTTIRRGPDNVUEMHGCTAUEMNGYMNKNDXGAEOVYBYUOFKVHBTIHTVREGOPGMUVHXSTAMNGRMNCNLUOEMNKNZZJERGTEFGMIGMGVXXAMHSGNMCKTAKXEKEVHHAIHM
    # ['ETYJRCKXKKATUIAGTGVHANNXOYKTVOUSNNUNZGGMXSCKEA', 'QFVTKJGAGKPIWQUPIPUGUGKGVUVIRPVTGCOKJTMGAGKXVI', 'UEAETIVOLSNANNEDRDECEYNAYOHHEGHARNENEEIVMNTEHH', 'NKGTREXGLKBKWYWTRNMTMMDEBFBTGMXMMLMZRFGXHMAKHM']
    
    #KEY = MIND
    #'KWHXZLRUEBNQPZRDXQGBIPVOQMIHDGBQQMYVQQFUGVALZONUACAGOWAIGARGMVQDZOEBMVQXBARWNMPDGARWTMLWTQANDMNOUBLLEABPQBULZOUDBXRQUVTWABUHYZNWTMEWTIAVAURWTQAJFPRBMZRPMSVQSMIHDGZRYMAWIQGKQDRUKBURGOUW'
    #['KZEPXIQDQQGZAOGMZMBNGTTDUEQZBUAYTTATFMMSDYIQKG', 'WLBZQPMGMQVOCWAVOVAMAMQMBABOXVBZMIUQPZSMGMQDBO', 'HRNRGVIBYFANAARQEQRPRLANLBUURTUNEARARRVIZAGRUU', 'XUQDBOHQVULUGIGDBXWDWWNOLPLDQWHWWVWJBPQHRWKURW']

    #KEY = ALZAR
    #YZTUEDPQSKAYCRVAWHTPWSHLVEGDRPOYDECSPHSIUYMIEGLQOLNOBOEFFREUAYCAEGCXAEDFOSVTMDCRUDDTYEJSHZNVQERLTSYZSDNMVTSHNXHLOPVNTMGKOEGEDRLSHVREGAESZLEKHTMGKHPXAIEXZKZNRDVVRJLODEYSWZTSDVVRJSHFURGT
    #['YDAAWEOSUGNFAGDTUENLSTHNORRSHHENRETRU', 'ZPYWSGYPYLOFYCFMDJVTDSLTELEZTPXRJYSJR', 'TQCHHDDHMQBRCXODDSQSNHOMGSGLMXZDLSDSG', 'USRTLRESIOOEAASCTHEYMNPGEHAEGAKVOWVHT', 'EKVPVPCIELEUEEVRYZRZVXVKDVEKKIZVDZVF']

    #klen is length of key. Should break cipher and return a list of 2 elements, its key and its plaintext. 
    #you should simply use the same frequency analysis we used to break a Caesar cipher.
    lowestval = distance(letter_counts(simplify_string(cipher)),frequencies)

    listofsec = split_string(simplify_string(cipher),klen)
    keybuild = ""
    combinedword = ""
    decodedmes = ""
    statuslet = ""
    q=0
    v=0
    #Caesar cipher below
    
    while q < len(listofsec):
        lowestval = distance(letter_counts(listofsec[q]),frequencies)  #change lowestval to allow for A?
        for i in alpha:
            newdecode = caesar_dec(listofsec[q], i)
            newint = distance(letter_counts(simplify_string(newdecode)),frequencies)
            if newint < lowestval or newint == lowestval:
                lowestval = newint
                statuslet = i
                decodedmes = newdecode

        keybuild += statuslet
        listofsec[q] = decodedmes
        q +=1

     #Each letter is sorted lets say, and we have the key. How to get it all into one string?
    while v < len(listofsec[0]): # the LONGEST string in the bunch:
        for a in listofsec:
            if len(a) >v:
                combinedword += a[v]
        v +=1

    return [keybuild, combinedword]


def vig_break(c, maxlen, frequencies):
    #This function takes three inputs, the ciphertext, a maximum length of the key, and a dictionary of frequencies in standard English. 
    #It should break the encryption and return the key and plaintext, 
    #as long as the real key is of length less than or equal to the maximum length given. 
    #To do this, simply use the attack above assuming each possible length of key. 
    #Then for each resulting plaintext, compare the letter frequencies to those of standard English. 
    #Whichever is closest you can assume is the correct key length. 
    #If multiple key lengths result in the same distance to standard English frequencies, return the shorter key.
    

    i =1
    finalkey = ""
    finalplaintext = ""
    placeholderkey = ""
    placeholderdistance= ""
    holdsthetwo = []

    basedistance = distance(letter_counts(simplify_string(c)), frequencies)

    while i < maxlen:
        holdsthetwo = vig_break_for_length(c, i, frequencies)
        placeholderkey = holdsthetwo[0]
        placeholderdistance = distance(letter_counts(simplify_string(holdsthetwo[1])),frequencies)
        if placeholderdistance < basedistance:
            basedistance = placeholderdistance
            finalkey = holdsthetwo[0]
            finalplaintext = holdsthetwo[1]
        i +=1
    return[finalkey, finalplaintext]



#############################################################
# A working substitution cipher
#############################################################

def sub_gen_key():
#    This is a function that generates a random key for your cipher. 
#It takes no inputs and its output should be a string of the 26 capital letters in the alphabet, 
#arranged in a random order. All orders should be equally likely.
    betalpha = ""
    fakealphabet = alpha
    for i in alpha:
        q = random.randint(0, len(fakealphabet)-1)
        betalpha += fakealphabet[q]
        fakealphabet = fakealphabet.replace(fakealphabet[q], "")
    return betalpha

def sub_enc(s, k):
#It takes two inputs, a simplified string and a key, and it outputs a valid ciphertext. 
#They key should be interpreted as above, meaning that the first letter is the ciphertext's replacement for A, 
#the second is the replacement for B, and so forth.
    i =0
    newdict = {}
    newstr = ""
    while i < len(alpha):
        newdict.update({alpha[i]: k[i]})
        i+=1
    for i in s:
        newstr += newdict[i]

    return newstr

def sub_dec(s, k):
#It takes two inputs, a ciphertext and a key, and it returns the original plaintext. Reverses above.
    i =0
    newdict = {}
    newstr = ""
    while i < len(alpha):
        newdict.update({k[i]: alpha[i]})
        i+=1
    for i in s:
        newstr += newdict[i]

    return newstr


#############################################################
# Breaking the substitution cipher
#############################################################

#Here on is broken??
#YOUUNDERSTANDREALITYWHILEEVERYONEELSEISRUNNINGAROUNDCONFUSEDANDANGRYANDUPSETBECAUSETHEYTHINKREALITYISSOMETHINGHAPPENINGTOTHEMRATHERTHANSOMETHINGTHEYAREMAKINGEVERYMOMENTWITHEVERYTHOUGHT

def count_trigrams(s):
#    take as input a string and output a dictionary of trigrams. 
#Each key should be a trigram, something like THE, and the corresponding value should be the number of 
#times it appears in the string.
    newdict = {}
    i=0
    while i < len(s)-2:
        if s[i:i+3] in newdict:
            newdict[s[i:i+3]] = newdict[s[i:i+3]] +1
        else:
            newdict.update({s[i:i+3] : 1})
        i +=1
    return newdict

 
# Uncomment the code below once the functions above are complete
english_trigrams = count_trigrams(simplify_string(file_to_string("twocities_full.txt")))
normalize(english_trigrams)

def map_log(d):
#    takes as input a dictionary of frequencies and replaces every value with the natural log of that value.
    for i in d:
        d[i] = math.log(d[i])
    #return d

# Uncomment the code below once the functions above are complete
map_log(english_trigrams) 

def trigram_score(s, english_trigrams):
    # score = t1*t2*...*tn
    #ln(score) = ln(t1) +ln(t2) +... ln(tn)

    #Given a string, we want to compute the above log-score for that string. 
    #This is simply the sum of the log-frequency (in standard English) of each trigram in the string. 
    #Low scores indicate that a string has more unusual trigrams in it.

    #This function should take two inputs, a string and a dictionary of trigram log-frequencies, 
    #and it should return the score of that string.
    #If a trigram isn't present in the dictionary (meaning that it never appeared in our large sample of English text), then count its log-frequency as -15. 
    

    dictoftri = count_trigrams(s)

    trigramtotal = 0
    for i in dictoftri:
        if i in english_trigrams:
            trigramtotal += english_trigrams[i]
        else:
            trigramtotal += -15 


    return trigramtotal

def sub_break(cipher, english_trigrams):
    #I have one thing to say about this section of code in particular: I Tried. 
    #Code has commented-out print statements/variables for testing purposes. 

    #kjhlmfgdpurwzciatbveyxqons is the key for mystery3....
    # score = t1*t2*...*tn
    #ln(score) = ln(t1) +ln(t2) +... ln(tn)
    #Is the trigram score for correct mystery3 -9370.868703104028

    cipher =  simplify_string(cipher)

    newdecript = ""
    newdecript2 = ""
    placeholderint = 0
    placeholderint2 = 0
    triscorendecript2 = 0
    i =0
    keeploop = True
    

    randomkey = sub_gen_key()
    newdecript = sub_dec(cipher, randomkey)
    holdkeyguess = trigram_score(newdecript, english_trigrams)
    keyGuess = randomkey

    #print(holdkeyguess)
    #r =0
    while keeploop:
        randomkey2 = list(randomkey)
        #print(randomkey)
        placeholderint = random.randint(0,len(randomkey)-1)
        placeholderint2 = placeholderint
        while placeholderint2 == placeholderint:
            placeholderint2 = random.randint(0,len(randomkey)-1)

        #print(placeholderint, placeholderint2)
        holderval = randomkey[placeholderint]
        holderval2 = randomkey[placeholderint2]

        randomkey2[placeholderint] = holderval2 
        randomkey2[placeholderint2] = holderval
        randomkey2 =  "".join(randomkey2)
        #print(randomkey)
        ##Swapping 2 variables in a string
        
        #newdecript2 = sub_dec(cipher, randomkey)
        triscorendecript2 = trigram_score(sub_dec(cipher, randomkey2), english_trigrams)
        if triscorendecript2 > trigram_score(sub_dec(cipher, randomkey), english_trigrams):
            randomkey = randomkey2
        else:
            triscorendecript2 = trigram_score(sub_dec(cipher, randomkey), english_trigrams)

        newdecript2 = sub_dec(cipher, randomkey)
        #print(triscorendecript2)
        if triscorendecript2 > holdkeyguess:
            i = 0
            keyGuess = randomkey
            holdkeyguess = triscorendecript2
            newdecript = newdecript2
            #print(holdkeyguess, keyGuess)
        else:
            i +=1
        #r +=1
        if i > 1000:
            keeploop = False

    #print(r)
    return [keyGuess, newdecript]


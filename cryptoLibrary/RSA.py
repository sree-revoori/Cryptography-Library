import math 
from random import randint 

def c2i(c, alphabet):
    return alphabet.index(c)  
    
def i2c(i, alphabet):
    return alphabet[i]
    
def prepare_string(s, alphabet) :
  temp = s 
  alphaList = list(alphabet)
  sList = list(temp)
  for index in range(len(sList)) : 
    for index2 in range(len(alphaList)) : 
      if temp[index] == alphaList[index2] :
        break
      if index2 + 1 == len(alphaList) :
        sList.remove(temp[index])
    
  final = ''.join(sList)
  return final
  
  def mod_inverse(a, m): 
  for number in range(0, m) : 
    temp = (number * a) % m
    if temp == 1 :
      return number
  print("Error: No possible inverse")
  return -1
  
  def miller_rabin_test(p): 
  if (p % 2) == 0: 
    #print("Number is composite")
    return False 
  #finding d such that p-1 = 2**r * d and d is odd 
  r, d = 0, p - 1 
  while(d%2 == 0) : 
    d = d//2 
    r = r + 1
    
  d = int(d)
  
  for index in range(1, 10) : 
    x = pow(randint(2, p-1), d, p)
    if (x == p - 1 or x == 1): 
      continue
    for r in range(1, r) : 
      x = (x * x) % p
      if(x == p) : 
        return False 
      if(x == p - 1) : 
        break 
    else : 
      return False 
  return True 
  
  def totient(num) : 
  totient = 0 
  for index in range(1, num) : #works better with smaller numbers
    if math.gcd(index, num) == 1: 
      totient = totient + 1
  return totient
  
  def calc_d(n, m) : 
  #print(str(greenList))
  
  a, b, u = 0, m, 1
  while n > 0 : 
      q = b // n # integer division
      n, a, b, u = b % n, u, n, a - q * u
  if b == 1 : 
      return a % m 
      
  def rsa(num, plaintext, alphabet) : 
  lowerBound = num - 1
  upperBound = num
  print("Your choice of low bound is two to the following power: " + str(lowerBound))
  print("Your choice of upper bound is two to the following power: " + str(upperBound))
  
  randomPrime1 = randint(pow(2, lowerBound), pow(2, upperBound))
  randomPrime2 = randint(pow(2, lowerBound), pow(2, upperBound))
  
  while(miller_rabin_test(randomPrime1)) == False : 
    randomPrime1 = randint(pow(2, lowerBound), pow(2, upperBound))
  while(miller_rabin_test(randomPrime2)) == False : 
    randomPrime2 = randint(pow(2, lowerBound), pow(2, upperBound))
    
  randomPrime1 = 605626429300532055681678497537    
  randomPrime2 = 424941193007525678030099023937 
  
  print("Your two primes are: " + str(randomPrime1) + "     " + str(randomPrime2))
  
  mod = randomPrime1 * randomPrime2
  mod = 1873788469697
  
  t = (randomPrime1 - 1) * (randomPrime2 - 1)
  
  print("The mod is: " + str(mod) + " and the totient is: " + str(t))
  
  e = 65537 
  
  if math.gcd(e, t) == 1: 
    pass
  else: 
    for number in range(1, t): 
      if (math.gcd(number, t)) == 1: 
        e = number
       
  d = calc_d(e, t) 
  #d = 47805616365403815519405205326263404439887475430604730880757484858225949531178382490388932549530254407837945983592298514189056426468833752590708160947947130696188829357561671314268790654506892125449716516811334050050477076583294717565294193911015241442065845060327426130862347034780311446406894806440298287305
    
  print("e is: " + str(e) + " and d is: " + str(d) + " and if this worked, this is 1:1")
  print("Your input is: " + plaintext)
  print("Your alphabet is: " + alphabet)
  #plaintext = plaintext.upper() 
  plaintext = prepare_string(plaintext, alphabet)
  print("Prepared input is: " + plaintext) 
  
  l = len(alphabet)
  largestPower = 0 
  
  while pow(l, largestPower) < mod: 
    largestPower += 1 

  largestPower = largestPower - 1
  
  print("Alphabet length is: " + str(l) + " and the highest power is " + str(largestPower))
  
  substringList = list()
  if(len(plaintext)%largestPower == 0): 
    numObjects = len(plaintext)/largestPower
  else: 
    numObjects = (len(plaintext)/largestPower) + 1
    numOfZ = largestPower - (len(plaintext)%largestPower)
    count = 0
    while (count < numOfZ) : 
      plaintext = plaintext + "Z"
      count = count + 1
  
  numObjects = int(numObjects)

  for index in range(numObjects) : 
    string = plaintext[:largestPower]
    plaintext = plaintext[largestPower:]
    substringList.append(string)
    
  
  print("Broked into substrings: " + str(substringList))

  numList = list()
  encryptedList = list()
  decryptedList = list()
  for i in range(len(substringList)) : 
    numFinal = 0
    for index in range(largestPower): 
      string = substringList[i]
      string = string[::-1]
      num = c2i(string[index], alphabet)
      temp = pow(l, index) * num 
      numFinal = numFinal + temp

    numList.append(numFinal)
    temp = (pow(numFinal, e, mod))
    encryptedList.append(temp)
    
    print("Become numbers: " + str(numList))
    encryptedList = [723561858195, 531725110566, 772213262664, 314592630414, 642218767332, 440420036978, 1268316719157]
    print("Encoded to: " + str(encryptedList))
    
    for k in range(len(encryptedList)) : 
        temp = pow(encryptedList[k], d, mod)
        decryptedList.append(temp)
    
    
    print("Decoded to: " + str(decryptedList))
    
    totalString = ""
    for k in range(len(decryptedList)) : 
        decrypted = decryptedList[k]
        string = ""
    while(decrypted > l) : 
      string += i2c(decrypted % l, alphabet)
      decrypted = decrypted // l
    totalString += string[::-1]
    
    print("Back to text: " + totalString)

  
      




    
    #pow(message, e, m)
    
    #send someone your e, m; they encrypt it and send back to you  
    #print(totient(1873788469697))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(rsa(512, "RSA ENCRYPTION IS NAMED AFTER RON RIVEST ADI SHAMIR AND LEONARD ADLEMAN", alphabet))
    #print(calc_d(65537, 157188310234213545456623160))
    
    
  
    
    
  
  
  
  
  
  

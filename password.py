import hashlib
import re

def getHash(oneString):
	return hashlib.sha256(oneString.encode('utf-8')).hexdigest()

#s_number = "".join([chr(i) for i in range(48, 58)])
#s_lowercase = "".join([chr(i) for i in range(97, 123)])
#s_uppercase = "".join([chr(i) for i in range(65, 91)])
#
#list_special = [chr(i) for i in range(33, 127)]
#list_special.remove('"')
#list_special.remove('`')
#list_special.remove('|')
#for c in s_number + s_lowercase + s_uppercase:
#	list_special.remove(c)
#s_special = "".join(list_special)

s_number = "0123456789"
s_lowercase = "abcdefghijklmnopqrstuvwxyz"
s_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s_special = "!#$%&'()*+,-./:;<=>?@[\\]^_{}~"

characterSetAll = {}
characterSetAll["a"] = "0123456789"
characterSetAll["b"] = "abcdefghijklmnopqrstuvwxyz"
characterSetAll["c"] = "0123456789abcdefghijklmnopqrstuvwxyz"
characterSetAll["d"] = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
characterSetAll["e"] = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}()[]#:;,.?!=+-*_~@$%^"
characterSetAll["A"] = s_number
characterSetAll["B"] = s_lowercase
characterSetAll["C"] = s_number * 3 + s_lowercase
characterSetAll["D"] = s_number * 3 + s_lowercase + s_uppercase
characterSetAll["E"] = s_number * 3 + s_lowercase + s_uppercase + s_special

print("\nWelcome!")
print("If you are not familiar with this small program, you can go to the following website to read the instructions.")
print("--------------------------------------------------")
print("https://www.leizhang.me/password/")

print("--------------------------------------------------")
print("Please input key.")
key_sentence = input("-->")

print("--------------------------------------------------")
print("Please input salt.")
salt = input("-->")
print("--------------------------------------------------")

pattern = re.compile(r"^(0[4-9]|1[0-9]|20)[a-eA-E]\w+$")
if not pattern.match(salt):
	print("Error with salt! Crashed!")
	print("--------------------------------------------------")
	exit(1)

hash_string = getHash(getHash(key_sentence) + salt)

passwordLength = int(salt[0 : 2])
oneGroupLength = int(64 / passwordLength)
passwordType = salt[2]
characterSet = characterSetAll[passwordType]

password = ""
for index in range(0, passwordLength):
	beginPosition = index * oneGroupLength
	endPosition = (index + 1) * oneGroupLength
	value = int(hash_string[beginPosition : endPosition], 16)
	password += characterSet[value % len(characterSet)]

print("\nThis is your password.")
print("--------------------------------------------------")
print(password)
print("--------------------------------------------------")
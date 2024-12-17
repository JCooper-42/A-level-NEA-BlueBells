import hashlib

class UserHandling:

    def __init__(self):
        self.hashed_password = ""

    def calchash(self, string):
        hash_obj = hashlib.sha512()
        hash_obj.update(string.encode())
        hashed_password = hash_obj.hexdigest() #hex encoding for hash
        return hashed_password

    def checkhash(self):
        with open("passwords.txt", "r") as file:
            if self.hashed_password in file.read():
                return True

    def makeaccount(password):
        hash_obj = hashlib.sha512() #Insta nce of hashlib
        hash_obj.update(password.encode())
        with open("passwords.txt", "a") as file:
            file.write(hash_obj.hexdigest())
            file.write("\n") #Write all new passwords on new line


if __name__ == "__main__":
    UH = UserHandling
    UH.makeaccount("Pass") #Pass pass to makeaccount


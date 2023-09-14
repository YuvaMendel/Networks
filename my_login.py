import hashlib
import sys
import secrets
def hash_passwd(passwd):
    """

return hashed 256 string

"""
    m = hashlib.sha256()
    m.update(passwd.encode())
    return m.hexdigest()

if __name__ == '__main__':
    if len(sys.argv) == 3:#Check That input was given
        try:#try to catch exeptions at file opening
             with open(sys.argv[1], 'r') as inputFile:#Open input file to read form
                for line in inputFile:#go over input file one line at a time
                    if(len(line) > 1):
                        line = line.split(":")#split the string to a list with the username and password
                        line[0] = line[0].strip()#remove spaces at the begining and end of username
                        line[1] = line[1].strip()#remove spaces at the begining and end of password
                        with open(sys.argv[2], 'a') as outputfile:#open output file at last position
                            salt = secrets.token_hex(8)  # Generate Slat
                            outputfile.write(line[0] + ":"  + hash_passwd(line[1]+salt) + ":" + salt +"\n")#Write The username, hashed password and salt to output file #Salt was chained at the end of the password before hash
             #The Output file is built in this format- Username:Hashed password:Salt
             #now I will create the dictionary
             users = {}
             with open((sys.argv[2]),'r') as infomationFile:
                 for line in infomationFile:
                     line = line.split((":"))
                     line[2] = line[2].replace("\n", "")
                     #line[0] = username(Key) - line[1] = hashed password - line[2]= Salt
                     users[line[0]] = (line[1], line[2])#The keys are the usernames and the values is a tuple (Hashed password, Salt)
             # Dict made, now user log in
             name = input("Please enter name ")#Username input
             passwd = input("Please enter password ")#Password input
             if name in users.keys():#Check if the user name is one of the keys in the dict
                 if hash_passwd(passwd + users[name][1]) == users[name][0]:#if the input password chained with the salt is equal to the hashed password Login was successful
                     print("Login success")
                 else:
                     print("Login failed")
             else:
                 print("Login failed")
        except Exception:#If there is an exeption it is about opening files
            print("Problam at opening file")
    else:
        print("Enter 2 Files as parameters")
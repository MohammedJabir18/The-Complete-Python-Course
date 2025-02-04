import os
import socket
import requests
import json

os.system('cls')


class Web_details:
    def input_details(self):
        self.url = input("Enter the URL here => ")
        self.web = self.url.split('://')[-1].split("/")[0]
        return self.web

    def fetch_details(self, site):
        self.site = site
        self.ip = socket.gethostbyname(self.site)
        self.req = requests.get(f"https://ipinfo.io/{self.ip}/json")
        self.data = json.loads(self.req.text)

    def save_details(self):
        f = open("Details.txt", 'a')

        f.write(f'\t{self.site}\n')
        for i, j in self.data.items():
            f.write(f"{i}: {j}\n")
        f.write("\n")
        f.close()

        f = open("Details.txt", "r")
        print(f.read())


site_1 = Web_details()
domain_name = site_1.input_details()
site_1.fetch_details(domain_name)
site_1.save_details()

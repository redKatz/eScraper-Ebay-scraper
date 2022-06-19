import bs4, requests, webbrowser
from pprint import pprint


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



print("\n\n\n\n\n\n\n")
f = open("ascii.json", "r")
file_contents = f.read()
print(bcolors.OKCYAN + file_contents + "\n\nby: redKatz" + bcolors.ENDC)
f.close()
print(bcolors.WARNING+"\n\n 𝙩𝙝𝙚 𝙖𝙪𝙩𝙝𝙤𝙧 𝙖𝙨𝙨𝙪𝙢𝙚𝙨 𝙣𝙤 𝙧𝙚𝙨𝙥𝙤𝙣𝙨𝙞𝙗𝙞𝙡𝙞𝙩𝙮 𝙛𝙤𝙧 𝙝𝙤𝙬 𝙩𝙝𝙞𝙨 𝙘𝙤𝙣𝙩𝙚𝙣𝙩 𝙬𝙞𝙡𝙡 𝙗𝙚 𝙪𝙨𝙚𝙙\n======================================================================="+bcolors.ENDC)




start = str(input("\n\nStart the program? y/n: "))
if start == "n":
	exit()
elif start == "y":
	prezzo_massimo = str(input("Entetr maxium price [obbligatory]: "))

ogg_da_ce = input("Enter object to search [Compulsorily compressed of two words divided by a *+*]")

	
LINK = ("https://www.ebay.it/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw="+ogg_da_ce+"&_sacat=0&LH_TitleDesc=0&_odkw=compiter+usato&_osacat=0" + "&_udhi=" + prezzo_massimo)
PRE_LINK_ANNUNCIO = "https://www.ebay.it/itm"


response = requests.get(LINK)   
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, 'html.parser')
div_annunci = soup.find('ul', class_='srp-results srp-list clearfix')
a_annunci = div_annunci.find_all('a')
link_annunci = []


count = 0
for a_annuncio in a_annunci:
	link_annuncio = str(a_annuncio.get('href'))
	if PRE_LINK_ANNUNCIO in link_annuncio:
		link_annunci.append(link_annuncio)
pprint(link_annunci)

print("\n\n"+bcolors.OKGREEN+"All link saved on: found.txt"+bcolors.ENDC)

with open(r"found.txt", "w") as f:
	for items in link_annunci:
		f.write("%s\n\n" % link_annunci)

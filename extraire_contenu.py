from bs4 import BeautifulSoup

# Chemin vers le fichier filtré contenant le code HTML
fichier_filtre = r'C:\Users\User\Desktop\debug\aujourdhui\aujourdhui\Nouveau site\devcube\sommaire\fichier_filtre.txt'
# Fichier de sortie pour les titres et le contenu
fichier_sortie = r'C:\Users\User\Desktop\debug\aujourdhui\aujourdhui\Nouveau site\devcube\sommaire\contenu_extrait.txt'

# Ouvre le fichier filtré et lit le contenu
with open(fichier_filtre, 'r', encoding='utf-8') as infile:
    contenu_html = infile.read()

# Utilise BeautifulSoup pour parser le HTML
soup = BeautifulSoup(contenu_html, 'html.parser')

# Ouvre le fichier de sortie pour écrire les titres et le contenu
with open(fichier_sortie, 'w', encoding='utf-8') as outfile:
    # Extraire les titres h1
    outfile.write("Titres H1:\n")
    for titre in soup.find_all('h1'):
        outfile.write(titre.get_text(strip=True) + '\n')
    
    # Extraire les titres h2
    outfile.write("\nTitres H2:\n")
    for titre in soup.find_all('h2'):
        outfile.write(titre.get_text(strip=True) + '\n')
        
    # Extraire les titres h3
    outfile.write("\nTitres H3:\n")
    for titre in soup.find_all('h3'):
        outfile.write(titre.get_text(strip=True) + '\n')
        
    # Extraire le contenu des paragraphes
    outfile.write("\nContenu des Paragraphes:\n")
    for paragraphe in soup.find_all('p'):
        outfile.write(paragraphe.get_text(strip=True) + '\n')

print("Extraction des titres et contenu réussie dans contenu_extrait.txt")

# pythonProjectfinal
Projeto de final do curso de Python oferecido pelo IPEA
# objetivo
Fazer o *clip* da unidades de saude por area programtica da cidade do Rio de Janeiro.
Herdar os dados de áreas programáticas (polígono) e passar para uma base de pontos.

Visando a otimização do trabalho com mapeamento territorial. 
# código
https://github.com/ChristianeAraujo/pythonProjectFinal/blob/master/venv/.gitignore


# How to install
conda create --name py39geo python=3.9 gdal fiona shapely geopandas
### Setting PyCharm informar o caminho do .conda/envs/py39geo
conda activate py39geo

## Sugestões
1. Renomear folder com dados
2. Criar arquivo main.py
3. Organizar código em funções
4. EXCLUIR folders .idea e venv do repositório

**delete a file from tracking**
# Comando para stop versioning file a directory
git rm --cached foo.txt
**a directory**

git rm -r --cached your_folder/

5. Loop e plot conjunto?

# Resultado
(p39geo) furtado@furtado:~/Documents/Professor/Christiane_pythonProjectFinal$ git rm -r --cached .idea/

rm '.idea/.gitignore'

rm '.idea/inspectionProfiles/Project_Default.xml'

rm '.idea/inspectionProfiles/profiles_settings.xml'

rm '.idea/misc.xml'

rm '.idea/modules.xml'

rm '.idea/pythonProjectFinal.iml'

rm '.idea/vcs.xml'

(p39geo) furtado@furtado:~/Documents/Professor/Christiane_pythonProjectFinal$ git rm -r --cached venv/

rm 'venv/.gitignore'

rm 'venv/Lib/site-packages/_distutils_hack/__init__.py'

rm 'venv/Lib/site-packages/_distutils_hack/override.py'

rm 'venv/Lib/site-packages/_virtualenv.pth'

rm 'venv/Lib/site-packages/_virtualenv.py'

#Importar el sistema operativo paraponer vavegar entre esos archivos
import os
#importar el modulo parapoder copiar y pegar archivos
import shutil

from_dir = 'C:\CodingMike'
to_dir = 'C:\phyton\proyecto 102'

list_of_files  = os.listdir(from_dir)
#print(list_of_files)

# mueve los archivos de imagen de la carpeta from_dir a to_dir

#siclo forque revisacada archivo en form_dirpara ver nombre y extension de cada uno de ellos

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    #print(extension)
    if extension == "":
        continue
    if extension in ['.pdf']:
        opcion1 = from_dir +  "/" + file_name
        opcion2 = to_dir +    "/" + file_name
        
        shutil.move(opcion2,opcion1)
      
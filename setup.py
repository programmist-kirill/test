import time
import shutil

name_user = 'kirill'
path = 'test-main'
file_path = '/home/' + name_user + '/update/' + path + '/setup.list'

def one(file_path,name_user,path):

	secrets = []

	try:
	    with open(file_path, 'r') as file:
	        for line in file:
	            secret = line.rstrip('\n')
	            secrets.append(secret)

	except FileNotFoundError:
	    print(f"File '{file_path}' not found.")
	except Exception as e:
	    print(f"An error occurred: {e}")

	# Access each secret by its index
	for i, secret in enumerate(secrets):
	    secret0 = secrets[0]

	time.sleep(0.1)
	print(secret)

def two(file_path,name_user,path):
	direcory_folder = '/home/kirill/update/' + path + '/'
	source_folder = direcory_folder
    destination_folder = '/home/kirill/ip/'
    files_to_move = os.listdir(source_folder)
    for file_name in files_to_move:
    	source_file = os.path.join(source_folder, file_name)
        destination_file = os.path.join(destination_folder, file_name)
        shutil.move(source_file, destination_file)
        print("Файлы успешно перемещены.")


if os.path.exists('/home/kirill/update/test-main/install.key'):
	two(file_path,name_user,path)
else:
	one(file_path,name_user,path)
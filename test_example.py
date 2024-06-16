import time

class main_locale:
	
	name_user = 'kirill'
	path = 'test-main'
	file_path = '/home/' + name_user + '/update/' + path + '/setup.list'
	file_name_package = '/home/' + name_user + '/update/' + path + '/setup.list'
	file_name_architecture = '/home/' + name_user + '/update/' + path + '/architecture'
	file_name_version = '/home/' + name_user + '/update/' + path + '/version'
	file_name_repositories = '/home/' + name_user + '/update/' + path + '/repositories'
	file_name_size = '/home/' + name_user + '/update/' + path '/size'

	def Package(file_path,file_name_package,name_user,path):

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
		    with open('/home/' + name_user + '/update/' + path +'/package','w') as fp:
		    	fp.write(secret)
	Package(file_path,file_name_package,name_user,path)


	def architecture(file_path,file_name_architecture,name_user,path):
		secrets = []
		try:
			with open(file_name_architecture, 'r') as file:
				for line in file:
					secret = line.rstrip('\n')
					secrets.append(secret)

		except FileNotFoundError:
			print(f"File '{file_name_architecture}' not found.")
		except Exception as e:
			print(f"An error occurred: {e}")

			# Access each secret by its index
		for i, secret in enumerate(secrets):
			secret0 = secrets[0]

			time.sleep(0.1)
			with open('/home/' + name_user + '/update/' + path + '/architecture','w') as fp:
		    	fp.write(secret)
	architecture(file_path,file_name_architecture,name_user,path)

	def version(file_path,file_name_version,name_user,path):
		secrets = []
		try:
			with open(file_name_version, 'r') as file:
				for line in file:
					secret = line.rstrip('\n')
					secrets.append(secret)

		except FileNotFoundError:
			print(f"File '{file_name_version}' not found.")
		except Exception as e:
			print(f"An error occurred: {e}")

			# Access each secret by its index
		for i, secret in enumerate(secrets):
			secret0 = secrets[0]

			time.sleep(0.1)
			with open('/home/' + name_user + '/update/' + path + '/version','w') as fp:
		    	fp.write(secret)
	version(file_path,file_name_version,name_user,path)


	def repositories(file_path,file_name_repositories,name_user,path):
		secrets = []
		try:
			with open(file_name_repositories, 'r') as file:
				for line in file:
					secret = line.rstrip('\n')
					secrets.append(secret)

		except FileNotFoundError:
			print(f"File '{file_name_repositories}' not found.")
		except Exception as e:
			print(f"An error occurred: {e}")

			# Access each secret by its index
		for i, secret in enumerate(secrets):
			secret0 = secrets[0]

			time.sleep(0.1)
			with open('/home/' + name_user + '/update/' + path + '/repositories','w') as fp:
		    	fp.write(secret)
	repositories(file_path,file_name_repositories,name_user,path)

	def size(file_name_size,name_user,path):
		secrets = []
		try:
			with open(file_name_size, 'r') as file:
				for line in file:
					secret = line.rstrip('\n')
					secrets.append(secret)
		except FileNotFoundError:
			print(f"File '{file_name_size}' not found.")
		except Exception as e:
			print(f"An error eccurred: {e}")

		for i,secret in enumerate(secrets):
			secret0 = secrets[0]

			time.sleep(0.5)
			with open('/home/' + name_user + '/update/' + path + '/size','w') as fp:
				fp.write(secret)
	size(file_name_size,name_user,path)
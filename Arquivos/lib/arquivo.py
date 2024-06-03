import os

def existe_arquivo(arq):
	return os.path.exists(arq)
		
def criar_arquivo(arq):
	a=open(arq,'w')
	a.close()
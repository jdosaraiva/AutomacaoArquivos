import subprocess
import platform

def start_jboss():
    try:
        jboss_path = r'C:\Desenvolvimento\jboss-eap-6.4\bin\standalone.bat'
        if platform.system() == "Windows":
            subprocess.Popen(f'start "" "{jboss_path}"', shell=True)
        else:
            subprocess.Popen(jboss_path, shell=True)
        print("Servidor JBoss iniciado com sucesso!")
    except:
        print("Erro ao iniciar o servidor JBoss.")

def start_node_service():
    try:
        node_path = r'D:\Desenvolvimento\node\sync\server.js'
        if platform.system() == "Windows":
            subprocess.Popen(['start', 'node', node_path], shell=True)
        else:
            subprocess.Popen(['node', node_path])
        print("Serviço Node.js iniciado com sucesso!")
    except:
        print("Erro ao iniciar o serviço Node.js.")

if __name__ == "__main__":
    start_jboss()
    start_node_service()

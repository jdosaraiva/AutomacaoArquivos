import subprocess
import psutil

def stop_process_by_name(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            proc.kill()

def find_process_by_port(port):
    for proc in psutil.process_iter(['pid', 'name', 'connections']):
        for conn in proc.connections():
            if conn.laddr.port == port:
                return proc
    return None

def stop_process_by_port(port):
    proc = find_process_by_port(port)
    if proc:
        print(f"Processo escutando na porta {port} encontrado. PID: {proc.pid}")
        proc.kill()
        print(f"Processo finalizado com sucesso.")
    else:
        print(f"Nenhum processo encontrado escutando na porta {port}.")

def stop_node_service():
    stop_process_by_name('node.exe')

def stop_jboss():
    try:
        subprocess.run([r'C:\Desenvolvimento\jboss-eap-6.4\bin\jboss-cli.bat', '--connect', 'command=:shutdown'], check=True, stdin=subprocess.PIPE)
        print("Servidor JBoss desligado com sucesso!")
    except subprocess.CalledProcessError:
        print("Erro ao desligar o servidor JBoss.")

if __name__ == "__main__":
    stop_node_service()
    stop_jboss()

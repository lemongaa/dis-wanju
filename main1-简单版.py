import subprocess
import threading
import socket
import time

def start_script(script_path):
    # ����ִ������
    cmd = f"nohup chmod +x {script_path} && ./{script_path} &"
    
    try:
        # ִ������
        subprocess.Popen(cmd, shell=True)
        print("�ű����ں�̨����")
        
    except Exception as e:
        print("�����ű�ʱ����", str(e))

def start_listening(port):
    # �����׽���
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # �󶨵�ָ���Ķ˿�
        server_socket.bind(('0.0.0.0', port))
        
        # ��ʼ��������
        server_socket.listen(1)
        print("���ڼ����˿�", port)
        
        while True:
            # �ȴ��ͻ�������
            client_socket, address = server_socket.accept()
            print("���յ�����", address, "������")
            
            # �������ݸ��ͻ���
            response = b"hello world"
            client_socket.sendall(response)
            
            # �ر���ͻ��˵�����
            client_socket.close()
            
    except Exception as e:
        print("��������", str(e))
        
    finally:
        # �رշ������׽���
        server_socket.close()

# �����ű���������Ϊ��̨��������
start_script('./start.sh')

# ��������
listening_thread = threading.Thread(target=start_listening, args=(10027,))
listening_thread.start()

# ��ؽű�����
script_path = './start.sh'
monitoring_cmd = f"pgrep -f {script_path}"
while True:
    process = subprocess.Popen(monitoring_cmd, shell=True, stdout=subprocess.PIPE)
    output = process.stdout.read()
    if output:
        print("�ű�����������")
    else:
        print("�ű�����δ�ҵ������������ű�")
        start_script(script_path)
    time.sleep(10)

import subprocess
from multiprocessing import Process

def server():
  subprocess.run("python ./server/echo-server.py", shell=True)
  
def client():
  subprocess.run("python ./client/echo-client.py", shell=True)


if __name__ == '__main__':
  processes = []

  p = Process(target=server)
  p.start()
  processes.append(p)

  p = Process(target=client)
  p.start()
  processes.append(p)

  for p in processes:
    p.join()
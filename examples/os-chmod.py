import os
import stat

os.chmod('/etc/passwd', 0777)
os.chmod('/etc/passwd', 0227)
os.chmod('/etc/passwd', 07)
os.chmod('/etc/passwd', 0664)
os.chmod('/etc/passwd', 0777)
os.chmod('/etc/passwd', 0777)
os.chmod('/etc/passwd', 0777)
os.chmod('/etc/passwd', 0777)
os.chmod('~/.bashrc', 511)
os.chmod('/etc/hosts', 0o777)
os.chmod('/etc/hosts', 0o777)
os.chmod('/tmp/oh_hai', 0x1ff)
os.chmod('/etc/passwd', stat.S_IRWXU)

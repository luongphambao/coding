import subprocess
import re
result = subprocess.check_output('curl -F"SoBaoDanh=02000146" diemthi.hcm.edu.vn/Home/Show')
#print(result)
convertResults =str(result)
s1=convertResults.replace('\\n', '')
s1=s1.replace('\\r','')
#print(s1)
s2=re.findall(r"[-+]?\d*\.\d+|\d+", s1)
s3=[i for i in s2 if i.find('.')>=0]
print(s3)
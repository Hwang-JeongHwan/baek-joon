import base64
#from base64 import b64decode로 해도 됨
#별도 라이브러리 사용하는 문제
 
T = int(input())
for test_case in range(1, T + 1):
    print('#'+str(test_case), base64.b64decode(input()).decode("UTF-8"))
    #print('#'+str(test_case), b64decode(input()).decode("UTF-8"))
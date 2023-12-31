# 웨어러블 디바이스 3D 시각화

개발 환경: Unity, python3, flask

## 개발환경 설치
 - flask 웹 프레임워크 사용
 
```
pip install flask
```

## 실행

로컬 테스트: web/app.py 파일 실행하고, 웹브라우져에서 http://127.0.0.1:5053 접속

```
python3 web/app.py

 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5053
```

## 웨어러블 디바이스 3D 시각화 서비스 주소

https://wde.baribarilab.com/visualization/

## 인터페이스

- 입력: 휴먼 모델 조인트
- 출력:

휴먼 모델 조인트 예시 


```
"j_chest_neck_joint1",                                                                                                     
"j_chest_neck_joint2",                                                                                                     
"j_chest_neck_joint3",                                                                                                     
"j_root_right_hip_joint1",                                                                                                 
"j_root_right_hip_joint2",                                                                                                 
"j_root_right_hip_joint3",                                                                                                 
"j_right_knee",                                                                                                            
"j_right_knee_right_ankle_joint1",                                                                                         
"j_right_knee_right_ankle_joint2",                                                                                         
"j_right_knee_right_ankle_joint3",                                                                                         
"j_chest_right_shoulder_joint1",                                                                                           
"j_chest_right_shoulder_joint2",                                                                                           
"j_chest_right_shoulder_joint3",                                                                                           
"j_right_elbow",                                                                                                           
"j_root_left_hip_joint1",                                                                                                  
"j_root_left_hip_joint2",                                                                                                  
"j_root_left_hip_joint3",                                                                                                  
"j_left_knee",                                                                                                             
"j_left_knee_left_ankle_joint1",                                                                                           
"j_left_knee_left_ankle_joint2",                                                                                           
"j_left_knee_left_ankle_joint3",                                                                                           
"j_chest_left_shoulder_joint1",                                                                                            
"j_chest_left_shoulder_joint2",                                                                                            
"j_chest_left_shoulder_joint3",                                                                                            
"j_left_elbow"          

0.0083330004,       -0.6199835200,        0.8662823200,       -0.1306245800,        0.6734501864,        0.0120737523,       -0.7390933410,        0.0077526900,        0.9953379246,       -0.0009718044,       -0.0020582775,       -0.0964221705,        0.9928368354,       -0.0003541672,        0.0282065367,       -0.1161003194,        0.9696291470,       -0.0334654647,       -0.0215958837,        0.2413151421,       -0.8441721262,        0.9983959013,       -0.0183369033,       -0.0035412139,        0.0534494347,        0.9760539729,       -0.0855567580,        0.1945358019,       -0.0464166441,        0.3289945640,        0.9989023343,       -0.0128185182,        0.0011344677,       -0.0450391519,       -0.1124410917,        0.9943610880,       -0.0173223798,       -0.0948270190,        0.0442017901,        0.9474308766,        0.1744457755,       -0.2622227473,        0.0564148594,        0.3519630970
0.0083330004,       -0.6210554000,        0.8656168400,       -0.1239723200,        0.6733822621,        0.0122347500,       -0.7391562264,        0.0073968214,        0.9954535243,       -0.0008676275,       -0.0026188403,       -0.0952085598,        0.9932737933,       -0.0005581508,        0.0292266055,       -0.1120386792,        0.9696833118,       -0.0336440140,       -0.0199325563,        0.2412157712,       -0.7915364866,        0.9986293035,       -0.0171136100,       -0.0026021000,        0.0493950167,        0.9755233933,       -0.0839376721,        0.1971697366,       -0.0493221170,        0.3276314620,        0.9987184739,       -0.0125077070,        0.0008735873,       -0.0490326828,       -0.1121583485,        0.9943148212,       -0.0168544626,       -0.0939597768,        0.0471754570,        0.9468077182,        0.1778701032,       -0.2621490491,        0.0565265173,        0.3634683075
```



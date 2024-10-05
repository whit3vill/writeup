![image](https://github.com/user-attachments/assets/d92acaba-ed05-4c1e-b31c-fd9a3c025df4)
인자를 주었을 때, 파일의 텍스트를 암호화해주는 프로그램으로 추정된다.

코드를 자세히 살펴보자.
![image](https://github.com/user-attachments/assets/039db7f2-3b05-4c43-8c2e-051230591036)
먼저 washing_machine이라는 함수에 input이 들어간다.
![image](https://github.com/user-attachments/assets/0faf7394-e861-4803-966e-8729b3ce6d10)
첫번째 for문은 a[i] ^= a[i-1] 형식의 xor chain을 만드는 부분이고,
두번째 for문은 가운데를 중심으로 바이트를 대칭시키는 부분인데, 문자열 순서를 뒤집는다고 이해해도 무방하다.
![image](https://github.com/user-attachments/assets/29fa1c2d-6016-42a0-b023-600b6aa8b977)
이후에 main함수에 2중 for문으로 input 문자열을 확장시킨다.
앞의 3바이트는 0, 1, input[i]이 저장되고,
140바이트를 특정 규칙에 따라 저장하고,
마지막 3바이트는 4, 1, i를 저장한다.
이렇게 inputLen만큼 반복해서 v20배열을 채워넣는다.
이렇게 확장한 v20배열은 runnnn함수로 간다.
![image](https://github.com/user-attachments/assets/ad33c402-bf29-4206-ab40-ed3cf178543d)
배열을 한글자씩 읽어서 case문으로 처리를 하는 방식인데, 
case를 하나하나 해석하다보니 동작하는 방식이 어셈블리와 유사했다.

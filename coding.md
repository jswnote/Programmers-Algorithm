# 여러가지 코딩할 때
입력과 출력 꼭 확인하기.

# 그냥 외워. 
```
list(map(int,input().split()))
```


## split 함수. 
문자열.split(seq = '구분자', maxsplit = 분할횟수).  
문자열을 일정한 규칙으로 잘라서 리스트로 만들어주는 함수.
seq default 값: 띄어쓰기, 엔터
maxsplit: 분할횟수

## argc, argv. 
```
int main(int argc, char* argv[])
```
보통 위와 같이 존재.

int argc는 전달된 인자의 개수.
실행파일 test.exe가 hello 123 hi 이런식으로 입력을 했다면,   
실행파일까지 인자의 개수가 총 4개임. 즉, argc = 4.

int* argv[] = {"test.exe", "hello", "123", "hi"} (숫자도 문자열로 인식)
이렇게 인자로 전달한 내용이 저장되는 문자(포인트)열 배열.

## 예외처리
```
try:
    코드1
except:
    코드2

```
코드1에 에러가 발생한다면, 코드2를 실행시킵니다. 코드1에서 어떠한 에러가 발생하더라도 에러를 발생시키지않고, (즉 프로그램을 종료시키지 않고) 코드2를 실행시킵니다.


## 2차원 리스트 만들기
```
a = []
m, n = map(int,input().split())

for i in range(m):
    line = []
    for j in range(n):
        line.append(int(input()))
    
    a.append(line)
        
        
print(a)
```

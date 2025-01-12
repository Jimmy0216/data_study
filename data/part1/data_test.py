import pandas as pd

# 데이터 프레임 생성
data = {
    '이름': ['영희', '철수', '순이'],
    '나이': [30, 40, 50]
}

df = pd.DataFrame(data)

# 데이터 프레임 출력
print(df)

# 나이 변수의 평균 계산
average_age = df['나이'].mean()

# 평균 출력
print("나이의 평균:", average_age)
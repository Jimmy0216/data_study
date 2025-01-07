import pandas as pd
import matplotlib.pyplot as plt

# 데이터 프레임 생성 (10명, 성별 포함)
data = {
    '이름': ['영희', '철수', '순이', '민수', '지현', '상훈', '하늘', '소영', '준호', '수빈'],
    '나이': [30, 40, 50, 25, 35, 45, 55, 28, 38, 48],
    '성별': ['여', '남', '여', '남', '여', '남', '여', '여', '남', '여']
}

df = pd.DataFrame(data)

# 데이터 프레임 출력
print(df)

# 성별에 따른 나이 평균 계산
average_age_by_gender = df.groupby('성별')['나이'].mean()

# 막대 그래프 생성
average_age_by_gender.plot(kind='bar', color=['blue', 'pink'])

# 그래프 제목 및 레이블 설정 (영문으로 변경)
plt.title('Average Age by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Age')

# 그래프 출력
plt.show()
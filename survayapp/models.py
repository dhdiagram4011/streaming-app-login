from django.db import models

# 로그인 후 설문조사 모델링
# 설문조사 목록

class Survay_name(models.Model):
    name = models.CharField(max_length=100)

class Survay_email(models.Model):
    email= models.EmailField(max_length=100)

class Survay_01(models.Model):
    question_01 = models.IntegerField()

class Survay_02(models.Model): 
    question_02 = models.IntegerField()

class Survay_03(models.Model):
    question_03 = models.CharField(max_length=8)

class Survay_04(models.Model):
    question_04 = models.IntegerField()

class Survay_05(models.Model):
    question_05 = models.IntegerField()

class Survay_06(models.Model):
    question_06 = models.IntegerField()

class Survay_07(models.Model):
    question_07 = models.CharField(max_length=10)

class Survay_08(models.Model):
    question_08 = models.CharField(max_length=10)

class Survay_09(models.Model):
    question_09 = models.CharField(max_length=10)

"""
1. 이름(실명 말고 개인이 입력하고 싶은 아이디) /name
2. 이메일 /email
3. 나의 휴대폰에 저장되어 있는 전화번호 갯수는?(친구만) /survay_01
4. 정말로 나의 속마음과 개인적인 부분까지 터놓고 말할 수 있는 친구는 몇명? /survay_02
5. 내 전화번호에는 ()명의 친구 연락처가 있으며 이중에 진짜 자주 연락하고 만나는 친구는 ()명이다.  /survay_03
6. 나는 하루에 몇잔의 커피를 마신다? /survay_04
7. 나는 평일에 업무적인 약속 말고 개인적인 약속이 몇개가 있다? /survay_05
8. 나는 주말에 업무적인 약속 말고 개인적인 약속이 몇개가 있다? /survay_06
9. 내가 직업을 선택하는 기준은?(입력예시 - 연봉, 미래전망) /survay_07
10. 나는 내가 자주가는 단골카페가 있다 (입력예시 - 있다, 없다, 자주가는편은 아니지만 있다) /survay_08
11. 나는 사람을 볼적에 이걸 가장 먼저 보고 중요하게 생각한다 (입력예시 - 외모, 성격, 첫인상) /survay_09
"""

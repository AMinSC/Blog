# Django-blog
Django learning with blog

## 1. 목적
- 요구사항 모두 구현해보기
    - ~~0 단계~~
    - ~~1 단계~~
    - ~~2 단계~~
    - 3 단계
        - ~~프로필 추가 및 수정~~
        - 댓글 기능(Create, Delete, Re Comments)
        - 배포(AWS Lightsail, nginx, uwsgi, gunicorn)
    - django-bootstrap5로 Templates적용

## 2. 개발환경

- Python 3.10.11
- Django 4.2.3
- Pillow 10.0.0

그 외 자세한 버전은 requirements.txt를 참고 부탁드리겠습니다.

## 3. 폴더 트리
```
├─.vscode
├─accounts
│  ├─migrations
│  │  └─__pycache__
│  ├─templates
│  │  └─accounts
│  └─__pycache__
├─blog
│  └─__pycache__
├─media
├─posts
│  ├─migrations
│  │  └─__pycache__
│  ├─templates
│  │  └─posts
│  └─__pycache__
├─static
│  ├─css
│  └─img
├─staticfiles
│  └─admin
│      ├─css
│      │  └─vendor
│      │      └─select2
│      ├─img
│      │  └─gis
│      └─js
│          ├─admin
│          └─vendor
│              ├─jquery
│              ├─select2
│              │  └─i18n
│              └─xregexp
├─templates
└─venv
```

## 4. ERD
![ERD](/asset/ERD.png)

- Post
    - cetegory
        - category_choices = (('일반', '일반'), ('공지사항', '공지사항'))
        - category = models.CharField(max_length=20, choices=category_choices)
        - ![settings](/asset/6.png)
    - created_at : (auto_now_add=True)
    - updated_at : (auto_now=True)
    - hit
        ```python
        def update_counter(self):
            self.hit = self.hit + 1
            self.save()
        ```

        `{{ post.update_counter }}`

    - img (Pillow)
        - models.py : (upload_to="")
            ![settings](/asset/post_img.png)

        - urls : 기존 urlpatterns에서 static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        
        - html : (form태그 속성중 enctype="multipart/form-data")
            | type | 내용 |
            |:---:|:------:|
            |`application/x-www-form-urlencoded`|default값으로 모든 문자가 전송되기 전에 인코딩됨(공백은 +, 특수문자는 ASCII HEX)|
            |`multipart/form-data`|바이너리 데이터를 효율적으로 전송할 수 있으나 웹에서 많이 사용되는 텍스트로만 이루어진 POST 전송은 오히려 MIME 헤더가 추가되기 때문에 오버 헤드가 발생|
            |`text/plain`|공백과 일반 텍스트는 가능하지만, 특수문자는 인코딩되지 않아 현재는 거의 사용하지 않음|

- User
    - username : (unique=True)
    - nickname, email : (blank=True, null=True)
    - created_at : (auto_now_add=True)
    - updated_at : (auto_now=True)

- Comment


## 5. 메인

1. 블로그 리스트(닉네임 변경전 아이디 노출)
    ![settings](/asset/1.png)

2. 닉네임 설정 후 닉네임 노출
    ![settings](/asset/2.png)

3. 이미지 노출 및 조회수
    ![settings](/asset/3.png)

4. 로그인
    ![settings](/asset/4.png)

5. 회원정보 수정
    ![settings](/asset/5.png)

## 6. 개선사항
- 댓글 작성(대댓글)
- 카테고리 고도화
    - 일반, 공지사항 -> 주제별 카테고리 (예) 음악, 영화 등)
- 글 작성 시, 폼 변경 및 이미지 처리 개선

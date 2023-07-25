# Django-blog
Django learning with blog


## 1. 목적
- 간단한 블로그
    - 회원가입, 로그인, 로그아웃
        - 회원정보 수정, 비밀번호 변경
    - 게시글 CRUD 기능
        - 인증(Authorization)
            - 본인 작성 게시판, 댓글만 수정 및 삭제 가능
        - 간단한 조회수 기능
        - 이미지 로드
        - 댓글, 대댓글 CRD
    - AWS Lightsail로 배포


## 2. 개발환경

- Python 3.10.11
- Django 4.2.3
- Pillow 10.0.0

그 외 자세한 버전은 requirements.txt를 참고 부탁드리겠습니다.


## 3. 배포환경

- AWS Lightsail(ubuntu 22.04 LTS)
    - Nginx 1.18.0
    - uWSGI 2.0.21

- [배포사이트](http://3.39.109.55)
    - 아직 도메인주소를 구매하지 않아, 포트번호로 되어 있습니다.


## 4. 폴더 트리
```
.
├── 8000
├── README.md
├── accounts
│   ├── migrations
│   ├── models.py
│   ├── static
│   └── templates
├── asset
├── blog
├── db.sqlite3
├── manage.py
├── media
├── posts
│   ├── migrations
│   ├── static
│   └── templates
├── requirements.txt
├── static
│   ├── admin
│   │   ├── css
│   │   ├── img
│   │   └── js
│   ├── assets
│   ├── css
│   ├── images
│   └── img
├── staticfile
│   ├── admin
│   │   ├── css
│   │   ├── img
│   │   └── js
│   ├── assets
│   ├── css
│   ├── images
│   └── img
├── staticfiles
│   └── admin
│       ├── css
│       ├── img
│       └── js
├── templates
└── venv
```

## 5. ERD
![ERD](/asset/ERD.png)

- Post
    - cetegory
        - category_choices = (('일반', '일반'), ('공지사항', '공지사항'))
        - category = models.CharField(max_length=20, choices=category_choices)
        - ![settings](/asset/db-table.png)
    - created_at : (auto_now_add=True)
    - updated_at : (auto_now=True)
    - hit
        ```python
        def update_counter(self):
            self.hit = self.hit + 1
            self.save()
        ```

        ~~`{{ post.update_counter }}`~~
        view클래스에서 메서드 호출해주기

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
    - post, writer : ForeignKey

- ReComment
    - parent : ForeignKey


## 6. 구현

1. 블로그 메인 화면
    ![settings](/asset/1.png)

2. 로그인
    ![settings](/asset/2.png)

3. 블로그 리스트
    ![settings](/asset/3.png)

4. 회원정보 수정(닉네임, 이메일)
    ![settings](/asset/4.png)

5. 회원정보 수정(비밀번호)
    ![settings](/asset/5.png)

6. 글작성(이미지)
    ![settings](/asset/6.png)

7. 게시글 상세 페이지
    ![settings](/asset/7.png)

## 7. 개선사항
- ~~댓글 작성(대댓글)~~
    - 꾸며주기(게시판 간격 등)
    - ~~blog:list에서 post당 댓글 갯수 표시해주기~~
        - 블로그 리스트에서 댓글 개수는 확인, 대댓글 개수는 확인 불가
- 블로그 리스트 간격 조정
- 카테고리 고도화
    - 일반, 공지사항 -> 주제별 카테고리 (예) 음악, 영화 등)

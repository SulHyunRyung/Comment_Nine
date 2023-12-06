---
title: 항해99 미니 프로젝트 에세이
author: eunchaelyu
date: 2023-12-06 10:00:00 +09:00
categories: [항해99, 미니 프로젝트]
tags: [항해99, 미니 프로젝트]
pin: true
img_path: '/posts/20231206'
---


# Mini Project Essay

## Team Time Table
  본 과정 시작하기 전에 조원들이랑 스터디 그라운드 룰을 정한다
- 매일 9시 출석체크 후 각자 할 일 브리핑
- 12시 30분까지 각자 할 일 진행 (카메라 켜두고)
- 12시 30분 오전 한 일 브리핑
- 1시~2시 점심시간
- 2시 오후 할 일 브리핑
- 5시 30분까지 각자 할 일 진행 (카메라 켜두고)
- 5시 30분 오후 한 일 브리핑
- 6시~7시 저녁시간
- 7시 프로젝트 합치기
- 9시 오늘 회고 후 해산
- **작업화면 공유하고 작업하기**


## What to do 
: 한줄 요약
: ``"COMMENTNINE"``
: [코드 리뷰 블로그 제작]
: 다양한 기능 구현하는 코드를 글로 작성하고 그에 대한 코드를 리뷰하는 댓글을 달 수 있는 페이지   

  
## 초기 와이어 프레임
![image](https://github.com/eunchaelyu/eunchaelyu.github.io/assets/119996957/20340add-65c4-4dbd-a892-34a4c4e614cd)

## 페이지 구성 및 기능 & 와이어 프레임
### 1. 로그인(아이디, 비밀번호) [login.html] ->하영님   
**구성**
> ‘/login’으로 ‘login.html’ 접속  
> ID, PW - input 필요  
> 로그인, 회원 가입 - button 필요

**기능**
> 로그인 상태인지 체크하는 session 필요  
> 회원 가입 페이지로 가는 버튼  
> 로그인 시도 → DB 데이터와 비교  
> 정보 일치할 경우 ‘조회’ 페이지로 이동

![image](https://github.com/eunchaelyu/eunchaelyu.github.io/assets/119996957/11835523-cf5d-4700-88af-a152bf834773)



### 2. 회원가입(아이디 중복확인, 아이디, 비밀번호) [join.html] ->동현님  
**구성**
> 아이디 중복 체크 - button 필요    
> 아이디, 비밀번호, 비밀번호 - input 필요    
> 회원가입 완료 - button 필요    

**기능**
> 아이디 중복 체크 - DB 데이터와 비교 필요    
> 회원가입 정보(아이디, 비밀번호) DB 테이블에 등록    
> 아이디 중복없이 회원가입 완료 후 Alert 창 띄우고 '로그인' 페이지로 이동

![image](https://github.com/eunchaelyu/eunchaelyu.github.io/assets/119996957/087eea49-7997-48e3-87e3-f14b40df1f65)

    

### 3. 전체 게시글 조회[index.html] ->동우님  
**구성**
> DB에서 데이터를 가져옴(제목,작성자,게시글,날짜) - session 체크 필요    

**기능** 
> 게시판에 정보를 정확하게 보냄 - 게시글 링크 정보 전달    
> 사용자의 정보를 DB에서 확인 후 게시글 작성페이지로 전달 - session 체크 필요

![image](https://github.com/eunchaelyu/eunchaelyu.github.io/assets/119996957/8558cd6c-4dc6-446a-9686-d5950d439625)



### 4. 해당 게시글/댓글 조회[post-view.html] -> 동우님, 은채님  
**구성**
> DB에서 데이터를 가져옴(게시글 내용, 댓글 내용, 타임) - session 체크 필요    
> 댓글 내용 담기 - input 필요    

**기능**
> 게시글 수정 - button 필요    
> 댓글 작성 완료 - button 필요

![image](https://github.com/eunchaelyu/eunchaelyu.github.io/assets/119996957/955dac7a-3507-426b-b0e9-50d51db6842e)


   
### 5. 게시글 작성 기능 [post-add.html] -> 대일님    
**구성**
> 게시글 내용 담기 - form 필요    
> DB에서 데이터를 받아옴(게시글 내용,타임) - session 체크 필요    

**기능**
> 게시글 작성 완료 - button 필요

![image](https://github.com/eunchaelyu/eunchaelyu.github.io/assets/119996957/7bd43d9b-333b-48cf-8148-346109eafddd)

 

### 6. 게시글 수정/삭제 기능 [post-edit.html] -> 대일님 
**구성**
> DB에서 데이터를 가져옴(게시글 내용) - session 체크 필요    

**기능**
> 게시글 내용 담기 - form 필요    
> 게시글 수정 완료 - button 필요    
> 게시글 삭제 - button 필요

![image](https://github.com/eunchaelyu/eunchaelyu.github.io/assets/119996957/5dbc8209-bfed-43cf-909b-4b67ef36bc7c)

   

### 7. 댓글 수정/삭제 기능 [comment-edit.html] -> 은채님  
**구성**
> DB에서 데이터를 가져옴(댓글 내용) - session 체크 필요    

**기능**
> 댓글 내용 담기 - form 필요    
> 댓글 수정 완료 - button 필요    
> 댓글 삭제 - button 필요

![image](https://github.com/eunchaelyu/eunchaelyu.github.io/assets/119996957/e072e80e-61b4-4dfb-b30c-192b08ab2de4)




## API(개발해야 하는 기능들)-수정 전

|기능|Method|URL|Request|Response|
| :-----------: | :-----------: | :-----------: | :----------- | :----------- |
| 로그인 정보 체크 | GET | /login  |  |      
| 로그인 시도 | POST | /login | {'user_id'=user_id,'user_password'=user_password} | 로그인 정보 |
| 회원가입 페이지 | GET | /join | {'user_id'=user_id,'user_password'=user_password} | 로그인 정보 |
| 회원가입 시도 | POST | /join | {'user_id'=user_id,'user_password'=user_password} | 로그인 정보 |
| 전체 게시글 조회 | GET | /index | {'user_id'=user_id, 'post_title'=post_title, 'time_stamp'=time_stamp} | 로그인 정보, 게시글 제목, 타임스탬프 |
| 해당 게시글 조회 | GET | /post-view | {'user_id'=user_id, 'time_stamp'=time_stamp, 'post_title'=post_title, 'post_content'=post_content, 'comment_content'=comment_content } | 로그인 정보, 게시글 제목, 게시글 내용, 타임스탬프, 댓글 내용 |
| 게시글 작성 | POST | /post-add | {'user_id'=user_id, 'time_stamp'=time_stamp, 'post_title'=post_title, 'post_content'=post_content } | 사용자 정보, 타임스탬프, 게시글 제목, 게시글 내용 |
| 게시글 수정/삭제 | POST | /post-edit | {'user_id'=user_id, 'post_title'=post_title, 'post_content'=post_content} | 사용자 정보, 게시글 제목, 게시글 내용 |
| 댓글 수정/삭제 | POST | /comment-edit | {'user_id'=user_id,'comment_content'=comment_content } | 사용자 정보, 댓글 내용 |


##기술 매니저님 피드백
> render_template: html을 서버에서 그려서 만들어주는 것
> 회원가입 페이지를 api 로 보내준다고 하면 다른 로그인, 게시글, 댓글 페이지도 api를 통해 render_template을 사용해야 한다
> GET/api/login과 GET/login로 구분해줘야 한다
> 엔드 포인트에 변수를 넣어서 사용할 수 있다 (/post/아이디)
> RESTFUL API
> GET 따로 POST 따로 분리해서 적는 게 가시성이 좋음


## API(개발해야 하는 기능들)-수정 후
|기능|Method|URL|Request|Response|
| :-----------: | :-----------: | :-----------: | :----------- | :----------- |
| 로그인 페이지 | GET | /login  |  |      
| 로그인 시도 | POST | /api/login | {'user_id'=user_id,'user_password'=user_password} | 로그인 정보 |

| 회원가입 페이지 | GET | /join | {'user_id'=user_id,'user_password'=user_password} | 로그인 정보 |
| 회원가입 시도 | POST | /api/join | {'user_id'=user_id,'user_password'=user_password} | 로그인 정보 |

| 전체 게시글 조회 | GET | /index | {'user_id'=user_id, 'post_title'=post_title, 'time_stamp'=time_stamp} | 로그인 정보, 게시글 제목, 타임스탬프 |
| 해당 게시글 조회 | GET | /post-view | {'user_id'=user_id, 'time_stamp'=time_stamp, 'post_title'=post_title, 'post_content'=post_content, 'comment_content'=comment_content } | 로그인 정보, 게시글 제목, 게시글 내용, 타임스탬프, 댓글 내용 |

| 게시글 작성 페이지 | GET | /post-add |  |   
| 게시글 작성 | POST | /api/post-add | {'user_id'=user_id, 'time_stamp'=time_stamp, 'post_title'=post_title, 'post_content'=post_content } | 사용자 정보, 타임스탬프, 게시글 제목, 게시글 내용 |

| 게시글 수정 페이지 | GET | /post-edit  |  |   
| 게시글 수정 | PUT | /api/post-edit | {'user_id'=user_id, 'post_title'=post_title, 'post_content'=post_content} | 사용자 정보, 게시글 제목, 게시글 내용 |
| 게시글 삭제 | DELETE | /api/post-edit | {'user_id'=user_id, 'post_title'=post_title, 'post_content'=post_content} | 사용자 정보, 게시글 제목, 게시글 내용 |

| 댓글 수정 페이지 | GET | /comment-edit  |  |   
| 댓글 수정 | PUT | /api/comment-edit | {'user_id'=user_id,'comment_content'=comment_content } | 사용자 정보, 댓글 내용 |
| 댓글 삭제 | DELETE | /api/comment-edit | {'user_id'=user_id,'comment_content'=comment_content } | 사용자 정보, 댓글 내용 |


## public github repo 주소
[Comment-Nine](https://github.com/SulHyunRyung/Commnet_Nine.git)

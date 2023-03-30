# pythonRPG_team
 
#### 라운드제도 
  - battle함수와 round함수 이용 (function.py에 두 함수 작성함)
    battle : 공격을 주고받음(채연님이 작성해주신 전투 while문을 그대로 함수로 만듦)
  - round : play 라운드에 따라 게임이 시작됨. round를 변수로 monster의 능력치가 조정되고 몬스터가 생성됨

  - round 5까지만 적용하였는데 더 필요하면 추가 가능

  ** 수정해야하는 부분 **
  1. 라운드 별 몬스터 능력치 수정필요
  2. 라운드 설명 추가 필요(스토리 추가)
  3. 몬스터 도감 수정
  4. 라운드 끝나면 플레이어 HP초기화 시킬지 말지 고민해보기

### 상점
  - store함수와 store_items함수 이용 (function.py에 제일 끝에 두 함수 작성함)
  - character init함수에 point 변수 추가
  - 몬스터를 공격 할 때 마다 attack에서 damage*0.4에 해당하는 point획득
  - 라운드가 끝날 때 마다 상점에 들어가서 포인트 확인 및 아이템 구매 가능 


# 가위 바위 보 게임
# 요구 사항
# 1. 플레이 할 게임 횟수를 입력 받는다 (5회 이내) -> 5회 이상(6) 입력 시 재입력 받아야 함
# 2. 가위 바위 보 게임 진행 결과에 따라 "gameResult"에 결과 값을 기록해 둔다
# 3. 현재 게임이 몇 회차인지 출력하고 입력을 받으면 입력 값의 공백을 제거한 다음 컴퓨터의 랜덤한 선택과 비교하여 결과를 함께 출력한다.
#    [결과 값은 다음 양식에 맞게 출력]
# -> (1/3)회차 유저:보, 컴퓨터:가위 [결과]:컴퓨터 승리
# 4. 정해진 게임 횟수가 종료 되면 게임 종료 메시지와 함께 유저 기준 총 몇판 몇승 했는지 출력한다.
# -> 총 3판 1승 2패
# BASIC END

# BASIC PLUS
# 4. 게임이 끝나면 유저가 원하는 게임 횟차의 상세한 게임 결과를 검색할 수 있는 기능을 제공 한다.
# 예) 유저가 1입력 -> (1/3)회차 유저:보, 컴퓨터:가위 [결과]:컴퓨터 승리
# 5. 게임 결과는 유저가 "q"를 입력할 때까지 반복해서 결과를 검색할 수 있도록 프로그램을 유지한다.
# 6. 유저가 "q"를 입력하면 프로그램 종료

import random


class RPSGame:
    def __init__(self):
        # 멤버 변수 선언 및 초기 세팅5
        self.gameCount = 0
        self.gameResult = {}
        # print(type(self.gameResult))
    ''' 
    def play_game(self):
        # 게임 진행 로직 함수
        global count
        count = input("게임 횟수 입력:")
        try:
            if int(count) == 0:
                print("0 이상 을 입력하세요")
                self.play_game()
            elif int(count) <= 5:
                print("게임수 : ", count)
                self.start_game()
            else:
                print('"5"이하만 입력가능합니다.')
                return self.play_game()
        except ValueError:
            print('5이하의 "숫자"만 입력가능합니다. ')
            return self.play_game()
    '''
 
        
    def start_game(self):
       game = ['가위','바위','보']
       game_result  = ['승','패','비김']
       
       game_cnt = 0
       user_win = 0
       com_win = 0
       # overCount = (int(count)/2 + 1)
       
       user_choice = input("가위, 바위, 보 입력:")
       if not user_choice in game:
            print("정확히 입력하세요")
            self.start_game()
        
        
        
                
                    
               
            
       
       
       
       
       ''' # (n/n) 회차
       while True:
        if game_cnt < int(count):
            print(game_cnt+1,"/",int(count),"회차")
            game_cnt +=1
            if game_cnt == int(count):
                break
       '''
        #for i in range(int(count)):
            #print(i)
    
    def show_result(self, number):
        # 게임 결과 검색 함수
        return self.gameResult[number]


if __name__ == "__main__":
    game = RPSGame()
    # game.play_game()
    game.start_game()
    # number = input("게임 결과 검색:")

    #print(game.show_result(int(number)))


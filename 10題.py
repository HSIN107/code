

import random


# ============================================================================
# 第1題：選舉投票程式
# ============================================================================
print("【第1題】選舉投票程式")
print("-" * 70)

def question_1():
    """
    兩位候選人：No.1 Nami、No.2 Chopper
    輸入5張選票，統計得票並判斷當選人
    """
    # 初始化票數
    nami_votes = 0
    chopper_votes = 0
    null_votes = 0
    
    # 投票5次
    for i in range(5):
        vote = int(input())
        
        if vote == 1:
            nami_votes += 1
        elif vote == 2:
            chopper_votes += 1
        else:
            null_votes += 1
        
        # 每次投票後顯示目前票數
        print(f"Total votes of No.1: Nami =  {nami_votes}")
        print(f"Total votes of No.2: Chopper =  {chopper_votes}")
        print(f"Total null votes =  {null_votes}")
    
    # 判斷當選人
    if nami_votes > chopper_votes:
        print("=> No.1 Nami won the election.")
    elif chopper_votes > nami_votes:
        print("=> No.2 Chopper won the election.")
    else:
        print("=> No one won the election.")


# ============================================================================
# 第2題：閏年判斷程式
# ============================================================================
print("\n【第2題】閏年判斷程式")
print("-" * 70)

def is_leap_year(year):
    """
    判斷是否為閏年
    規則：每四年一閏，每百年不閏，但每四百年也一閏
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def question_2():
    """
    不定數迴圈輸入年份判斷閏年
    輸入-9999結束
    """
    while True:
        year = int(input())
        
        # 輸入-9999結束
        if year == -9999:
            break
        
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")


# ============================================================================
# 第3題：等腰三角形
# ============================================================================
print("\n【第3題】等腰三角形")
print("-" * 70)

def draw_triangle(n):
    """
    畫出高度為n的等腰三角形
    """
    for i in range(1, n + 1):
        # 計算空格數和星號數
        spaces = n - i
        stars = 2 * i - 1
        
        # 印出空格和星號
        print(' ' * spaces + '*' * stars)

def question_3():
    """
    根據輸入的n畫出對應的等腰三角形
    """
    n = int(input())
    draw_triangle(n)


# ============================================================================
# 第4題：計算第幾天
# ============================================================================
print("\n【第4題】計算第幾天")
print("-" * 70)

def day_of_year(year, month, day):
    """
    計算是該年的第幾天（考慮閏年）
    """
    # 每月天數（平年）
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 如果是閏年，2月有29天
    if is_leap_year(year):
        days_in_month[1] = 29
    
    # 計算總天數
    total_days = sum(days_in_month[:month - 1]) + day
    
    return total_days

def question_4():
    """
    輸入某年某月某日，判斷這一天是這一年的第幾天
    """
    print("請輸入年份：", end="")
    year = int(input())
    print("請輸入月份：", end="")
    month = int(input())
    print("請輸入日期：", end="")
    day = int(input())
    
    result = day_of_year(year, month, day)
    print(f"{year}年{month}月{day}日是該年的第{result}天")


# ============================================================================
# 第5題：三位數排列
# ============================================================================
print("\n【第5題】三位數排列")
print("-" * 70)

def generate_three_digit_numbers():
    """
    用1,2,3,4生成所有互不相同且無重複數字的三位數
    """
    numbers = []
    count = 0
    
    # 百位數：1, 2, 3, 4
    for i in range(1, 5):
        # 十位數：不能與百位相同
        for j in range(1, 5):
            if j != i:
                # 個位數：不能與百位和十位相同
                for k in range(1, 5):
                    if k != i and k != j:
                        number = i * 100 + j * 10 + k
                        numbers.append(number)
                        count += 1
    
    return numbers, count

def question_5():
    """
    用1,2,3,4能組成多少個互不相同且無重複數字的三位數？各是多少？
    """
    numbers, count = generate_three_digit_numbers()
    
    print(f"用1,2,3,4能組成{count}個互不相同且無重複數字的三位數")
    print("\n這些三位數分別是：")
    
    # 每行顯示10個數字
    for i, num in enumerate(numbers, 1):
        print(num, end="  ")
        if i % 10 == 0:
            print()  # 換行
    
    if len(numbers) % 10 != 0:
        print()  # 最後換行


# ============================================================================
# 第6題：質因數分解
# ============================================================================
print("\n【第6題】質因數分解")
print("-" * 70)

def prime_factorization(n):
    """
    將整數分解質因數
    """
    factors = []
    divisor = 2
    original_n = n
    
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1
            # 優化：如果divisor已經大於sqrt(n)，則n本身是質數
            if divisor * divisor > n and n > 1:
                factors.append(n)
                break
    
    return original_n, factors

def question_6():
    """
    輸入整數，輸出質因數分解
    例如：輸入90，印出90=2*3*3*5
    """
    print("請輸入一個整數：", end="")
    n = int(input())
    
    num, factors = prime_factorization(n)
    factor_str = '*'.join(map(str, factors))
    print(f"{num}={factor_str}")


# ============================================================================
# 第7題：彈跳球計算
# ============================================================================
print("\n【第7題】彈跳球計算")
print("-" * 70)

def bouncing_ball():
    """
    一球從100米高度落下，每次反彈回原高度的一半
    求第10次落地時共經過多少米？第10次反彈多高？
    """
    initial_height = 100.0  # 初始高度100米
    total_distance = 0.0    # 總經過距離
    current_height = initial_height
    
    # 第一次落地
    total_distance = initial_height
    
    # 從第2次到第10次落地
    for i in range(2, 11):
        # 反彈高度是上一次的一半
        current_height = current_height / 2
        
        # 上升距離 + 下降距離
        total_distance += current_height * 2
    
    # 第10次反彈高度
    tenth_bounce_height = current_height / 2
    
    return total_distance, tenth_bounce_height

def question_7():
    """
    彈跳球距離計算
    """
    distance, height = bouncing_ball()
    
    print(f"第10次落地時，球共經過 {distance} 米")
    print(f"第10次反彈高度為 {height} 米")


# ============================================================================
# 第8題：剪刀石頭布遊戲
# ============================================================================
print("\n【第8題】剪刀石頭布遊戲")
print("-" * 70)

def get_choice_name(choice):
    """取得選擇的名稱"""
    choices = {1: "石頭", 2: "剪刀", 3: "布"}
    return choices.get(choice, "未知")

def judge_winner(player, computer):
    """判斷勝負"""
    if player == computer:
        return "平局"
    elif (player == 1 and computer == 2) or \
         (player == 2 and computer == 3) or \
         (player == 3 and computer == 1):
        return "玩家勝利"
    else:
        return "電腦勝利"

def question_8():
    """
    剪刀石頭布遊戲
    石頭(1)、剪刀(2)、布(3)、退出(4)
    """
    print("----石頭剪刀布遊戲開始----")
    print("請按下面提示出拳")
    print("石頭[1],剪刀[2],布[3],退出[4]")
    
    while True:
        try:
            player_choice = int(input("請玩家出拳："))
            
            # 退出遊戲
            if player_choice == 4:
                print("遊戲退出")
                print("遊戲結束")
                break
            
            # 檢查輸入是否有效
            if player_choice not in [1, 2, 3]:
                print("輸入錯誤，請輸入1-4之間的數字")
                continue
            
            # 電腦隨機出拳（1-3）
            computer_choice = random.randint(1, 3)
            
            # 判斷勝負
            result = judge_winner(player_choice, computer_choice)
            
            # 顯示結果
            print(f"玩家出拳為{player_choice}，電腦出拳為{computer_choice}，{result}")
            
        except ValueError:
            print("輸入錯誤，請輸入數字")


# ============================================================================
# 第9題：撲克牌發牌
# ============================================================================
print("\n【第9題】撲克牌發牌")
print("-" * 70)

def create_deck():
    """生成一副撲克牌（不含鬼牌）"""
    suits = ['♠', '♥', '♦', '♣']  # 黑桃、紅心、方塊、梅花
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(f"{suit}{rank}")
    
    return deck

def shuffle_deck(deck):
    """洗牌"""
    random.shuffle(deck)
    return deck

def display_cards(cards, cards_per_row=13):
    """顯示牌組，每行顯示指定數量的牌"""
    for i in range(0, len(cards), cards_per_row):
        row = cards[i:i + cards_per_row]
        # 格式化輸出，每張牌佔固定寬度
        for card in row:
            print(f"{card:<4}", end="")
        print()  # 換行

def question_9():
    """
    撲克牌發牌：生成、洗牌、發牌
    """
    # 生成撲克牌
    deck = create_deck()
    print(f"生成了一副撲克牌，共 {len(deck)} 張\n")
    
    # 洗牌
    deck = shuffle_deck(deck)
    print("洗牌後的牌組：")
    display_cards(deck)
    
    # 可以擴展：發牌給玩家
    print("\n--- 發牌示範 ---")
    num_players = 4
    cards_per_player = 5
    
    for i in range(num_players):
        print(f"\n玩家 {i+1} 的牌：")
        player_cards = deck[i*cards_per_player:(i+1)*cards_per_player]
        display_cards(player_cards, cards_per_row=5)


# ============================================================================
# 第10題：平方計算
# ============================================================================
print("\n【第10題】平方計算")
print("-" * 70)

def question_10():
    """
    求輸入數字的平方，如果平方後小於50則退出
    如輸入特殊符號則輸出：輸入錯誤
    """
    while True:
        try:
            user_input = input("輸入一個數字：")
            
            # 嘗試轉換為浮點數
            num = float(user_input)
            
            # 計算平方
            square = num ** 2
            
            print(f"其平方為： {square}")
            
            # 如果平方小於50則退出
            if square < 50:
                print("平方小於50，退出")
                break
                
        except ValueError:
            # 無法轉換為數字（包含特殊符號）
            print("輸入錯誤")


# ============================================================================
# 主程式選單
# ============================================================================
def main_menu():
    """
    主選單：選擇要執行的題目
    """
    print("\n" + "=" * 70)
    print("請選擇要執行的題目（1-10）或0退出：")
    print("=" * 70)
    print("  1. 選舉投票程式")
    print("  2. 閏年判斷程式")
    print("  3. 等腰三角形")
    print("  4. 計算第幾天")
    print("  5. 三位數排列")
    print("  6. 質因數分解")
    print("  7. 彈跳球計算")
    print("  8. 剪刀石頭布遊戲")
    print("  9. 撲克牌發牌")
    print(" 10. 平方計算")
    print("  0. 退出程式")
    print("=" * 70)
    
    try:
        choice = int(input("\n請輸入選項 (0-10): "))
        
        if choice == 1:
            question_1()
        elif choice == 2:
            question_2()
        elif choice == 3:
            question_3()
        elif choice == 4:
            question_4()
        elif choice == 5:
            question_5()
        elif choice == 6:
            question_6()
        elif choice == 7:
            question_7()
        elif choice == 8:
            question_8()
        elif choice == 9:
            question_9()
        elif choice == 10:
            question_10()
        elif choice == 0:
            print("\n感謝使用！再見！")
            return False
        else:
            print("\n無效的選項，請輸入0-10之間的數字")
        
        return True
        
    except ValueError:
        print("\n輸入錯誤，請輸入數字")
        return True


# ============================================================================
# 程式入口
# ============================================================================
if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("Python 練習題 - 10題完整程式碼集合")
    print("作者：s12490040 辛哲磊")
    print("日期：2025年11月10日")
    print("=" * 70)
    
    # 主迴圈
    while True:
        if not main_menu():
            break
        
        # 詢問是否繼續
        print("\n" + "-" * 70)
        continue_choice = input("是否繼續執行其他題目？(y/n): ")
        if continue_choice.lower() != 'y':
            print("\n感謝使用！再見！")
            break
    
    print("\n程式結束")
    print("=" * 70)

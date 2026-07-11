# 🎲 Bài tập: Mô phỏng trò chơi Five Dice
# Nền tảng: freeCodeCamp - Python Basics Workshop
# Mục tiêu: Luyện tập về loops, list comprehension và xử lý logic xúc xắc ngẫu nhiên.


def five_dice(dice):
    counts = {}
    for die in dice:
        if die in counts:
            counts[die] += 1
        else:
            counts[die] = 1
            
    frequencies = sorted(counts.values(), reverse=True)
    
    if frequencies == [5]:
        return "five of a kind"
    elif frequencies == [4, 1]:
        return "four of a kind"
    elif frequencies == [3, 2]:
        return "full house"
    elif frequencies == [3, 1, 1]:
        return "three of a kind"
    elif frequencies == [2, 2, 1]:
        return "two pair"
    elif frequencies == [2, 1, 1, 1]:
        return "pair"
    else:
        sorted_dice = sorted(dice)
        if sorted_dice[4] - sorted_dice[0] == 4:
            return "large straight"
        elif (sorted_dice[3] - sorted_dice[0] == 3) or (sorted_dice[4] - sorted_dice[1] == 3):
            return "small straight"
        else:
            return "no pair"

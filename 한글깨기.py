# Developed by Sunghyun Cho on Feb 25, 2019.

class 한글분해():

    초성들 = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ",
            "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
    중성들 = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ",
            "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
    종성들 = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ",
            "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]

    def __init__(self, 입력):
        self.원본 = 입력
        if not ord('가') <= ord(입력) <= ord('힣'):
            self.종성 = "   "
            self.중성 = "   "
            self.초성 = " " + 입력 + " "
        else:
            self.한글번호 = ord(입력) - 0xAC00
            # 0xAC00는 첫번째 완전형 한글 "가"의 유니코드의 값으로, "self.한글번호"는 이 문자가 몇 번째 한글인지 나타냅니다.

            self.종성번호 = int(self.한글번호 % 28)
            # 종성의 개수가 28개이므로, 같은 종성은 한글 번호가 28 증가할 때마다 돌아옵니다.
            # "가 각 갂 갃 간 갅 갆 갇 갈 갉 갊 갋 갌 갍 갎 갏 감 갑 값 갓 갔 강 갖 갗 갘 같 갚 갛"까지가 28이고 그 다음에 "개"가 오는 것처럼요.
            # 따라서 mod 28의 값을 구하면 종성의 번호를 알 수 있습니다.

            self.중성번호 = int(((self.한글번호 - self.종성번호) / 28 ) % 21)
            # 한글번호에서 종성 번호를 빼게 되면 종성이 없어진 형태의 한글이 나오게 됩니다.
            # "간"에서 종성번호 4를 빼면 "가"가 나오는 것처럼요.
            # 이 값을 이를 28로 나누게 되면, "종성을 제외한 값들만 따졌을 때 몇 번째 글자인지" 나오게 됩니다.
            # "가 개 갸 걔 거 게 겨 계 고 과 괘 괴 교 구..."에서, 중성은 21개이므로 마찬가지로 21번마다 같은 중성이 반복됩니다.
            # 따라서 mod 21의 값을 구하면 중성의 번호를 알 수 있습니다.

            self.초성번호 = int((((self.한글번호 - self.종성번호) / 28 ) / 21))
            # 같은 원리로 초성 번호 또한 구할 수 있습니다.
            # 이번에는 간단하게 중성의 반복 주기가 몇 번 돌아갔는지를 계산하면 됩니다.
            # 그 값은 ((self.한글번호 - self.종성번호) / 28 )를 21로 나눈 몫과 같습니다.

            self.종성 = self.종성들[self.종성번호]
            self.중성 = self.중성들[self.중성번호]
            self.초성 = self.초성들[self.초성번호]
            # 마지막으로 미리 가지고 있던 유니코드 배열에서 필요한 값을 찾아 대입합니다.

    def 종성이_있다면(self):
        if self.종성 != "":
            return True
        else:
            return False

    def 가로형중성을_가진다면(self):
        if self.중성 in ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅣ"]:
            return True
        else:
            return False

    def 인쇄(self):
        print(self.원본, "을 분해함. 초성:", self.초성, "중성:", self.중성, "종성:", self.종성)

def 차원분석(파자):
    길이 = 1 # 초성의 길이
    높이 = 1 # 초성의 높이

    if 파자.가로형중성을_가진다면():
        길이 = 길이 + 1
    else:
        높이 = 높이 + 1
    if 파자.종성이_있다면():
        높이 = 높이 + 1
    return [길이, 높이]

깨야할_한글 = list(input("\x1b[1;32m" + "깰 한글을 입력하세요: " + "\x1b[0m"))
줄1 = []
줄2 = []
줄3 = []

for 한글 in 깨야할_한글:
    파자 = 한글분해(한글)
    차원 = 차원분석(파자)
    길이 = 차원[0]
    높이 = 차원[1]
    if 길이 == 2:
        줄1.append(파자.초성 + 파자.중성)
        if(높이 == 2):
            줄2.append("  " + 파자.종성)
        else:
            줄2.append("    ")
        줄3.append("    ")
    else:
        줄1.append(파자.초성)
        줄2.append(파자.중성)
        if 높이 == 3:
            줄3.append(파자.종성)
        else:
            줄3.append("  ")

print("\n\x1b[1;32m" + "결과: " + "\x1b[0m\n")
for 글자 in 줄1:
    print(글자, end="")
print()
for 글자 in 줄2:
    print(글자, end="")
print()
for 글자 in 줄3:
    print(글자, end="")
print()
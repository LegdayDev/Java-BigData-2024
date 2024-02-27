# file: p32_osDir.py
# desc: 운영체제 디렉토리 확인하기

import os


def search(dirName):
    try:
        fileNames = os.listdir(dirName)  # listdir() : List 타입 반환
        for fileName in fileNames: # fielName
            fullName = os.path.join(dirName, fileName)
            if os.path.isdir(fullName):  # 하위 디렉터리가 있으면 재귀호출
                search(fullName)
            else:
                ext = os.path.splitext(fullName)[-1]  # 튜플 마지막값(확장자)를 반환
                if ext == ".py":  # 파이썬 파일만 출력
                    with open(fullName, mode = 'r', encoding='utf-8') as fp: # with 로 파일을 열면 close()가 필요없다.
                        print(f'파일명 : {fullName} , 라인수 : {len(fp.readlines())}줄')
    except PermissionError as e:  # 접근권한이 없을 때
        print("접근권한이 없습니다.", e.args)

if __name__ == "__main__":
    search(
        "/Users/jaeyoung/Desktop/workspaces/python_lab/Java-BigData-2024/day03"
    )  # 해당 디렉토리 하위 디렉토리를 모두 출력

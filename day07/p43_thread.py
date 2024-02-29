# file: p43_thread.py
# desc: 스레드 기본

from threading import Thread, current_thread
import time


class BackgroundWorker(Thread):
    def __init__(self, name) -> None:
        super().__init__(name=name)
        self._name = f"{current_thread().getName()} : {name}"
        # Python 3.10 부터는 getName() 말고 name 을 쓰면된다.

    def run(self) -> None:
        print(f"Background Worker 시작 >> {self._name}\n")
        time.sleep(3)
        print(f"Background Worker 종료 >> {self._name}\n")


print("Main Thread 시작")  # 메인 엔트리에서 시작되는 프로세스는 메인스레드
for i in range(5):
    name = f"Sub Thread {i}"
    th = BackgroundWorker(name)
    th.start()  # run() 실행

print("Main Thread 종료")

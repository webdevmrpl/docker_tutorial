import time

if __name__ == "__main__":
    print("WORKER: Container has started (condition: service_started).")
    time.sleep(5)
    print("WORKER: Finished some work. DB health not required for startup.")
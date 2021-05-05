from logic.hourly_worker import HourlyWorker
from logic.fixed_worker import FixedWorker

if __name__ == '__main__':
    workers = [FixedWorker(1, "John", 160), HourlyWorker(
        2, "Alex", 1), FixedWorker(3, "Mark", 200), HourlyWorker(4, "Viktor", 2)]
    sorted_workers = sorted(workers)
    print(f"Sorted list: {sorted_workers}")
    print(f"Last identifiers: {[worker.id for worker in sorted_workers[-3:]]}")

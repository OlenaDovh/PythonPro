default_time = 60


def training_session(workout_rounds: int) -> None:
    """Adjusts training time using default one"""
    time_per_round = default_time
    print("Результат:")

    def adjust_time() -> int:
        """Changes training time for each period (5min) """
        return time_per_round - 5

    for round_num in range(1, workout_rounds + 1):
        if time_per_round <= 0:
            print("Час вичерпано, тренування завершено.")
            break
        if round_num > 1:
            time_per_round = adjust_time()
            print(f"Раунд {round_num}: {time_per_round} (після коригування)")
        else:
            print(f"Раунд {round_num}: {time_per_round}")


training_session(100)

def score_(n: int, arr: list) -> int:
    sorted_scores = sorted(list(arr), reverse=True)
    runner_up = None
    for n in sorted_scores:
        if n < sorted_scores[0]:
            runner_up = n
            break
    print(runner_up, end=" ")
    return runner_up
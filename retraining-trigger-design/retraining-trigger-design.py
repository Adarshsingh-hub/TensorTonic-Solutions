def retraining_policy(daily_stats, config):
    drift_threshold = config["drift_threshold"]
    performance_threshold = config["performance_threshold"]
    max_staleness = config["max_staleness"]
    cooldown = config["cooldown"]
    retrain_cost = config["retrain_cost"]
    budget = config["budget"]

    retrain_days = []

    days_since_retrain = 0
    last_retrain_day = None

    for stats in daily_stats:
        day = stats["day"]
        drift = stats["drift_score"]
        perf = stats["performance"]

        # increment staleness counter
        days_since_retrain += 1

        # triggers
        drift_trigger = drift > drift_threshold
        perf_trigger = perf < performance_threshold
        stale_trigger = days_since_retrain >= max_staleness

        trigger = drift_trigger or perf_trigger or stale_trigger

        # constraints
        cooldown_ok = last_retrain_day is None or (day - last_retrain_day) >= cooldown
        budget_ok = budget >= retrain_cost

        if trigger and cooldown_ok and budget_ok:
            retrain_days.append(day)

            budget -= retrain_cost
            last_retrain_day = day
            days_since_retrain = 0

    return retrain_days
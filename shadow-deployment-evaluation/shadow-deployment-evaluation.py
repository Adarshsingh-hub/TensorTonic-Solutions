import math

def evaluate_shadow(production_log, shadow_log, criteria):
    n = len(production_log)

    prod_correct = sum(1 for r in production_log if r["prediction"] == r["actual"])
    shadow_correct = sum(1 for r in shadow_log if r["prediction"] == r["actual"])

    production_accuracy = prod_correct / n
    shadow_accuracy = shadow_correct / n
    accuracy_gain = shadow_accuracy - production_accuracy


    agreement = sum(
        1 for p, s in zip(production_log, shadow_log)
        if p["prediction"] == s["prediction"]
    )
    agreement_rate = agreement / n


    latencies = sorted(r["latency_ms"] for r in shadow_log)
    index = math.ceil(0.95 * n) - 1
    shadow_latency_p95 = latencies[index]


    promote = (
        accuracy_gain >= criteria["min_accuracy_gain"]
        and shadow_latency_p95 <= criteria["max_latency_p95"]
        and agreement_rate >= criteria["min_agreement_rate"]
    )

    return {
        "promote": promote,
        "metrics": {
            "shadow_accuracy": shadow_accuracy,
            "production_accuracy": production_accuracy,
            "accuracy_gain": accuracy_gain,
            "shadow_latency_p95": shadow_latency_p95,
            "agreement_rate": agreement_rate,
        },
    }
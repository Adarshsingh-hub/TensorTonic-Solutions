import numpy as np

def calibrate_isotonic(cal_labels, cal_probs, new_probs):
    cal_labels = np.array(cal_labels, dtype=float)
    cal_probs = np.array(cal_probs, dtype=float)

    order = np.argsort(cal_probs)
    cal_probs = cal_probs[order]
    cal_labels = cal_labels[order]

    y = cal_labels.copy()
    w = np.ones(len(y))

    i = 0
    while i < len(y) - 1:
        if y[i] > y[i + 1]:
            total_w = w[i] + w[i + 1]
            avg = (y[i]*w[i] + y[i+1]*w[i+1]) / total_w

            y[i] = y[i+1] = avg
            w[i] = w[i+1] = total_w

            j = i
            while j > 0 and y[j-1] > y[j]:
                total_w = w[j-1] + w[j]
                avg = (y[j-1]*w[j-1] + y[j]*w[j]) / total_w
                y[j-1] = y[j] = avg
                w[j-1] = w[j] = total_w
                j -= 1
            i = max(j,0)
        else:
            i += 1

    cal_vals = y
    
    results = []
    for q in new_probs:
        if q <= cal_probs[0]:
            results.append(cal_vals[0])
        elif q >= cal_probs[-1]:
            results.append(cal_vals[-1])
        else:
            idx = np.searchsorted(cal_probs, q) - 1
            p1, p2 = cal_probs[idx], cal_probs[idx+1]
            c1, c2 = cal_vals[idx], cal_vals[idx+1]

            t = (q - p1) / (p2 - p1)
            results.append(c1 + t * (c2 - c1))

    return results
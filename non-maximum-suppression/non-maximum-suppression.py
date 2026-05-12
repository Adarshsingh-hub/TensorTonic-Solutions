def nms(boxes, scores, iou_threshold):
    """
    Apply Non-Maximum Suppression.
    Returns a list of indices of kept boxes.
    """
    if not boxes:
        return []

    def iou(box1, box2):
        # Intersection coordinates
        x1 = max(box1[0], box2[0])
        y1 = max(box1[1], box2[1])
        x2 = min(box1[2], box2[2])
        y2 = min(box1[3], box2[3])

        # Intersection area
        inter_w = max(0, x2 - x1)
        inter_h = max(0, y2 - y1)
        intersection = inter_w * inter_h

        # Areas
        area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
        area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])

        union = area1 + area2 - intersection
        if union == 0:
            return 0.0

        return intersection / union

    # Sort indices by score descending
    order = sorted(range(len(boxes)), key=lambda i: scores[i], reverse=True)

    keep = []

    while order:
        current = order.pop(0)
        keep.append(current)

        remaining = []
        for idx in order:
            if iou(boxes[current], boxes[idx]) < iou_threshold:
                remaining.append(idx)

        order = remaining

    return keep
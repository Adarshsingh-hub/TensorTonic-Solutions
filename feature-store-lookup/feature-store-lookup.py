def feature_store_lookup(feature_store, requests, defaults):
    """
    Join offline user features with online request-time features.
    """
    result = []
    
    for req in requests:
        user_id = req["user_id"]
        online = req["online_features"]
        
        # Get offline features or defaults
        offline = feature_store.get(user_id, defaults)
        
        # Merge dictionaries
        combined = {**offline, **online}
        
        result.append(combined)
    
    return result
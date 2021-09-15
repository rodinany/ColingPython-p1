def solution(x1, y1, x2, y2):
    if (x2-x1==1 or x1==x2 or x1-x2==1) and (y1-y2==1 or y1==y2 or y2-y1==1):
        return True
    else:
        return False

    

def solution(total):
    hours = total // 60
    minutes = total - hours * 60
    if hours > 23:
        hours = hours % 24
    if minutes == 0:
        minutes = f'0{minutes}'
    total = f'{hours} {minutes}'
    return total
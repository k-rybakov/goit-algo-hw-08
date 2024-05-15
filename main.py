import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)  # перетворюємо список кабелів у піраміду
    
    total_cost = 0
    while len(cables) > 1:
        # видаляємо два найменші кабелі з купи
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)
        
        # об'єднуємо їх та додаємо новий кабель назад у купу
        new_cable = cable1 + cable2

        total_cost += new_cable  # додаємо витрати на об'єднання
        heapq.heappush(cables, new_cable)
    
    return total_cost


cables = [4, 3, 2, 6, 3, 1]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables)) # 47

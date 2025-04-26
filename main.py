import random

def manhattan_distance(point1, point2):
    
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def k_means_manhattan(data_points, k, max_iterations=100):
    
    
    cluster_centers = random.sample(data_points, k)
    
    for _ in range(max_iterations):
       
        clusters = [[] for _ in range(k)]
        
        for data_point in data_points:
            
            distances = [manhattan_distance(data_point, center) for center in cluster_centers]
            
            closest_cluster_index = distances.index(min(distances))
            
            clusters[closest_cluster_index].append(data_point)
            
       
        new_cluster_centers = []
        for cluster in clusters:
            
            if cluster:
               
                mean_x = sum(point[0] for point in cluster) / len(cluster)
                
                mean_y = sum(point[1] for point in cluster) / len(cluster)
                
                new_cluster_centers.append((mean_x, mean_y))
                
                
            else:
               
               
                new_cluster_centers.append(random.choice(data_points)) 
                
    
        if new_cluster_centers == cluster_centers:
            break
        cluster_centers = new_cluster_centers
        
        
    return clusters, cluster_centers

if __name__ == "__main__":
   
   
    data_points = [(random.randint(0, 19), random.randint(0, 19)) for _ in range(100)]
    k = 5

    clusters, cluster_centers = k_means_manhattan(data_points, k)

   
   
    grid = [['.' for _ in range(20)] for _ in range(20)]



    for i, center in enumerate(cluster_centers):
        
        grid[int(center[1])][int(center[0])] = 'C'

    
    
    for i, cluster in enumerate(clusters):
        
        for point in cluster:
            
            grid[point[1]][point[0]] = str(i)

    for row in grid:
        
        print(' '.join(row))

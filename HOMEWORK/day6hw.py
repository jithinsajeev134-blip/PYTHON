blog_views = [150, 800, 2500, 600, 1200, 450, 3000]

total_views = 0
no_of_trending_views = 0    

for views in blog_views:
    if views > 1000:
        print("Trending")
        no_of_trending_views += 1
    elif 500 <= views <= 1000:
        print("Average")
    else:
        print("Low Traffic")
        
        total_views += views
        
print(total_views)
print(no_of_trending_views)
    

    
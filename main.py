import numpy as np
import matplotlib.pyplot as plt

def main():
    print( "aa" )

    # 円グラフを描画
    x = np.array( [70,30] )
    colors = ["lightgreen", "white"]
    plt.pie( x, counterclock=False, startangle=90, colors=colors )
 
    # 中心 (0,0) に 60% の大きさで円を描画
    centre_circle = plt.Circle( ( 0, 0 ), 0.6, color='black', fc='white', linewidth=0 )
    fig = plt.gcf()
    fig.gca().add_artist( centre_circle )

    plt.show()

main()

#<i class="fab fa-java"></i>
#<i class="fab fa-html5"></i>
#<i class="fab fa-css3-alt"></i>
#<i class="fab fa-php"></i>
#<i class="fas fa-database"></i>
#<i class="fab fa-python"></i>

#<i class="fab fa-sass"></i>

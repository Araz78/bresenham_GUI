from bokeh.plotting import figure, output_file, show, save
#=========================================== input x1,x2 y1,y2 values
def bresenham(X1,X2,Y1,Y2):
    x1 = X1
    y1 = Y1
    x2 = X2
    y2 = Y2
    #=========================================== Calculate the values of Delta x,y & P0 & m
    Delta_x = x2 - x1
    Delta_y = y2 - y1
    P_Zero  = ((2 * Delta_y) - Delta_x)
    #=========================================== Insert the values ​​of x,y
    X_k = [xk for xk in range(x1 , x2+1)]
    len_X_k = len(X_k)
    len_X_k-=1

    Y_k = []
    first = y1
    Y_k.append(first)
    w = first

    P_k = []
    P_k.append(P_Zero)

    for i in range(0 , len_X_k):
        if P_k[i] < 0:
            w+=0
            Y_k.append(w)
            new_p_k = P_k[i] + (2 * Delta_y)
            P_k.append(new_p_k)

        else:
            w+=1
            Y_k.append(w)
            new_p_k = (P_k[i] + ((2 * Delta_y) - (2 * Delta_x)))
            P_k.append(new_p_k)
    #=========================================== Draw lines
    html = output_file("Bresenham lines.html")

    p = figure(title="Bresenham Algorithm", x_axis_label='x', y_axis_label='y')
    p.line(X_k, Y_k, legend_label="Temp.", line_width=5)
    save(p)
            
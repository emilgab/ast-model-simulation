def linear_graph(height=5, textwidth=r"\textwidth-1cm", caption="Placeholder caption text",
                label="Placeholder label text",
                plots=[[(0,25),(1,50),(2,75),(3,100)],[(0,10),(1,25),(2,50),(3,75)],[(0,5),(1,20),(2,45),(3,70)]],
                plot_names=["One","Two","Three"],
                legend_position=4):

    legend_anchors = ["","north","east","south","west"]

    print("---------------\n")
    print(r"\begin{figure}[H]")
    print(r"    \centering")
    print(r"    \begin{tikzpicture}")
    print(r"    \begin{axis}[")
    print(r"    scale only axis,")
    print(f"    height={height}cm,")
    print(f"    width={textwidth},")
    print(r"    legend style={at={(0.3,0.9),anchor="+legend_anchors[legend_position]+"}},")
    print(r"    /pgf/number format/.cd,")
    print(r"    use comma,")
    print(r"    1000 sep={}]")
    print(r"    ]")

    colors = ["red","blue","orange","green","black"]

    for iteration,plot in enumerate(plots):
        print(r"    \addplot[mark=none,thick,"+colors[iteration]+"] coordinates {")
        for x,y in plot:
            print(f"        ({x},{y})")
        print(r"    };")
        print(r"    \addlegendentry{"+plot_names[iteration]+"}")


    print(r"    \end{axis}")
    print(r"    \end{tikzpicture}")
    print(r"    \caption{"+caption+"}")
    print(r"    \label{"+"fig:"+label+"}")
    print(r"\end{figure}")
linear_graph()

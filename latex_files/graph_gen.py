def linear_graph(plots):
    print("---------------\n")
    print(r"\begin{figure}[H]")
    print(r"    \centering")
    print(r"    \begin{tikzpicture}")
    print(r"    \begin{axis}[")
    print(r"    scale only axis,")
    print(f"    height=5cm,")
    print(r"    width=\textwidth-1cm,")
    print(r"    legend style={at={(0.3,0.9),anchor=west}},")
    print(r"    /pgf/number format/.cd,")
    print(r"    use comma,")
    print(r"    1000 sep={}]")
    print(r"    ]")

    plot_names = ["One","Two","Three","Four","Five","Six"]
    colors = ["red","blue","orange","green","black"]

    for iteration,plot in enumerate(plots):
        print(r"    \addplot[mark=none,thick,"+colors[iteration]+"] coordinates {")
        for x,y in plot:
            print(f"        ({x},{y})")
        print(r"    };")
        print(r"    \addlegendentry{"+plot_names[iteration]+"}")

    print(r"    \end{axis}")
    print(r"    \end{tikzpicture}")
    print(r"    \caption{Placeholder text}")
    print(r"    \label{Placeholder text}")
    print(r"\end{figure}")


def linear_graph_double_y(plots):
    plots_one = plots[0:2]
    plots_two = plots[2:]
    plot_names = ["One","Two","Three","Four","Five"]
    colors = ["red","blue","orange","green","black"]
    used_plot_names = []
    print("---------------\n")
    print(r"\begin{figure}[H]")
    print(r"    \centering")
    print(r"    \begin{tikzpicture}")
    print(r"    \pgfplotsset{")
    print(r"    scale only axis,")
    print(f"    height=5cm,")
    print(r"    width=\textwidth-2.7cm,")
    print(r"    legend style={at={(0.3,0.9),anchor=west}},")
    print(r"    /pgf/number format/.cd,")
    print(r"    use comma,")
    print(r"    1000 sep={}]")
    print(r"    scaled x ticks=base 10:3,")
    print(r"    }")
    print(r"    \begin{axis}[")
    print(r"    axis y line*=left,")
    # print(r"    ymin=0, ymax=100,")
    print(r"    xlabel=x-axis,")
    print(r"    ylabel=y-axis 1,")
    print(r"    ]")

    counter = 0

    for plot in plots_one:
        print(r"    \addplot[",colors[counter],']')
        print(r"    coordinates{")
        for x,y in plot:
            print(f"    ({x},{y})")
        print(r"    };  \label"+"{"+plot_names[counter]+'}')
        used_plot_names.append(plot_names[counter])
        counter += 1

    print(r"    \end{axis}")
    print(r"    \begin{axis}[")
    print(r"    axis y line*=right,")
    print(r"    axis x line=none,")
    # print(r"    ymin=0, ymax=100,")
    print(r"    ylabel=y-axis 2")
    print(r"    ]")
    for iteration,name in enumerate(used_plot_names):
        print(r"    \addlegendimage{/pgfplots/refstyle=",name,r"}\addlegendentry{","plot ",iteration,"}")

    for plot in plots_two:
        print(r"    \addplot[",colors[counter],']')
        print(r"    coordinates{")
        for x,y in plot:
            print(f"    ({x},{y})")
        print(r"    };  \addlegendentry"+"{"+plot_names[counter]+'}')
        used_plot_names.append(plot_names[counter])
        counter += 1
    print(r"    \end{axis}")

    print(r"    \end{tikzpicture}")
    print(r"    \caption{Placeholder text}")
    print(r"    \label{Placeholder text}")
    print("\end{figure}\n")

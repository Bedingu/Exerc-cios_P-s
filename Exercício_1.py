import matplotlib.pyplot as plt
from pandas import read_excel


df = read_excel(r"C:\Users\bedin\OneDrive\Área de Trabalho\Projetos_Pós\Exercicios.xlsx", names = ['x2','y2'])

plt.plot(df['x2'], df['y2'], linestyle = '--', marker ='o', color = 'blue', markersize = 4)

plt.xlabel ('Eixo x', fontsize =15)
plt.ylabel ('Eixo y', fontsize =15)

plt.title('Exercício 1')

plt.legend(['Gráfico Exercício 1'], fontsize =14)

axes = plt.gca()
axes.yaxis.grid(b=True, color='black', alpha=0.3, linestyle='-.', linewidth=1)

plt.figure(figsize=(10.5,9))

plt.show()








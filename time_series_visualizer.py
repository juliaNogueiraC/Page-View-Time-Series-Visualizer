import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Limpar os dados
def clean_data():
    df = pd.read_csv('fcc-forum-pageviews.csv')
    df = df[(df["value"] >= df["value"].quantile(0.025)) & 
            (df["value"] <= df["value"].quantile(0.975))]
    return df

# Desenhar o gráfico de linha
def draw_line_plot():
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df["value"], color="r")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Salvar imagem e retornar a figura
    fig.savefig('line_plot.png')
    return fig

# Desenhar o gráfico de barras
def draw_bar_plot():
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

    # Extrair o ano e mês da data
    df['year'] = df.index.year
    df['month'] = df.index.strftime('%B')  # Converter o índice para o nome do mês

    # Agrupar por ano e mês e calcular a média das visualizações diárias de página
    df_avg = df.groupby(['year', 'month'])['value'].mean().reset_index()

    # Plotar o gráfico de barras
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(x='year', y='value', hue='month', data=df_avg)

    # Definir os rótulos dos eixos e o título
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Average Daily Page Views per Month')

    # Personalizar a legenda
    ax.legend(title='Months')

    # Exibir o gráfico
    plt.show()

    return ax

# Desenhar o gráfico de box plot
def draw_box_plot():
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

    # Extrair o ano e mês da data
    df['year'] = df.index.year
    df['month'] = df.index.strftime('%B')  # Converter o índice para o nome do mês

    # Criar cópias do DataFrame para cada gráfico
    df_year = df.copy()
    df_month = df.copy()

    # Criar subplots
    fig, axes = plt.subplots(1, 2, figsize=(20, 6))

    # Plotar o box plot para distribuição dos valores ao longo dos anos
    sns.boxplot(x='year', y='value', data=df_year, ax=axes[0])
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')

    # Plotar o box plot para distribuição dos valores ao longo dos meses
    df_month['month_num'] = df_month.index.month
    df_month = df_month.sort_values('month_num')
    sns.boxplot(x='month', y='value', data=df_month, ax=axes[1])
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')

    # Personalizar os rótulos dos meses no eixo x
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    axes[1].set_xticklabels(month_order, rotation=45)

    # Ajustar layout
    plt.tight_layout()

    # Salvar a imagem
    plt.savefig('box_plot.png')

    # Exibir os gráficos
    plt.show()

    return fig

import matplotlib.pyplot as plt
import streamlit as st

def atualizar_graficos(placeholder, df):
    """
    Função para atualizar os gráficos na aba 'Gráficos'.
    placeholder: Um objeto st.empty() do Streamlit para exibir o gráfico.
    df: O DataFrame com os dados.
    """
    with placeholder.container():
        # Exemplo: Gráfico de Rentabilidade por Papel
        if "Papel" in df.columns and "Rentabilidade" in df.columns:
            fig, ax = plt.subplots()
            ax.bar(df["Papel"], df["Rentabilidade"].astype(float))
            ax.set_title("Rentabilidade por Papel")
            ax.set_xlabel("Papel")
            ax.set_ylabel("Rentabilidade (%)")
            plt.xticks(rotation=45)
            st.pyplot(fig)
            plt.close(fig)  # Fechar a figura para liberar memória
        else:
            st.warning("Colunas 'Papel' e 'Rentabilidade' não encontradas no DataFrame.")

def atualizar_analise(placeholder, df):
    """
    Função para atualizar a análise geral na aba 'Análise Geral'.
    placeholder: Um objeto st.empty() do Streamlit para exibir a análise.
    df: O DataFrame com os dados.
    """
    with placeholder.container():
        st.subheader("Análise Geral")
        if not df.empty:
            # Exemplo: Estatísticas básicas
            total_investido = df["Total Investido"].astype(float).sum()
            valor_atual = df["Valor Atual"].astype(float).sum()
            rentabilidade_media = df["Rentabilidade"].astype(float).mean()

            st.write(f"**Total Investido:** R$ {total_investido:,.2f}")
            st.write(f"**Valor Atual:** R$ {valor_atual:,.2f}")
            st.write(f"**Rentabilidade Média:** {rentabilidade_media:.2f}%")

            # Exemplo: Gráfico de pizza para distribuição de investimentos
            if "Papel" in df.columns and "Valor Atual" in df.columns:
                fig, ax = plt.subplots()
                ax.pie(df["Valor Atual"].astype(float), labels=df["Papel"], autopct='%1.1f%%')
                ax.set_title("Distribuição do Valor Atual por Papel")
                st.pyplot(fig)
                plt.close(fig)  # Fechar a figura para liberar memória
        else:
            st.warning("Nenhum dado disponível para análise.")

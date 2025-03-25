# Carregar dados do CSV
dados <- read.csv("dados_agricultura.csv", encoding = "UTF-8")

# Exibir os dados carregados (conferência rápida)
print(dados)

# Cálculos estatísticos básicos:
media_area <- mean(dados$Area_m2)
desvio_area <- sd(dados$Area_m2)

media_insumo <- mean(dados$Qtd_total_insumo)
desvio_insumo <- sd(dados$Qtd_total_insumo)

# Exibir resultados claramente:
cat("------ Estatísticas Básicas ------\n")
cat("Área média plantada:", media_area, "m²\n")
cat("Desvio padrão da área plantada:", desvio_area, "m²\n\n")

cat("Quantidade média de insumo:", media_insumo, "unidades\n")
cat("Desvio padrão da quantidade de insumo:", desvio_insumo, "unidades\n")

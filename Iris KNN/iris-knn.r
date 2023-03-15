filename <- "iris.csv"
datos <- read.csv(filename, sep = ";", dec = ".", header = "true")

# Inicio de pruebas
for(i in 1:10) {
    muestra <- sample(1:105, 45)
}
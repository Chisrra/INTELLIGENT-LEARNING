#P1 definir la función y su derivada
f <- function(x) {
    return(2 * (x^2) * cos(x) - 5 * x)
}

f_prima <- function(x) {
    return((4 * x * cos(x)) - (2 * (x^2) * sin(x)) - 5)
}

#P2 Elejir el valor inicial
x <- runif(1, min = -5, max = 5)
taza_aprendizaje <- 0.01
print(sprintf("Valor inicial de x es: %.2f", x))

#P3 Crear e inicializar los vectores que almacenaran los puntos de x, y
x_vals <- c(x)
y_vals <- c(f(x))

#P4 realizar la busqueda del minimo y guardar el recorrido
for (i in 1:1000) {
    x <- x - (taza_aprendizaje * f_prima(x))
    y <- f(x)
    x_vals <- c(x_vals, x)
    y_vals <- c(y_vals, y)
}

print(sprintf("Este es el mínimo aproximadamente: %.2f", x))

#P5 Graficar la funcion y sus puntos
windows()
plot(f, xlim = c(-5, 5), type = "l", lwd = 2, col = "blue", 
    main = "Función 2*(x^2)*cos(x) - 5*x", xlab = "x", ylab = "f(x)")
points(x_vals, y_vals, col = "red")
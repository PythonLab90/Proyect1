function inicio() {
    let palabra = 'Busca los Mejores Productos'
    let h1 = document.querySelector('h1')
    h1.textContent = ''

    for (let i = 0; i < palabra.length; i++) {
        setTimeout(() => {
            h1.textContent += palabra[i]
        }, i * 125)
    }
}

document.addEventListener('DOMContentLoaded', inicio)

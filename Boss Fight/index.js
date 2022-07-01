const canvas = document.querySelector('canvas');
const c = canvas.getContext('2d')

canvas.width = 960
canvas.height = 704

//making canvas visible as a white rectangle
c.fillStyle = 'white'
c.fillRect(0, 0, canvas.width, canvas.height)

//Need to create HTML image in order to use it
const image = new Image()
image.src = './img/BattleGrounds.png'
console.log(image)

image.onload = () => {
    c.drawImage(image, 0, 0)
}

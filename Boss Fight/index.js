const canvas = document.querySelector('canvas');
const c = canvas.getContext('2d')

canvas.width = 1024
canvas.height = 576

//making canvas visible as a white rectangle
c.fillStyle = 'white'
c.fillRect(0, 0, canvas.width, canvas.height)

//Need to create HTML image in order to use it
const image = new Image()
image.src = './img/BattleGrounds.png'
console.log(image)

image.onload = () => {
    c.drawImage(image)
}

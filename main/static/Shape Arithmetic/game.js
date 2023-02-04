const shapes = document.querySelectorAll('.shape');
const selectButton = document.querySelector('#select-shapes');

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

selectButton.addEventListener('click', function() {
  // hide all shapes
  for (let i = 0; i < shapes.length; i++) {
    shapes[i].style.display = 'none';
  }
  
  // randomly select and display 3 shapes
  const selectedShapes = [];
  for (let i = 0; i < 3; i++) {
    let randomIndex = getRandomInt(shapes.length);
    while (selectedShapes.includes(randomIndex)) {
      randomIndex = getRandomInt(shapes.length);
    }
    selectedShapes.push(randomIndex);
    shapes[randomIndex].style.display = 'block';
  }
});
# simulador

# animate

animate__animated
animate__delay-2s
animate__infinite

# Movimento mouse

const delta = 6;
let startX;
let startY;

element.addEventListener('mousedown', function (event) {
  startX = event.pageX;
  startY = event.pageY;
});

element.addEventListener('mouseup', function (event) {
  const diffX = Math.abs(event.pageX - startX);
  const diffY = Math.abs(event.pageY - startY);

  if (diffX < delta && diffY < delta) {
    // Click!
  }
});

<!-- onmouseover -->
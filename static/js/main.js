const button = document.querySelector('.test');

const burger = document.querySelector('.burger-container');
const lines = document.querySelectorAll('.line');
const text = document.querySelector('h1');

burger.addEventListener('click', () => {
  lines.forEach(line => {
    line.classList.toggle('close');
  })
  text.classList.toggle('text');
})
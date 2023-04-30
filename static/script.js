const carouselItems = document.querySelectorAll('.carousel-item');
let currentIndex = 0;

setInterval(() => {
  const nextIndex = (currentIndex + 1) % carouselItems.length;
  carouselItems[currentIndex].classList.remove('active');
  carouselItems[nextIndex].classList.add('next');
  setTimeout(() => {
    carouselItems[nextIndex].classList.remove('next');
    carouselItems[nextIndex].classList.add('active');
  }, 1000);
  currentIndex = nextIndex;
}, 3000);
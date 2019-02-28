$(document).ready(function(){
  var
  currentImage,
  currentImageIndex,
  nextImage,
  nextImageIndex,
  prevImage,
  prevImageIndex;
  $(".next").click(function(){
    currentImage = $(".curry");
    currentImageIndex  = currentImage.index();
    nextImageIndex = currentImageIndex + 1;
    if(nextImageIndex == 3){
      nextImageIndex = 0;
    }
    nextImage = $(".img").eq(nextImageIndex);
    currentImage.fadeOut(1000);
    currentImage.removeClass("curry");
    nextImage.fadeIn(1000);
    nextImage.addClass("curry");
  });

  $(".prev").click(function(){
    currentImage = $(".curry");
    currentImageIndex = currentImage.index();
    prevImageIndex = currentImageIndex - 1;
    if(prevImageIndex == -1){
      prevImageIndex = 2;
    }
    prevImage = $(".img").eq(prevImageIndex);
    currentImage.fadeOut(1000);
    currentImage.removeClass("curry");
    prevImage.fadeIn(1000);
    prevImage.addClass("curry");
  });
});

$(document).ready(function () {
  var
  currentImage,
  currentImageIndex,
  nextImage,
  nextImageIndex;

  setInterval(function(){
      currentImage = $(".curry");
      currentImageIndex  = currentImage.index();
      nextImageIndex = currentImageIndex + 1;
      if(nextImageIndex == 3){
        nextImageIndex = 0;
      }
      nextImage = $(".img").eq(nextImageIndex);
      currentImage.fadeOut(1000);
      currentImage.removeClass("curry");
      nextImage.fadeIn(1000);
      nextImage.addClass("curry");
    }, 7000);
});

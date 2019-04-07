$(document).ready(function(){
  var
  currentImage,
  currentImageIndex,
  nextImage,
  nextImageIndex,
  prevImage,
  prevImageIndex,
  currentLink,
  nextLink,
  prevLink;
  $(".next").click(function(){
    currentImage = $(".curry");
    currentLink = $(".currentLink");
    currentImageIndex  = currentImage.index();
    nextImageIndex = currentImageIndex + 1;
    if(nextImageIndex == 3){
      nextImageIndex = 0;
    }
    nextImage = $(".img").eq(nextImageIndex);
    nextLink = $(".slink").eq(nextImageIndex);
    currentImage.fadeOut(1000);
    currentLink.removeClass("currentLink");
    currentImage.removeClass("curry");
    nextImage.fadeIn(1000);
    nextLink.addClass("currentLink");
    nextImage.addClass("curry");
  });

  $(".prev").click(function(){
    currentImage = $(".curry");
    currentLink = $(".currentLink");
    currentImageIndex = currentImage.index();
    prevImageIndex = currentImageIndex - 1;
    if(prevImageIndex == -1){
      prevImageIndex = 2;
    }
    prevImage = $(".img").eq(prevImageIndex)
    prevLink = $(".slink").eq(prevImageIndex);
    currentImage.fadeOut(1000);
    currentLink.removeClass("currentLink");
    currentImage.removeClass("curry");
    prevImage.fadeIn(1000);
    prevLink.addClass("currentLink");
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
      currentLink = $(".currentLink");
      currentImageIndex  = currentImage.index();
      nextImageIndex = currentImageIndex + 1;
      if(nextImageIndex == 3){
        nextImageIndex = 0;
      }
      nextImage = $(".img").eq(nextImageIndex);
      nextLink = $(".slink").eq(nextImageIndex);
      currentImage.fadeOut(1000);
      currentLink.removeClass("currentLink");
      currentImage.removeClass("curry");
      nextImage.fadeIn(1000);
      nextLink.addClass("currentLink");
      nextImage.addClass("curry");
    }, 7000);
});

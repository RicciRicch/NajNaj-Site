
const burger = document.getElementById("burger");
const links = document.querySelectorAll('li')
const navBar = document.getElementById("navmenu")
const phone = document.getElementById('phone')

burger.addEventListener('click',()=>{
    navBar.classList.toggle('left-[0]')
    phone.classList.toggle('hidden')
    if (burger.classList.contains('ri-menu-line')) {
    burger.classList.remove('ri-menu-line');
    burger.classList.add('ri-close-circle-line');
    } 
    else {
    burger.classList.remove('ri-close-circle-line');
    burger.classList.add('ri-menu-line');
    }

} )

links.forEach(link =>{
    link.addEventListener('click', ()=>{
        navBar.classList.toggle('left-[0]')
       
        if (burger.classList.contains('ri-menu-line')) {
        burger.classList.remove('ri-menu-line');
        burger.classList.add('ri-close-circle-line');
        } 
        else {
        burger.classList.remove('ri-close-circle-line');
        burger.classList.add('ri-menu-line');
        }
    })
})


document.addEventListener("DOMContentLoaded", function () {
    const videoPlayer = document.getElementById("videoPlayer");

   const videos = [
    "/static/video/monte_carlo.MOV",
    "/static/video/pudinzi.MOV",
    "/static/video/slana_najnaj.MOV",
    "/static/video/kinderferrero.MOV",
    "/static/video/bobe.MOV",
    "/static/video/malinanadev.MOV",
    "/static/video/jagode.MOV",
    "/static/video/palacinka1.MOV",
    "/static/video/palacinka2.MOV",
    "/static/video/svetleci.MOV",
    "/static/video/palacinka3.MOV",
    "/static/video/kinder.MOV",
    "/static/video/slushy.MOV",
    "/static/video/slanapal.MOV",
  ];

    let currentVideoIndex = 0;

    function playNextVideo() {
      // Fade out
      videoPlayer.classList.remove("fade-in");
      videoPlayer.classList.add("fade-out");

      // Sačekaj da se fade-out završi pre promene videa
      setTimeout(() => {
        videoPlayer.src = videos[currentVideoIndex];
        videoPlayer.load();
        videoPlayer.play();

        // Kada krene novi video, fade-in
        videoPlayer.classList.remove("fade-out");
        videoPlayer.classList.add("fade-in");

        currentVideoIndex = (currentVideoIndex + 1) % videos.length;
      }, 700); // isto vreme kao u CSS transition
    }

    videoPlayer.addEventListener("ended", playNextVideo);

    playNextVideo();
  });


const burger = document.getElementById("burger");
const links = document.querySelectorAll('li')
const navBar = document.getElementById("navmenu")

burger.addEventListener('click',()=>{
    navBar.classList.toggle('left-[0]')
    
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
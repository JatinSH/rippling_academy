let randColor;

function randomColor(){

    randColor = "rgb(" + Math.floor(Math.random()*255) + "," + Math.floor(Math.random()*255)  + "," + Math.floor(Math.random()*255) + ")";
}

let gridItems = document.querySelectorAll('.grid-items');
/*
gridItems.forEach(function(element){

    element.addEventListener("mouseover", function(event){
        event.target.style.opacity = 0;
    }) 
    element.addEventListener("mouseout", function(event){
        event.target.style.opacity = 1;
    }) 
})
*/
document.body.addEventListener("click", function (){
    randomColor();            
    gridItems.forEach(function(element){
        element.style.backgroundColor = randColor;
    })
});
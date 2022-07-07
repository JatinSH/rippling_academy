const date = new Date();

function renderer(){

  date.setDate(1);
  const firstDayIndex = date.getDay();
  const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];
  console.log(date.getFullYear());
  document.querySelector('.month').innerHTML = months[date.getMonth()];
  document.querySelector('.year').innerHTML = date.getFullYear();

  let days = "";
  const monthDay = document.querySelectorAll('.date');
  const weekNumber = document.querySelectorAll('.week');
  const lastDay = new Date(date.getFullYear(), date.getMonth()+1, 0).getDate();
  const oneJan = new Date(date.getFullYear(),0,1);
  const numberOfDays = Math.floor((date - oneJan)/(24*60*60*1000));
  let Week = Math.ceil(numberOfDays/7);
  
  for(let x = 1; x < 7; ++x){

    weekNumber[x-1].innerHTML = Week+1; 
    Week++;
  }

  

  let index = 0;
  for(let i = 1; i<=lastDay; ++i){
    if(firstDayIndex+i-2<0)
    {
      index = 7;
      console.log("here");
    }

    monthDay[index+firstDayIndex+i-2].innerHTML = i;
    if(i===new Date().getDate()&&date.getMonth()===new Date().getMonth()&&date.getFullYear()===new Date().getFullYear())
      monthDay[index+firstDayIndex+i-2].style.backgroundColor = "rgba(35, 162, 164)";
    else
    monthDay[index+firstDayIndex+i-2].style.backgroundColor = "rgba(35, 162, 164, 0.5)";

  }

  for(let j=0; j < index+firstDayIndex-1; ++j){
    monthDay[j].innerHTML = "";
    monthDay[j].style.backgroundColor = "rgba(190, 197, 197, 0.5)";
  }
  for(let j=firstDayIndex + lastDay-1+index; j < 42; ++j){
    monthDay[j].innerHTML = "";
    monthDay[j].style.backgroundColor = "rgba(190, 197, 197, 0.5)"
  }

}

document.querySelector('.previous').addEventListener('click',()=>{

    date.setMonth(date.getMonth()-1);
    renderer();
})

document.querySelector('.next').addEventListener('click',()=>{

    console.log("next");
    date.setMonth(date.getMonth()+1);
    renderer();
  })
renderer();

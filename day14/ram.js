// console.log("hai from the JS file")
// const nameList = [
//     "Ram",
//     "Sam",
//     "Jam",
//     "Fam",
//     "Jas",
//     "Boss",
//     "Ros",
//     "Ram"
// ]

// const doc = document.getElementsByTagName("div")
// let div = doc[0];
// div.textContent = "BVC Testing Python Batch"

// let cskDiv = document.getElementById("csk")

// cskDiv.style.backgroundColor = "yellow"
// cskDiv.style.border = "1px solid black"


// cskDiv.textContent = "csk"
// console.log(cskDiv)


// const headings = document.getElementsByTagName("h1");
// console.log(headings);
// for(let i = 0 ; i<headings.length ; i++)
// {
//     headings[i].style.fontStyle = "italic"
    
// }


// const allDivs = document.getElementsByTagName("div");
// for(let i = 0 ; i<allDivs.length ; i++)
// {
//     allDivs[i].classList.add("boring")
// }

// const newDiv =  document.createElement("div")

// newDiv.textContent = "Test Div 4";
// newDiv.classList.add("boring");

// const parent = document.getElementById("container")
// parent.appendChild(newDiv);

// console.log(parent)

// const bye = document.createElement("h1");
// bye.textContent = "Bye! Bye!";

// document.body.appendChild(bye);

// const addDiv = ()=>{
//     const ram = document.createElement("div");
    
//     ram.classList.add("boring");

//     const parent = document.getElementById("container");
//     ram.textContent = `Test div ${(parent.children.length + 1)}`;
//     parent.appendChild(ram);
// }

// const clicked = ()=>{
//     nameList.push("New Name");
//     console.log(nameList)
// }

const addDiv = (name)=>{
    const ram = document.createElement("div");
    
    ram.classList.add("boring");

    const parent = document.getElementById("container");
    ram.textContent = name;
    parent.appendChild(ram);
}

// nameList.forEach((param1 , index)=>{
//     addDiv(param1);
// })



const button = document.querySelector("#button1")

button.addEventListener("mouseover" , ()=>{
    button.style.backgroundColor = "red"
    button.style.scale = 1.2
})

button.addEventListener("mouseout" , ()=>{
    button.style.backgroundColor = "white"
    button.style.scale = 0.9
})

button.addEventListener("dblclick" , ()=>{
    console.log("double clicked bro")
})

button.addEventListener("click" , ()=>{
    const newH1 = document.createElement("h1")
    console.log()
    newH1.textContent = document.getElementById("input").value
    document.getElementById("container").appendChild(newH1)
})

document.getElementById("input").addEventListener("change" , (event)=>{
    const key = document.querySelector("#keys")
    key.textContent = event.target.value
    console.log(event.target.value)
})

document.body.addEventListener("mousedown" , ()=>{
    document.body.style.backgroundColor = "black"
})

document.body.addEventListener("mouseup" , ()=>{
    document.body.style.backgroundColor = "white"
})



// document.body.addEventListener("keydown" , (event)=>{
//     console.log("event",event)
//     key.textContent = "keydown";
//     if(event.ctrlKey && event.key == "s")
//     console.log("Saving Document.....")
// })

// window.addEventListener("resize" , resizeFunction)

window.addEventListener("scroll" , ()=>{
    //     let color = ["red" , "blue" , "green" , "yellow" , "orange" , "purple" , "black" , "pink" , "cyan" , "teal", "gray"]
    // document.body.style.backgroundColor = color[Math.ceil(Math.random()*10)]
    document.getElementsByTagName("p")[0].classList.add("ani")

})



console.log(button)


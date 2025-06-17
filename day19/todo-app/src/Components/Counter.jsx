import React, { useEffect, useState } from 'react'

const Counter = () => {

    const [balls , setBalls] = useState(0);
    const [overs , setOvers] = useState(0);


    const handleBalls = () =>{

        if(balls + 1 == 6)
        {
            setOvers(overs + 1);
            setBalls(0);
        }
        else
            setBalls(balls + 1);
    }

    // useEffect(()=>{
    //     console.log("balls changed");
    // } , [balls]);

    // useEffect(()=>{
    //     console.log("Overs changed");
    // } , [overs]);

    useEffect(()=>{
        console.log("side effect :" , overs , balls)
    } , [balls , overs])

  return (
    <div>
        <h1>Overs : {overs}.{balls}</h1>
        <button onClick={handleBalls} >add ball</button>
    </div>
  )
}

export default Counter
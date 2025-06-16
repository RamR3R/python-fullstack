import React, { useState } from 'react' 

const CricketScore = (props) => {
    console.log("props" ,props)
    console.log("targert = " , props.target)
    //states are created here inside the function
    const [runs , setRuns] = useState(0);
    const [wickets , setWickets] = useState(0);
    const [target , setTarget] = useState(props.target);



    // const handleSix = () =>{
    //     setRuns(runs + 6);
    // }

    // const handleFour = () =>{
    //     setRuns(runs + 4);
    // }

    const handleOne = () =>{
        setRuns(runs + 1);
    }

    const handleRuns = (run) => {
        if(runs + run >= target)
            alert("Target Chased");
        setRuns(runs + run)
    };

    // overs done => "Failed to Chase Target"

    const handleWicket = () =>{

        if(wickets + 1 == 10)
            alert("All Out");

        setWickets(wickets + 1); // it will take some time to update
    }
  return (
    <>
        <h1>Scrore : {runs} / {wickets}</h1>
        <h2>Current Over : {3}</h2>
        <h2>Overs Left: {17}</h2>
        {
            wickets < 10 && runs < target ?
            <div>
                <button onClick={()=>handleRuns(6)} >Six</button>
                <button onClick={()=>handleRuns(4)} >Four</button>
                {
                    //Add 3 2 dotball also
                }
                <button onClick={handleOne} >One</button>
                <button onClick={handleWicket} >Wicket</button>
            </div>
            :
            <h2>Game Over</h2>
        }


    </>
    
  )
}

export default CricketScore